# Echo client program
import socket

HOST = '10.101.211.49'    # The remote host
PORT = 50007              # The same port as used by the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'trojan')
    data = s.recv(1024)
print('Received', repr(data))