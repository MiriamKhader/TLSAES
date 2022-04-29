import getpass
import socket
from Crypto.Cipher import AES

serverIP = "127.0.0.1"
serverPort = 8000
cipherKey = b'bQeThWmZq4t7w!z%C*F-JaNdRfUjXn2r'  # encryption key client1 use to encrypt message onto the server for decryption
nonce = b'dRgUkXp2s5v8y/B?E(G+KbPeShVmYq3t'  # nonce key for validation

client1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client1.connect((serverIP, serverPort))

try:
    msgInput = getpass.getpass(prompt="Enter Message: ")
    print(msgInput)
except Exception as error:
    print('Error', error)
else:
    msgRaw = msgInput.encode()

    cipher = AES.new(cipherKey, AES.MODE_EAX, nonce)
    ciphertext, tag = cipher.encrypt_and_digest(msgRaw)

    print(ciphertext)

    client1.send(ciphertext)
    client1.close()



