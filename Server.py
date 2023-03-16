from socket import * #socket 불러오기
from threading import *
import time

def send(sock):
    while True:
        sendData = input('>>>')
        sock.send(sendData.encode('utf-8'))

def receive(sock):
    while True:
        recvData = sock.recv(1024)
        print('상대방 :', recvData.decode('utf-8'))


port = 8080

serverSock = socket(AF_INET, SOCK_STREAM)
serverSock.bind(('127.0.0.1', port))
serverSock.listen(3)

print('%d번 포트로 접속 대기중...'%port)

connectionSock, addr = serverSock.accept()
#accept()는 소켓에 누군가가 접속하여 연결되었을 때에 비로소 결과 값이 return되는 함수
#이 후에, 서버에 접속한 상대방과 데이터를 주고받기 위해서는 accept()함수로 생성된 connectionSock 이라는 소켓을 주로 이용

print(str(addr), '에서 접속되었습니다.')

sender = Thread(target = send, args=(connectionSock,))
receiver = Thread(target=receive, args=(connectionSock,))

sender.start()
receiver.start()

while True:
    time.sleep(1)
    pass
