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

for i in range(0,8):
	P(500*i,0,0)
	FixPoint()
	V(1000,0,0)
	Bent(150,90,45*i)
	Vc(500)
	Bent(150,90,45*i)





