"""
소켓생성
바인딩
접속대기
접속수락
데이터 송/수신
접속종료
"""

import socket
print("1. 소켓생성")
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("2. 바인딩")
sock.bind(("", 12000))

print("3. 접속대기")
sock.listen()

print("4. 접속대기")
c_sock, addr = sock.accept()

print("5. 데이터 송/수신")
receive_data = c_sock.recv(1024)
print("수신한 데이터: {}".format(receive_data))

print("6. 접속종료")
c_sock.close()
sock.close()


