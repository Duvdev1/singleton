import time
from datetime import datetime


class MyTimer():
    _instance = None

    def __init__(self):
        raise RuntimeError('Call instance() instead')

    @classmethod
    def start_timer(cls):
        if cls._instance is None:
            cls._instance = cls.__new__(cls)
            cls._instance.time = datetime.now()
        return cls._instance

    def get_time(self):
        return datetime.now() - self._instance.time


timer1 = MyTimer.start_timer()

print('t1 vs t2')
time.sleep(1)
timer2 = MyTimer.start_timer()
print(timer1.get_time())
print(timer2.get_time())

print('t1 vs t3')
time.sleep(3)
timer3 = MyTimer.start_timer()
print(timer1.get_time())
print(timer3.get_time())
