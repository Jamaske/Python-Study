import socket

TIMEOUT = 10
client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_sock.settimeout(TIMEOUT)
try:
    client_sock.connect(("192.168.31.73", 8080))
    while True:
        inp = input(">>")
        client_sock.sendall(inp.encode())
        data = client_sock.recv(1024).decode()
        print(data)
except socket.timeout:
    print("Connection timeout")
finally:
    client_sock.close()