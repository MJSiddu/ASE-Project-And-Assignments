import random
import sys

# Parent class Col
class Col(object):
  def __init__(self):
    self.n = 0

# Num class derived from Col
class Num(Col):
  # initialize
  def __init__(self):
    Col.__init__(self)
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

# main block
if __name__ == "__main__":
  nums = []
  # generate 100 random numbers
  for _ in range(100):
    nums.append(random.randint(1,100))
  
  mean = []
  sd = []

  obj = Num()  

  for i in range(1, 101):
    # invoke add
    obj.add(nums[i-1])
    if (i % 10 == 0):
      sd.append(obj.sd)
      mean.append(obj.mu)
    
  for i in range(100, 9, -1):
    if (i % 10 == 0):
      index = int(i / 10) - 1
      
      # print results
      print ("-------------------------------")
      if (round(mean[index],2) == round(obj.mu, 2)):
        print ("Mean is equal - {}".format(mean[index]))
      if (round(sd[index],2) == round(obj.sd, 2)):
        print ("SD is equal - {}".format(sd[index]))
        
    # invoke delete
    obj.delete(nums[i-1])

# Sym class derived from Col
class Sym(Col):
  def __init__(self):
    Col.__init__(self)
    pass

# Some class derived from Col
class Some(Col):
  def __init__(self):
    Col.__init__(self)
    pass
