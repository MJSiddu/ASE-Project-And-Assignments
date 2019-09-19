# Num class derived from Col
from col import Col

class Num(Col):
  # initialize
  def __init__(self, col, text):
    Col.__init__(self, 0, col, text)
    self.mu = 0
    self.m2 = 0
    self.sd = 0

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
  def delete(self, val):
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

  def numLike(self, x):
    var = self.sd ** 2
    denom = (3.14159 * 2 * var) ** 0.5
    num = 2.71828 ** ( -(x - self.mu) ** 2 / (2 * var + 0.0001))
    return num / (denom + 10 ** -64)
