import socket
from Crypto.Cipher import AES

#put servers IP
serverIP = "192.168.0.24"
serverPort = 8000
cipherKey = b'bQeThWmZq4t7w!z%C*F-JaNdRfUjXn2r'
nonce = b'dRgUkXp2s5v8y/B?E(G+KbPeShVmYq3t'

client2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client2.connect((serverIP, serverPort))

data, tag = client2.recvfrom(1024)

cipher = AES.new(cipherKey, AES.MODE_EAX, nonce)
plaintext = cipher.decrypt(data)

print(plaintext.decode())

client2.close()
