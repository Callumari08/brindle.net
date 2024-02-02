import socket
import threading


name = input("Server Name: ")
try:
    port = int(input("Press RETURN to use the default port (40674)\nor\nEnter a Unique port:\n"))
except:
    port = 40674

s = socket.socket()
print("Socket successfully created")


# listen with an undefined IP
s.bind(("", port))
print("Socket binded to " + str(port))

print("Public server IP address", socket.gethostbyname(socket.gethostname()))

s.listen(5)

print("Socket is listening")


def serve():
    while True:
        # this varible is used so we can see what the client sent us
        recieved = ""
        # Establish connection with client.
        c, addr = s.accept()
        print('Got connection from', addr)
        welcome = "Thank you for using BrindleNet 1.1!\nYou are now connected to " + name
        c.send(welcome.encode())
        # Continually print what the client sends until they give the exit code ('&exit')
        while recieved != "&exit":
            print(recieved)
            recieved = c.recv(1024).decode()
            # Send a command to the client, so that once multi-user contact is established, it will not freeze waiting for a response
            c.send(b'&brindlesent')
    c.send(b'&exit')

threadymcthreadface = threading.Thread(target = serve)
threadymcthreadface2 = threading.Thread(target = serve)
threadymcthreadface3 = threading.Thread(target = serve)
threadymcthreadface4 = threading.Thread(target = serve)

threadymcthreadface.start()
threadymcthreadface2.start()
threadymcthreadface3.start()
threadymcthreadface4.start()
threadymcthreadface.join()
threadymcthreadface2.join()
threadymcthreadface3.join()
threadymcthreadface4.join()
