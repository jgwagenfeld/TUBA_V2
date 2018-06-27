#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 18:11:46 2018

@author: jangeorg
"""
import salome
salome.salome_init()
import GEOM
from salome.geom import geomBuilder
geompy = geomBuilder.New(salome.myStudy)


		
H,B,Tw,Tf,R=1056.0,314.0,36.0,64.0,30.0
sketchStr = "Sketcher:F %g %g:" % (Tw/2, 0)
sketchStr += "TT %g %g:" % (Tw/2, H/2-Tf-R)
sketchStr += "C %g %g:" % (-R, 90)
sketchStr += "TT %g %g:" % (B/2, H/2-Tf)
sketchStr += "TT %g %g:" % (B/2, H/2)
sketchStr += "TT %g %g:" % (-B/2, H/2)

sketchStr += "TT %g %g:" % (-B/2, H/2-Tf)
sketchStr += "TT %g %g:" % (-Tw/2-R, H/2-Tf)
sketchStr += "C %g %g:" % (-R, 90)
sketchStr += "TT %g %g:" % (-Tw/2, -H/2+Tf+R)
sketchStr += "C %g %g:" % (-R, 90)
sketchStr += "TT %g %g:" % (-B/2, -H/2+Tf)
sketchStr += "TT %g %g:" % (-B/2, -H/2)
sketchStr += "TT %g %g:" % (B/2, -H/2)
sketchStr += "TT %g %g:" % (B/2, -H/2+Tf)
sketchStr += "TT %g %g:" % (Tw/2+R, -H/2+Tf)
sketchStr += "C %g %g:" % (-R, 90)
sketchStr += "TT %g %g:WW" % (Tw/2, 0)


Sketcher = geompy.MakeSketcher(sketchStr)
id_Sketcher = geompy.addToStudy(Sketcher, "Sketcher")