from threading import Thread

def hola():
    v = [i for i in range(10000)]
    print(len(v))

a = Thread(target=hola, args=(), name='Thread-name')
a.start()
a.join()