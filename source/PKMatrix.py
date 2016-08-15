from PKVar import *

class PKMatrix:
	def __init__(self,rows_columns=None):
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
		for i in range(0,len(self.elements)):
			print "(",
			for j in range(0,len(self.elements[0])):
				print self.elements[i][j].returnString(),
			print ")"	
	def __add__(self,param):
		if(len(param.elements) is not len(self.elements) and len(param.elements[0]) is not len(self.elements[0])):
			print "ERROR: Cannot add matrices of varying dimensions\n"
			return PKMatrix()
		new_list = []
		for i, k in zip(self.elements, param.elements):
			new_list.append([])
			for j, l in zip(i, k):
				new_list[-1].append(j+l)
	
		temp = PKMatrix(new_list)
		return temp

	def __sub__(self,param):
		
		if(len(param.elements) is not len(self.elements) and len(param.elements[0]) is not len(self.elements[0])):
			print "ERROR: Cannot subtract matrices of varying dimensions\n"
			return PKMatrix()
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

	def __mul__(self,param):

		if isinstance(param,float) or isinstance(param,int):
			new_list = []
			for i in range(0,len(self.elements)):
                                new_list.append([])
				for l in range(0,len(self.elements[0])):
					new_list[-1].append(self.elements[i][l]*param)
			temp = PKMatrix(new_list)
			return temp
		
		if(len(param.elements) is not len(self.elements[0])):
			print "ERROR: cannot multiply matrices with set dimensions\n"
			return PKMatrix()
		tranpose_param = param.Transpose()
		new_list = []
		for i in range(0,len(self.elements)):
			new_list.append([])
			for j in range(0,len(self.elements[0])):
				new_list[-1].append(PKVar(0,0))
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

	def Trace(self):
		x = PKVar(0,0)
		if(len(self.elements[0]) is not len(self.elements)):
			print "ERROR: Trace can only be calculated for a square matrix!\n"
			return PKVar(0,0)

		for i in range(0,len(self.elements)):
			x = x + self.elements[i][i]
		return x

	def Print(self):
		return self.__str__()	
