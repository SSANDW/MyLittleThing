import socket
import threading

def sendMsg(sock) :
    while True:
        data = input()
        data = "유저: " + data
        sock.send(data.encode('utf-8'))

def recvMsg(sock) :
    while True:
        data = sock.recv(1024)
        print(data.decode('utf-8'))

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect(("49.142.150.204", 9898))

data = sock.recv(1024)
print(data.decode('utf-8'))
data = sock.recv(1024)
print(data.decode('utf-8'))

t1 = threading.Thread(target= sendMsg, args=(sock,))
t2 = threading.Thread(target= recvMsg, args=(sock,))

t2.start()
t1.start()

t1.join()
t2.join()