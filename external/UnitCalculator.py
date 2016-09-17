# The MIT License (MIT)
#
# Copyright (c) 2013 Stefan Reiterer  - maldun.finsterschreck@gmail.com
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

# This Module enables unit conversion

class PhysicalUnit(object):
    """
    Base class for physical units.
    """

    def __init__(self,factor = 1.0):
        """
        Constructor for deriving SI units.
        Factor is initiated with 1.
        """
        self.factor = factor

    def __call__(self,other = None):
        """
        Call method that can be passed on
        """
        if other is None: # SelfConversion
            other = auto_converter.getCorrectUnit(self)

        if isinstance(other,type(self)):
            return self.factor/other.factor
        else:
            raise ValueError("Error: Not the correct units!")

    def __mul__(self,other):
        """
        Overload multiplication to enable unit algebra. 
        """
        if isinstance(other,PhysicalUnit):
            correct = auto_converter.getCorrectUnit(other)
            other =  other.factor/correct.factor
        
        correct = auto_converter.getCorrectUnit(self)
        return other*(self.factor/correct.factor)

    def __rmul__(self,other):
        """
        Overload multiplication to enable unit algebra. 
        """        
        correct = auto_converter.getCorrectUnit(self)
        return other*(self.factor/correct.factor)


    def __div__(self,other):
        """
        Overload division to enable unit algebra. 
        """
        if isinstance(other,PhysicalUnit):
            correct = auto_converter.getCorrectUnit(other)
            other =  (other.factor/correct.factor)
        
        correct = auto_converter.getCorrectUnit(self)
        return (self.factor/correct.factor)/other 

    def __rdiv__(self,other):
        """
        Overload division to enable unit algebra. 
        """        
        correct = auto_converter.getCorrectUnit(self)
        return other/(self.factor/correct.factor)

    def __pow__(self,power):
        correct = auto_converter.getCorrectUnit(self)
        return (self.factor/correct.factor)**power


# Distance Units

class MeterUnit(PhysicalUnit):
    """
    Unit for distance in meter 
    """
    pass 

# Mass Units

class KiloGrammUnit(PhysicalUnit):
    """
    Unit for distance in meter 
    """
    pass

# Pressure Units

class PascalUnit(PhysicalUnit):
    """
    Unit for pressure in Pascal 
    """
    pass

# Class for Force

class NewtonUnit(PhysicalUnit):
    """
    Unit for force in Newton 
    """
    pass

class SecondUnit(PhysicalUnit):
    """
    Unit for time in secons 
    """
    pass

class RadiantUnit(PhysicalUnit):
    """
    Unit for radiants 
    """
    pass

class KelvinUnit(PhysicalUnit):
    """
    Unit for temperature in Kelvin degree
    """
    def __init__(self,factor=1.0,translation=0.0):        
        
        self.factor = factor
        self.translation = translation


    def convertWithOrigin(self,to_convert, other_unit = None):

        if other_unit is None:
            other_unit = auto_converter.getCorrectUnit(self)

        return to_convert*(self.factor/other_unit.factor)+(self.translation - other_unit.translation)

class WattUnit(PhysicalUnit):
    """
    Unit for power in Watt 
    """
    pass

class JouleUnit(PhysicalUnit):
    """
    Unit for energy in Joule 
    """
    pass

# declare units

# metric
km = MeterUnit(1e+3)
m = MeterUnit()
dm = MeterUnit(1e-1)
cm = MeterUnit(1e-2)
mm = MeterUnit(1e-3)

# mass 
kg = KiloGrammUnit()
g = KiloGrammUnit(1e-3)
T = KiloGrammUnit(1e+3)

# pressure
Pa = PascalUnit()
MPa = PascalUnit(1e+6)
bar = PascalUnit(1e+5)
mbar = PascalUnit(1e+2)

# force
kN = NewtonUnit(1e+3)
N = NewtonUnit()

# time
sec = SecondUnit()
minute = SecondUnit(60.)
hour = SecondUnit((60.**2)) 

# radiant
from math import pi
rad = RadiantUnit()
grad = RadiantUnit(pi/180.)

# temperature
degK = KelvinUnit()
degC = KelvinUnit(1.0,273.15) # still to do! 

# power
W = WattUnit()
mW = WattUnit(1e-3)

# energy
J = JouleUnit()
mJ = JouleUnit(1e-3)



# Unit Systems

class UnitSystem(object):
    """
    Basis container class for unit systems
    """
    def getDistance(self):
        return self._distance

    def getMass(self):
        return self._mass

    def getPressure(self):
        return self._pressure

    def getForce(self):
        return self._force

    def getTime(self):
        return self._time

    def getRadiant(self):
        return self._radiant

    def getTemperature(self):
        return self._temperature

    def getPower(self):
        return self._power

    def getEnergy(self):
        return self._energy

class SystemeInternationale(UnitSystem):
    """
    Container class for SI units
    """
    def __init__(self):
        
        self._distance = m
        self._mass = kg
        self._pressure = Pa 
        self._force = N
        self._time = sec
        self._radiant = rad
        self._temperature = degK
        self._power = W
        self._energy = J

class MeterKilogrammSec(UnitSystem):
    """
    Container class for SI units 
    in Meter Kilogramm and Seconds,
    but with Degree in Celsius
    """
    def __init__(self):
        
        self._distance = m
        self._mass = kg
        self._pressure = Pa 
        self._force = N
        self._time = sec
        self._radiant = rad
        self._temperature = degC
        self._power = W
        self._energy = J


class MilimeterAndTon(UnitSystem):
    """
    Container class for SI units
    with distance in mm and
    mass in tons
    """
    def __init__(self):
        
        self._distance = mm
        self._mass = T
        self._pressure = MPa 
        self._force = N
        self._time = sec
        self._radiant = rad
        self._temperature = degC
        self._power = mW
        self._energy = mJ

# Class for autoconversion

class UnitAutoConverter(object):
    """
    Class for autoconversion of unit systems
    """

    def __init__(self,unit_system):
        """
        Init method stores the
        unit system of the choice
        """
        self._unitSystem = unit_system

    def setUnitSystem(self,unit_system):
        """
        Resets the unit system
        """
        self._unitSystem = unit_system

    def __call__(self,unit_system):
        """
        Call method changes unit system 
        """
        self.setUnitSystem(unit_system)

    def getCorrectUnit(self,unit):
        """
        gets a object of unit type
        and returns the corresponding
        unit of the unit system
        """
        if isinstance(unit,MeterUnit):
            return self._unitSystem.getDistance()
        elif isinstance(unit,KiloGrammUnit):
            return self._unitSystem.getMass()
        elif isinstance(unit,PascalUnit):
            return self._unitSystem.getPressure()
        elif isinstance(unit,NewtonUnit):
            return self._unitSystem.getForce()
        elif isinstance(unit,SecondUnit):
            return self._unitSystem.getTime()
        elif isinstance(unit,RadiantUnit):
            return self._unitSystem.getRadiant()
        elif isinstance(unit,KelvinUnit):
            return self._unitSystem.getTemperature()
        elif isinstance(unit,WattUnit):
            return self._unitSystem.getPower()
        elif isinstance(unit,JouleUnit):
            return self._unitSystem.getEnergy()
        else:
            raise ValueError("Error: Not a valid unit!")
    
SI = SystemeInternationale()
MKS = MeterKilogrammSec()
mmNS = MilimeterAndTon()

auto_converter = UnitAutoConverter(MKS) # Default autoconversion

