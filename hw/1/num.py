import random
import sys

class Col(object):
  def __init__(self):
    self.n = 0

class Num(Col):
  def __init__(self):
    Col.__init__(self)
    self.mu = 0
    self.m2 = 0
    self.sd = 0

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

  def update_sd(self):
    self.sd = (self.m2 / (self.n - 1)) ** 0.5


if __name__ == "__main__":
  nums = []
  for _ in range(100):
    nums.append(random.randint(1,100))
  
  mean = []
  sd = []

  obj = Num()  

  for i in range(1, 101):
    obj.add(nums[i-1])
    if (i % 10 == 0):
      sd.append(obj.sd)
      mean.append(obj.mu)
    
  for i in range(100, 9, -1):
    if (i % 10 == 0):
      index = int(i / 10) - 1
      print ("-------------------------------")
      if (round(mean[index],2) == round(obj.mu, 2)):
        print ("Mean is equal - {}".format(mean[index]))
      if (round(sd[index],2) == round(obj.sd, 2)):
        print ("SD is equal - {}".format(sd[index]))
    obj.delete(nums[i-1])


class Sym(Col):
  def __init__(self):
    Col.__init__(self)
    pass
  
class Sym(Col):
  def __init__(self):
    Col.__init__(self)
    pass