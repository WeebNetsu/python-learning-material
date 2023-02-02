import socket
import threading

HEADER = 64 # 64 bytes (determains max message length)
# we use capital letters to show that they are constant
PORT = 5050
# you can either enter your IP address in the bottom, or you can let python detect it (socket.gethostbyname(socket.gethostname()))
# I gad problems with socket.gethostbyname(socket.gethostname()) so i used my ip
SERVER = "192.168.1.134"
# to let this work over the internet (and not just locally or LAN) then change the above to your public ip address
# which can be found by either googling it or: curl ifconfig.me
# NOTE: DO NOT SHOW YOUR PUBLIC IP ADDRESS IN THE TUTORIAL!!!!!!!!
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT = "!DISCONNECT"

# AF_INET (connection) = ipv4 
# SOCK_STREAM -> the way we transfer data
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR) # binds the socket with the address

"""
NOTE: We willnot be creating a messaging app, only be covering how sockets work

If you want to create a message app, try to globally keep all the messages sent and check if the user
has received it, if they haven't receive the latest message, send it to them
"""

def handle_client(conn, addr):
    print(f"New Connection: {addr}")

    connected = True
    while connected:
        # Note: conn.recv will not continue with the code until triggred
        # this is why we have threads, to allow other clients to still do
        # what they should without waiting for the below to execute
        msg_length = conn.recv(HEADER).decode(FORMAT) # get message length
        if msg_length: # only run if an actual message was received
            msg_length = int(msg_length)

            msg = conn.recv(msg_length).decode(FORMAT) # receive message and decode it into text

            if msg == DISCONNECT: # if they sent !DISCONNECT
                connected = False

            print(f"{addr}: {msg}") # display the message the person sent
            conn.send("Messag Received".encode(FORMAT))

    conn.close() # close current connection

def start():
    server.listen() # listen for new connections
    print(f"Server is listening on {SERVER}")

    while True:
        conn, addr = server.accept() # return socket representing a connection
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"Amount Connections: {threading.activeCount() - 1}")

print("Server is starting.......")
start()