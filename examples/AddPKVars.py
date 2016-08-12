import sys
sys.path.insert(0, '../source/')

from PKVar import *

x = PKVar(100.,10.)
y = PKVar(56.,0.34)

print "Vector 1:",
x.Print()
print "Vector 2:",
y.Print()
z = x+y
print "\nAddition: ",
z.Print()
z = x-y
print "\nSubtraction: ",
z.Print()
z = x*y
print "\nMultiplication: ",
z.Print()
z = x/y
print "\nDivision: ",
z.Print()
