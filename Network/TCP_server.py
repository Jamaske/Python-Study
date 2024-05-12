import socket
import select

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)

server_socket.bind(('localhost', 8080))
server_socket.listen()
inputs = [server_socket]

server_important_data = {"DNS":"гроб", "TCP":"было страшно, но я это сделал", "IP":"круто", "UDP":"я уважаю, что они делают", "NTP":"я этого не понимаю"}

clients = {}
print("Server started")
while True:

    for sock in select.select(inputs, [], [])[0]:
        if sock == server_socket:
            client_socket, client_addres = server_socket.accept()
            print(f"New connection from addres {client_addres}")
            inputs.append(client_socket)
            clients[client_socket] = client_addres
        else:
            if data := sock.recv(1024).decode():
                print(f"Data from {clients[sock]}\n{data}")
                #client request processing
                response = server_important_data.get(data, "invalid request")
                sock.sendall(response.encode())
            else:
                print(f"Client {clients[sock]} disconnected")
                inputs.remove(sock)
                del clients[sock]
                sock.close()