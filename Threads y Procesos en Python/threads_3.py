import time
from threading import Thread, Lock

lock = Lock()

class BankFacilito:

    def __init__(self) -> None:
        self.balance = 0

    def deposito(self):
        for _ in range(10_000_000):
            lock.acquire()
            self.balance += 1
            lock.release()
            
    def withdraw(self):
        for _ in range(10_000_000):
            with lock:
                self.balance -= 1
            
bank = BankFacilito()

start = time.time()

thread_a = Thread(target=bank.deposito)
thread_b = Thread(target=bank.withdraw)

thread_a.start()
thread_b.start()

thread_a.join()
thread_b.join()

print("Se demoró ",time.time()-start)

print(bank.balance)