from pktools.PKVar import PKVar

class PKLorentzVector:

	def __init__(self,x0=PKVar(0,0),x1=PKVar(0,0),x2=PKVar(0,0),x3=PKVar(0,0)):
		self.X = [x0,x1,x2,x3]
		self.magn_ = pow(x0*x0-x1*x1-x2*x2-x3*x3, 0.5)
	
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

	def Print(self):
		print("({}, {}, {}, {})".format(self.X[0], self.X[1], self.X[2], self.X[3]))
