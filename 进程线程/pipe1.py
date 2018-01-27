import multiprocessing
import random
import time,os

def proc_send(pipe,urls):
    for url in urls:
        print('Process{} send:{}'.format(os.getpid(),url))
        pipe.send(url)
        delay = random.random()
        time.sleep(delay)

def proc_recv(pipe):
    print('process startss')
    while True:
        print('Process{} rev:{}'.format(os.getpid(),pipe.recv()))
        time.sleep(0.1)


if __name__=='__main__':
    pipe = multiprocessing.Pipe()
    p2 =multiprocessing.Process(target = proc_recv,args=(pipe[1],))
    p1 = multiprocessing.Process(target=proc_send,args=(pipe[0],['url_'+str(i) for i in range(10)]))

    p2.start()
    p1.start()
    p1.join()
    p2.terminate()