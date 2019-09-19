# Sym class derived from Col
import math
from col import Col

class Sym(Col):
  # initialize
  def __init__(self, col, text):
    Col.__init__(self, 0, col, text)
    self.mode = 0
    self.most = 0
    self.map = {}

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

  def symEnt(self):
    res = 0
    for i in self.map.keys():
      p = self.map[i]/self.n
      res -= (p)*(math.log(p)/math.log(2))
    return res

  def symLike(self, x, prior, m):
    f = self.map[x] if x in self.map else 0
    return (f + m * prior) / (self.n + m)
