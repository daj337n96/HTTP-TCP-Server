from socket import *
#import re
from datetime import datetime
import threading

local_dt = datetime.now()
SERVER = gethostbyname(gethostname())
PORT = 8000

# Headers
data_to_client = "HTTP/1.1 200 OK\r\n"
data_to_client += "Date:"+str(local_dt)+"\r\n"
data_to_client += "Connection: Keep-Alive\r\n"
data_to_client += "Content-type: text/html; charset=utf-8\r\n"
data_to_client += "\r\n"
# Form to display on webpage
FORM = "<html><body>"
FORM += "<form action= 'HTTP_TCP_server.py' method= 'POST'>"
FORM += "<ul><li>"
FORM += "<label for='input text'> Input text here: </label>"
FORM += "<input type= 'text' id='name' name='text'>"
FORM += " <button>Enter</button>"
FORM += "</li></ul>"
FORM += "</form>"
FORM += "</body></html>\r\n\r\n"
# Form to reply
FORM_REPLY = "<html><body>"
FORM_REPLY += "You Entered: "
FORM_REPLY += "</body></html>\r\n\r\n"
       
def createserver():
    # create the socket 
    serversocket = socket(AF_INET, SOCK_STREAM)
    server_address = (SERVER, PORT)
    try:
        # bind it to localhost that is waiting on port SERVER
        serversocket.bind(server_address)
        # allow 5 more connections to be on hold for ahwile
        serversocket.listen(5)
        while(1):
            # server accepts while client somewhere is doing .connect
            # address holds the IP and port
            # 3-way handshake??
            (clientsocket, address) = serversocket.accept()
            print(f"[clientsocket] {address}")

            client_data = clientsocket.recv(5000).decode()
            data_length = len(client_data)
            pieces = client_data.split("\n")
            #print(pieces)
            # valid data
            if(len(pieces) > 0):
                # print out the HTTP GET and favicon
                # the HTTP GET request houses the word we typed
                # GET /hello HTTP/1.1
                HTTP_response(clientsocket, data_to_client+FORM)
                OBJECT = extract_object_POST(pieces)
                #print(f"OBJECT = {OBJECT}")
                if (len(OBJECT)>0):
                    HTTP_response(clientsocket, FORM_REPLY+OBJECT)
                    clientsocket.shutdown(SHUT_WR)
                   
    except KeyboardInterrupt:
        print("\nShutting down......\n")
    except Exception as exc:
        print("Error: \n")
        print(exc)
    serversocket.close()
    
# ------------------------Functions------------------------    
# Handles extracting the client's requested object
def extract_object_POST(pieces):
    data_length = len(pieces)
    #print(pieces[data_length-1])
    object_to_send = pieces[data_length-1][5:].replace('+', ' ')
    #print(pieces)
    if(len(object_to_send)>0):

        print(f"Text to display: {object_to_send}\n")
    OBJECT = object_to_send
    return OBJECT

# Handles HTTP responses
def HTTP_response(clientsocket, form_to_display):
    data_to_client = form_to_display
    # encode data before sending 
    clientsocket.sendall(data_to_client.encode())
    #clientsocket.shutdown(SHUT_WR)


print(f"Access http://{SERVER}:{PORT}")
createserver()
            
        
