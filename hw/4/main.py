from zeroR import ZeroR
from nb import Nb
from abcd import Abcd

import os
import sys
from helper import fromString
 
def report(classifier, data, pre_train):
  model = classifier(data[0])
  abcd = Abcd()

  for i in range(1, pre_train+1):
    model.train(data[i])

  for i in range(pre_train+1, len(data)):
    actual, predicted = model.classify(data[i])
    abcd.abcd1(actual, predicted)
    model.train(data[i])
  
  abcd.abcdReport()


if __name__=="__main__":
  root = os.path.dirname(__file__)
  files = {
    "weathernon": os.path.join(root, 'data/weathernon.csv'),
    "diabetes": os.path.join(root, 'data/diabetes.csv')
  }

  classifiers = [ZeroR, Nb]
  pre_train = [[3, 4], [3,20]]
  counter = 0
  for filename, path in files.items():

    print("\n")
    print(filename)

    with open(path) as f:
      raw = f.read()
    data = []

    for lst in fromString(raw):
      data.append(lst)
    
    for pre, classifier in zip(pre_train[counter], classifiers):
      print(classifier.__name__)
      report(classifier, data, pre)
    counter += 1

  

