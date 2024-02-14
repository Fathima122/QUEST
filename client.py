import socket
d=socket.socket()
# # #server bind port and client will ony connect to it
d.connect(('localhost',9999)) #ip address of server and the port number 
# ##to connect with
    


name=input('Enter your name : ')
# c.send((name))
d.send(bytes(name,'utf-8'))

# # # # # print(c.recv(1024))  # buffer size 
# # # # # # # # # # # printing b ie it is bytes to string for that decode it

# print(c.recv(1024).decode())


a="welcome"
print(a[1:5:1])

