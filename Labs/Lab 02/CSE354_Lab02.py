#############################################################################
# Program:
#    Lab 02 Python Web Server, Computer Networks
#    Brother Jones, CSE354
# Author:
#    Whitney LeSueur
# Summary:
#    This program will launch a webserver capable of returning the text and 
#     images of a given HTML file.
#
#############################################################################
#############################################################################
#
# Changes made to my code for the Python Web Server Take-2:
#   - Removed dependency on Flask module, as I was advised this might 
#     invalidate given instructions
#
#############################################################################

import base64
from socket import *
import sys
import os
import string


# Return proper content type
def contentType(filepath):
   # Based on the file extension, return the content type 
   # that is part  of the "Content-type:" header"
    return "text/html"

def parseToken(request_line):
    line = request_line.split(" ")
    http_type = line[2]
    request_type = line[0]
    requested_file = line[1]
    return request_type, requested_file, http_type


def file_exists(requested_file):
    files = get_list_of_filenames_of_type(SERVER_FOLDER)
    if requested_file.translate(str.maketrans('', '', string.punctuation)) in files:
        return True
    else:
        return False


def read_file(requested_file):
    requested_file = "." + requested_file
    print("file:", requested_file)
    file = open(requested_file, 'r')
    data = file.read()
    index = requested_file.find(".")
    file_type = requested_file[index:-1:1]
    return data, file_type

# Read file or return 404 Error (if applicable)
def build_response(token, requested_file, http_type):
    CRLF = "\r\n"
    if file_exists(requested_file):
        file_data, file_type = read_file(requested_file)
        response = http_type + "200 OK\n"
        response += "Server: localhost\n"
        response += "Content - Length: " + str(len(file_data)) + "\n"
        response += "Content - Type: " + contentType(file_type) + "\n"
        response += CRLF
        response += file_data
    else:
        response = http_type + "404 Not Found\n"
        response += "Server: localhost\n"
        response += "Content - Length: 230\n"
        response += "Content - Type: text / html; charset = iso - 8859 - 1\n"
        response += "Connection: Closed\n"
        response += CRLF
        response += '<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN"><html><head><title>404 Not Found</title></head><body><h1>Not Found</h1><p>The requested URL' + requested_file + 'was not found on this server.</p></body></html>'

    return response


def get_list_of_filenames_of_type(root_dir):
    file_names = []
    for subdir, dirs, files in os.walk(root_dir):
        for file in files:
            file_names.append(str(os.path.join(subdir, file)).translate(str.maketrans('', '', string.punctuation)))
    return file_names


# Server Connection Setup, Defaults to port 6789
serverPort = int(sys.argv[1]) if len(sys.argv) == 2 else 6789
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print("Currently running server on port ", str(serverPort))

SERVER_FOLDER = "./cse354webServerFiles"

try:
    while 1:
        connectionSocket, addr = serverSocket.accept()
        request = connectionSocket.recv(1024).decode('ascii')
        
        request_list = request.splitlines()
        print(request_list[0])

        token, requested_file, http_type = parseToken(request_list[0])

        response = build_response(token, requested_file, http_type)

        connectionSocket.send(response.encode('ascii'))

        connectionSocket.close()

except KeyboardInterrupt:
    print("\nClosing Server")
    serverSocket.close()
    quit()
