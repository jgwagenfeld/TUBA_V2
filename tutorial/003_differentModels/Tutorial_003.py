#---UnitCalculator to use different input units---
from external.UnitCalculator import *
auto_converter(mmNS)


Material("SS304")
Temperature(550,T_ref=20)
Pressure(2*bar())


Model("TUYAU")

outerRadius=35
WallThickness=4
SectionTube(outerRadius,WallThickness)


P(0,0,0)
FixPoint()
V(1000,0,0)
Bent(150,90,90)
Vc(1000)
Force(100,0,0)



Model("TUBE")

P(0,1000,0)
FixPoint()
V(1000,0,0)
Bent(150,90,90)
Vc(1000)
Force(100,0,0)




