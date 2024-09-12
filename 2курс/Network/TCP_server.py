import socket
import select

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)

server_socket.bind(('localhost', 8080))
server_socket.listen()
inputs = [server_socket]

server_important_data = {"DNS":"гроб", "TCP":"было страшно, но я это сделал", "IP":"круто", "UDP":"я уважаю, что они делают", "NTP":"я этого не понимаю"}

sessions = {}
clients = {"123":{'password':"123", "socks":[]}, "1234":{'password':"1234", "socks":[]}}
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
            # Этот блок try except нужен для того чтобы не падал сервер при дисконекте клиента
            # Если клиент отключается, а мы пытаемся сделать recv() то сервер упадет с ConnectionResetError
            # Ловим эту ошибку и удаляем клиента из списка подключенных
            # Выводи отладочную информацию и закрываем его сокет
            try:
                data = sock.recv(1024).decode()
            except ConnectionResetError:
                print(f"Client {session['ip']} disconnected")
                if "username" in session: clients[session["username"]]["socks"].remove(sock)
                inputs.remove(sock)
                del sessions[sock]
                sock.close()
                continue
            if data:
                print(f"Data from {session['ip']}\n{data}")
                #client request processing
                splited = data.split() 
                comand = splited[0] if data[0] == '\\' else None
                response = "default response"
                if "username" not in session and comand not in  ("\\login", "\\register"):
                    response =  "to proceed login with comand\n\\login <username> <password> \nor register new account with command\n\\register <username> <password>"
                else:
                    match comand:
                        case "\\register":
                            if len(splited) != 3:
                                response = "invalid register parameters format"
                            else:
                                _, name, pswd = splited
                                if name in clients:
                                    response = "this username is already occupied"
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
                            print("messegeing")
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