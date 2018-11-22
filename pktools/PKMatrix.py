import logging
logging.basicConfig()

class PKMatrix:
    def __init__(self,rows_columns=None):
        self._logger = logging.getLogger(__class__.__name__)
        if rows_columns is None:
            rows_columns = []
        self.elements = rows_columns
        self.outstring = ""
    def addRow(self,row):
        self.elements.append(row)
    def addColumn(self,column):
        for i in range(0,len(self.elements)-1):
            self.elements[i].append(column[i])
    def __str__(self):
        outputstring = ""
        for i in range(0,len(self.elements)):
            outputstring += "("
            for j in range(0,len(self.elements[0])):
                outputstring += "%s " % self.elements[i][j].__str__()
            outputstring +=  ")\n"    
        return outputstring
    def __add__(self,param):
        if(len(param.elements) is not len(self.elements) and len(param.elements[0]) is not len(self.elements[0])):
            self._logger.error("Cannot add matrices of varying dimensions")
            exit(1)
        new_list = []
        for i, k in zip(self.elements, param.elements):
            new_list.append([])
            for j, l in zip(i, k):
                new_list[-1].append(j+l)
    
        temp = PKMatrix(new_list)
        return temp

    def __sub__(self,param):
        
        if(len(param.elements) is not len(self.elements) and len(param.elements[0]) is not len(self.elements[0])):
            self._logger.error("Cannot subtract matrices of varying dimensions")
            exit(1)
        new_list = []
        for i, k in zip(self.elements, param.elements):
            new_list.append([])
            for j, l in zip(i, k):
                new_list[-1].append(j-l)
    
        temp = PKMatrix(new_list)
        return temp

    def Transpose(self):
            
        new_list = []
        for i in range(0,len(self.elements[0])):
            new_list.append([])
            for j in range(0,len(self.elements)):
                new_list[i].append(self.elements[j][i])
        temp = PKMatrix(new_list)    

        return temp

    def Conjugate(self):
        try:
            new_list = []
            for i in range(0,len(self.elements)):
                   new_list.append([])
                   for l in range(0,len(self.elements[0])):
                      new_list[-1].append(self.elements[i][l].Conjugate())
            temp = PKMatrix(new_list)
        except AttributeError:
            self._logger.error("Elements of PKMatrix not of type PKComplexVar")
            return PKMatrix()
        return temp

    def Dagger(self):
        temp = self.Conjugate()    
        temp = temp.Transpose()
        return temp
    def __mul__(self,param):

        if isinstance(param,float) or isinstance(param,int) or isinstance(param, PKComplexVar):
            new_list = []
            for i in range(0,len(self.elements)):
                new_list.append([])
                for l in range(0,len(self.elements[0])):
                    new_list[-1].append(self.elements[i][l]*param)
            temp = PKMatrix(new_list)
            return temp
        
        if(len(param.elements) is not len(self.elements[0])):
            self._logger.error("Cannot multiply matrices with set dimensions")
            return PKMatrix()
        tranpose_param = param.Transpose()
        new_list = []
        for i in range(0,len(self.elements)):
            new_list.append([])
            for j in range(0,len(self.elements[0])):
                new_list[-1].append(0*self.elements[0][0])
                for l in range(0,len(self.elements)):
                    new_list[-1][-1] = new_list[-1][-1] + self.elements[i][l]*param.elements[l][j]

        temp = PKMatrix(new_list)
        return temp
    def __rmul__(self,param):
        if isinstance(param,float) or isinstance(param,int):
                        new_list = []
                        for i in range(0,len(self.elements)):
                                new_list.append([])
                                for l in range(0,len(self.elements[0])):
                                        new_list[-1].append(self.elements[i][l]*param)
                        temp = PKMatrix(new_list)
                        return temp
    def __div__(self,param):
        
        if isinstance(param,float) or isinstance(param,int):
                        new_list = []
                        for i in range(0,len(self.elements)):
                                new_list.append([])
                                for l in range(0,len(self.elements[0])):
                                        new_list[-1].append(self.elements[i][l]/param)
                        temp = PKMatrix(new_list)
                        return temp

    def Trace(self):
        x = self.elements[0][0]
        if(len(self.elements[0]) is not len(self.elements)):
            self._logger.error("Trace can only be calculated for a square matrix!")
            return None

        for i in range(0,len(self.elements)):
            x = x + self.elements[i][i]
        return x

    def __iadd__(self,param):
        temp = self + param
        return temp
    
    def __isub__(self,param):
        temp = self - param
        return temp
    def __imul__(self,param):
        temp = self*param
        return temp
    
    def __pow__(self,index):
        temp = self
        for i in range(0,index):
            temp *= self
        return temp


def Commutator(a,b):
    return a*b - b*a
def Anticommutator(a,b):
    return a*b + b*a
