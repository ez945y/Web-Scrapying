from threading import Thread, Lock
from random import randint
from time import time, sleep

class thread(Thread):
    def __init__(self, acc, money):
        super().__init__()
        self._account = acc
        self._money = money

    def run(self):
        self._account.deposit(self._money)

class Account(object):
    def __init__(self):
        self._balance = 0
        self._lock = Lock()
    def deposit(self, money):
        self._lock.acquire()
        try:
            sleep(0.01)
            self._balance += money
        finally:
            self._lock.release()
    @property
    def balance(self):
        return self._balance


def main():
    acc = Account()
    lis = []
    for _ in range(100):
        t= thread(acc,1)
        lis.append(t)
        t.start()
    for t in lis:
        t.join()
    print("帳戶餘額為%d元" % acc.balance)

if __name__ == '__main__':
    main()