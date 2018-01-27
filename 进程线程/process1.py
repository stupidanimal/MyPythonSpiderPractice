import os
from multiprocessing import Process
def run_proc(name):
    print('Child process {} ({}) Running...'.format(name,os.getpid()))

if __name__=='__main__':
    print('Parent process %s.'%os.getpid())
    for i in range(5):
        p = Process(target=run_proc,args=(str(i),))
        print('Process will start')
        p.start()
    p.join()
    print('Process end')