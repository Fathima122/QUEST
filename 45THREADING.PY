# creating threads without class

# import time
# import threading
# a=[1,2,3,4]

# def cube(n):
#     for i in n:
#         print('cube of : ',i**3)
#         print(threading.currentThread())
#         time.sleep(1)

# def square(h):
#     for i in h:
#         print('square of :',i**2)
#         # print(threading.currentThread())
#         time.sleep(1)
# cube(a)
# square(a)

# t1=threading.Thread(target=cube,args=(a,)) #ceating threads
# t1.start()
# t2=threading.Thread(target=square,args=(a,))
# t2.start()

# t1.setName('cube thread')
# print(threading.enumerate()) 

# creating threads with class 
# 


# from threading import Thread
# import time

# # # crate a class as subclass to Thread class
# class MyThread(Thread):

# # # override the run() method of thrad
#     def cube(self,b):

#         for i in b:
#             print('--------------------',i)
#             print('cube of  : ',i**3)
#             time.sleep(1)

#     def run(self):
#         # for i in range(1,6):
#         #     print(i)
#             time.sleep(3)
#             print('/////////////////////////')
#             a=(1,2,3,4)
#             self.cube(a)


# # create an instance of MyTHrad class
# t1=MyThread()
# t1.start()

# import threading
# x=0
# # lock
# def increment(lock):
#     global x
#     for i in range(10):
#         lock.acquire()
#         x+=1
        # print(x)
        # print(x,threading.currentThread())
#         lock.release()
# def main_task():
#     # global x
#     # x=0
#     lock=threading.Lock()
#     # t1=threading.Thread(target=increment)
#     # t2=threading.Thread(target=increment)
#     # # t2.setName('T2')
#     t1=threading.Thread(target=increment,args=(lock,))
#     t2=threading.Thread(target=increment,args=(lock,))
#     t1.start()
#     t2.start()
#     t1.join()
#     t2.join()

# for i in range(10):
#     main_task()
#     print('Iteration  {0}: x= {1}'.format(i,x))



# import threading 
# import time

# a=[1,2,3,4]
# def cube(m):
#     for i in m:
#         print('cube of :',i**3)
#         print(threading.currentThread())
#         time.sleep(1)

# def square(n):
#     for i in n:
#         print('square of : ' ,i**2)
#         print(threading.currentThread())
#         time.sleep(1)

# t1=threading.Thread(target=cube,args=(a,))
# t1.start()

# t2=threading.Thread(target=square,args=(a,))
# t2.start()
# t1.setName('cube thread')
# t2.setName('sq thread')
# print(threading.enumerate())


# cube(a)


# from threading import Thread
# import time

# class MyThread(Thread):
#     def cube(self,n):
#         for i in n:
#             print('cube of :', i**3)
#             time.sleep(2)
    


#     def run(self):
#         # for i in range(1,6):
#         #     print(i)
#         time.sleep(3)
#         a=[1,2,3,4]
#         self.cube(a)
# class SqThread(Thread):
        

#     def square(self,j):
#         for i in j:
#             time.sleep(2)
#             print('square of :', i**2)
#             # time.sleep(2)
    
        
#     def run(self):

#         b=[1,2,3,4]
#         self.square(b)



# t1=MyThread()
# t1.start()
# t2=SqThread()
# t2.start()
# #


# import threading
# x=0

# def thread_task(lock):
#     global x
#     for i in range(100000):
#         lock.acquire()
#         x+=1
#         lock.release()
# def main_task():
#     lock=threading.Lock()

#     t1=threading.Thread(target=thread_task,args=(lock,))
#     t2=threading.Thread(target=thread_task,args=(lock,))
#     t1.start()
#     t2.start()
#     t1.join()
#     t2.join()

# for i in range(10):
#     main_task()
#     print('{}'.format(x))