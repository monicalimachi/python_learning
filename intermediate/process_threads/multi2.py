from threading import Thread, Lock
import time
#Create global variable
database_value=0

def increase(lock):
    global database_value

    #adding locks manually
    #Use Lock to prevents another thread to access to this code at the same time
    """     lock.acquire()
    local_copy=database_value
    local_copy +=1
    time.sleep(0.1)
    database_value = local_copy
    lock.release() """
    
    #Adding locks another way:
    with lock:
        local_copy=database_value
        local_copy +=1
        time.sleep(0.1)
        database_value=local_copy

if __name__=="__main__":

    lock=Lock()                                        #Added for manually
    print('start value', database_value)
    thread1=Thread(target=increase, args=(lock,))
    thread2=Thread(target=increase, args=(lock,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()
    
    print('end value', database_value)
    print('end main')