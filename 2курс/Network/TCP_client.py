import socket
import threading

TIMEOUT = 10
# client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client_sock.settimeout(TIMEOUT)
# try:
#     client_sock.connect(("localhost", 8080))
#     while True:
#         inp = input(">>")
#         client_sock.sendall(inp.encode())
#         data = client_sock.recv(1024).decode()
#         print(data)
# except socket.timeout:
#     print("Connection timeout")
# finally:
#     client_sock.close()

def send_data(sock: socket, data: str) -> None:
    try:
        sock.sendall(data.encode())
    except Exception as e:
        print(f"Exception: {e}")


def receive_data(sock: socket) -> None:
    try:
        while True:
            data = sock.recv(1024).decode()
            print(data)
    except Exception as e:
        print(f"Exception: {e}")



def main():
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # пришлось убрать таймаут, т.к. он срабатывал в потоке приема данных
    # Наверное надо как-то подумать и сделать с таймаутом, например убирать таймаут в потоке приема данных
    # А потом возвращать его обратно
    # client_sock.settimeout(TIMEOUT)
    try:
        client_sock.connect(("localhost", 8080))
    except socket.timeout:
        print("Connection timeout")
        client_sock.close()
    # Мы создаем отдельный поток для приема данных, чтобы не блокировать основной поток
    receive_thread = threading.Thread(target=receive_data, args=(client_sock,))
    receive_thread.start()
    # Тут счиатй тот же самый цикл, что был и у тебя, добавил условие выхода из цикла по команде exit
    # и обработку исключения KeyboardInterrupt, которое возникает при нажатии Ctrl+C
    while True:
        try:
            inp = input(">>")
            if inp == "exit":
                break
            send_data(client_sock, inp)
        except KeyboardInterrupt:
            client_sock.close()
            print("Client stopped")
            break
    
if __name__ == "__main__":
    main()