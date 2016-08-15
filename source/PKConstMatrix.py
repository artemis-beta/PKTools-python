from PKMatrix import *
from PKComplexVar import *

#####PAULI########
def Pauli(label=0):
	temp = PKMatrix([])
	if label is 0:
		print "ERROR: Invalid option for 'Pauli', state 1,2,3 for x,y,z"
	elif label is 1:
		temp = PKMatrix([[PKComplexVar(1,0),PKComplexVar(0,0)],[PKComplexVar(0,0),PKComplexVar(1,0)]])
	elif label is 2:
		temp =  PKMatrix([[PKComplexVar(0,0),PKComplexVar(0,-1)],[PKComplexVar(0,1),PKComplexVar(0,0)]])
	elif label is 3:
		temp = PKMatrix([[PKComplexVar(1,0),PKComplexVar(0,0)],[PKComplexVar(0,0),PKComplexVar(-1,0)]])
	return temp
