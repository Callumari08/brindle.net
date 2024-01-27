import socket

s = socket.socket()

port = int(input("Enter the Port you want to use (Default: 40674)\n"))

s.connect((input("Enter the IP address of the server you want to connect to:\n"), port))

recieved = ""
# runs as long as we haven't recieved the exit signal from the server
while recieved != "&exit":
    recieved = s.recv(1024).decode()
    if recieved != "&brindlesent":
        print(recieved)
    s.send(input("Send a message:\n").encode())
