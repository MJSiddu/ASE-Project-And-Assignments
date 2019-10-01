# Parent class Col
from  lib   import *

class Col(Pretty):
  def __init__(self, n, col, text):
    self.n = n
    self.col = col
    self.text = text

  
  def __add__(self,x):
    y = self.key(x)
    if y != THE.char.skip: 
      self.n += 1
      self.add(y)
    return x

  def __sub__(self,x):
    y = self.key(x)
    if y != THE.char.skip: 
      self.n -= 1
      self.sub(y)
    return x
  
  def xpect(self,another):
    n = self.n + another.n
    return self.n/n*self.variety() + another.n/n*another.variety()