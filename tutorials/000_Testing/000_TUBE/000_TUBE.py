#---UnitCalculator to use different input units---
from external.UnitCalculator import *
auto_converter(mmNS)

outerRadius=35.0   #in mm
WallThickness=4.0   #in mm

SectionTube(outerRadius,WallThickness)
Material("SS304")  #Check the material library or autodoc for a complete list of available material properties.

#Sets the temperature of the vector objects. T_ref denotes the temperature at which thermal dilatation is supposed to be 0.
Temperature(550,T_ref=20)

#Set the internal pressure of the piping. The unit bar() is a function from UnitCalculator which translates bar to N/mm2
#These unit functions can only be used if the UnitCalculator module is imported(first lines)
Pressure(2*bar())
#---------------------------------

P(x=0,y=0,z=0,name="a") 										#equivalent to P(0,0,0,"a)
FixPoint()     													#equivalent to Block(x=0,y=0,z=0,rx=0,ry=0,rz=0)
V(2*m(),0,0)
Bent(radius=400,angle_deg=45,orientation=90,mode="add")
Vc(length=500)

P(x=0,y=100,z=0)
FixPoint()     													#equivalent to Block(x=0,y=0,z=0,rx=0,ry=0,rz=0)
V(2*m(),0,0)    														
Bent(radius=400,angle_deg=45,orientation=90,mode="intersect")
Vc(length=500)


SectionTube("DN150","SCH-STD")									#check TUBA/Section/tables what kind of pipes are available

P(0,1000,0,name="c")  
FixPoint()
P(2000,1000,0,name="d")
Vp("d","c")
Bent(radius=200,vector=(0,0,1),mode="intersect")
Vc(length=500)
Force(x=0,y=100,z=100)

gotoP("c")
SectionTube("3 1/2","SCH-STD")
for i in range(0,5):
	V(0,0,100)


