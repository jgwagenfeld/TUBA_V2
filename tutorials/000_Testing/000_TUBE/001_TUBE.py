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

Windload(x=40*m()/sec(),y=0,z=0)  #mm/s in mmNS system
Insulation(insulation_thickness=100, insulation_density=300*kg()/m()**3)
#---------------------------------

P(x=0,y=0,z=0,name="a") 										#equivalent to P(0,0,0,"a)
FixPoint()     													#equivalent to Block(x=0,y=0,z=0,rx=0,ry=0,rz=0)
V(1000,0,0)
Bent(radius=500,angle_deg=90,orientation=0,mode="add")
SectionTube(outerRadius+100,WallThickness)
V_Reducer(length=50)
FixPoint()
Vc(length=500)
Bent(radius=1000,angle_deg=90,orientation=0,mode="add")
#Bent(radius=400,angle_deg=45,orientation=90,mode="add") 


