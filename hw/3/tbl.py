from helper import fromString, compiler
from num import Num
from sym import Sym
from row import Row

class Tbl(object):

  def __init__(self):
    self.cols = []
    self.rows = []
    self.goals = []
    self.xs = []
    self.nums = []
    self.syms = []
    self.min = []

  def read(self, data):
    self.data = []
    for lst in fromString(data):
      self.data.append(lst)
  
    # Generate the columns 
    if self.data:
      self.generateCols(self.data[0])

    # Add data to the columns 
    for i in range(1, len(self.data)):
      if(isinstance(self.data[i], list) == True):
        self.addRow(self.data[i])
        self.updateCols(self.data[i])

    
  def generateCols(self, colList):
    for i, col in enumerate(colList):
      if "<" in col or ">" in col or "$" in col:
        self.cols.append(Num(i, col))
        self.nums.append(i)
      else:
        self.cols.append(Sym(i, col))
        self.syms.append(i)

      if "<" in col or ">" in col or "!" in col:
        self.goals.append(i)
      else:
        self.xs.append(i)
      
      if "<" in col:
        self.min.append(i)

  def dump(self):
    print("\n")
    print("IN OUR IMPLEMENTATION, DROPPED COLUMNS ARE NOT CONSIDERED DURING COLUMN INDEXING")
    print("\n")
    print("EX: For the given column headers -- 'outlook, ?$temp,  <humid, wind, !play',") 
    print("Temp column will be dropped. After dropping the temp column, the index of humid column will be 2 according to our implementation and not 3 as shown in sample out")
    print("\n")
    print("So please verify the answers accordingly")
    print("\n")
    print("t.cols")
    for i in range(len(self.cols)):
      if isinstance(self.cols[i], Num):
        print("|   {}".format(i+1))
        print("|  |  add : Num1")
        print("|  |  txt: {}".format(self.cols[i].text))
        print("|  |  col :{}".format(self.cols[i].col + 1))
        print("|  |  m2 :{}".format(self.cols[i].m2))
        print("|  |  mu :{}".format(self.cols[i].mu))
        print("|  |  n :{}".format(self.cols[i].n))
        print("|  |  sd :{}".format(self.cols[i].sd))
      else:
        print("|   {}".format(i+1))
        print("|  |  add : Sym1")
        print("|  |  col :{}".format(self.cols[i].col + 1))
        print("|  |  txt: {}".format(self.cols[i].text))
        print("|  |  mode: {}".format(self.cols[i].mode))
        print("|  |  most: {}".format(self.cols[i].most))
        print("|  |  n :{}".format(self.cols[i].n))
        print("|  |  cnt :{}".format(self.cols[i].map))
    
    print("t.my")
    print("|   class: {}".format(len(self.cols)))
    print("|   goals: {}".format(self.goals))
    print("|   nums: {}".format(self.nums))
    print("|   syms: {}".format(self.syms))
    print("|   w : {} : -1".format(self.min))
    print("|   xs : {}".format(self.xs))
    
 

  def addRow(self, rowData):
      self.rows.append(Row(rowData))

  def updateCols(self, rowData):
    for i, val in enumerate(rowData):
      if i in self.nums:
        op = compiler(val)
        data = op(val)
        if not isinstance(data, str):
          self.cols[i].add(int(val))
      else:
        if "?" in str(val):
          pass
        else:
          self.cols[i].add(val)