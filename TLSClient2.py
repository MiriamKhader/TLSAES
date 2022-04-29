import socket
from Crypto.Cipher import AES

serverIP = "127.0.0.1"
serverPort = 8000

cipherKey = b'bQeThWmZq4t7w!z%C*F-JaNdRfUjXn2r'  # encryption key client1 use to encrypt message onto the server for decryption
nonce = b'dRgUkXp2s5v8y/B?E(G+KbPeShVmYq3t'  # nonce key for validation

client2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client2.connect((serverIP, serverPort))

data, tag = client2.recvfrom(1024)

cipher = AES.new(cipherKey, AES.MODE_EAX, nonce)  # Encrypt - Authenticate - Translate
plaintext = cipher.decrypt(data)

print(plaintext.decode())

client2.close()
