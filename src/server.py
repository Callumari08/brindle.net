# first of all import the socket library
import socket

# next create a socket object
s = socket.socket()
print ("Socket successfully created")

# reserve a port on your computer in our
# case it is 40674 but it can be anything
port = 40674

# Next bind to the port
# we have not typed any ip in the ip field
# instead we have inputted an empty string
# this makes the server listen to requests
# coming from other computers on the network
s.bind(('', port))
print ("socket binded to %s" %(port))

# put the socket into listening mode
s.listen(5) 
print ("socket is listening")

while True:
    # Initialise a variable that we will use to store what the client has sent us
    recieved = 0
    # Establish connection with client.
    c, addr = s.accept()
    print ('Got connection from', addr)
    # Send them the welcome message
    c.send(b'Thank you for connecting to BrindleNet 1.0')
    # Continually print what the client sends until they give the exit code ('&exit')
    while recieved != "&exit":
        print(recieved)
        recieved = c.recv(1024).decode()
        # Send a command to the client, so that once multi-user contact is established, it will not freeze waiting for a response
        c.send(b'&brindlesent')
    #The client is waiting for the exit code to exit with
    c.send(b'&exit')
