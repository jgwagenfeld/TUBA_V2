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

Model("TUBE")
SectionTube(60,3)
Temperature(20,T_ref=20)
Material("SS316")


h=1000

P(0,0,0)
Block(0,0,0)

for p in range(0,3):
    for i in range (1,5-p):
        V((-1)**p*h,0,0)
    V((-1)**(p+1)*h/2,0,h)	

V((-1)**(p+1)*h,0,0)
Vp('P0','P8')
Vp('P8','P1')
Vp('P1','P7')
Vp('P7','P2')
Vp('P2','P6')
Vp('P6','P3')
Vp('P3','P5')

Vp('P5','P11')
Vp('P11','P6')
Vp('P6','P10')
Vp('P10','P7')
Vp('P7','P9')

Vp('P9','P13')
Vp('P13','P10')
Vp('P10','P12')

gotoP('P4')
Block(0,0,0)

gotoP('P2')
Force(0,0,-1000)

Calculate("Statique_Linear")

