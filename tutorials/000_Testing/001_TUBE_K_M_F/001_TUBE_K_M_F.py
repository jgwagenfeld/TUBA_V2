#---UnitCalculator to use different input units---
from external.UnitCalculator import *
auto_converter(mmNS)

outerRadius=35.0   #in mm
WallThickness=4.0   #in mm

SectionTube(outerRadius,WallThickness)
Material("ACIER")  #Check the material library or autodoc for a complete list of available material properties.

#Sets the temperature of the vector objects. T_ref denotes the temperature at which thermal dilatation is supposed to be 0.
Temperature("20.0+2*x",T_ref=100.0)

#Set the internal pressure of the piping. The unit bar() is a function from UnitCalculator which translates bar to N/mm2
#These unit functions can only be used if the UnitCalculator module is imported(first lines)
Pressure(2*bar())

P(0,0,0)  
FixPoint()

V(1000,0,0)
Force(x=0,y=50,z=0)

V(10000,0,0)
Block(z=0)

V(1000,0,0)
Spring(20,20,20)

V(1000,0,0)
Mass(5*kg())

Temperature("1440.0+x+z",T_ref=20.0)
Vc(10000)
Block(y=-0.5*m())

Vc(1000)
Bent(1500,90,90)
Vc(1000)

