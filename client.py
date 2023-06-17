import socket
from threading import Thread

# function to receive messages from the server
def recv():
    try:
        while True:
            msg = c.recv(1024)
            if not msg:
                break
            print(msg.decode())
    except:
        print("Connection closed")
        
# function to send messages to the server
def send():
    try:
        while True:
            msg = input()
            if (msg == "--"):
                c.close()
            msg = "Client:" + msg
            c.send(msg.encode())
    except:
        print("Connection closed")
        
# create a socket object
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 12345
c.connect((host, port))
print(f"Client started on port:{port}")

Thread(target=recv).start()
send()
