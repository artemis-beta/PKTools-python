import uuid
from pint import UnitRegistry
from math import pi

nu = UnitRegistry()

class Resistor:

    def __init__(self, resistance, name="{}".format(uuid.uuid4())):
        self.R = resistance*nu.ohm
        self.name = name
        self.type = "Resistor"
    self.symbol = "--===--"
    self.current = 0

    def setName(self, name):
        self.name = name

    def getVoltage(self, current):
        return current*self.R

    def getCurrent(self, voltage):
        return voltage*self.R    

    def getPower(self, current):
        return current*current*self.R


class Bulb(Resistor):
    def __init__(self, resistance):
        self.R = resistance*nu.ohms
        self.type = "Bulb"
        self.symbol = "--({})--".format(resistance)

class Inductor:
    def __init__(self, inductance, name="{}".format(uuid.uuid4())):
        self.L = inductance
        self.type = "Inductor"
        self.symbol = "--(((()--"

class Capacitor:
    def __init__(self, capacitance, name="{}".format(uuid.uuid4())):
        self.C = capacitance
        self.type = "Capacitor"
        self.symvol = "--||--"

class Switch:
    def __init__(self):
        self.state = True
        self.symbol = "--o__o--"
        self.type = "Switch"
 
    def On(self):
       self.state = True
       self.symbol = "--o__o--"

    def Off(self):
       self.state = False
       self.symbol = "--o/ o--"

    def Change(self):
       if self.state == True:
           self.state = False
           self.symbol = "--o/ o--"
       else:
           self.state = True
           self.symbol = "--o__o--"

class Wire:
   def __init__(self, material="Default", length=0.05*nu.meter, radius=1E-4*nu.meter):
       self.symbol = "----"
       if material == "Default":
           self.resistivity = 0
           self.R = 0*nu.ohm
       else:
           self.resistivity = material_dict[material]*nu.ohm*nu.meter
           self.R = self.resistivity*length*pow(pi*radius*radius,-1)     
class Battery:
    def __init__(self, voltage):
       self.symbol = "--|:--"
       self.V = voltage*nu.V    


class PKCircuit:
    def __init__(self, power_source):
        if isinstance(power_source, Battery):
           self.powerType = "DC"
        else:
           self.powerType = "AC"

        self.powerSource = power_source
        self.components = {'0' : self.powerSource}
        self.numComponents = 0
        self.R = 0*nu.ohm
    def addInSeries(self, other):
        if other.R != 0*nu.ohm:
            other.current = (self.powerSource.V)/other.R
            return self.R + other.R

    def addInParallel(self, other):
        combinedR = 0 
        for element in other:
            combinedR += pow(element.R, -1)
        return self.R + pow(combinedR, -1)
 

    def addComponentInSeries(self, component, wire=Wire()):
        self.numComponents += 1
        if component.type != "Switch":
            self.R = self.addInSeries(wire)
            self.R = self.addInSeries(component)
        self.components['{}'.format(self.numComponents)] = wire
        self.numComponents += 1
        self.components['{}'.format(self.numComponents)] = component

    def addComponentsInParallel(self, componentlist, wire=Wire()):
        alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.numComponents += 1
        self.R = self.addInSeries(wire)
        self.components['{}'.format(self.numComponents)] = wire
        self.numComponents += 1
        key = '{}'.format(self.numComponents)
        self.components[key] = {}
        self.R = self.addInParallel(componentlist)
        for i, element in enumerate(componentlist):
           self.components[key][key+alpha[i]] = element 
    
    def getResistance(self):
        return self.R

    def printComponents(self):
        print(self.components)

    def printCircuit(self):
        outstring = "o"
        for element in self.components:
            outstring += self.components[element].symbol
        outstring += "o"
        print(outstring)
