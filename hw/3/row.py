from helper import compiler

class Row(object):
  def __init__(self, data):
    self.cells = []
    for val in data:
      op = compiler(val)
      self.cells.append(op(val))

    self.cooked = []
    self.dom = 0