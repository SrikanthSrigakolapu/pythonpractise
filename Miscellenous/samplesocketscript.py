import socket as sc

#sc.setdefaulttimeout(2)
s=sc.socket()
s.connect(("192.168.223.65",80))
print(s.recv(1024))