
# This is TCPServer.py

import sys
from socket import *

DEFAULT_VALUE = 6789
serverPort = int(sys.argv[1]) if len(sys.argv) == 2 else DEFAULT_VALUE

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('The Server is ready to receive')

try:
   while 1:
      connectionSocket, addr = serverSocket.accept()
      sentence = connectionSocket.recv(1024).decode('ascii')
      print ("Received from client: ", sentence)
      capitalizedSentence = sentence.upper()
      connectionSocket.send(capitalizedSentence.encode('ascii'))
      connectionSocket.close()

except KeyboardInterrupt:
   print("\nClosing Server")
   serverSocket.close()


