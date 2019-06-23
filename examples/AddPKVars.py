from pktools import PKVar

x = PKVar(100.,10.)
y = PKVar(56.,0.34)

print("Vector 1:")
print(x)

print("Vector 2:")
print(y)
z = x+y
print("\nAddition: ")
print(z)
z = x-y
print("\nSubtraction: ")
print(z)
z = x*y
print("\nMultiplication: ")
print(z)
z = x/y
print("\nDivision: ")
print(z)
