import socket

TIMEOUT = 10
client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_sock.settimeout(TIMEOUT)
try:
    client_sock.connect(('localhost', 8080))
    inp = input("Input text:")
    client_sock.sendall(inp.encode())
    data = client_sock.recv(1024).decode()
    print('Server response:', data)
except socket.timeout:
    print("Connection timeout")
finally:
    client_sock.close()