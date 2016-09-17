UnitCalculator
==============

Simple Python Module for Unit Conversion
This Module is distributet under MIT License and
should be used freely.

Version
=======

Version 0.2

Installation
============

Change into your desired directory (e.g. your home directory) and
execute

git clone https://github.com/maldun/UnitCalculator.git

Usage
=====

We assume here that the module is installed in the home directory.
In (I)Python:

In [1]: import os

In [2]: os.chdir(os.path.expanduser("~"))

In [3]: from UnitCalculator import *

In [4]: kg() # Default

Out[4]: 1.0

In [5]: kg(T) # Convert kg to Ton

Out[5]: 0.001

In [6]: auto_converter(mmNS) # Start automatic conversion to mm and T system

In [7]: kg()

Out[7]: 0.001

In [8]: auto_converter(SI) # Convert to SI

In [9]: 1000*mm() # Convert 1000mm to SI m

Out[9]: 1.0

In [10]: auto_converter(mmNS) 

In [11]: 8050*(kg()/m()**3) # Converts density of steel from kg/m^3 to T/mm^3

Out[11]: 8.05e-09

In [12]: N/m**2 # Since Version 0.2 direct algebra use is also supported

Out[12]: 1e-06

In [13]: gramm = KiloGrammUnit(1e-3) # Easy (re)definition of units

In [14]: 8050*(kg/m**3) # Converts density of steel from kg/m^3 to T/mm^3 since v0.2

Out[14]: 8.05e-09

In [15]: degK.convertWithOrigin(0.0) #To convert temperature with considering the origin of the scale

Out[15]: -273.15


In fact the commands kg(), kg(T), m() etc. only return the conversion factors between two units,
so don't forget the multiplication symbol!

Usage in Code Aster
===================

Add to your .comm file (Assuming the module is installed in home):

import sys

sys.path.append(os.path.expanduser("~"))

from UnitCalculator import *

Example in .comm file
=====================

import sys
import os

# Assuming module is in home directory

sys.path.append(os.path.expanduser("~"))

from UnitCalculator import *

auto_converter(mmNS)

DEBUT();

#define material --> steel
MA=DEFI_MATERIAU(ELAS=_F(E=2.1e+11*Pa, # automatically --> 2.1e+5 MPa 
                         NU=0.3,
			 RHO=8050*(kg/m**3), # automatically --> 8.05e-09 T/mm**3
			 ),
		);
...

Supportet Units
===============

Metric: km, m, dm, cm, mm
Mass: T, kg, g
Pressure: Pa, MPa
Force: kN, N
Time: sec, minute, hour
Radiant: rad, grad
Temperature: degK, degC
Power: W, mW
Energy: J, mJ

Predefined Unit Sets
====================

class SystemeInternationale(UnitSystem): # SI
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

class MeterKilogrammSec(UnitSystem): # MKS
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


class MilimeterAndTon(UnitSystem): # mmNS
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

Custom Units and Unitsets
=========================

To Create your own units, e.g. to create
micrometer, simply add 

mum = MeterUnit(1e-6) # Example for µm unit

What is this? MeterUnit is the Unit base class for
length units, where the standard unit is meter. The
factor 1e-6 is the conversion factor to meter (1 µm = 1e-6 m).

another example for foot:

ft = MeterUnit(0.3048)

You can also define a whole new base unit. 
For example use foot as new Unit base for lengths add

class FootUnit(PhysicalUnit):
      pass

Then you can define other units which use foot as base e.g.:

ft = FootUnit() # Base unit
yard = FootUnit(3.0) # Derived unit

To define a new Unit set add it like:

class MilimeterAndTon(UnitSystem): # mmNS
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

mmNS = MilimeterAndTon() # now it can be used by auto_converter with auto_converter(mmNS)

Feel free to add your unit systems and units to the UnitCalculator.py file and
push them to my repo on github! This way we could create a quite good collection of frequently 
used units and unit systems!
If possible incorporate also unit tests in unit_tests.py to ensure that the newly 
created units work correctly! 

License
=======

The MIT License (MIT)

Copyright (c) 2013 Stefan Reiterer - maldun.finsterschreck@gmail.com

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
