import math

from lib import THE, Pretty, same, first, last, ordered
from sym import Sym
from num import Num


class Div(Pretty):
    def check(self, r, l):
        if(self.yis == Num):
            return abs(r.sd - l.sd) >= self.epsilon
        else:
            return abs(r.symEnt() - l.symEnt()) >= self.epsilon
    
    def get_int(self, r):
        if(isinstance(r, int) or isinstance(r, float)):
            return r
        else:
            return ord(r)

    def __divide(self, lo, hi, b4, rank):
        "Find a split between lo and hi, then recurse on each split."
        l = self.yis(key=self.y)
        r = self.yis(self._lst_y[lo:hi], key=self.y)
        best = b4.variety()
        cut = None
        for j in range(lo, hi):
            l + self._lst_y[j]
            r - self._lst_y[j]
            if l.n >= self.step:
                if r.n >= self.step:
                    now = self.y(self._lst_y[j-1])
                    after = self.y(self._lst_y[j])
                    if now == after:
                        continue
                    if self.check(r, l):
                        if self.get_int(after) - self.get_int(self.start) >= self.epsilon:
                            if self.get_int(self.stop) - self.get_int(now) >= self.epsilon:
                                xpect = l.xpect(r)
                                if xpect*THE.div.trivial < best:
                                    best, cut = xpect, j
        if cut:
            ls, rs = self._lst_y[lo:cut], self._lst_y[cut:hi]
            if self.yis == Num:
                print(str(rank) + ' x.n    ' + str(cut - lo) + ' | x.lo ' + str(round(self._lst_x[lo], 5)) + '  x.hi ' + str(round(self._lst_x[cut-1], 5))
                    + ' | y.lo ' + str(round(self._lst_y[lo], 5)) + ' y.hi ' + str(round(self._lst_y[cut-1], 5)))
            if self.yis == Sym:
                sym_obj = self.yis(self._lst_y[lo:cut])
                print(str(rank) + ' x.n    ' + str(cut - lo) + ' | x.lo ' + str(round(self._lst_x[lo], 5)) + '  x.hi ' + str(round(self._lst_x[cut-1], 5))
                    + ' | y.mode ' + str(sym_obj.mode) + ' y.ent ' + str(sym_obj.symEnt()))

            rank = self.__divide(lo, cut, self.yis(ls, key=self.y), rank) + 1
            rank = self.__divide(cut, hi, self.yis(rs, key=self.y), rank)
        else:
            self.gain += b4.n * b4.variety()
            b4.rank = rank
            self.ranges += [b4]
        return rank

    def __init__(self, lst, yis, x=same, y=same):

        self.x_list = [i[0] for i in lst]

        self.y_list = [i[1] for i in lst]

        self.yis = yis

        self._lst_x = ordered(self.x_list, key=x)
        self._lst_y = ordered(self.y_list, key=y)

        self.b4 = self.yis(self._lst_y, key=y)
        self.gain = 0
        self.x = x
        self.y = y
        self.step = int(len(self._lst_y)**THE.div.min)
        self.stop = y(last(self._lst_y))
        self.start = y(first(self._lst_y))
        self.ranges = []
        self.epsilon = self.b4.variety() * THE.div.cohen
        self.__divide(1, len(self._lst_y), self.b4, 1)
        self.gain /= len(self._lst_y)
