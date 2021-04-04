from socket import *

SERVER = 'localhost'
PORT = 8000

mysock = socket(AF_INET, SOCK_STREAM)
mysock.connect((SERVER,PORT))
# format of the cmd GET <object> HTTP/1.1
#cmd = 'GET http://127.0.0.1/romeo.txt HTTP/1.1\r\n\r\n'.encode()
cmd = 'GET http/ HTTP1.1'.encode()
mysock.send(cmd)

while True:
    # data is the html file seny by the server
    data = mysock.recv(512)
    if len(data)<1:
        break;
    print(data.decode(), end='')

mysock.close()
