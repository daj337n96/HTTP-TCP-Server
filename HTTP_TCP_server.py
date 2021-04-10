from socket import *
import re
import threading
from datetime import datetime
import time


#################################### Setup SERVER & PORT ####################################
local_dt = datetime.now()
SERVER = gethostbyname(gethostname())
PORT = 8000
server_address = (SERVER, PORT)
serversocket = socket(AF_INET, SOCK_STREAM)
# Bind it to localhost that is waiting on port SERVER
serversocket.bind(server_address)

#################################### Define FORM & Client reply ####################################
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
FORM += "<label for='input text'> Please Input text here: </label>"
FORM += "<input type= 'text' id='name' name='text'>"
FORM += " <button>Enter</button>"
FORM += "</li></ul>"
FORM += "</form>"
FORM += "</body></html>\r\n\r\n"
# Form to reply
FORM_REPLY = "<html><body>"
FORM_REPLY += "You Entered: "
FORM_REPLY += "</body></html>\r\n\r\n"

#################################### Functions ####################################  
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

#################################### Client conenction and comms ####################################
# Handles client with the new thread
def handle_client(clientsocket, address):
            print(f"[NEW CONNECTION] {address} connected\n")
            connected = True
            while connected:
                client_data = clientsocket.recv(5000).decode()
                data_length = len(client_data)
                pieces = client_data.split("\n")
                    #print(pieces)
                # Valid data
                if(len(pieces) > 0):
                    # print out the HTTP GET and favicon
                    # Client sends HTTP GET
                    # Client sends HTTP POST and Server posts entered text
                    # Dsiplays form --> HTTP_response
                    HTTP_response(clientsocket, data_to_client+FORM)
                    OBJECT = extract_object_POST(pieces)
                    #print(f"OBJECT = {OBJECT}")
                    if (len(OBJECT)>0):
                        # Updates form eith entered text --> HTTP_response
                        HTTP_response(clientsocket, FORM_REPLY+OBJECT)
                # Buffer time before leaving function
                # Leaves function so server can handle multiple tabs on browser
                # Some browser has limited tabs per domain
                time.sleep(10)
                connected = False

# Wait for client to connect and direct it to a new thread                    
def createserver():
    # Listen for connection then can start new thread
    serversocket.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        # Server accepts client with socket and address
        (clientsocket, address) = serversocket.accept()
        # New thread started for client --> handle_client
        thread = threading.Thread(target=handle_client, args=(clientsocket, address))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount()-1}\n")
        #print(f"[clientsocket] {address}")


print(f"Access http://{SERVER}:{PORT}")
createserver()
            
        
from socket import *
import re
import threading
from datetime import datetime
import time


#################################### Setup SERVER & PORT ####################################
local_dt = datetime.now()
SERVER = gethostbyname(gethostname())
PORT = 8000
server_address = (SERVER, PORT)
serversocket = socket(AF_INET, SOCK_STREAM)
# Bind it to localhost that is waiting on port SERVER
serversocket.bind(server_address)

#################################### Define FORM & Client reply ####################################
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
FORM += "<label for='input text'> Please Input text here: </label>"
FORM += "<input type= 'text' id='name' name='text'>"
FORM += " <button>Enter</button>"
FORM += "</li></ul>"
FORM += "</form>"
FORM += "</body></html>\r\n\r\n"
# Form to reply
FORM_REPLY = "<html><body>"
FORM_REPLY += "You Entered: "
FORM_REPLY += "</body></html>\r\n\r\n"

#################################### Functions ####################################  
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

#################################### Client conenction and comms ####################################
# Handles client with the new thread
def handle_client(clientsocket, address):
            print(f"[NEW CONNECTION] {address} connected\n")
            connected = True
            while connected:
                client_data = clientsocket.recv(5000).decode()
                data_length = len(client_data)
                pieces = client_data.split("\n")
                    #print(pieces)
                # Valid data
                if(len(pieces) > 0):
                    # print out the HTTP GET and favicon
                    # Client sends HTTP GET
                    # Client sends HTTP POST and Server posts entered text
                    # Dsiplays form --> HTTP_response
                    HTTP_response(clientsocket, data_to_client+FORM)
                    OBJECT = extract_object_POST(pieces)
                    #print(f"OBJECT = {OBJECT}")
                    if (len(OBJECT)>0):
                        # Updates form eith entered text --> HTTP_response
                        HTTP_response(clientsocket, FORM_REPLY+OBJECT)
                # Buffer time before leaving function
                # Leaves function so server can handle multiple tabs on browser
                # Some browser has limited tabs per domain
                time.sleep(10)
                connected = False

# Wait for client to connect and direct it to a new thread                    
def createserver():
    # Listen for connection then can start new thread
    serversocket.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        # Server accepts client with socket and address
        (clientsocket, address) = serversocket.accept()
        # New thread started for client --> handle_client
        thread = threading.Thread(target=handle_client, args=(clientsocket, address))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount()-1}\n")
        #print(f"[clientsocket] {address}")


print(f"Access http://{SERVER}:{PORT}")
createserver()
            
        
