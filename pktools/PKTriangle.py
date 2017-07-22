from math import pi,sin,cos,acos,asin,atan

def CosineRuleSide(side1,side2,angle):
        '''Calculates the 3rd Side of a Triangle Using the Cosine Rule
        
    CosineRuleSide(side1, side2, angle3)
        '''
        return pow(pow(side1,2)+pow(side2,2) - 2*side1*side2*cos(angle),0.5)

def CosineRuleAngle(side1,side2,side3):
        '''Calculates the 3rd Angle of a Triangle Using the Cosine Rule
        
    CosineRuleSide(side1, side2, side3)
        '''
        return acos((pow(side1,2)+pow(side2,2)-pow(side3,2))/(2*side1*side2))

class PKTriangle:
    '''PKTriangle Class for creating a Triangle Geometric Object

    PKTriangle(val1, val2, val3, Type='AAS')

    Type         Define Triangle either using the combination of two angles
                 and a single side 'AAS' or two sides and a single angle 'SSA'
    '''
    def __init__(self,val1,val2,val3,Type="AAS"):
        self.type_     = Type
        self.angles    = [0,0,0]
        self.sides     = [0,0,0]
        self.placement = [0,0]
        if(self.type_ is "AAS"):
        	self.angles[0] = val1*1.0
        	self.angles[1] = val2*1.0
        	self.sides[2] = val3*1.0
        	
        	self.angles[2] = pi - (val1+val2)
        	self.sides[1] = (self.sides[2]/sin(self.angles[2]))*sin(self.angles[1])
        	self.sides[0] = (self.sides[2]/sin(self.angles[2]))*sin(self.angles[0])
        
        elif(self.type_ is "SSA"):
        	self.sides[0] = val1*1.0
        	self.sides[1] = val2*1.0
        	self.angles[2] = val3*1.0
        
        	self.sides[2] = CosineRuleSide(self.sides[0],self.sides[1],self.angles[2])
        	self.angles[0] = asin((sin(self.angles[2])/self.sides[2])*self.sides[0])
        
        else:
        	print("ERROR: Invalid Type of '%s', options are 'AAS' or 'SSA'")
                        
    def __str__(self):
    	return "PKTriangle_%s(ANGLES%s,SIDES%s)" % (self.type_,self.angles,self.sides)
    
    def Print(self):
    	self.__str__()
    
    def isRightAngled(self):
    	for angle in self.angles:
    		if(angle > 0.5*0.99*pi and angle < 0.5*1.01*pi):
    			return True
    	return False
    
    def Place(self, location):
        self.placement = location
    
    def View(self):
        from numpy import array
        import matplotlib.pyplot as plt
    
        coord_1 = array(self.placement)
        coord_2 = array(self.placement)+array([cos(self.angles[0]),sin(self.angles[0])])
        coord_3 = array(self.placement)+array([self.sides[1],0])

        print(coord_1, coord_2, coord_3)
        plt.plot((coord_1[0], coord_2[0]), (coord_1[1], coord_2[1]), 'b-')
        plt.plot((coord_1[0], coord_3[0]), (coord_1[1], coord_3[1]), 'b-')
        plt.plot((coord_3[0], coord_2[0]), (coord_3[1], coord_2[1]), 'b-')
        plt.show()
