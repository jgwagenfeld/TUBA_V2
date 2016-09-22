#---UnitCalculator to use different input units---
from external.UnitCalculator import *
auto_converter(mmNS)

outerRadius=35
WallThickness=4

Model("TUYAU")
SectionTube(outerRadius,WallThickness)
Material("SS304")
Temperature(550,T_ref=20)
Pressure(2*bar())

P(0,0,0)
FixPoint()
V(1000,0,0)

for i in range(0,4):
	Vc(1000)
	Block(y=0,z=0)

Vc(1000)
Bent(150,90,0)
Vc(1000)
Block(y=-1000)

Calculate("Statique_Linear")
