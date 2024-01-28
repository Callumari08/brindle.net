import socket

s = socket.socket()

port = input("Press RETURN to use default port\nor\nEnter a unique port\n")
# uses default port if no unique port has been specified
if port == "":
    port = 40674
port = int(port)
s.connect((input("Enter the IP address of the server you want to connect to:\n"), port))

recieved = ""
# runs as long as we haven't recieved the exit signal from the server
while recieved != "&exit":
    recieved = s.recv(1024).decode()
    if recieved != "&brindlesent":
        print(recieved)
    s.send(input("Send a message:\n").encode())

