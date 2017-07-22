from pktools import PKTriangle
from math import atan

triangle = PKTriangle(3,3,(4./3.)*atan(1),"SSA")
print("Triangle 1:\t%s" % triangle)
triangle2 = PKTriangle(2*atan(1),(4./3.)*atan(1),15.,"AAS")
print("Triangle 2:\t%s" % triangle2)
print("Is Right Angled?")
print triangle2.isRightAngled()
