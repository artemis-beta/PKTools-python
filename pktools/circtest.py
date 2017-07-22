from PKCircuit import *

b = Battery(10)

x = PKCircuit(b)

r1 = Resistor(10)
r2 = Resistor(10)
r3 = Resistor(10)
r4 = Resistor(10)

s = Switch()
l = Bulb(0.1)

x.addComponentInSeries(r1)
x.addComponentInSeries(s)
x.addComponentInSeries(l)

#x.addComponentsInParallel([r2, r3, r4])

x.printCircuit()
print x.R
