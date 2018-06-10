#---UnitCalculator to use different input units---
from external.UnitCalculator import *
auto_converter(mmNS)

outerRadius=35.0   #in mm
WallThickness=4.0   #in mm

SectionTube(outerRadius,WallThickness)
Material("SS304")  #Check the material library or autodoc for a complete list of available material properties.

P(0,0,0)  
FixPoint()
V(0,0,4000,name='top')
Force(x=1000)

SectionCable(4,10000)
V(1000,1000,-4000)
Block(x=0,y=0,z=0)

gotoP('top')
V(1000,-1000,-4000)
Block(x=0,y=0,z=0)
