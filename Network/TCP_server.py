import socket
import select

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)

server_socket.bind(('192.168.31.73', 8080))
server_socket.listen()
inputs = [server_socket]

server_important_data = {"DNS":"гроб", "TCP":"было страшно, но я это сделал", "IP":"круто", "UDP":"я уважаю, что они делают", "NTP":"я этого не понимаю"}

sessions = {}
clients = {}
print("Server started")
while True:

    for sock in select.select(inputs, [], [])[0]:
        if sock == server_socket:
            client_socket, client_addres = server_socket.accept()
            print(f"New connection from addres {client_addres}")
            inputs.append(client_socket)
            sessions[client_socket] = {'ip':client_addres}
            
        else:

            session = sessions[sock]
            data = sock.recv(1024).decode()
            if data:
                print(f"Data from {session['ip']}\n{data}")
                #client request processing
                splited = data.split() 
                comand = splited[0] if data[0] == '\\' else None
                response = "default response"
                if "username" not in session and comand not in  ("\\login", "\\register"):
                    response =  "to proceed login with comand\n\\login <username> <password> \nor register new accaunt with comand\n\\register <username> <password>"
                else:
                    match comand:
                        case "\\register":
                            if len(splited) != 3:
                                response = "invalid register parameters format"
                            else:
                                _, name, pswd = splited
                                if name in clients:
                                    response = "that username is already accupyed"
                                else:
                                    clients[name] = {'password':pswd, "socks":[]}
                                    response = "new accaunt succesfuly created"
                        case "\\login":
                            if len(splited) != 3:
                                response = "invalid login parameters format"
                            else:
                                _, name, pswd = splited
                                if name not in clients or clients[name]["password"] != pswd:
                                    response = "incorect password"
                                else:
                                    if 'username' in session:
                                        clients[session['username']]['socks'].remove(sock)
                                    session['username'] = name
                                    clients[name]["socks"].append(sock)
                                    response = f"logged by: {name}"
                        case _:
                            response = "ok"
                            print("massegeing")
                            for dest_sock in inputs:
                                if dest_sock not in (server_socket, sock):
                                    print(f"forwarding from {session['username']} to {sessions[dest_sock]['ip']}")
                                    dest_sock.sendall(f"{session['username']} > {data}\n".encode())

                sock.sendall(response.encode())
            else:
                print(f"Client {session['ip']} disconnected")
                if "username" in session: clients[session["username"]]["socks"].remove(sock)
                inputs.remove(sock)
                del sessions[sock]
                sock.close()