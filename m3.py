#!/bin/python3
import yara

class m3:

  def __init__(self,path):
    print("Bulding m3")
    self.yara_patterns = yara.compile(filepath=path)

  def yarunra(self,s):
    return(self.yara_patterns.match(s))
