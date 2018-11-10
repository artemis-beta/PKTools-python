from pktools.PKVar import *

import logging

logging.basicConfig()

class PKLorentzVector:
    def __init__(self,x0=PKVar(1,0),x1=PKVar(0,0),x2=PKVar(0,0),x3=PKVar(0,0)):
        self._logger = logging.getLogger(__class__.__name__)
        self.X = [x0,x1,x2,x3]
        try:
            assert x0 > x1 and x0 > x2 and x0 > x3
        except AssertionError:
            self._logger.error("x0 component of four vector must be greater than others. Got " +
                                ', '.join([i.__str__() for i in self.X]))
            exit(1)
        for i, arg in enumerate(self.X):
            if isinstance(arg, float) or isinstance(arg, int):
                self.X[i] = PKVar(arg, 0)
        self.magn_ = (self.X[0]**2-self.X[1]**2-self.X[2]**2-self.X[3]**2)**0.5
    
    @classmethod
    def fromDoubles(cls,x0,x1,x2,x3,x0err=0,x1err=0,x2err=0,x3err=0):
        return cls(PKVar(x0,x0err),PKVar(x1,x1err),PKVar(x2,x2err),PKVar(x3,x3err))
    
    def getMagnitude(self):
        return self.magn_

    def __add__(self,param):
        temp = PKLorentzVector()
        for i in range(0,3):
            temp.X[i] = self.X[i] + param.X[i]
        return temp

    def __sub__(self,param):
        temp = PKLorentzVector()
        for i in range(0,3):
            temp.X[i] = self.X[i] - param.X[i]
        return temp

    def __str__(self):
        return "({}, {}, {}, {})".format(self.X[0].__str__(),
                                         self.X[1].__str__(),
                                         self.X[2].__str__(),
                                         self.X[3].__str__())
