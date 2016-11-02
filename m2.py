#!/bin/python3
from multiprocessing import Lock,Pool
from time import sleep
from random import randint
from m3 import m3

class m2:

  def __init__(self):
    print("Bulding m2")
    self.l = Lock()
    self.v = ["/home/phenely/git/python/yara/HelloWorld.txt",
              "/home/phenely/git/python/yara/test.txt",
              "/home/phenely/git/python/yara/test2.txt",
              "/home/phenely/git/python/yara/test3.txt"]
    self.y = m3("/home/phenely/git/python/yara/rules.yara")

  def yara_callback(self,results):
    if results is not None and results != {}:
      print(results)

  def run_spot_run(self,s,q):
    with self.l:
      y = m3("/home/phenely/git/python/yara/rules.yara")
    print(s + " starting")
    pool = Pool(processes=1)
    while True:
      y1 = pool.apply_async(y.yarunra, (q.get()[0], ), callback=self.yara_callback)
      sleep(randint(0,14))

  def put_spot_put(self,s,q):
    print(s + " starting")
    while True:
      sleep(randint(0,9))
      i = randint(0,len(self.v))
      print(s + " putting " + self.v[i-1])
      q.put([self.v[i-1]])

  def inspect(self,p):
    pool = Pool(processes=1)
    y1 = pool.apply_async(self.y.yarunra, (p, ), callback=self.yara_callback)
    pool.close()
    pool.join()
