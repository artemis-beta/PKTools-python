from pktools.PKMatrix import *
from pktools.PKComplexVar import *

import logging
logging.basicConfig()

#####PAULI########
def Pauli(label=0):
    _logger = logging.getLogger("Pauli")
    temp = PKMatrix([])
    if label is 0:
        _logger.error("Invalid option for 'Pauli', state 1,2,3 for x,y,z")
    elif label is 1:
        temp = PKMatrix([[PKComplexVar(1,0),PKComplexVar(0,0)],[PKComplexVar(0,0),PKComplexVar(1,0)]])
    elif label is 2:
        temp =  PKMatrix([[PKComplexVar(0,0),PKComplexVar(0,-1)],[PKComplexVar(0,1),PKComplexVar(0,0)]])
    elif label is 3:
        temp = PKMatrix([[PKComplexVar(1,0),PKComplexVar(0,0)],[PKComplexVar(0,0),PKComplexVar(-1,0)]])
    return temp

#####DIRAC########
def Dirac(label=-1):
	temp = PKMatrix([])
        _logger = logging.getLogger("Dirac")
	if label not in [0, 1, 2, 3, 4, 5]:
		_logger.error("Invalid option for 'Dirac', state 0,1,2,3,4,5")
                exit(1)
	elif label is 0:
		temp = PKMatrix([[PKComplexVar(1,0), PKComplexVar(0,0), PKComplexVar(0,0), PKComplexVar(0,0)],
				 [PKComplexVar(0,0), PKComplexVar(1,0), PKComplexVar(0,0), PKComplexVar(0,0)],
				 [PKComplexVar(0,0), PKComplexVar(0,0), PKComplexVar(-1,0), PKComplexVar(0,0)], 
				 [PKComplexVar(0,0), PKComplexVar(0,0), PKComplexVar(0,0), PKComplexVar(-1,0)]]) 
	elif label is 1:
		temp = PKMatrix([[PKComplexVar(0,0), PKComplexVar(0,0), PKComplexVar(0,0), PKComplexVar(1,0)],
				 [PKComplexVar(0,0), PKComplexVar(0,0), PKComplexVar(1,0), PKComplexVar(0,0)],
				 [PKComplexVar(0,0), PKComplexVar(-1,0), PKComplexVar(0,0), PKComplexVar(0,0)],
				 [PKComplexVar(-1,0), PKComplexVar(0,0), PKComplexVar(0,0), PKComplexVar(0,0)]]) 
	elif label is 2:
		temp = PKMatrix([[PKComplexVar(0,0), PKComplexVar(0,0), PKComplexVar(0,0), PKComplexVar(-1,0)],
				 [PKComplexVar(0,0), PKComplexVar(0,0), PKComplexVar(1,0), PKComplexVar(0,0)], 
				 [PKComplexVar(0,0), PKComplexVar(1,0), PKComplexVar(0,0), PKComplexVar(0,0)],
				 [PKComplexVar(-1,0), PKComplexVar(0,0), PKComplexVar(0,0), PKComplexVar(0,0)]]) 
	elif label is 3:
		temp = PKMatrix([[PKComplexVar(0,0), PKComplexVar(0,0), PKComplexVar(1,0), PKComplexVar(0,0)],
				 [PKComplexVar(0,0), PKComplexVar(0,0), PKComplexVar(0,0), PKComplexVar(-1,0)],
				 [PKComplexVar(-1,0), PKComplexVar(0,0), PKComplexVar(0,0), PKComplexVar(0,0)],
				 [PKComplexVar(0,0), PKComplexVar(1,0), PKComplexVar(0,0), PKComplexVar(0,0)]]) 
	elif label is 5:
		temp = PKMatrix([[PKComplexVar(0,0), PKComplexVar(0,0), PKComplexVar(1,0), PKComplexVar(0,0)],
				 [PKComplexVar(0,0), PKComplexVar(0,0), PKComplexVar(0,0), PKComplexVar(1,0)],
				 [PKComplexVar(1,0), PKComplexVar(0,0), PKComplexVar(0,0), PKComplexVar(0,0)],
				 [PKComplexVar(0,0), PKComplexVar(1,0), PKComplexVar(0,0), PKComplexVar(0,0)]]) 
	
	return temp

## DEFINE SPINORS

class Spinor:
	def __init__(self, type_, lorentz_vec, mass):
            
	    self._v_up = PKMatrix([[PKComplexVar(1,0)],
                                   [PKComplexVar(0,0)], 
                                   [PKComplexVar(lorentz_vec.X[3].value/(lorentz_vec.X[0].value+mass),0)],

    		                   [PKComplexVar(lorentz_vec.X[1].value/(lorentz_vec.X[0].value+mass),lorentz_vec.X[2].value/(lorentz_vec.X[0].value+mass))]])


	    self._type = None
		
	    if type_ == 'v1':
		self._type = self._v_up
		self.elements = self._type.elements

	def __rmul__(self, other):
		return other*self._type

	def __str__(self):
		return self._type.__str__()

	def Print(self):
		print(self.__str__())

	def Transpose(self):
		return self._type.Transpose()

## DEFINE DIRAC EQUATION MATRICES
def alpha(int_):
        _logger = logging.getLogger("Dirac:alpha")
	try:
		return Dirac(int_)
	except:
		_logger.error("Invalid Integer")
                exit(1)

def beta():
	return Dirac(0)

def g():
	temp = PKMatrix([[PKComplexVar(1,0), PKComplexVar(0,0), PKComplexVar(0,0), PKComplexVar(0,0)],
                         [PKComplexVar(0,0), PKComplexVar(-1,0), PKComplexVar(0,0), PKComplexVar(0,0)],
                         [PKComplexVar(0,0), PKComplexVar(0,0), PKComplexVar(-1,0), PKComplexVar(0,0)],
                         [PKComplexVar(0,0), PKComplexVar(0,0), PKComplexVar(0,0), PKComplexVar(-1,0)]])
	return temp		
