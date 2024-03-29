from threading import Thread, Lock, current_thread
from queue import Queue
import time

#uses FIFO example 1
""" 
if __name__=="__main__":
    q=Queue()
    q.put(1)
    q.put(2)
    q.put(3)

    #3 2 1 -->
    first = q.get()
    print(first)

    #q.task_done()
    #q.join() 

    print('end main') """

#Example2 : with queue we can easily change data, multiple threads print in same line 2 statements
def worker(q,lock):
    while True:
        value = q.get()
        #processing ...
        #Add with lock , and lock parameter to don't print in same thread data
        with lock:
            print(f'in {current_thread().name} got {value}')
        q.task_done()

if __name__=="__main__":
    q=Queue()
    lock=Lock()         #Adding lock
    num_threads = 10

    for i in range(num_threads):
        thread = Thread(target=worker,args=(q,lock))
        thread.daemon=True
        thread.start()
    
    for i in range(1, 21):
        q.put(i)
    
    q.join()
    print('end main')