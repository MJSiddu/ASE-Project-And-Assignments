from tbl import Tbl
from collections import defaultdict

import math

class Nb(object):

  def getTbl(self):
    tbl = Tbl()
    tbl.generateCols(self.cols)
    return tbl

  def __init__(self, cols):
    self.cols = cols
    self.things = {}
    self.tbl = self.getTbl()
    self.goalIndex = self.tbl.goals[0]

    self.n = -1
    self.m = 2
    self.k = 1

  def ensureClassExists(self, _class):
    if _class not in self.things.keys():
      self.things[_class] = self.getTbl()

  def train(self, row):
    curr_class = row[self.goalIndex]
    self.ensureClassExists(curr_class)
    self.things[curr_class].addRow(row)
    self.tbl.addRow(row)
    self.n += 1

  def classify(self, row):
    most = -float('inf')
    guess = None
    for _class in self.things.keys():
      guess = _class if guess is None else guess
      like = self.bayestheorem(row, _class)
      if like > most:
        most = like
        guess = _class
    
    return row[self.goalIndex], guess

  def bayestheorem(self, row, _class):
    like = prior = (len(self.things[_class].rows) + self.k) / (self.n + self.k + len(self.things))
    like = math.log(like)
    curr_tbl = self.things[_class]
    for c in curr_tbl.xs:
      x = row[c]
      if c in curr_tbl.nums:
        temp = curr_tbl.cols[c].numLike(x)
        if temp != 0:
          like += math.log(temp)
      else:
        like += math.log(curr_tbl.cols[c].symLike(x, prior, self.m))
    return like



