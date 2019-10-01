# Sym class derived from Col
import math
from  lib   import *
from col import Col


class Sym(Col):
  # initialize
  def __init__(self, inits=[], col=0, text="", w=1,key=same):
    Col.__init__(self, 0, col, text)
    self.key = key 
    self.rank, self.like = 1,1
    self.w = w
    self.map = {}
    self.mode = None
    self.most = 0
    [self + x for x in inits]

   # add function
  def add(self, val):
    self.n += 1
    self.count = 0
    if val in self.map.keys(): 
        self.count = self.map[val] + 1
        self.map[val] = self.count
    else: 
        self.count = 1
        self.map[val] = self.count

    if self.count > self.most:
      self.mode = val
      self.most = self.count
  
  def variety(self): 
    return self.symEnt()

  def symEnt(self):
    res = 0
    for i in self.map.keys():
      p = self.map[i]/self.n
      if p > 0:
        res -= (p)*(math.log(p)/math.log(2))
    return res

  def symLike(self, x, prior, m):
    f = self.map[x] if x in self.map else 0
    return (f + m * prior) / (self.n + m)

  def sub(self, val):
    self.n -= 1
    self.count = 0
    if val in self.map.keys() and self.map[val] > 0: 
        self.count = self.map[val] - 1
        self.map[val] = self.count
    else: 
        self.map[val] = self.count
        del self.map[val]
    
    temp_mode = None
    temp_most = 0
    for val in self.map.keys():
      if self.map[val] > temp_most:
        temp_most = self.map[val]
        temp_mode = val
    self.mode = temp_mode
    self.most = temp_most