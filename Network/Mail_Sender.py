import socket
import ssl
import time

class helper:
    def __init__(self, server, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((server,port))
        self.mail = ssl.create_default_context().wrap_socket(server_hostname=server,sock = self.sock)

    
    def send_comand(self, comand):
        self.mail.send((comand + '\r\n').encode())
        print("REPL ", self.mail.recv(2024).decode())
        #time.sleep(1)
    
    def send_mail(self, text):
        self.mail.send(text.encode())

    def __del__(self):
        self.mail.close()
        self.sock.close()


mail_server = "smtp.mail.ru"
port = 465 #что за порт

A = helper(mail_server, port)
A.send_comand("EHLO Dima")
A.send_comand("AUTH LOGIN")
A.send_comand("YWFhLXRlc3RlcjIwMjRAbWFpbC5ydQ==")
A.send_comand('Tkg4S3JYVlJiZEJqY3FRWkNaNEc=')
A.send_comand('MAIL FROM: aaa-tester2024@mail.ru')
A.send_comand('RCPT TO: aaa-tester2024@mail.ru')
A.send_comand("DATA")
A.send_mail("\
    From: aaa-tester2024@mail.ru\r\n\
    To: aaa-tester2024@mail.ru\r\n\
    Subject: Task 6 - Cherniavsky\r\n\
    \r\n\
    Message Text\r\n\
    ")
A.send_comand("\r\n\
    .\r\n\
    ")
A.send_comand("QUIT")
print(A.mail.recv(2024).decode())