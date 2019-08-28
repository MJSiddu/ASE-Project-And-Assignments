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
      if(round(sd[index],2) == round(obj.sd, 2)):
        print ("-------------------------------")
        print ("Values are equal - {}".format(sd[index]))
    obj.delete(nums[i-1])


class Sym(Col):
  def __init__(self):
    Col.__init__(self)
    pass
  
class Sym(Col):
  def __init__(self):
    Col.__init__(self)
    pass

```


## Output

```
-------------------------------
Values are equal - 28.426556085975157
-------------------------------
Values are equal - 28.461703029260967
-------------------------------
Values are equal - 28.379210500075494
-------------------------------
Values are equal - 28.351301086403875
-------------------------------
Values are equal - 28.743262536513456
-------------------------------
Values are equal - 28.465202530493983
-------------------------------
Values are equal - 28.38995849926068
-------------------------------
Values are equal - 27.322699080754656
-------------------------------
Values are equal - 27.885621648742962
-------------------------------
Values are equal - 22.26207537495101

```