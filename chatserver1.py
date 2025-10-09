import socket
host = 'localhost'
port = 6767
s= socket.socket()
s.bind((host,port))
s.listen(1)
c,addr = s.accept()
print("a client connected")
while True:
    data = c.recv(1024)
    if not data:
        break
    print("From client: " + str(data.decode()))
    data1 = input("enter response:")
    c.send(data1.encode())
c.close()