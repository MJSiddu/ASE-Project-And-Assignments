## Code

```python

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
      if (round(sd[index],2) == round(obj.sd, 2)):
        print ("-------------------------------")
        print ("Values are equal - {}".format(sd[index]))
      if (round(mean[index],2) == round(obj.mu, 2)):
        print ("-------------------------------")
        print ("Values are equal - {}".format(mu[index]))
    obj.delete(nums[i-1])


class Sym(Col):
  def __init__(self):
    Col.__init__(self)
    pass
  
class Some(Col):
  def __init__(self):
    Col.__init__(self)
    pass

```


## Output

```
-------------------------------
Mean is equal - 51.62
SD is equal - 29.666421517543462
-------------------------------
Mean is equal - 52.56666666666666
SD is equal - 30.103585213336785
-------------------------------
Mean is equal - 54.5
SD is equal - 30.3231540392169
-------------------------------
Mean is equal - 53.41428571428572
SD is equal - 30.440958704904588
-------------------------------
Mean is equal - 54.78333333333333
SD is equal - 29.869825864493112
-------------------------------
Mean is equal - 52.239999999999995
SD is equal - 29.32127457763634
-------------------------------
Mean is equal - 55.974999999999994
SD is equal - 29.882236812579425
-------------------------------
Mean is equal - 57.499999999999986
SD is equal - 29.481437760288987
-------------------------------
Mean is equal - 56.6
SD is equal - 29.19336622554767
-------------------------------
Mean is equal - 57.60000000000001
SD is equal - 34.712149650134506

```