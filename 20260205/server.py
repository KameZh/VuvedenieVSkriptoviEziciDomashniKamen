# Echo server program
import socket
import random
import datetime
import os
image_path = r'C:/Users/samol/Pictures/trojan.png'

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    while True:
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            while True:
                data = conn.recv(1024)
                if not data: break
                if data == b'time':
                    data = str(datetime.datetime.now()).encode()
                elif data == b'Number':
                    data = str(random.randint(1, 100)).encode()
                elif data == b'ip':
                    data = socket.gethostbyname(socket.gethostname()).encode()
                elif data == b'File':
                    with open('text.txt', 'r') as f:
                        data = f.read().encode()
                elif data == b'trojan':
                    os.startfile(image_path)
                    data = b'Image opened!'
                conn.sendall(data)