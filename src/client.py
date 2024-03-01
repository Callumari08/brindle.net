import socket

DEFAULT_PORT = 11419

def main():
    s = socket.socket()

    ip = input("IP Of Server: ")
    
    s.connect((ip, DEFAULT_PORT))

    buffer = ""

    while buffer != "EXIT":
        buffer = s.recv(1024).decode()
        
        while buffer != "":
            print(buffer)
            
        buffer = ""

if __name__ == "__main__":
    main()