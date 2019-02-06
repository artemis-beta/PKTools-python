from pktools import PKLorentzVector, PKVar

a = PKLorentzVector(PKVar(493.,2.),PKVar(-5.6,0.1),PKVar(1.8,0.1),PKVar(0,0))
b = PKLorentzVector(PKVar(511.,3.),PKVar(5.6,0.1),PKVar(-1.8,0.1),PKVar(0,0))
print("Lorentz Vector 1: ")
a.Print()
print("Lorentz Vector 2: ")
b.Print()
print("Addition: \n")
c = a+b
c.Print()
