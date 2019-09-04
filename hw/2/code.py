import random
import sys
import re

# Parent class Col
class Col(object):
  def __init__(self, n, col, text):
    self.n = n
    self.col = col
    self.text = text

class Tbl(object):

  def __init__(self, strData):
    self.data = strData
    self.cols = []
    self.rows =[]

  def read(self, file):
    pass

  def dump(self):
    pass


# Num class derived from Col
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

def compiler(x):
    "return something that can compile strings of type x"
    try: int(x); return int 
    except:
        try: float(x); return float
        except: return str

def string(s):
  "read lines from a string"
  for line in s.splitlines(): yield line

def file(fname):
  "read lines from a fie"
  with open(fname) as fs:
      for line in fs: yield line

def zipped(archive,fname):
  "read lines from a zipped file"
  with zipfile.ZipFile(archive) as z:
     with z.open(fname) as f:
        for line in f: yield line

def rows(src, 
         sep=     ",",
         doomed = r'([\n\t\r ]|#.*)'):
  "convert lines into lists, killing whitespace and comments"
  for line in src:
    line = line.strip()
    line = re.sub(doomed, '', line)
    if line:
      yield line.split(sep)

def cells(src):
  "convert strings into their right types"
  total = 0
  oks = None
  drop = []
  headers = []
  for n,cells in enumerate(src):
    if n==0:
        for i in range(len(cells)):
            if "?" in cells[i]:
                drop.append(i)
            else:
                headers.append(cells[i])
        total = len(headers)
        yield headers
    else:
       for i in range(len(drop)):
           del cells[drop[i]] 

       if (len(cells) != total):
           yield "E> skipping line {}".format(n+1)
       else:
           oks = [compiler(cell) for cell in cells]
           yield [f(cell) for f,cell in zip(oks,cells)]

def fromString(s):
  "putting it all together"
  for lst in cells(rows(string(s))):
    yield lst


# main block
if __name__=="__main__":
  s="""
  $cloudCover, ?$temp, $humid, $wind,  $playHours
  100,        68,    80,    0,    3   # comments
  0,          85,    85,    0,    0
  0,          80,    90,    10,   0
  60,         83,    86,    0,    4
  100,        70,    96,    0,    3
  100,        65,    70,    20,   0
  70,         64,    65,    15,   5
  0,          72,    95,    0,    0
  0,          69,    70,    0,    4
  80,         75,    80,    0,    3
  0,          75,    70,    18
  60,         72,    90,    10,   ?
  40,         81,    75,    0,    2    
  100,        71,    91,    15,   0
  """
 
  for lst in fromString(s):
    print(lst)