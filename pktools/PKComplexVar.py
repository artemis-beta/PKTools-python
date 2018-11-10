from math import pi, tan, atan

import logging
logging.basicConfig()

class PKComplexVar:
    def __init__(self,re=0,im=0):
        self._logger = logging.getLogger(__class__.__name__)
        self.real = re
        self.imaginary = im
        self.modulus = pow(self.real**2 + self.imaginary**2,0.5)
        if self.real is not 0:
            self.arg = tan(self.imaginary/self.real)
        else:
            self.arg = 0
    def getRe(self):
        return self.real

    def getIm(self):
        return self.imaginary

    def getMod(self):
        return self.modulus

    def getArg(self):
        return self.arg
    
    def returnString(self,option=0):
        outstring = ""
        if option is 0:
            if self.real is not 0 or self.imaginary is 0:
                outstring += "%f" % self.real
            if self.imaginary is not 0:
                if(self.imaginary > 0):
                    outstring += "+"
                outstring += "%fi" % self.imaginary

        elif option is 1:
            if self.imaginary is 0:
                outstring = "1"
            else:
                outstring += "%f*exp(" % self.modulus 
                if(self.arg < 0):
                    outstring += "-"
                outstring += str(self.arg) + "i)"
        
        elif option is 2:
            if self.imaginary is 0:
                outstring = "1"
            else:
                outstring += "%f*cos(%f)" % (self.real,self.arg)
                if self.imaginary > 0:
                    outstring += "+"
                outstring += "%fi*sin(%f)" % (self.imaginary,self.arg)
        return outstring
    def __str__(self):
        return self.returnString(0)
    def Print(self):
        print self.__str__()
    def __add__(self,param):
        temp = PKComplexVar(0,0)
        temp.real = self.real + param.real
        temp.imaginary = self.imaginary + param.imaginary
        return temp

    def __sub__(self,param):
        temp = PKComplexVar(0,0)
        temp.real = self.real - param.real
        temp.imaginary = self.imaginary - param.imaginary
        return temp

    def __mul__(self,param):
        temp = PKComplexVar(0,0)
        if isinstance(param,int) or  isinstance(param,float):        
            if self.real is not 0:
                temp.real = self.real*param
            if self.imaginary is not 0:
                temp.imaginary = self.imaginary*param
            return temp
        temp.real = (self.real*param.real)-(self.imaginary*param.imaginary)
        temp.imaginary = (self.real*param.imaginary + self.imaginary*param.real)
        return temp

    def Conjugate(self):
        temp = PKComplexVar(0,0)
        temp.real = self.real
        temp.imaginary = -1*self.imaginary
        return temp
    def __rmul__(self,param):
        return self.__mul__(param)
    def __div__(self,param):
        temp = PKComplexVar(0,0)
        if isinstance(param,int) or  isinstance(param,float):        
            if self.real is not 0:    
                temp.real = self.real/param
            if self.imaginary is not 0:    
                temp.imaginary = self.imaginary/param
            return temp
        modulus = self.modulus/param.modulus
        arg_temp = self.arg - param.arg
        temp.real = modulus/pow(1+atan(arg_temp),0.5)
        temp.imaginary = modulus*atan(arg_temp)/pow(1+pow(atan(arg_temp),2),0.5)
        return temp
