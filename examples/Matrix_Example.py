from pktools import PKMatrix

a = PKMatrix()

print "Construct a 3x3 matrix:\n"
a.addRow([PKVar(12.,0.1),PKVar(15.,0.2),PKVar(11.,0.3)])
a.addRow([PKVar(5.,0.2),PKVar(7.,0.1),PKVar(9.,0.3)])
a.addRow([PKVar(10.,0.1),PKVar(5.,0.1),PKVar(8.,0.1)])

a.Print()

print "Construct another 3x3 matrix:\n"
b = PKMatrix()
b.addRow([PKVar(2.,0.1),PKVar(1.,0.2),PKVar(1.,0.3)])
b.addRow([PKVar(6.,0.2),PKVar(5.,0.1),PKVar(3.,0.3)])
b.addRow([PKVar(0.,0.1),PKVar(2.,0.1),PKVar(1.,0.1)])

b.Print()

print "Add them together:\n"
c = a+b
c.Print()
print "Multiply them together:\n"
d = a*b
d.Print()
print "Take the Transpose:\n"
c.Transpose().Print()
print "The Trace is:\n"
c.Trace().Print()
print "\nLets Try a 2x3 matrix\n"
d = PKMatrix()
d.addRow([PKVar(1.4,0.2),PKVar(5.8,0.2)])
d.addRow([PKVar(3.2,0.1),PKVar(1.5,0.4)])
d.addRow([PKVar(6.0,0.3),PKVar(5.6,0.1)])
d.Print()
print "Take the Transpose:\n"
d.Transpose().Print()
print "Can't do the Trace!\n"
d.Trace()
