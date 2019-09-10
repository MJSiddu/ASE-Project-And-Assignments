from collections import defaultdict

class Abcd(object):
  def __init__(self, data="data", rx="rx"):
    self.a = defaultdict(int)
    self.b = defaultdict(int)
    self.c = defaultdict(int)
    self.d = defaultdict(int)
    self.known = defaultdict(int)
    self.data = data 
    self.rx = rx
    self.yes = self.no = 0

  def abcd1(self, want, got):
    self.known[want] += 1
    self.known[got] += 1
    if self.known[want] == 1:
      self.a[want] = self.yes + self.no
    if self.known[got] == 1:
      self.a[got] = self.yes + self.no

    if want == got:
      self.yes += 1
    else :
      self.no += 1
    
    for key in self.known.keys():
      if (want == key):
        if want == got:
          self.d[key] += 1 
        else:
          self.b[key] += 1
      else:
        if key == got:
          self.c[key] += 1
        else:
          self.a[key] += 1

  def abcdReport(self):
    print(" db   | rx | num |  a |  b |  c |  d | acc | pre |  pd |  pf |   f |   g | class")
    print(" ---- | -- | --- | -- | -- | -- | -- | --- | --- | --- | --- | --- | --- | -----")
    for x in self.known.keys():
      
      a = self.a[x]
      b = self.b[x]
      c = self.c[x]
      d = self.d[x]
      
      if b+d > 0:
        pd = d / (b+d) 
      
      if a + c > 0: 
        pf = c / (a + c)
        pn = ( b + d ) / ( a + c )
  
      if c + d > 0:
        prec = d / ( c + d )

      if 1 - pf + pd > 0: 
        g = 2 * ( 1 - pf ) * pd / (1 - pf + pd)

      if prec + pd > 0:
        f = 2 * prec * pd / (prec + pd)   

      if self.yes + self.no > 0: 
        acc = self.yes / (self.yes + self.no)
      
      print(" {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} ".format(
        self.data, self.rx, self.yes + self.no, a, b, c, d, round(acc, 2), round(prec, 2), round(pd, 2), round(pf, 2), round(f, 2), round(g, 2), x))

if __name__ == "__main__":
  obj = Abcd()
  for i in range(1, 7):
    obj.abcd1("yes", "yes")
  for i in range(1, 3):
    obj.abcd1("no", "no")
  for i in range(1, 6):
    obj.abcd1("maybe", "maybe")
  
  obj.abcd1("maybe", "no")
  obj.abcdReport()

  




