import socket
s=socket.socket()
# 2 parameter one is type of network(ipv4 
# or ipv6 )
# 2nd is type of n/w tcp or udp by default
#  it is tcp connection oriented

print('socket created')# it is server sockect 
# #it expect connections
# # bind socket with port number, it has ip 
# # address too

s.bind(('localhost',9999))# has to pas ip address
# # and prt number# # bcoz same machine is server and # client
# # can give any port number available# range(0-65535)
# # # dont use in 1000 bcz busy with# windows # # services etc
# # wait client to connect and sent number 
# # #no of clients to connect at a time
s.listen(3)
print('wait for coonections')
while True:
    # pass
    c,address=s.accept()# gives client socket
# # # # # # #  #    and its address
    print('connected with : ',address)
    # print('---------------------')
    print('connected with  : ',c)
    
# # # # # # # # # # #     
# # self generated port number of client 
# # # # # # # # # # # #----------------------
# # # # # # # # # # #     
# # to get name from client
    # n=c.recv(1024)
    # print('-----------',n)
    # nn=c.recv(1024).decode()
    # print('.........',nn)
    # print('connected with : ',address,nn)
    # c.send('welcome')
    c.send(bytes('welcome','utf-8'))
# # # # # # # # # # # # # #     # #to be send in byte and set it format too

# # # # # # # # # # # #     c.close()# to close the connection



# import socket 
# s=socket.socket()
# print('socket created')

# s.bind(('local host',9999))
# s.listen(3)
# print('wait for connections')
# while True:
#     c,address=s.accept()
#     print('connected with :',address)
#     print('connected with :',c)




