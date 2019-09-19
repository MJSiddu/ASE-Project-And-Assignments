from tbl import Tbl

class ZeroR(object):
  def __init__(self, cols):
    self.tbl = Tbl()
    self.tbl.generateCols(cols)
    self.goalIndex = self.tbl.goals[0]
  
  def train(self, row):
    self.tbl.addRow(row)

  def classify(self, row):
    return row[self.goalIndex], self.tbl.cols[self.goalIndex].mode