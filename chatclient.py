import socket
host = 'localhost'
port = 6767
s = socket.socket()
s. connect((host,port))
str = input("enter data:")
while str !='exit':
    s.send(str.encode())
    data = s.recv(1024)
    print("from server:",data)
    str = input("enter data:")
s.close()

