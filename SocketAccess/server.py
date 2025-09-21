import socket
import threading

def sendMsg(sock) :
    while True:
        data = input()
        data = "관리자: " + data
        sock.send(data.encode('utf-8'))

def recvMsg(sock) :
    while True:
        data = sock.recv(1024)
        print(data.decode('utf-8'))

HOST = '192.168.0.5'
PORT = 7777

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

sock.bind((HOST, PORT))

sock.listen()

print("[+] 관리자 대화")
print("[+] 유저 기다리는중..")

conn, addr = sock.accept()
print(conn)
print(addr)

print("[+] 유저 입장..")

conn.send("[+] 관리자 대화".encode())
conn.send("[+] 도움이 필요한 내용 입력해주세요!".encode())

t1 = threading.Thread(target= sendMsg, args=(conn,))
t2 = threading.Thread(target= recvMsg, args=(conn,))

t1.start()
t2.start()

t1.join()
t2.join()