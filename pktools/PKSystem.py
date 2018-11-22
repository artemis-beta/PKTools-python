from pktools.PKVar import PKVar
from pktools.PKMatrix import PKMatrix

class PKObject:
    def __init__(self, pk_coord_matrix, forces, mass):
        self._coordinates = pk_coord_matrix
        assert isinstance(self._coordinates, PKMatrix), "ERROR: Coordinate must be of type 'PKMatrix'"
        self._x = pk_coord_matrix.elements[0][0]
        self._y = pk_coord_matrix.elements[0][1]
        self._z = pk_coord_matrix.elements[0][2]
        self._force_list = forces
        self._Fx = PKVar(0,0)
        self._Fy = PKVar(0,0)
        self._Fz = PKVar(0,0)

        self.boundary = None

        self._mass = mass if isinstance(mass, PKVar) else PKVar(mass,0)
        
        for force in self._force_list:
            assert isinstance(force, PKMatrix), "ERROR: Force must be of type 'PKMatrix'"
            self._Fx += force.elements[0][0]
            self._Fy += force.elements[0][1]
            self._Fz += force.elements[0][2]

        self._Force = PKMatrix([self._Fx, self._Fy, self._Fz])

    def getForce(self):
        return self._Force
  
    def getAcceleration(self):
        return self._Force/self._mass

    def getMass(self):
        return self._mass

    def isTouching(self, other, radius):
        return self.boundary(radius, other)

    def _bound_circ(self, radius, i):
        if radius > pow((self._x+i[0].value)**2+(self._y+i[1].value)**2,0.5) and radius > pow((self._x+i[0].value)**2+(self._z+i[2].value)**2,0.5) and radius > pow((self._y+i[1].value)**2+(self._z+i[2].value)**2,0.5):
            return True
        else:
            return False

    def _bound_rect(self, radius, i):
        if i[0].value <= self._x+radius and i[0].value >= self._x-radius and i[1].value <= self._y+radius and i[1].value >= self._y-radius and i[2].value <= self._z+radius and i[2].value >= self._z-radius:
             return True
        else:
             return False


    def isCircle(self, radius):
        self.boundary = self._bound_circ

    def isSquare(self, radius):
        self.boundary = self._bound_rect

class PKSystem:
    def __init__(self):    
        self._objects = {}
