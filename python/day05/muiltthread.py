# coding:utf-8
import time
import random
import threading
import multiprocessing

class Concurrent:
    def __init__(self):
        self.gap = random.randint(1, 5)

    def damao_sleep(self):
        print('damao睡觉啦{0}'.format(self.gap))
        time.sleep(self.gap)
        print('damao睡醒啦')

    def ermao_sleep(self):
        print('ermao睡觉啦{0}'.format(self.gap))
        time.sleep(self.gap)
        print('ermao睡醒啦')

if __name__=='__main__':
    con=Concurrent()
    # 线程并行
    # thread = threading.Thread(target=con.damao_sleep)
    # thread.start()
    # thread = threading.Thread(target=con.ermao_sleep)
    # thread.start()
    # damao_sleep()
    # ermao_sleep()

    #  进程并行
    process=multiprocessing.Process(target=con.damao_sleep)
    process.start()
    process=multiprocessing.Process(target=con.ermao_sleep)
    process.start()