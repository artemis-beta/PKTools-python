from math import *

class PKVar:

    def __init__(self,val,error):
        self.value = val
        self.error = error
    
    def GetVal(self):
        return self.value
    
    def GetError(self):
        return self.error

    def Power(self,x):
        temp = PKVar(0,1E-310)
        if (self.value is 0 and x < 1):
            return temp
        else:
            temp.error = x*pow(self.value,x-1)*self.error
        temp.value = pow(self.value,x)
        return temp
    
    def Sqrt(self):
        return self.Power(0.5)
    
    def __add__(self,param):
        temp = PKVar(0,0)
        temp.value = self.value + param.value
        temp.error = pow(pow(self.error,2)+pow(param.error,2),0.5)
        return temp
    
    def __sub__(self,param):
        temp = PKVar(0,0)
        temp.value = self.value - param.value
        temp.error = pow(pow(self.error,2)+pow(param.error,2),0.5)
        return temp

    def __mul__(self,param):
        
        temp = PKVar(0,0)
        if isinstance(param,int) or isinstance(param,float):
            temp.value = self.value*param
            temp.error = self.error*param    
            return temp
        temp.value = self.value * param.value
        temp.error = pow(pow(param.value*self.error,2)+pow(self.value*param.error,2),0.5);

        return temp

    def __rmul__(self,param):
        return self.__mul__(param)


    def __div__(self,param):
        
        temp = PKVar(0,0)
        if isinstance(param,int) or isinstance(param,float):
            temp.value = self.value/param
            temp.error = self.error/param
            return temp    
        temp.value = self.value / param.value
        temp.error = pow(pow(self.error/param.value,2)+pow(self.value*param.error,2)*pow(param.value,-4),0.5)
        return temp
    
    def __str__(self):
        return "%3f +/- %3f" % (self.value,self.error)
    def Print(self):        
        print("%3f +/- %3f" % (self.value,self.error))
