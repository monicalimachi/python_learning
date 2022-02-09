from multiprocessing import Process, Value, Array, Lock
import time

# Create for single value
""" def add_100(number,lock):
    for i in range(100):
        time.sleep(0.01)

        #lock.acquire()                  #When use lock.acquire always uses lock.release to close
        #number.value+=1
        #lock.release() 
        
        with lock:                          #Another way to use lock 
            number.value+=1

if __name__=="__main__":
    lock=Lock()                     #Add Lock option to prevent different processes run in same thread
    shared_number=Value('i',0)
    print('Number at beginning is', shared_number.value)

    p1= Process(target=add_100, args=(shared_number,lock))
    p2= Process(target=add_100, args=(shared_number,lock))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print('number at end is: ', shared_number.value) """

#Create function for an Array and add values
def add_100(numbers,lock):
    for i in range(100):
        time.sleep(0.01)
        for i in range(len(numbers)):
            with lock:
                numbers[i]+=1

if __name__=="__main__":

    lock=Lock()
    shared_array=Array('d',[0.0,100.0,200.0])
    print('array at the beginning is', shared_array[:])

    p1= Process(target=add_100, args=(shared_array,lock))
    p2= Process(target=add_100, args=(shared_array,lock))
    p3= Process(target=add_100, args=(shared_array,lock))

    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()

    print('array at end is: ', shared_array[:])
