#!/bin/python

import multiprocessing
import m2
from time import sleep
from random import randint

def run_spot_run(s,q):
    m = m2.m2()
#    with self.l:
#        y = m3("/home/phenely/git/python/yara/rules.yara")
    print(s + " starting")
#    pool = Pool(processes=1)
    while True:
#        y1 = pool.apply_async(y.yarunra, (q.get()[0], ), callback=self.yara_callback)
        s = q.get()[0]
        if (s == "Hello World"):
            m.inspect("/home/phenely/git/python/yara/HelloWorld.txt")
        elif (s == "test"):
            m.inspect("/home/phenely/git/python/yara/test.txt")
        elif (s == "test2"):
            m.inspect("/home/phenely/git/python/yara/test2.txt")
        elif (s == "test3"):
            m.inspect("/home/phenely/git/python/yara/test3.txt")
        sleep(randint(0,14))

def put_spot_put(s,q):
    v = ["Hello World",
       "test",
       "test2",
       "test3"]
    print(s + " starting")
    while True:
        sleep(randint(0,9))
        i = randint(0,len(v))
        print(s + " putting " + v[i-1])
        q.put([v[i-1]])

def main():
    #m = m2.m2()
    q = multiprocessing.Queue()
    #m.run_spot_run("test",q)
    pool = [multiprocessing.Process(target=run_spot_run,args=("get-%i" % (i), q, )) for i in range(20)]
    pool1 = [multiprocessing.Process(target=put_spot_put,args=("put-%i" % (i), q, )) for i in range(5)]

    for p in pool:
        p.start()
    #for p in pool:
    #    p.join()

    for p in pool1:
        p.start()
    #for p in pool1:
    #    p.join()

if __name__ == '__main__':
    main()
