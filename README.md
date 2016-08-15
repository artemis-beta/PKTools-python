# 2016 JCNK Hackathon Python Club: PKTools Library
Just a place for us to bolt together some code as part of training in our spare time.
## PKTriangle
A simple class which can be given either Side-Side-Angle (`"SSA"`) or Angle-Angle-Side (`"AAS"`) value combinations, the other values are then calculated to give a triangle:
```
PKTriangle(par1,par2,par3,"AAS")
```
an example can be found in the `examples` folder:
```
PKTriangle_Example.py
```

## PKVariables and PKLorentz Vector
Two classes have been added which allow the inclusion of errors alongside variables. The Lorentz Vector class `PKLorentzVector` allows construction of a four vector using four `PKVars` with variables and their respective errors. Two examples have been included to illustrate:
```
AddPKVars.py
```
```
LorentzVectors.py
```
which can be found in the `examples` folder.

## PKMatrix
A class that allows the construction of up to a 10x10 matrix using `PKVar` or `PKComplexVar` variables. Construction is through either manually creating a `columns[rows[]]`, list of lists, the length then being the number of columns, or by creating an empty instance:
```
matrix = PKMatrix()
matrix.addRow(PKComplexVar(1,0),PKComplexVar(0,0))
matrix.addRow(PKComplexVar(0,0),PKComplexVar(1,0))
```
this example being one of the Pauli matrices. 
