#---UnitCalculator to use different input units---
from external.UnitCalculator import *
auto_converter(mmNS)

outerRadius=35.0   #in mm
WallThickness=4.0   #in mm


Material("SS304")  #Check the material library or autodoc for a complete list of available material properties.

#Sets the temperature of the vector objects. T_ref denotes the temperature at which thermal dilatation is supposed to be 0.
Temperature(550,T_ref=20)

#Set the internal pressure of the piping. The unit bar() is a function from UnitCalculator which translates bar to N/mm2
#These unit functions can only be used if the UnitCalculator module is imported(first lines)
Pressure(2*bar())

SectionTuyau(outerRadius,WallThickness)
P(0,0,0)  
FixPoint()
V(1000,0,0)
Force(0,1000,0)
V(1000,0,0)


SectionTube(outerRadius,WallThickness)
V(100,0,0,"Junction")
V(100,0,0,"EndA")
gotoP("Junction")
V(0,100,0,"EndB")


SectionTuyau(outerRadius,WallThickness)
Vc(1000)   #continues at EndB
gotoP("EndA")
Vc(1000)
Spring(20,20,20)

Calculate("Statique_Linear")
