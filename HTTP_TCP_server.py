from socket import *
import re


#SERVER = "localhost"
#SERVER = "192.168.86.23"
SERVER = gethostbyname(gethostname())
PORT = 8000

OBJECT = ""

def createserver():
    # create the socket 
    serversocket = socket(AF_INET, SOCK_STREAM)
    server_address = (SERVER, PORT)
    try:
        # bind it to localhost that is waiting on port SERVER
        serversocket.bind(server_address)
        # allow 5 more connections to be on hold for ahwile
        serversocket.listen(5)
        #print(f"[LISTENING] Server is listening on {PORT}")
        while(1):
            # server accepts while client somewhere is doing .connect
            # address holds the IP and port
            # 3-way handshake??
            (clientsocket, address) = serversocket.accept()
            print(f"[clientsocket] {address}")

            client_data = clientsocket.recv(5000).decode()
            data_length = len(client_data)
            #print(f"size = {data_length}")
            # break pieces by \n
            pieces = client_data.split("\n")
            # valid data
            if(len(pieces) > 0):
                # print out the HTTP GET and favicon
                # the HTTP GET request houses the word we typed
                # GET /hello HTTP/1.1
                OBJECT = extract_object(pieces)

            # HTTP response
            data_to_client = "HTTP/1.1 200 OK\r\n"
            data_to_client += "content-type: text/html; charset=utf-8\r\n"
            data_to_client += "\r\n"
            # actual data response 
            data_to_client += "<html><body>"+OBJECT+"<body><html>\r\n\r\n"
            # encode data before sending 
            clientsocket.sendall(data_to_client.encode())
            clientsocket.shutdown(SHUT_WR)
            
    except KeyboardInterrupt:
        print("\nShutting down......\n")

    except Exception as exc:
        print("Error: \n")
        print(exc)
    serversocket.close()
    
# Handles extracting the client's requested object
def extract_object(pieces):
    START = pieces[0].find("T")+2 # START val = pos of GET
    END = pieces[0].find("HTTP", START) # END val = START to HTTP
    if pieces[0][START] == "/":
        START += 1

    object_to_send = pieces[0][START:END].replace("%20"," ")
    print(pieces[0])
    print(f"Text to display: {object_to_send}\n")
    #OBJECT = OBJECT.replace(" ", object_to_send)
    OBJECT = object_to_send
    return OBJECT

print(f"Access http://{SERVER}:8000")
createserver()
            
        
