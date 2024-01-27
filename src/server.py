# first of all import the socket library
import socket

# next create a socket object
s = socket.socket()
print("Socket successfully created")

# reserve a port on your computer in our
# case it is 40674 but it can be anything
port = 40674

# listen with an undefined IP
s.bind(('', port))
print("socket binded to %s" %(port))

s.listen(5) 
print("socket is listening")

recieved = ""
while True:
    # Establish connection with client.
    c, addr = s.accept()
    print('Got connection from', addr)
    c.send(b'Thank you for connecting to BrindleNet 1.0')
    # Continually print what the client sends until they give the exit code ('&exit')
    while recieved != "&exit":
        print(recieved)
        recieved = c.recv(1024).decode()
        # Send a command to the client, so that once multi-user contact is established, it will not freeze waiting for a response
        c.send(b'&brindlesent')
    c.send(b'&exit')
