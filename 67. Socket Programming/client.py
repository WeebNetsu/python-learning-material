import socket

HEADER = 64 # 64 bytes (determains max message length)
# we use capital letters to show that they are constant
PORT = 5050
# you can either enter your IP address in the bottom, or you can let python detect it (what I'm doing)
SERVER = "192.168.1.134" # this is the address mine is currently running on
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT = "!DISCONNECT"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR) # connects the client with the address

def send(msg):
    message = msg.encode(FORMAT) # we need to encode it to bytes before we can send it
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    # we need to pad the rest of the message space with white space (in bytes: b' ') before we can send it
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(HEADER).decode(FORMAT))

send("Hello World!")
send(DISCONNECT)     