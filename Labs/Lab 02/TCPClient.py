
# This is TCPClient.py

from socket import *
serverName = 'localhost'
serverPort = 6789
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

sentence = input('Input lowercase sentence: ')

clientSocket.send(sentence.encode('ascii'))
print("Sentence sent to change to upper case: ", sentence)

modifiedSentence = clientSocket.recv(1024).decode('ascii')
print("From Server: ", modifiedSentence)

clientSocket.close()


