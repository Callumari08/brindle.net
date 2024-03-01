import socket

HOST = "127.0.0.1"
DEFAULT_PORT = 11419

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, DEFAULT_PORT))
        s.listen()
        conn = s.accept() 
        addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                conn.sendall(data)
    
if __name__ == "__main__":
    main()