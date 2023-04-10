from threading import Thread
from time import sleep
import logging

logging.basicConfig(level=logging.DEBUG)

def first(sleepig_time:int):
    logging.debug('first')
    sleep(sleepig_time)
    logging.debug('sleep first')

def second(sleepig_time:int):
    logging.debug('second')
    sleep(sleepig_time)
    logging.debug('sleep second')

t1 = Thread(target=first, args=(3,))
t2 = Thread(target=second, args=(5,))

t1.start()
t2.start()
'''
end
DEBUG:root:first
DEBUG:root:second
DEBUG:root:sleep first
DEBUG:root:sleep second
'''

t1.join()#join to main thread
t2.join()

'''
DEBUG:root:first
DEBUG:root:second
DEBUG:root:sleep first
DEBUG:root:sleep second
end
'''

print ('end')


class TreadTest(Thread):

    def run(self) -> None:
        sleeping_time = self._args[0]
        logging.debug('third')
        sleep(sleeping_time)
        logging.debug('sleep third')

t3 = TreadTest(args=(3,))
t3.start()
t3.join()

