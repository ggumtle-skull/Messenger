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
#serverSock 이라는 소켓만들기 / AF_INET는 IPv4를 의미 / SOCK_STREAM은 소켓 타입중 하나로 양방향 통신
serverSock.bind(('',port))
#앞부분은 ip 뒷부분은 포트임 (ip,port)형식 / '' 이부분은 공백일시 모든 인터페이스와 연결이 가능
#즉 port번 포트에서 모든 인터페이스에게 연결하도록 한다
serverSock.listen(3)
#listen은 접속을 기다리는 것인데 listen()안에 숫자는 해당 소켓이 총 몇개의 동시접속을 허용하는지를 설정

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
