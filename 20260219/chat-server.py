import socket
import threading

import socket
import threading
import json
import time
import os

HOST = ''
PORT = 50007

clients = []
clients_lock = threading.Lock()
history = []
history_file = os.path.join(os.path.dirname(__file__), 'history.json')

def save_history():
	try:
		with open(history_file, 'w', encoding='utf-8') as f:
			json.dump(history, f, ensure_ascii=False)
	except Exception:
		pass

def clear_history():
	try:
		with open(history_file, 'w', encoding='utf-8') as f:
			json.dump([], f)
	except Exception:
		pass

def load_history():
	global history
	try:
		if os.path.exists(history_file):
			with open(history_file, 'r', encoding='utf-8') as f:
				data = json.load(f)
				if isinstance(data, list):
					history = data
	except Exception:
		history = []

def broadcast_json(obj, sender=None):
	data = (json.dumps(obj, ensure_ascii=False) + '\n').encode('utf-8')
	with clients_lock:
		for c in clients[:]:
			try:
				c.sendall(data)
			except Exception:
				try:
					clients.remove(c)
					c.close()
				except ValueError:
					pass

def handle_client(conn, addr):
	print(f'Connected: {addr}')
	# send current history to the new client
	try:
		hist_obj = {'type': 'history', 'items': history}
		conn.sendall((json.dumps(hist_obj, ensure_ascii=False) + '\n').encode('utf-8'))
	except Exception:
		pass

	with clients_lock:
		clients.append(conn)

	buffer = b''
	try:
		while True:
			try:
				data = conn.recv(4096)
			except (ConnectionResetError, ConnectionAbortedError):
				break
			if not data:
				break
			buffer += data
			while b'\n' in buffer:
				line, buffer = buffer.split(b'\n', 1)
				if not line:
					continue
				try:
					obj = json.loads(line.decode('utf-8'))
				except Exception:
					# fallback: treat as plain text
					text = line.decode('utf-8', errors='ignore')
					obj = {'type': 'message', 'name': '', 'text': text, 'time': time.strftime('%Y-%m-%d %H:%M:%S')}

				if obj.get('type') == 'message':
					# attach server timestamp if missing
					if 'time' not in obj:
						obj['time'] = time.strftime('%Y-%m-%d %H:%M:%S')
					history.append(obj)
					save_history()
					broadcast_json(obj, sender=conn)
	finally:
		with clients_lock:
			if conn in clients:
				clients.remove(conn)
		try:
			conn.close()
		except Exception:
			pass
		print(f'Disconnected: {addr}')

def main():
	# load existing history (if any); do NOT clear on start so new clients receive it
	load_history()

	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		s.bind((HOST, PORT))
		s.listen()
		print(f'Server listening on port {PORT}')
		try:
			while True:
				conn, addr = s.accept()
				t = threading.Thread(target=handle_client, args=(conn, addr), daemon=True)
				t.start()
		except KeyboardInterrupt:
			print('\nShutting down server, clearing history.')
		finally:
			clear_history()

if __name__ == '__main__':
	main()

