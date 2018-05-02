#---UnitCalculator to use different input units---
from external.UnitCalculator import *
auto_converter(mmNS)

outerRadius=35.0   #in mm
WallThickness=4.0   #in mm

SectionTuyau(outerRadius,WallThickness) #Model("TUYAU")
Material("SS304")  #Check the material library or autodoc for a complete list of available material properties.

#Sets the temperature of the vector objects. T_ref denotes the temperature at which thermal dilatation is supposed to be 0.
Temperature(550,T_ref=20)



P(0,-1000,0)  
FixPoint()
V(1000,0,0)
Block(z=0)
V(1000,0,0)
Block(z=0)


P(0,0,0)  
FixPoint()
V(1000,0,0)
Block(z=0)
Friction(mu=1)
V(1000,0,0)
Block(z=0)
Friction(mu=1)

P(0,500,0)  
FixPoint()
V(-1000,0,0)
Block(z=0)
Friction(mu=1)
V(-1000,0,0)
Block(z=0)
Friction(mu=1)





P(0,1000,0)  
FixPoint()
V(1000,0,0)
Block(z=0)
Force(z=-50)
Friction(mu=1)
V(1000,0,0)
Block(z=0)
Friction(mu=1)
Spring(3,3,3)



Calculate("Statique_Linear")
