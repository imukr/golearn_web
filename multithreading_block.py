import logging
from threading import Thread, Lock
from time import time, sleep

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s %(message)s')
logger = logging.getLogger(__name__)

lock = Lock()


# def func(t: int, locker:Lock):
#     time1 = time()
#     lock.acquire()
#     sleep(t)
#     time2 = time()
#     lock.release()
#     logging.debug(f'{time2-time1}')

def func(t: int, locker:Lock):
    time1 = time()
    with locker:
        sleep(t)
        time2 = time()
    logging.debug(f'{time2-time1}')

t1 = Thread(target=func, args=(3, lock))
t2 = Thread(target=func, args=(5, lock))

t1.start()
t2.start()
t1.join()
t2.join()