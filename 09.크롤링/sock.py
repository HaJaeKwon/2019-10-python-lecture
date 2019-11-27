import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

google_ip = socket.gethostbyname("google.com")
sock.connect((google_ip, 80))

sock.send("GET / HTTP/1.1\n".encode())
sock.send("\n".encode())

buffer = sock.recv(4096)
buffer = buffer.decode().replace("\r\n", "\n")
sock.close()

print(buffer)
