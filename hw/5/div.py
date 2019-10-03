import math

from lib import THE, Pretty, same, first, last, ordered
from sym import Sym
from num import Num
import copy


class Div(Pretty):

    def check(self, r, l):
        return abs(r.mu - l.mu) >= self.epsilon

    def __divide(self, lo, hi, xr, yr, rank):
        "Find a split between lo and hi, then recurse on each split."
        xb4 = copy.deepcopy(xr)
        xb4.stats = copy.deepcopy(yr)
        xl = self.xis(key=self.x)
        yl = self.yis(key=self.y)
        best = yr.variety()
        cut = None
        for j in range(lo,hi):
            xl + self._lst[j]
            yl + self._lst[j]
            xr - self._lst[j]
            yr - self._lst[j]

            if xl.n >= self.step:
                if xr.n >= self.step:
                    now = self.x(self._lst[j-1])
                    after = self.x(self._lst[j])
                    if now == after:
                        continue
                    if self.check(xr, xl):
                        if after - self.start >= self.epsilon:
                            if self.stop - now >= self.epsilon:
                                xpect = yl.xpect(yr)
                                if xpect*THE.div.trivial < best:
                                    best, cut = xpect, j
        if cut:
            ls, rs = self._lst[lo:cut], self._lst[cut:hi]
            if self.yis == Num:
                print(str(rank) + ' x.n    ' + str(cut - lo) + ' | x.lo ' + str(round(self._lst[lo][0], 5)) + '  x.hi ' + str(round(self._lst[cut-1][0], 5))
                    + ' | y.lo ' + str(round(self._lst[lo][1], 5)) + ' y.hi ' + str(round(self._lst[cut-1][1], 5)))
            if self.yis == Sym:
                cur = self._lst[lo:cut]
                cur_y = [ x[1] for x in cur ]
                sym_obj = self.yis(cur_y)
                print(str(rank) + ' x.n    ' + str(cut - lo) + ' | x.lo ' + str(round(self._lst[lo][0], 5)) + '  x.hi ' + str(round(self._lst[cut-1][0], 5))
                    + ' | y.mode ' + str(sym_obj.mode) + ' y.ent ' + str(sym_obj.symEnt()))

            rank = self.__divide(lo, cut, self.xis(ls, key=self.x), self.yis(ls, key=self.y), rank) + 1
            rank = self.__divide(cut, hi, self.xis(rs, key=self.x), self.yis(rs, key=self.y), rank)
        else:
            xb4.rank = rank
            self.ranges += [ xb4 ]
        return rank


    def __init__(self, lst, yis, xis = Num, x=first, y=last):
        self.x, self.xis = x, xis
        self.y, self.yis = y, yis
        self._lst = ordered(lst,key=x)
        self.xs = self.xis(self._lst,key=x)
        self.ys = self.yis(self._lst,key=y)
        self.gain     = 0                             
        self.step     = int(len(self._lst)**THE.div.min) 
        self.stop     = x(last(self._lst))               
        self.start    = x(first(self._lst))              
        self.ranges   = []    
        self.epsilon  = self.xs.sd * THE.div.cohen     
        self.__divide(1, len(self._lst), self.xs, self.ys, 1) 
