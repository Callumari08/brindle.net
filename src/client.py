# imports socket library
import socket

# creating socket object
s = socket.socket()

# defines port you want to connect to
port = 40674

# connects to server on local computer; defines 'received'
s.connect(("172.26.26.44", port))
recieved = 0

# receives data from server
while recieved != "&exit":
    recieved = s.recv(1024).decode()
    if recieved != "&brindlesent":
        print(recieved)
    s.send(input("Send a message:\n").encode())
