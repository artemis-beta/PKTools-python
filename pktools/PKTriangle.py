from math import pi,sin,cos,acos,asin,atan
import logging
logging.basicConfig()

def CosineRuleSide(side1,side2,angle):
    return pow(pow(side1,2)+pow(side2,2) - 2*side1*side2*cos(angle),0.5)
def CosineRuleAngle(side1,side2,side3):
    return acos((pow(side1,2)+pow(side2,2)-pow(side3,2))/(2*side1*side2))

class PKTriangle:
    def __init__(self,val1,val2,val3,Type="AAS"):
        self._logger = logging.getLogger(__class__.__name__)
        self.type_ = Type
        self.angles = [0,0,0]
        self.sides = [0,0,0]
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
            self._logger.error("Invalid Type of '%s', options are 'AAS' or 'SSA'")

    def __str__(self):
        return "PKTriangle_%s(ANGLES%s,SIDES%s)" % (self.type_,self.angles,self.sides)

    def Print(self):
        self.__str__()

    def isRightAngled(self):
        for angle in self.angles:
            if(angle > 0.5*0.99*pi and angle < 0.5*1.01*pi):
                return True
        return False

