# This context will close the file, even exceptions happens

with open('notest.txt', 'w') as file:
    file.write('some todo...')

# This will be executed it doesn't matter what
file = open('notest.txt','w')
try:
    file.write('some todo...')
finally:


# Lock option multithread, multiprocess
from threading import Lock
lock = Lock()
lock.acquire()              # always add both acquire and release to close Lock
#
lock.release()

# using is another way to do
with lock:  
    # some thing

# use class a as context manager
class ManagedFile:
    def __init__(self, filename):
        print('init')
        self.filename = filename

    def __enter__(self):
        print('enter')
        self.file=open(self.filename,'w')
        return self.file

    def __exit__(self, exc_type,exc_value,exc_traceback):
        if self.file:
            self.file.close()
        if exc_type is not None:
            print('exception has been handled')
        #print('exc:', exc_type,exc_value)
        print('exit')
        return True
with ManagedFile('notes.txt') as file:
    print('do some stuff...')
    file.write('some todo...')
    file.somemethod()
print('continuing')