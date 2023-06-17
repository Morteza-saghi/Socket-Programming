import socket
from threading import Thread

def recv():
    try:
        while True:
            msg = c.recv(1024)
            if not msg:
                break
            print(msg.decode())
    except:
        print("Closed")

def send():
    try:
        while True:
            msg = input()
            if (msg == "--"):
                c.close()
            msg = "Server:" + msg
            c.send(msg.encode())
    except:
        print("Closed")
        
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 12345
s.bind((host, port))
s.listen(5)
print(f"Server started on {host}:{port}")
c, addr = s.accept()
print(f"Client {addr} is connected.")

Thread(target=recv).start()
send()
