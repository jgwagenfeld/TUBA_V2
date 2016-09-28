# -*- coding: utf-8 -*-
#---Import of the TUBA-namespace --> in the TUB-file only necessary to access autocompletion and help in Spyder
from tuba.define_geometry import *
from tuba.define_properties import *
from tuba.define_simulation import *
from tuba.define_macros import *

#---UnitCalculator to use different input units---
from external.UnitCalculator import *
auto_converter(mmNS)
####################################################
####################################################

Model("RECTANGULAR")
SectionRectangular(60,60,3,3)
Temperature(20,T_ref=20)
Material("SS316")


h=1000

P(0,0,0,"Punkt_A")
FixPoint()
P(h,0,0)
Block(z=0)
P(h,h,0)
Block(z=0)
P(0,h,0)
Block(z=0)

P(h/2,h/2,2*h,"Spitze")

Vp("Punkt_A","P3")
LinearForce(z=-1000)

Vp("Punkt_A","P1")
Vp("P1","P2")
Vp("P2","P3")

SectionRectangular(30,30,3,3)

Vp("Punkt_A","Spitze")
Vp("Spitze","P1")
Vp("Spitze","P2")
Vp("Spitze","P3")

gotoP("Spitze")
Force(z=-1000)
