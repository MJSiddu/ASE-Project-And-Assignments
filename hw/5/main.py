from div import Div
from lib import *
from num import Num
from sym import Sym

import random
r= random.random
seed=random.seed

def num(i):
  if i<0.4: return [i,     r()*0.1]
  if i<0.6: return [i, 0.4+r()*0.1]
  return           [i, 0.8+r()*0.1]

def x(n):
  seed(1)
  return  [      r()*0.05 for _ in range(n)] + \
          [0.2 + r()*0.05 for _ in range(n)] +  \
          [0.4 + r()*0.05 for _ in range(n)] +   \
          [0.6 + r()*0.05 for _ in range(n)] +    \
          [0.8 + r()*0.05 for _ in range(n)]

def xnum(n):
  return  [num(one) for one in x(n)]


def xsym(n):
  return  [sym(one) for one in xx(n)] * 5

def sym(i):
  if i<0.4: return [i, "a"]
  if i<0.6: return [i, "b"]
  return           [i, "c"]

def xx(n):
  seed(1)
  return  [      r()*0.05 for _ in range(n)] + \
          [0.2 + r()*0.05 for _ in range(n)] +  \
          [0.4 + r()*0.05 for _ in range(n)] +   \
          [0.6 + r()*0.05 for _ in range(n)] +    \
          [0.8 + r()*0.05 for _ in range(n)]


if __name__=="__main__":
  res_num = xnum(55)
  res_sym = xsym(55)
  
  # print(res_num)

  # obj = Div(lst = res_num , yis = Num, x=first, y=last)

  # print(res_sym)

  # obj = Div(lst = res_sym , yis = Sym, x=first, y=last)


  obj = Div(lst = res_num , yis = Num)

  print("----------------------------------------------------------------------------------------")
  print("----------------------------------------------------------------------------------------")

  obj = Div(lst = res_sym , yis = Sym)





