#---UnitCalculator to use different input units---
from external.UnitCalculator import *
auto_converter(mmNS)

outerRadius=35.0   #in mm
WallThickness=4.0   #in mm

#Define the global properties of the following vector objects
#----------------------------------------------------------------
SectionTube(outerRadius,WallThickness)
Material("SS304")  #Check the material library or autodoc for a complete list of available material properties.

#Sets the temperature of the vector objects. T_ref denotes the temperature at which thermal dilatation is supposed to be 0.
Temperature(550,T_ref=20)

#Set the internal pressure of the piping. The unit bar() is a function from UnitCalculator which translates bar to N/mm2
#These unit functions can only be used if the UnitCalculator module is imported(first lines)
Pressure(2*bar())


#Start to define the geometry
#----------------------------------------------------------------
#Creates the startpoint of the piping system.
P(0,0,0)   #(x,y,z)
#The property Fixpoint() is applied to the startpoint blocking all degrees of freedom.
FixPoint()

#From the startpoint, a 1000mm(mmNS) long vector-object is created carrying all 
#the above defined global properties(Model,SectionTube,Material,Pressure).
V(1000,0,0)

#Creates 2 colinear vectors (colinear to the last created vector) and blocks the y and z direction of each vector-endpoint.
for i in range(0,2):
	Vc(1000)
	Block(y=0,z=0)

Vc(1000)
#For the endpoint of the last vector, a force in negative z-direction of 1000N (mmNS) is defined
Force(0,0,-1000)
Vc(1000)
#For the endpoint of the last vector, a stiffness in x and y-direction of 100N/mm (mmNS) is defined
Spring(100,100,0,0,0,0)

#Changes the global property "Temperature" - all created vector-objects after this statement will have the new value
Temperature(20,T_ref=20)

#Creates the special vector-object "Bent" with a bentradius of 150mm, a bent-angle of 90degree and an orientation of 0degree (dihedral angle)
Bent(150,90,0)
Block(z=0)
Vc(1000)
# In this special case of the Block-function, the endpoint of the last vector is displaced 1000mm (mmNS) in -y-direction.
Block(z=-1000)

Calculate("Statique_Linear")
