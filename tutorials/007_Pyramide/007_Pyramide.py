# -*- coding: utf-8 -*-
#---UnitCalculator to use different input units---
from external.UnitCalculator import *
auto_converter(mmNS)
####################################################
####################################################

SectionRectangular(60,60,3,3)
Temperature(20,T_ref=20)
Material("SS316")

h=1000

P(0,0,0,"A")
FixPoint()
P(h,0,0)
Block(z=0)
P(h,h,0)
Block(z=0)
P(0,h,0)
Block(z=0)

P(h/2,h/2,2*h,"top")

Vp("A","P3")
LinearForce(z=-1000)

Vp("A","P1")
Vp("P1","P2")
Vp("P2","P3")

SectionRectangular(30,30,3,3)

Vp("A","top")
Vp("top","P1")
Vp("top","P2")
Vp("top","P3")

gotoP("top")
Force(z=-1000)
