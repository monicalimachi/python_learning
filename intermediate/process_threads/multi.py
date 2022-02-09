#Example for multiprocesing
""" from asyncio import threads
from multiprocessing import Process
import os
import time

#Add function
def square_numbers():
    for i in range(100):
        i*i
        time.sleep(0.1)


processes=[]
num_processes= os.cpu_count()

#Create processes
for i in range(num_processes):
    p=Process(target=square_numbers)
    processes.append(p)

#Start
for p in processes:
    p.start()

#join
for p in processes:
    p.join()
    
print('end main') """


# Example for multithreading
from threading import Thread
import os
import time

def square_numbers():
    for i in range(100):
        i*i
        time.sleep(0.3)


threads=[]
num_threads= 10

#Create threads
for i in range(num_threads):
    t=Thread(target=square_numbers)
    threads.append(t)

#Start
for t in threads:
    t.start()

#join
for t in threads:
    t.join()
    
print('end main')
