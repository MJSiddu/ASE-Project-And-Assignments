from helper import fromString, compiler
from num import Num
from row import Row

class Tbl(object):

  def __init__(self):
    self.cols = []
    self.rows =[]

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
      self.cols.append(Num(i, col))

  def dump(self):
    print("t.cols")
    for i in range(len(self.cols)):
      print("|   {}".format(i+1))
      print("|  |  txt: {}".format(self.cols[i].text))
      print("|  |  col :{}".format(self.cols[i].col + 1))
      print("|  |  m2 :{}".format(self.cols[i].m2))
      print("|  |  mu :{}".format(self.cols[i].mu))
      print("|  |  n :{}".format(self.cols[i].n))
      print("|  |  sd :{}".format(self.cols[i].sd))
    print("t.rows")
    for i in range(len(self.rows)):
      print("|   {}".format(i+1))
      print("|  |  dom: {}".format(self.rows[i].dom))
      print("|  |  cooked :{}".format(self.rows[i].cooked))
      print("|  |  cells :{}".format(self.rows[i].cells))

  def addRow(self, rowData):
      self.rows.append(Row(rowData))

  def updateCols(self, rowData):
    for i, val in enumerate(rowData):
      op = compiler(val)
      data = op(val)
      if not isinstance(data, str):
        self.cols[i].add(int(val))