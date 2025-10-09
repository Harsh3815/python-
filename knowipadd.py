import socket
host = 'www.instagram.com'
try :
    addr = socket.gethostbyname(host)
    print("ip address:"+ addr)
except socket.gaierror:
    print("website not exist")
