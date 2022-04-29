import socket

serverIP = "127.0.0.1"
serverPort = 8000
TCPBuffer = 1024

TCPserver = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
TCPserver.bind((serverIP, serverPort))
TCPserver.listen(2)

conn1, addr1 = TCPserver.accept()
print("Connedted to client1", addr1)
conn2, addr2 = TCPserver.accept()

data = conn1.recv(TCPBuffer)
print(data)
conn2.sendall(data)

TCPserver.close()

