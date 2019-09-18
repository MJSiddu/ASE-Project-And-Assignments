import re

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

# def zipped(archive,fname):
#   "read lines from a zipped file"
#   with zipfile.ZipFile(archive) as z:
#      with z.open(fname) as f:
#         for line in f: yield line

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