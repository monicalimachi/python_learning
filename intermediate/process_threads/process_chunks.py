from multiprocessing import Pool
from unittest import result

#process pool - Create different chunks to process values in different processes in parallel
def cube(number):
    return number * number * number


if __name__=="__main__":

    numbers=range(10)
    pool=Pool()

    # map, apply, join, close
    result= pool.map(cube,numbers)
    #pool.apply(cube, numbers[0])        #this execute 1 argument
    
    pool.close()
    pool.join()

    print(result)