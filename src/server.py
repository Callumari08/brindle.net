import socket

name = input("Server Name: ")
try:
    port = int(input("Port: (Default: 14642)"))
except:
    port = 14642

s = socket.socket()
print("Socket successfully created")


# listen with an undefined IP
s.bind(("", port))
print("Socket binded to " + str(port))

print("Public server IP address", socket.gethostbyname(socket.gethostname()))

s.listen(5)

print("Socket is listening")

while True:
    # this varible is used so we can see what the client sent us
    recieved = ""
    # Establish connection with client.
    c, addr = s.accept()
    print('Got connection from', addr)
    c.send(b"Thank you for connecting to " + name.encode())
    # Continually print what the client sends until they give the exit code ('&exit')
    while recieved != "&exit":
        print(recieved)
        recieved = c.recv(1024).decode()
        # Send a command to the client, so that once multi-user contact is established, it will not freeze waiting for a response
        c.send(b'&brindlesent')
    c.send(b'&exit')
