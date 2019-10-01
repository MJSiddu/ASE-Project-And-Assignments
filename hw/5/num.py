# Num class derived from Col
from col import Col
from  lib   import *
import math

class Num(Col):
  # initialize
  def __init__(self, inits=[], col=0, text="", w=1,key=same):
    Col.__init__(self, 0, col, text)
    self.key = key 
    self.rank, self.like = 1,1
    self.w = w
    self.lo, self.hi = 10 ** 32, -10 ** 32
    self.mu = 0
    self.m2 = 0
    self.sd = 0
    [self + x for x in inits]

  # add function
  def add(self, val):
    self.n += 1
    d1 = val - self.mu
    self.mu += d1 / self.n
    d2 = val - self.mu
    self.m2 += d1 * d2

    # Update sd
    if (self.m2 < 0 or self.n < 2):
      self.sd = 0
      return

    self.update_sd()
  
  # delete function
  def sub(self, val):
    if (self.m2 < 0 or self.n < 2):
      self.sd = 0
      return  

    self.n -= 1
    d1 = val - self.mu
    self.mu -= d1 / self.n
    d2 = val - self.mu
    self.m2 -= d1 * d2

    # Update sd
    self.update_sd()

  # update function (helper)
  def update_sd(self):
    self.sd = (self.m2 / (self.n - 1)) ** 0.5

  def variety(self): 
    return self.sd

  def sd(self):
    return self.sd

  def numLike(self, x):
    var = self.sd ** 2
    denom = (3.14159 * 2 * var) ** 0.5
    num = 2.71828 ** ( -(x - self.mu) ** 2 / (2 * var + 0.0001))
    return num / (denom + 10 ** -64)
