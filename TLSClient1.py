import socket
from Crypto.Cipher import AES

#put servers IP
serverIP = "192.168.0.24"
serverPort = 8000

cipherKey = b'bQeThWmZq4t7w!z%C*F-JaNdRfUjXn2r'
nonce = b'dRgUkXp2s5v8y/B?E(G+KbPeShVmYq3t'

client1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client1.connect((serverIP, serverPort))
while True:
    try:
        print("enter message: ")
        msgInput = input()

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
    break


