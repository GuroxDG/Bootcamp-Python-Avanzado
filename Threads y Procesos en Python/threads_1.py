import time
from threading import Thread

def reading():
    time.sleep(3)
    print('Reading..')

def sleeping():
    time.sleep(3)
    print('Sleeping..')

start = time.time()

Thread_a = Thread(target=reading)
Thread_b = Thread(target=sleeping)

Thread_a.start()
Thread_b.start()

print(time.time()-start)

# 6.001855134963989 normal
# 0.0 Threads