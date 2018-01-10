#---UnitCalculator to use different input units---
from external.UnitCalculator import *
auto_converter(mmNS)

outerRadius=35.0   #in mm
WallThickness=4.0   #in mm

Model("RECTANGULAR")
SectionRectangular(60,100,3,3)
Material("SS304")  #Check the material library or autodoc for a complete list of available material properties.

#Sets the temperature of the vector objects. T_ref denotes the temperature at which thermal dilatation is supposed to be 0.
Temperature(20,T_ref=20)

#Set the internal pressure of the piping. The unit bar() is a function from UnitCalculator which translates bar to N/mm2
#These unit functions can only be used if the UnitCalculator module is imported(first lines)
Pressure(2*bar())



P(0,0,0)  
FixPoint()
#SectionOrientation(0)
V(1000,0,0)
V(0,0,1000)
V(-1000,0,0)
Force(z=10000)

P(0,1000,0)  
FixPoint()
SectionOrientation(45)
V(1000,0,0)
V(0,0,1000)
V(-1000,0,0)
Force(z=10000)

P(0,2000,0)  
FixPoint()
SectionOrientation(90)
V(1000,0,0)
V(0,0,1000)
V(-1000,0,0)
Force(z=10000)

P(0,3000,0)  
FixPoint()
SectionOrientation(135)
V(1000,0,0)
V(0,0,1000)
V(-1000,0,0)
Force(z=10000)


Calculate("Statique_Linear")
