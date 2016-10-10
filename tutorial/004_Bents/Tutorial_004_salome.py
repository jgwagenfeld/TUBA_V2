#!/usr/bin/python 3
# -*- coding: iso-8859-1 -*-

import time
time1=time.time()
import sys
sys.path.append('/home/caelinux/TUBAV2')
sys.path.append(' /home/jangeorg/TUBA/tutorial/004_Bents ')

import salome
import GEOM
import math
import SMESH
from salome.smesh import smeshBuilder
import SALOMEDS
import StdMeshers
import NETGENPlugin

salome.salome_init()
study   = salome.myStudy
studyId = salome.myStudyId

from salome.geom import geomBuilder
geompy = geomBuilder.New(salome.myStudy)

smesh = smeshBuilder.New(salome.myStudy)

from salome.geom import geomtools
geompy = geomtools.getGeompy(studyId)

from salome.kernel.studyedit import getStudyEditor
studyEditor = getStudyEditor(studyId)

gst = geomtools.GeomStudyTools(studyEditor)
gg = salome.ImportComponentGUI("GEOM")

def Project():
    O = geompy.MakeVertex(0,0,0)
    O_id = geompy.addToStudy(O,"O")
    Vx= geompy.MakeVectorDXDYDZ(1,0,0)
    gst.addShapeToStudy(Vx,"Vx")
    Vy= geompy.MakeVectorDXDYDZ(0,1,0)
    geompy.addToStudy(Vy,"Vy")
    Vz= geompy.MakeVectorDXDYDZ(0,0,1)
    geompy.addToStudy(Vz,"Vz")
    # List of elements which are added to the study
    Liste=[]
    ListeV=[]
    L1=[]
    L2=[]
    List_id=[]
    ERREUR=False

    #gst.deleteShape(Obj)
            

    P0= geompy.MakeVertex(0, 0, 0 )
    geompy.addToStudy(P0,"P0 ")
    Vd2x_P0 = geompy.MakeVectorDXDYDZ(1.0, 0.0, 0.0)
    P0_vd2x=    geompy.MakeTranslationVectorDistance(P0,Vd2x_P0,100)
    Vd2x_P0= geompy.MakeVector(P0,P0_vd2x)
    geompy.addToStudy(Vd2x_P0,"Vd2x_P0 " )

    P1= geompy.MakeVertex(850.0, 0.0, 0.0 )
    geompy.addToStudy(P1,"P1 ")
    Vd2x_P1 = geompy.MakeVectorDXDYDZ(1.0, 0.0, 0.0)
    P1_vd2x=    geompy.MakeTranslationVectorDistance(P1,Vd2x_P1,100)
    Vd2x_P1= geompy.MakeVector(P1,P1_vd2x)
    geompy.addToStudy(Vd2x_P1,"Vd2x_P1 " )

    P1_2_center= geompy.MakeVertex(850.0, 150.0, 0.0 )
    geompy.addToStudy(P1_2_center,"P1_2_center ")
    Vd2x_P1_2_center = geompy.MakeVectorDXDYDZ(1, 0, 0)
    P1_2_center_vd2x=    geompy.MakeTranslationVectorDistance(P1_2_center,Vd2x_P1_2_center,100)
    Vd2x_P1_2_center= geompy.MakeVector(P1_2_center,P1_2_center_vd2x)
    geompy.addToStudy(Vd2x_P1_2_center,"Vd2x_P1_2_center " )

    P2= geompy.MakeVertex(1000.0, 150.0, 0.0 )
    geompy.addToStudy(P2,"P2 ")
    Vd2x_P2 = geompy.MakeVectorDXDYDZ(6.123233995736766e-17, 1.0, 0.0)
    P2_vd2x=    geompy.MakeTranslationVectorDistance(P2,Vd2x_P2,100)
    Vd2x_P2= geompy.MakeVector(P2,P2_vd2x)
    geompy.addToStudy(Vd2x_P2,"Vd2x_P2 " )

    P3= geompy.MakeVertex(1000.0, 500.0, 0.0 )
    geompy.addToStudy(P3,"P3 ")
    Vd2x_P3 = geompy.MakeVectorDXDYDZ(6.123233995736766e-17, 1.0, 0.0)
    P3_vd2x=    geompy.MakeTranslationVectorDistance(P3,Vd2x_P3,100)
    Vd2x_P3= geompy.MakeVector(P3,P3_vd2x)
    geompy.addToStudy(Vd2x_P3,"Vd2x_P3 " )

    P3_4_center= geompy.MakeVertex(850.0, 500.0, 0.0 )
    geompy.addToStudy(P3_4_center,"P3_4_center ")
    Vd2x_P3_4_center = geompy.MakeVectorDXDYDZ(1, 0, 0)
    P3_4_center_vd2x=    geompy.MakeTranslationVectorDistance(P3_4_center,Vd2x_P3_4_center,100)
    Vd2x_P3_4_center= geompy.MakeVector(P3_4_center,P3_4_center_vd2x)
    geompy.addToStudy(Vd2x_P3_4_center,"Vd2x_P3_4_center " )

    P4= geompy.MakeVertex(850.0, 650.0, 0.0 )
    geompy.addToStudy(P4,"P4 ")
    Vd2x_P4 = geompy.MakeVectorDXDYDZ(-1.0, 1.2246467991473532e-16, 0.0)
    P4_vd2x=    geompy.MakeTranslationVectorDistance(P4,Vd2x_P4,100)
    Vd2x_P4= geompy.MakeVector(P4,P4_vd2x)
    geompy.addToStudy(Vd2x_P4,"Vd2x_P4 " )

    P5= geompy.MakeVertex(500, 0, 0 )
    geompy.addToStudy(P5,"P5 ")
    Vd2x_P5 = geompy.MakeVectorDXDYDZ(1.0, 0.0, 0.0)
    P5_vd2x=    geompy.MakeTranslationVectorDistance(P5,Vd2x_P5,100)
    Vd2x_P5= geompy.MakeVector(P5,P5_vd2x)
    geompy.addToStudy(Vd2x_P5,"Vd2x_P5 " )

    P6= geompy.MakeVertex(1350.0, 0.0, 0.0 )
    geompy.addToStudy(P6,"P6 ")
    Vd2x_P6 = geompy.MakeVectorDXDYDZ(1.0, 0.0, 0.0)
    P6_vd2x=    geompy.MakeTranslationVectorDistance(P6,Vd2x_P6,100)
    Vd2x_P6= geompy.MakeVector(P6,P6_vd2x)
    geompy.addToStudy(Vd2x_P6,"Vd2x_P6 " )

    P6_7_center= geompy.MakeVertex(1350.0, 106.06601717798213, 106.06601717798212 )
    geompy.addToStudy(P6_7_center,"P6_7_center ")
    Vd2x_P6_7_center = geompy.MakeVectorDXDYDZ(1, 0, 0)
    P6_7_center_vd2x=    geompy.MakeTranslationVectorDistance(P6_7_center,Vd2x_P6_7_center,100)
    Vd2x_P6_7_center= geompy.MakeVector(P6_7_center,P6_7_center_vd2x)
    geompy.addToStudy(Vd2x_P6_7_center,"Vd2x_P6_7_center " )

    P7= geompy.MakeVertex(1500.0, 106.06601717798213, 106.06601717798212 )
    geompy.addToStudy(P7,"P7 ")
    Vd2x_P7 = geompy.MakeVectorDXDYDZ(6.123233995736766e-17, 0.7071067811865476, 0.7071067811865475)
    P7_vd2x=    geompy.MakeTranslationVectorDistance(P7,Vd2x_P7,100)
    Vd2x_P7= geompy.MakeVector(P7,P7_vd2x)
    geompy.addToStudy(Vd2x_P7,"Vd2x_P7 " )

    P8= geompy.MakeVertex(1500.0, 353.5533905932738, 353.5533905932737 )
    geompy.addToStudy(P8,"P8 ")
    Vd2x_P8 = geompy.MakeVectorDXDYDZ(6.123233995736766e-17, 0.7071067811865476, 0.7071067811865475)
    P8_vd2x=    geompy.MakeTranslationVectorDistance(P8,Vd2x_P8,100)
    Vd2x_P8= geompy.MakeVector(P8,P8_vd2x)
    geompy.addToStudy(Vd2x_P8,"Vd2x_P8 " )

    P8_9_center= geompy.MakeVertex(1393.933982822018, 428.5533905932738, 278.5533905932737 )
    geompy.addToStudy(P8_9_center,"P8_9_center ")
    Vd2x_P8_9_center = geompy.MakeVectorDXDYDZ(1, 0, 0)
    P8_9_center_vd2x=    geompy.MakeTranslationVectorDistance(P8_9_center,Vd2x_P8_9_center,100)
    Vd2x_P8_9_center= geompy.MakeVector(P8_9_center,P8_9_center_vd2x)
    geompy.addToStudy(Vd2x_P8_9_center,"Vd2x_P8_9_center " )

    P9= geompy.MakeVertex(1393.933982822018, 534.619407771256, 384.61940777125585 )
    geompy.addToStudy(P9,"P9 ")
    Vd2x_P9 = geompy.MakeVectorDXDYDZ(-0.7071067811865476, 0.5, -0.49999999999999994)
    P9_vd2x=    geompy.MakeTranslationVectorDistance(P9,Vd2x_P9,100)
    Vd2x_P9= geompy.MakeVector(P9,P9_vd2x)
    geompy.addToStudy(Vd2x_P9,"Vd2x_P9 " )

    P10= geompy.MakeVertex(1000, 0, 0 )
    geompy.addToStudy(P10,"P10 ")
    Vd2x_P10 = geompy.MakeVectorDXDYDZ(1.0, 0.0, 0.0)
    P10_vd2x=    geompy.MakeTranslationVectorDistance(P10,Vd2x_P10,100)
    Vd2x_P10= geompy.MakeVector(P10,P10_vd2x)
    geompy.addToStudy(Vd2x_P10,"Vd2x_P10 " )

    P11= geompy.MakeVertex(1850.0, 0.0, 0.0 )
    geompy.addToStudy(P11,"P11 ")
    Vd2x_P11 = geompy.MakeVectorDXDYDZ(1.0, 0.0, 0.0)
    P11_vd2x=    geompy.MakeTranslationVectorDistance(P11,Vd2x_P11,100)
    Vd2x_P11= geompy.MakeVector(P11,P11_vd2x)
    geompy.addToStudy(Vd2x_P11,"Vd2x_P11 " )

    P11_12_center= geompy.MakeVertex(1850.0, 9.184850993605149e-15, 150.0 )
    geompy.addToStudy(P11_12_center,"P11_12_center ")
    Vd2x_P11_12_center = geompy.MakeVectorDXDYDZ(1, 0, 0)
    P11_12_center_vd2x=    geompy.MakeTranslationVectorDistance(P11_12_center,Vd2x_P11_12_center,100)
    Vd2x_P11_12_center= geompy.MakeVector(P11_12_center,P11_12_center_vd2x)
    geompy.addToStudy(Vd2x_P11_12_center,"Vd2x_P11_12_center " )

    P12= geompy.MakeVertex(2000.0, 9.184850993605149e-15, 150.0 )
    geompy.addToStudy(P12,"P12 ")
    Vd2x_P12 = geompy.MakeVectorDXDYDZ(6.123233995736766e-17, 6.123233995736766e-17, 1.0)
    P12_vd2x=    geompy.MakeTranslationVectorDistance(P12,Vd2x_P12,100)
    Vd2x_P12= geompy.MakeVector(P12,P12_vd2x)
    geompy.addToStudy(Vd2x_P12,"Vd2x_P12 " )

    P13= geompy.MakeVertex(2000.0, 3.061616997868383e-14, 500.0 )
    geompy.addToStudy(P13,"P13 ")
    Vd2x_P13 = geompy.MakeVectorDXDYDZ(6.123233995736766e-17, 6.123233995736766e-17, 1.0)
    P13_vd2x=    geompy.MakeTranslationVectorDistance(P13,Vd2x_P13,100)
    Vd2x_P13= geompy.MakeVector(P13,P13_vd2x)
    geompy.addToStudy(Vd2x_P13,"Vd2x_P13 " )

    P13_14_center= geompy.MakeVertex(1850.0, 3.980102097228898e-14, 500.0 )
    geompy.addToStudy(P13_14_center,"P13_14_center ")
    Vd2x_P13_14_center = geompy.MakeVectorDXDYDZ(1, 0, 0)
    P13_14_center_vd2x=    geompy.MakeTranslationVectorDistance(P13_14_center,Vd2x_P13_14_center,100)
    Vd2x_P13_14_center= geompy.MakeVector(P13_14_center,P13_14_center_vd2x)
    geompy.addToStudy(Vd2x_P13_14_center,"Vd2x_P13_14_center " )

    P14= geompy.MakeVertex(1850.0, 4.898587196589413e-14, 650.0 )
    geompy.addToStudy(P14,"P14 ")
    Vd2x_P14 = geompy.MakeVectorDXDYDZ(-1.0, 6.123233995736765e-17, 1.2246467991473532e-16)
    P14_vd2x=    geompy.MakeTranslationVectorDistance(P14,Vd2x_P14,100)
    Vd2x_P14= geompy.MakeVector(P14,P14_vd2x)
    geompy.addToStudy(Vd2x_P14,"Vd2x_P14 " )

    P15= geompy.MakeVertex(1500, 0, 0 )
    geompy.addToStudy(P15,"P15 ")
    Vd2x_P15 = geompy.MakeVectorDXDYDZ(1.0, 0.0, 0.0)
    P15_vd2x=    geompy.MakeTranslationVectorDistance(P15,Vd2x_P15,100)
    Vd2x_P15= geompy.MakeVector(P15,P15_vd2x)
    geompy.addToStudy(Vd2x_P15,"Vd2x_P15 " )

    P16= geompy.MakeVertex(2350.0, 0.0, 0.0 )
    geompy.addToStudy(P16,"P16 ")
    Vd2x_P16 = geompy.MakeVectorDXDYDZ(1.0, 0.0, 0.0)
    P16_vd2x=    geompy.MakeTranslationVectorDistance(P16,Vd2x_P16,100)
    Vd2x_P16= geompy.MakeVector(P16,P16_vd2x)
    geompy.addToStudy(Vd2x_P16,"Vd2x_P16 " )

    P16_17_center= geompy.MakeVertex(2350.0, -106.06601717798212, 106.06601717798213 )
    geompy.addToStudy(P16_17_center,"P16_17_center ")
    Vd2x_P16_17_center = geompy.MakeVectorDXDYDZ(1, 0, 0)
    P16_17_center_vd2x=    geompy.MakeTranslationVectorDistance(P16_17_center,Vd2x_P16_17_center,100)
    Vd2x_P16_17_center= geompy.MakeVector(P16_17_center,P16_17_center_vd2x)
    geompy.addToStudy(Vd2x_P16_17_center,"Vd2x_P16_17_center " )

    P17= geompy.MakeVertex(2500.0, -106.06601717798212, 106.06601717798213 )
    geompy.addToStudy(P17,"P17 ")
    Vd2x_P17 = geompy.MakeVectorDXDYDZ(6.123233995736766e-17, -0.7071067811865475, 0.7071067811865476)
    P17_vd2x=    geompy.MakeTranslationVectorDistance(P17,Vd2x_P17,100)
    Vd2x_P17= geompy.MakeVector(P17,P17_vd2x)
    geompy.addToStudy(Vd2x_P17,"Vd2x_P17 " )

    P18= geompy.MakeVertex(2500.0, -353.5533905932737, 353.5533905932738 )
    geompy.addToStudy(P18,"P18 ")
    Vd2x_P18 = geompy.MakeVectorDXDYDZ(6.123233995736766e-17, -0.7071067811865475, 0.7071067811865476)
    P18_vd2x=    geompy.MakeTranslationVectorDistance(P18,Vd2x_P18,100)
    Vd2x_P18= geompy.MakeVector(P18,P18_vd2x)
    geompy.addToStudy(Vd2x_P18,"Vd2x_P18 " )

    P18_19_center= geompy.MakeVertex(2393.9339828220177, -428.5533905932737, 278.5533905932738 )
    geompy.addToStudy(P18_19_center,"P18_19_center ")
    Vd2x_P18_19_center = geompy.MakeVectorDXDYDZ(1, 0, 0)
    P18_19_center_vd2x=    geompy.MakeTranslationVectorDistance(P18_19_center,Vd2x_P18_19_center,100)
    Vd2x_P18_19_center= geompy.MakeVector(P18_19_center,P18_19_center_vd2x)
    geompy.addToStudy(Vd2x_P18_19_center,"Vd2x_P18_19_center " )

    P19= geompy.MakeVertex(2393.9339828220177, -534.6194077712559, 384.6194077712559 )
    geompy.addToStudy(P19,"P19 ")
    Vd2x_P19 = geompy.MakeVectorDXDYDZ(-0.7071067811865476, -0.5000000000000001, -0.49999999999999983)
    P19_vd2x=    geompy.MakeTranslationVectorDistance(P19,Vd2x_P19,100)
    Vd2x_P19= geompy.MakeVector(P19,P19_vd2x)
    geompy.addToStudy(Vd2x_P19,"Vd2x_P19 " )

    P20= geompy.MakeVertex(2000, 0, 0 )
    geompy.addToStudy(P20,"P20 ")
    Vd2x_P20 = geompy.MakeVectorDXDYDZ(1.0, 0.0, 0.0)
    P20_vd2x=    geompy.MakeTranslationVectorDistance(P20,Vd2x_P20,100)
    Vd2x_P20= geompy.MakeVector(P20,P20_vd2x)
    geompy.addToStudy(Vd2x_P20,"Vd2x_P20 " )

    P21= geompy.MakeVertex(2850.0, 0.0, 0.0 )
    geompy.addToStudy(P21,"P21 ")
    Vd2x_P21 = geompy.MakeVectorDXDYDZ(1.0, 0.0, 0.0)
    P21_vd2x=    geompy.MakeTranslationVectorDistance(P21,Vd2x_P21,100)
    Vd2x_P21= geompy.MakeVector(P21,P21_vd2x)
    geompy.addToStudy(Vd2x_P21,"Vd2x_P21 " )

    P21_22_center= geompy.MakeVertex(2850.0, -150.0, 1.8369701987210297e-14 )
    geompy.addToStudy(P21_22_center,"P21_22_center ")
    Vd2x_P21_22_center = geompy.MakeVectorDXDYDZ(1, 0, 0)
    P21_22_center_vd2x=    geompy.MakeTranslationVectorDistance(P21_22_center,Vd2x_P21_22_center,100)
    Vd2x_P21_22_center= geompy.MakeVector(P21_22_center,P21_22_center_vd2x)
    geompy.addToStudy(Vd2x_P21_22_center,"Vd2x_P21_22_center " )

    P22= geompy.MakeVertex(3000.0, -150.0, 1.8369701987210297e-14 )
    geompy.addToStudy(P22,"P22 ")
    Vd2x_P22 = geompy.MakeVectorDXDYDZ(6.123233995736766e-17, -1.0, 1.2246467991473532e-16)
    P22_vd2x=    geompy.MakeTranslationVectorDistance(P22,Vd2x_P22,100)
    Vd2x_P22= geompy.MakeVector(P22,P22_vd2x)
    geompy.addToStudy(Vd2x_P22,"Vd2x_P22 " )

    P23= geompy.MakeVertex(3000.0, -500.0, 6.123233995736766e-14 )
    geompy.addToStudy(P23,"P23 ")
    Vd2x_P23 = geompy.MakeVectorDXDYDZ(6.123233995736766e-17, -1.0, 1.2246467991473532e-16)
    P23_vd2x=    geompy.MakeTranslationVectorDistance(P23,Vd2x_P23,100)
    Vd2x_P23= geompy.MakeVector(P23,P23_vd2x)
    geompy.addToStudy(Vd2x_P23,"Vd2x_P23 " )

    P23_24_center= geompy.MakeVertex(2932.9179606750063, -500.0, -134.16407864998732 )
    geompy.addToStudy(P23_24_center,"P23_24_center ")
    Vd2x_P23_24_center = geompy.MakeVectorDXDYDZ(1, 0, 0)
    P23_24_center_vd2x=    geompy.MakeTranslationVectorDistance(P23_24_center,Vd2x_P23_24_center,100)
    Vd2x_P23_24_center= geompy.MakeVector(P23_24_center,P23_24_center_vd2x)
    geompy.addToStudy(Vd2x_P23_24_center,"Vd2x_P23_24_center " )

    P24= geompy.MakeVertex(2932.9179606750063, -650.0, -134.1640786499873 )
    geompy.addToStudy(P24,"P24 ")
    Vd2x_P24 = geompy.MakeVectorDXDYDZ(-0.44721359549995804, -1.9815201452341832e-16, -0.8944271909999159)
    P24_vd2x=    geompy.MakeTranslationVectorDistance(P24,Vd2x_P24,100)
    Vd2x_P24= geompy.MakeVector(P24,P24_vd2x)
    geompy.addToStudy(Vd2x_P24,"Vd2x_P24 " )

    P25= geompy.MakeVertex(2500, 0, 0 )
    geompy.addToStudy(P25,"P25 ")
    Vd2x_P25 = geompy.MakeVectorDXDYDZ(1.0, 0.0, 0.0)
    P25_vd2x=    geompy.MakeTranslationVectorDistance(P25,Vd2x_P25,100)
    Vd2x_P25= geompy.MakeVector(P25,P25_vd2x)
    geompy.addToStudy(Vd2x_P25,"Vd2x_P25 " )

    P26= geompy.MakeVertex(3350.0, 0.0, 0.0 )
    geompy.addToStudy(P26,"P26 ")
    Vd2x_P26 = geompy.MakeVectorDXDYDZ(1.0, 0.0, 0.0)
    P26_vd2x=    geompy.MakeTranslationVectorDistance(P26,Vd2x_P26,100)
    Vd2x_P26= geompy.MakeVector(P26,P26_vd2x)
    geompy.addToStudy(Vd2x_P26,"Vd2x_P26 " )

    P26_27_center= geompy.MakeVertex(3350.0, -106.06601717798215, -106.06601717798212 )
    geompy.addToStudy(P26_27_center,"P26_27_center ")
    Vd2x_P26_27_center = geompy.MakeVectorDXDYDZ(1, 0, 0)
    P26_27_center_vd2x=    geompy.MakeTranslationVectorDistance(P26_27_center,Vd2x_P26_27_center,100)
    Vd2x_P26_27_center= geompy.MakeVector(P26_27_center,P26_27_center_vd2x)
    geompy.addToStudy(Vd2x_P26_27_center,"Vd2x_P26_27_center " )

    P27= geompy.MakeVertex(3500.0, -106.06601717798215, -106.06601717798212 )
    geompy.addToStudy(P27,"P27 ")
    Vd2x_P27 = geompy.MakeVectorDXDYDZ(6.123233995736766e-17, -0.7071067811865477, -0.7071067811865475)
    P27_vd2x=    geompy.MakeTranslationVectorDistance(P27,Vd2x_P27,100)
    Vd2x_P27= geompy.MakeVector(P27,P27_vd2x)
    geompy.addToStudy(Vd2x_P27,"Vd2x_P27 " )

    P28= geompy.MakeVertex(3500.0, -353.55339059327383, -353.5533905932737 )
    geompy.addToStudy(P28,"P28 ")
    Vd2x_P28 = geompy.MakeVectorDXDYDZ(6.123233995736766e-17, -0.7071067811865477, -0.7071067811865475)
    P28_vd2x=    geompy.MakeTranslationVectorDistance(P28,Vd2x_P28,100)
    Vd2x_P28= geompy.MakeVector(P28,P28_vd2x)
    geompy.addToStudy(Vd2x_P28,"Vd2x_P28 " )

    P28_29_center= geompy.MakeVertex(3393.9339828220177, -428.55339059327383, -278.55339059327366 )
    geompy.addToStudy(P28_29_center,"P28_29_center ")
    Vd2x_P28_29_center = geompy.MakeVectorDXDYDZ(1, 0, 0)
    P28_29_center_vd2x=    geompy.MakeTranslationVectorDistance(P28_29_center,Vd2x_P28_29_center,100)
    Vd2x_P28_29_center= geompy.MakeVector(P28_29_center,P28_29_center_vd2x)
    geompy.addToStudy(Vd2x_P28_29_center,"Vd2x_P28_29_center " )

    P29= geompy.MakeVertex(3393.9339828220177, -534.619407771256, -384.6194077712558 )
    geompy.addToStudy(P29,"P29 ")
    Vd2x_P29 = geompy.MakeVectorDXDYDZ(-0.7071067811865475, -0.5000000000000001, 0.5000000000000002)
    P29_vd2x=    geompy.MakeTranslationVectorDistance(P29,Vd2x_P29,100)
    Vd2x_P29= geompy.MakeVector(P29,P29_vd2x)
    geompy.addToStudy(Vd2x_P29,"Vd2x_P29 " )

    P30= geompy.MakeVertex(3000, 0, 0 )
    geompy.addToStudy(P30,"P30 ")
    Vd2x_P30 = geompy.MakeVectorDXDYDZ(1.0, 0.0, 0.0)
    P30_vd2x=    geompy.MakeTranslationVectorDistance(P30,Vd2x_P30,100)
    Vd2x_P30= geompy.MakeVector(P30,P30_vd2x)
    geompy.addToStudy(Vd2x_P30,"Vd2x_P30 " )

    P31= geompy.MakeVertex(3850.0, 0.0, 0.0 )
    geompy.addToStudy(P31,"P31 ")
    Vd2x_P31 = geompy.MakeVectorDXDYDZ(1.0, 0.0, 0.0)
    P31_vd2x=    geompy.MakeTranslationVectorDistance(P31,Vd2x_P31,100)
    Vd2x_P31= geompy.MakeVector(P31,P31_vd2x)
    geompy.addToStudy(Vd2x_P31,"Vd2x_P31 " )

    P31_32_center= geompy.MakeVertex(3850.0, -2.7554552980815446e-14, -150.0 )
    geompy.addToStudy(P31_32_center,"P31_32_center ")
    Vd2x_P31_32_center = geompy.MakeVectorDXDYDZ(1, 0, 0)
    P31_32_center_vd2x=    geompy.MakeTranslationVectorDistance(P31_32_center,Vd2x_P31_32_center,100)
    Vd2x_P31_32_center= geompy.MakeVector(P31_32_center,P31_32_center_vd2x)
    geompy.addToStudy(Vd2x_P31_32_center,"Vd2x_P31_32_center " )

    P32= geompy.MakeVertex(4000.0, -2.7554552980815443e-14, -150.0 )
    geompy.addToStudy(P32,"P32 ")
    Vd2x_P32 = geompy.MakeVectorDXDYDZ(6.123233995736766e-17, -1.8369701987210297e-16, -1.0)
    P32_vd2x=    geompy.MakeTranslationVectorDistance(P32,Vd2x_P32,100)
    Vd2x_P32= geompy.MakeVector(P32,P32_vd2x)
    geompy.addToStudy(Vd2x_P32,"Vd2x_P32 " )

    P33= geompy.MakeVertex(4000.0, -9.184850993605147e-14, -500.0 )
    geompy.addToStudy(P33,"P33 ")
    Vd2x_P33 = geompy.MakeVectorDXDYDZ(6.123233995736766e-17, -1.8369701987210297e-16, -1.0)
    P33_vd2x=    geompy.MakeTranslationVectorDistance(P33,Vd2x_P33,100)
    Vd2x_P33= geompy.MakeVector(P33,P33_vd2x)
    geompy.addToStudy(Vd2x_P33,"Vd2x_P33 " )

    P33_34_center= geompy.MakeVertex(3850.0, -1.1940306291686692e-13, -500.0 )
    geompy.addToStudy(P33_34_center,"P33_34_center ")
    Vd2x_P33_34_center = geompy.MakeVectorDXDYDZ(1, 0, 0)
    P33_34_center_vd2x=    geompy.MakeTranslationVectorDistance(P33_34_center,Vd2x_P33_34_center,100)
    Vd2x_P33_34_center= geompy.MakeVector(P33_34_center,P33_34_center_vd2x)
    geompy.addToStudy(Vd2x_P33_34_center,"Vd2x_P33_34_center " )

    P34= geompy.MakeVertex(3850.0, -1.4695761589768238e-13, -650.0 )
    geompy.addToStudy(P34,"P34 ")
    Vd2x_P34 = geompy.MakeVectorDXDYDZ(-1.0, -1.8369701987210294e-16, -1.224646799147353e-16)
    P34_vd2x=    geompy.MakeTranslationVectorDistance(P34,Vd2x_P34,100)
    Vd2x_P34= geompy.MakeVector(P34,P34_vd2x)
    geompy.addToStudy(Vd2x_P34,"Vd2x_P34 " )

    P35= geompy.MakeVertex(3500, 0, 0 )
    geompy.addToStudy(P35,"P35 ")
    Vd2x_P35 = geompy.MakeVectorDXDYDZ(1.0, 0.0, 0.0)
    P35_vd2x=    geompy.MakeTranslationVectorDistance(P35,Vd2x_P35,100)
    Vd2x_P35= geompy.MakeVector(P35,P35_vd2x)
    geompy.addToStudy(Vd2x_P35,"Vd2x_P35 " )

    P36= geompy.MakeVertex(4350.0, 0.0, 0.0 )
    geompy.addToStudy(P36,"P36 ")
    Vd2x_P36 = geompy.MakeVectorDXDYDZ(1.0, 0.0, 0.0)
    P36_vd2x=    geompy.MakeTranslationVectorDistance(P36,Vd2x_P36,100)
    Vd2x_P36= geompy.MakeVector(P36,P36_vd2x)
    geompy.addToStudy(Vd2x_P36,"Vd2x_P36 " )

    P36_37_center= geompy.MakeVertex(4350.0, 106.0660171779821, -106.06601717798215 )
    geompy.addToStudy(P36_37_center,"P36_37_center ")
    Vd2x_P36_37_center = geompy.MakeVectorDXDYDZ(1, 0, 0)
    P36_37_center_vd2x=    geompy.MakeTranslationVectorDistance(P36_37_center,Vd2x_P36_37_center,100)
    Vd2x_P36_37_center= geompy.MakeVector(P36_37_center,P36_37_center_vd2x)
    geompy.addToStudy(Vd2x_P36_37_center,"Vd2x_P36_37_center " )

    P37= geompy.MakeVertex(4500.0, 106.0660171779821, -106.06601717798215 )
    geompy.addToStudy(P37,"P37 ")
    Vd2x_P37 = geompy.MakeVectorDXDYDZ(6.123233995736767e-17, 0.7071067811865474, -0.7071067811865478)
    P37_vd2x=    geompy.MakeTranslationVectorDistance(P37,Vd2x_P37,100)
    Vd2x_P37= geompy.MakeVector(P37,P37_vd2x)
    geompy.addToStudy(Vd2x_P37,"Vd2x_P37 " )

    P38= geompy.MakeVertex(4500.0, 353.55339059327366, -353.5533905932738 )
    geompy.addToStudy(P38,"P38 ")
    Vd2x_P38 = geompy.MakeVectorDXDYDZ(6.123233995736767e-17, 0.7071067811865474, -0.7071067811865478)
    P38_vd2x=    geompy.MakeTranslationVectorDistance(P38,Vd2x_P38,100)
    Vd2x_P38= geompy.MakeVector(P38,P38_vd2x)
    geompy.addToStudy(Vd2x_P38,"Vd2x_P38 " )

    P38_39_center= geompy.MakeVertex(4393.933982822018, 428.55339059327366, -278.55339059327383 )
    geompy.addToStudy(P38_39_center,"P38_39_center ")
    Vd2x_P38_39_center = geompy.MakeVectorDXDYDZ(1, 0, 0)
    P38_39_center_vd2x=    geompy.MakeTranslationVectorDistance(P38_39_center,Vd2x_P38_39_center,100)
    Vd2x_P38_39_center= geompy.MakeVector(P38_39_center,P38_39_center_vd2x)
    geompy.addToStudy(Vd2x_P38_39_center,"Vd2x_P38_39_center " )

    P39= geompy.MakeVertex(4393.933982822018, 534.6194077712557, -384.619407771256 )
    geompy.addToStudy(P39,"P39 ")
    Vd2x_P39 = geompy.MakeVectorDXDYDZ(-0.7071067811865478, 0.5000000000000002, 0.4999999999999997)
    P39_vd2x=    geompy.MakeTranslationVectorDistance(P39,Vd2x_P39,100)
    Vd2x_P39= geompy.MakeVector(P39,P39_vd2x)
    geompy.addToStudy(Vd2x_P39,"Vd2x_P39 " )

    try:
      print("Add V0")
      V0= geompy.MakeVector(P0,P1)
      #Liste.append([P0,"P0"])
      geompy.addToStudy(V0,"V0" )
      Liste.append([V0,"V0"])
      ListeV.append(V0)
        

      _C1 = geompy.MakeCircle(P0, V0,35)
      _C2 = geompy.MakeCircle(P0, V0,31)
      FaceTube = geompy.MakeFaceWires([_C1, _C2], 1)
      Liste.append([_C1 ,"CercleExt"])
      Liste.append([_C2 ,"CercleInt"])
            

    except:
       ERREUR=True
       print ("   =>ERROR BUILDING THE GEOMETRY!")
       for x in Liste :
           geompy.addToStudy(x[0],x[1])
       return

    try:
       V0M = smesh.Mesh(V0)
       Decoupage = V0M.Segment()
       Decoupage.NumberOfSegments(8)
       Quadratic_Mesh = Decoupage.QuadraticMesh()

       smesh.SetName(V0M,'V0')
       V0M.Compute()
       V0M.Group(P0)
       V0M.Group(P1)
       V0M.GroupOnGeom(V0)
    except:
       ERREUR=True
       print ("   =>ERROR WHILE GENERATING THE MESH!_")
       return
        


    if ListeV!=[]:
       _W=geompy.MakeWire(ListeV,1e-7)
       Pipe = geompy.MakePipe( FaceTube ,_W)
       Pipe.SetColor(SALOMEDS.Color(0.8,0.8,0.8))
       Pipe_id=geompy.addToStudy(Pipe,"Pipe")
       gg.createAndDisplayGO(Pipe_id)
       gg.setDisplayMode(Pipe_id,1)
       for x in Liste:
           geompy.addToStudyInFather(Pipe,x[0],x[1])
       Liste=[]
       ListeV=[]
    

    try:
      print("Add  V_Bent1 ")
      Liste=[]
      V_Bent1 = geompy.MakeArcCenter(P1_2_center,P1,P2)
      geompy.addToStudy(V_Bent1,"V_Bent1")
      Liste.append([V_Bent1,"V_Bent1"])
      ListeV.append(V_Bent1)

         

      C1 = geompy.MakeCircle(P1,Vd2x_P1,35)
      C2 = geompy.MakeCircle(P1,Vd2x_P1,31)
      FaceTube = geompy.MakeFaceWires([C1, C2], 1)
      Liste.append([C1 ,"CercleExt"])
      Liste.append([C2 ,"CercleInt"])
            


    except:
       ERREUR=True
       print ("   =>ERROR BUILDING THE GEOMETRY!")
       for x in Liste :
           geompy.addToStudy(x[0],x[1])
       return

    try:
       V_Bent1M = smesh.Mesh(V_Bent1)
       Decoupage = V_Bent1M.Segment()
       Decoupage.NumberOfSegments(8)
       Quadratic_Mesh = Decoupage.QuadraticMesh()

       smesh.SetName(V_Bent1M,'V_Bent1')
       V_Bent1M.Compute()
       V_Bent1M.GroupOnFilter( SMESH.NODE,'P1', smesh.GetFilter( SMESH.NODE, SMESH.FT_LyingOnGeom,'=',P1))
       V_Bent1M.GroupOnFilter( SMESH.NODE,'P2', smesh.GetFilter( SMESH.NODE, SMESH.FT_LyingOnGeom,'=',P2))
       V_Bent1M.GroupOnGeom(V_Bent1)
    except:
       ERREUR=True
       print ("   =>ERROR WHILE GENERATING THE MESH!_")
       return
            


    if ListeV!=[]:
       _W=geompy.MakeWire(ListeV,1e-7)
       Pipe = geompy.MakePipe( FaceTube ,_W)
       Pipe.SetColor(SALOMEDS.Color(0.8,0.8,0.8))
       Pipe_id=geompy.addToStudy(Pipe,"Pipe")
       gg.createAndDisplayGO(Pipe_id)
       gg.setDisplayMode(Pipe_id,1)
       for x in Liste:
           geompy.addToStudyInFather(Pipe,x[0],x[1])
       Liste=[]
       ListeV=[]
    

    try:
      print("Add V2")
      V2= geompy.MakeVector(P2,P3)
      #Liste.append([P2,"P2"])
      geompy.addToStudy(V2,"V2" )
      Liste.append([V2,"V2"])
      ListeV.append(V2)
        

      _C1 = geompy.MakeCircle(P2, V2,35)
      _C2 = geompy.MakeCircle(P2, V2,31)
      FaceTube = geompy.MakeFaceWires([_C1, _C2], 1)
      Liste.append([_C1 ,"CercleExt"])
      Liste.append([_C2 ,"CercleInt"])
            

    except:
       ERREUR=True
       print ("   =>ERROR BUILDING THE GEOMETRY!")
       for x in Liste :
           geompy.addToStudy(x[0],x[1])
       return

    try:
       V2M = smesh.Mesh(V2)
       Decoupage = V2M.Segment()
       Decoupage.NumberOfSegments(8)
       Quadratic_Mesh = Decoupage.QuadraticMesh()

       smesh.SetName(V2M,'V2')
       V2M.Compute()
       V2M.Group(P2)
       V2M.Group(P3)
       V2M.GroupOnGeom(V2)
    except:
       ERREUR=True
       print ("   =>ERROR WHILE GENERATING THE MESH!_")
       return
        


    if ListeV!=[]:
       _W=geompy.MakeWire(ListeV,1e-7)
       Pipe = geompy.MakePipe( FaceTube ,_W)
       Pipe.SetColor(SALOMEDS.Color(0.8,0.8,0.8))
       Pipe_id=geompy.addToStudy(Pipe,"Pipe")
       gg.createAndDisplayGO(Pipe_id)
       gg.setDisplayMode(Pipe_id,1)
       for x in Liste:
           geompy.addToStudyInFather(Pipe,x[0],x[1])
       Liste=[]
       ListeV=[]
    

    try:
      print("Add  V_Bent3 ")
      Liste=[]
      V_Bent3 = geompy.MakeArcCenter(P3_4_center,P3,P4)
      geompy.addToStudy(V_Bent3,"V_Bent3")
      Liste.append([V_Bent3,"V_Bent3"])
      ListeV.append(V_Bent3)

         

      C1 = geompy.MakeCircle(P3,Vd2x_P3,35)
      C2 = geompy.MakeCircle(P3,Vd2x_P3,31)
      FaceTube = geompy.MakeFaceWires([C1, C2], 1)
      Liste.append([C1 ,"CercleExt"])
      Liste.append([C2 ,"CercleInt"])
            


    except:
       ERREUR=True
       print ("   =>ERROR BUILDING THE GEOMETRY!")
       for x in Liste :
           geompy.addToStudy(x[0],x[1])
       return

    try:
       V_Bent3M = smesh.Mesh(V_Bent3)
       Decoupage = V_Bent3M.Segment()
       Decoupage.NumberOfSegments(8)
       Quadratic_Mesh = Decoupage.QuadraticMesh()

       smesh.SetName(V_Bent3M,'V_Bent3')
       V_Bent3M.Compute()
       V_Bent3M.GroupOnFilter( SMESH.NODE,'P3', smesh.GetFilter( SMESH.NODE, SMESH.FT_LyingOnGeom,'=',P3))
       V_Bent3M.GroupOnFilter( SMESH.NODE,'P4', smesh.GetFilter( SMESH.NODE, SMESH.FT_LyingOnGeom,'=',P4))
       V_Bent3M.GroupOnGeom(V_Bent3)
    except:
       ERREUR=True
       print ("   =>ERROR WHILE GENERATING THE MESH!_")
       return
            


    if ListeV!=[]:
       _W=geompy.MakeWire(ListeV,1e-7)
       Pipe = geompy.MakePipe( FaceTube ,_W)
       Pipe.SetColor(SALOMEDS.Color(0.8,0.8,0.8))
       Pipe_id=geompy.addToStudy(Pipe,"Pipe")
       gg.createAndDisplayGO(Pipe_id)
       gg.setDisplayMode(Pipe_id,1)
       for x in Liste:
           geompy.addToStudyInFather(Pipe,x[0],x[1])
       Liste=[]
       ListeV=[]
    

    try:
      print("Add V4")
      V4= geompy.MakeVector(P5,P6)
      #Liste.append([P5,"P5"])
      geompy.addToStudy(V4,"V4" )
      Liste.append([V4,"V4"])
      ListeV.append(V4)
        

      _C1 = geompy.MakeCircle(P5, V4,35)
      _C2 = geompy.MakeCircle(P5, V4,31)
      FaceTube = geompy.MakeFaceWires([_C1, _C2], 1)
      Liste.append([_C1 ,"CercleExt"])
      Liste.append([_C2 ,"CercleInt"])
            

    except:
       ERREUR=True
       print ("   =>ERROR BUILDING THE GEOMETRY!")
       for x in Liste :
           geompy.addToStudy(x[0],x[1])
       return

    try:
       V4M = smesh.Mesh(V4)
       Decoupage = V4M.Segment()
       Decoupage.NumberOfSegments(8)
       Quadratic_Mesh = Decoupage.QuadraticMesh()

       smesh.SetName(V4M,'V4')
       V4M.Compute()
       V4M.Group(P5)
       V4M.Group(P6)
       V4M.GroupOnGeom(V4)
    except:
       ERREUR=True
       print ("   =>ERROR WHILE GENERATING THE MESH!_")
       return
        


    if ListeV!=[]:
       _W=geompy.MakeWire(ListeV,1e-7)
       Pipe = geompy.MakePipe( FaceTube ,_W)
       Pipe.SetColor(SALOMEDS.Color(0.8,0.8,0.8))
       Pipe_id=geompy.addToStudy(Pipe,"Pipe")
       gg.createAndDisplayGO(Pipe_id)
       gg.setDisplayMode(Pipe_id,1)
       for x in Liste:
           geompy.addToStudyInFather(Pipe,x[0],x[1])
       Liste=[]
       ListeV=[]
    

    try:
      print("Add  V_Bent5 ")
      Liste=[]
      V_Bent5 = geompy.MakeArcCenter(P6_7_center,P6,P7)
      geompy.addToStudy(V_Bent5,"V_Bent5")
      Liste.append([V_Bent5,"V_Bent5"])
      ListeV.append(V_Bent5)

         

      C1 = geompy.MakeCircle(P6,Vd2x_P6,35)
      C2 = geompy.MakeCircle(P6,Vd2x_P6,31)
      FaceTube = geompy.MakeFaceWires([C1, C2], 1)
      Liste.append([C1 ,"CercleExt"])
      Liste.append([C2 ,"CercleInt"])
            


    except:
       ERREUR=True
       print ("   =>ERROR BUILDING THE GEOMETRY!")
       for x in Liste :
           geompy.addToStudy(x[0],x[1])
       return

    try:
       V_Bent5M = smesh.Mesh(V_Bent5)
       Decoupage = V_Bent5M.Segment()
       Decoupage.NumberOfSegments(8)
       Quadratic_Mesh = Decoupage.QuadraticMesh()

       smesh.SetName(V_Bent5M,'V_Bent5')
       V_Bent5M.Compute()
       V_Bent5M.GroupOnFilter( SMESH.NODE,'P6', smesh.GetFilter( SMESH.NODE, SMESH.FT_LyingOnGeom,'=',P6))
       V_Bent5M.GroupOnFilter( SMESH.NODE,'P7', smesh.GetFilter( SMESH.NODE, SMESH.FT_LyingOnGeom,'=',P7))
       V_Bent5M.GroupOnGeom(V_Bent5)
    except:
       ERREUR=True
       print ("   =>ERROR WHILE GENERATING THE MESH!_")
       return
            


    if ListeV!=[]:
       _W=geompy.MakeWire(ListeV,1e-7)
       Pipe = geompy.MakePipe( FaceTube ,_W)
       Pipe.SetColor(SALOMEDS.Color(0.8,0.8,0.8))
       Pipe_id=geompy.addToStudy(Pipe,"Pipe")
       gg.createAndDisplayGO(Pipe_id)
       gg.setDisplayMode(Pipe_id,1)
       for x in Liste:
           geompy.addToStudyInFather(Pipe,x[0],x[1])
       Liste=[]
       ListeV=[]
    

    try:
      print("Add V6")
      V6= geompy.MakeVector(P7,P8)
      #Liste.append([P7,"P7"])
      geompy.addToStudy(V6,"V6" )
      Liste.append([V6,"V6"])
      ListeV.append(V6)
        

      _C1 = geompy.MakeCircle(P7, V6,35)
      _C2 = geompy.MakeCircle(P7, V6,31)
      FaceTube = geompy.MakeFaceWires([_C1, _C2], 1)
      Liste.append([_C1 ,"CercleExt"])
      Liste.append([_C2 ,"CercleInt"])
            

    except:
       ERREUR=True
       print ("   =>ERROR BUILDING THE GEOMETRY!")
       for x in Liste :
           geompy.addToStudy(x[0],x[1])
       return

    try:
       V6M = smesh.Mesh(V6)
       Decoupage = V6M.Segment()
       Decoupage.NumberOfSegments(8)
       Quadratic_Mesh = Decoupage.QuadraticMesh()

       smesh.SetName(V6M,'V6')
       V6M.Compute()
       V6M.Group(P7)
       V6M.Group(P8)
       V6M.GroupOnGeom(V6)
    except:
       ERREUR=True
       print ("   =>ERROR WHILE GENERATING THE MESH!_")
       return
        


    if ListeV!=[]:
       _W=geompy.MakeWire(ListeV,1e-7)
       Pipe = geompy.MakePipe( FaceTube ,_W)
       Pipe.SetColor(SALOMEDS.Color(0.8,0.8,0.8))
       Pipe_id=geompy.addToStudy(Pipe,"Pipe")
       gg.createAndDisplayGO(Pipe_id)
       gg.setDisplayMode(Pipe_id,1)
       for x in Liste:
           geompy.addToStudyInFather(Pipe,x[0],x[1])
       Liste=[]
       ListeV=[]
    

    try:
      print("Add  V_Bent7 ")
      Liste=[]
      V_Bent7 = geompy.MakeArcCenter(P8_9_center,P8,P9)
      geompy.addToStudy(V_Bent7,"V_Bent7")
      Liste.append([V_Bent7,"V_Bent7"])
      ListeV.append(V_Bent7)

         

      C1 = geompy.MakeCircle(P8,Vd2x_P8,35)
      C2 = geompy.MakeCircle(P8,Vd2x_P8,31)
      FaceTube = geompy.MakeFaceWires([C1, C2], 1)
      Liste.append([C1 ,"CercleExt"])
      Liste.append([C2 ,"CercleInt"])
            


    except:
       ERREUR=True
       print ("   =>ERROR BUILDING THE GEOMETRY!")
       for x in Liste :
           geompy.addToStudy(x[0],x[1])
       return

    try:
       V_Bent7M = smesh.Mesh(V_Bent7)
       Decoupage = V_Bent7M.Segment()
       Decoupage.NumberOfSegments(8)
       Quadratic_Mesh = Decoupage.QuadraticMesh()

       smesh.SetName(V_Bent7M,'V_Bent7')
       V_Bent7M.Compute()
       V_Bent7M.GroupOnFilter( SMESH.NODE,'P8', smesh.GetFilter( SMESH.NODE, SMESH.FT_LyingOnGeom,'=',P8))
       V_Bent7M.GroupOnFilter( SMESH.NODE,'P9', smesh.GetFilter( SMESH.NODE, SMESH.FT_LyingOnGeom,'=',P9))
       V_Bent7M.GroupOnGeom(V_Bent7)
    except:
       ERREUR=True
       print ("   =>ERROR WHILE GENERATING THE MESH!_")
       return
            


    if ListeV!=[]:
       _W=geompy.MakeWire(ListeV,1e-7)
       Pipe = geompy.MakePipe( FaceTube ,_W)
       Pipe.SetColor(SALOMEDS.Color(0.8,0.8,0.8))
       Pipe_id=geompy.addToStudy(Pipe,"Pipe")
       gg.createAndDisplayGO(Pipe_id)
       gg.setDisplayMode(Pipe_id,1)
       for x in Liste:
           geompy.addToStudyInFather(Pipe,x[0],x[1])
       Liste=[]
       ListeV=[]
    

    try:
      print("Add V8")
      V8= geompy.MakeVector(P10,P11)
      #Liste.append([P10,"P10"])
      geompy.addToStudy(V8,"V8" )
      Liste.append([V8,"V8"])
      ListeV.append(V8)
        

      _C1 = geompy.MakeCircle(P10, V8,35)
      _C2 = geompy.MakeCircle(P10, V8,31)
      FaceTube = geompy.MakeFaceWires([_C1, _C2], 1)
      Liste.append([_C1 ,"CercleExt"])
      Liste.append([_C2 ,"CercleInt"])
            

    except:
       ERREUR=True
       print ("   =>ERROR BUILDING THE GEOMETRY!")
       for x in Liste :
           geompy.addToStudy(x[0],x[1])
       return

    try:
       V8M = smesh.Mesh(V8)
       Decoupage = V8M.Segment()
       Decoupage.NumberOfSegments(8)
       Quadratic_Mesh = Decoupage.QuadraticMesh()

       smesh.SetName(V8M,'V8')
       V8M.Compute()
       V8M.Group(P10)
       V8M.Group(P11)
       V8M.GroupOnGeom(V8)
    except:
       ERREUR=True
       print ("   =>ERROR WHILE GENERATING THE MESH!_")
       return
        


    if ListeV!=[]:
       _W=geompy.MakeWire(ListeV,1e-7)
       Pipe = geompy.MakePipe( FaceTube ,_W)
       Pipe.SetColor(SALOMEDS.Color(0.8,0.8,0.8))
       Pipe_id=geompy.addToStudy(Pipe,"Pipe")
       gg.createAndDisplayGO(Pipe_id)
       gg.setDisplayMode(Pipe_id,1)
       for x in Liste:
           geompy.addToStudyInFather(Pipe,x[0],x[1])
       Liste=[]
       ListeV=[]
    

    try:
      print("Add  V_Bent9 ")
      Liste=[]
      V_Bent9 = geompy.MakeArcCenter(P11_12_center,P11,P12)
      geompy.addToStudy(V_Bent9,"V_Bent9")
      Liste.append([V_Bent9,"V_Bent9"])
      ListeV.append(V_Bent9)

         

      C1 = geompy.MakeCircle(P11,Vd2x_P11,35)
      C2 = geompy.MakeCircle(P11,Vd2x_P11,31)
      FaceTube = geompy.MakeFaceWires([C1, C2], 1)
      Liste.append([C1 ,"CercleExt"])
      Liste.append([C2 ,"CercleInt"])
            


    except:
       ERREUR=True
       print ("   =>ERROR BUILDING THE GEOMETRY!")
       for x in Liste :
           geompy.addToStudy(x[0],x[1])
       return

    try:
       V_Bent9M = smesh.Mesh(V_Bent9)
       Decoupage = V_Bent9M.Segment()
       Decoupage.NumberOfSegments(8)
       Quadratic_Mesh = Decoupage.QuadraticMesh()

       smesh.SetName(V_Bent9M,'V_Bent9')
       V_Bent9M.Compute()
       V_Bent9M.GroupOnFilter( SMESH.NODE,'P11', smesh.GetFilter( SMESH.NODE, SMESH.FT_LyingOnGeom,'=',P11))
       V_Bent9M.GroupOnFilter( SMESH.NODE,'P12', smesh.GetFilter( SMESH.NODE, SMESH.FT_LyingOnGeom,'=',P12))
       V_Bent9M.GroupOnGeom(V_Bent9)
    except:
       ERREUR=True
       print ("   =>ERROR WHILE GENERATING THE MESH!_")
       return
            


    if ListeV!=[]:
       _W=geompy.MakeWire(ListeV,1e-7)
       Pipe = geompy.MakePipe( FaceTube ,_W)
       Pipe.SetColor(SALOMEDS.Color(0.8,0.8,0.8))
       Pipe_id=geompy.addToStudy(Pipe,"Pipe")
       gg.createAndDisplayGO(Pipe_id)
       gg.setDisplayMode(Pipe_id,1)
       for x in Liste:
           geompy.addToStudyInFather(Pipe,x[0],x[1])
       Liste=[]
       ListeV=[]
    

    try:
      print("Add V10")
      V10= geompy.MakeVector(P12,P13)
      #Liste.append([P12,"P12"])
      geompy.addToStudy(V10,"V10" )
      Liste.append([V10,"V10"])
      ListeV.append(V10)
        

      _C1 = geompy.MakeCircle(P12, V10,35)
      _C2 = geompy.MakeCircle(P12, V10,31)
      FaceTube = geompy.MakeFaceWires([_C1, _C2], 1)
      Liste.append([_C1 ,"CercleExt"])
      Liste.append([_C2 ,"CercleInt"])
            

    except:
       ERREUR=True
       print ("   =>ERROR BUILDING THE GEOMETRY!")
       for x in Liste :
           geompy.addToStudy(x[0],x[1])
       return

    try:
       V10M = smesh.Mesh(V10)
       Decoupage = V10M.Segment()
       Decoupage.NumberOfSegments(8)
       Quadratic_Mesh = Decoupage.QuadraticMesh()

       smesh.SetName(V10M,'V10')
       V10M.Compute()
       V10M.Group(P12)
       V10M.Group(P13)
       V10M.GroupOnGeom(V10)
    except:
       ERREUR=True
       print ("   =>ERROR WHILE GENERATING THE MESH!_")
       return
        


    if ListeV!=[]:
       _W=geompy.MakeWire(ListeV,1e-7)
       Pipe = geompy.MakePipe( FaceTube ,_W)
       Pipe.SetColor(SALOMEDS.Color(0.8,0.8,0.8))
       Pipe_id=geompy.addToStudy(Pipe,"Pipe")
       gg.createAndDisplayGO(Pipe_id)
       gg.setDisplayMode(Pipe_id,1)
       for x in Liste:
           geompy.addToStudyInFather(Pipe,x[0],x[1])
       Liste=[]
       ListeV=[]
    

    try:
      print("Add  V_Bent11 ")
      Liste=[]
      V_Bent11 = geompy.MakeArcCenter(P13_14_center,P13,P14)
      geompy.addToStudy(V_Bent11,"V_Bent11")
      Liste.append([V_Bent11,"V_Bent11"])
      ListeV.append(V_Bent11)

         

      C1 = geompy.MakeCircle(P13,Vd2x_P13,35)
      C2 = geompy.MakeCircle(P13,Vd2x_P13,31)
      FaceTube = geompy.MakeFaceWires([C1, C2], 1)
      Liste.append([C1 ,"CercleExt"])
      Liste.append([C2 ,"CercleInt"])
            


    except:
       ERREUR=True
       print ("   =>ERROR BUILDING THE GEOMETRY!")
       for x in Liste :
           geompy.addToStudy(x[0],x[1])
       return

    try:
       V_Bent11M = smesh.Mesh(V_Bent11)
       Decoupage = V_Bent11M.Segment()
       Decoupage.NumberOfSegments(8)
       Quadratic_Mesh = Decoupage.QuadraticMesh()

       smesh.SetName(V_Bent11M,'V_Bent11')
       V_Bent11M.Compute()
       V_Bent11M.GroupOnFilter( SMESH.NODE,'P13', smesh.GetFilter( SMESH.NODE, SMESH.FT_LyingOnGeom,'=',P13))
       V_Bent11M.GroupOnFilter( SMESH.NODE,'P14', smesh.GetFilter( SMESH.NODE, SMESH.FT_LyingOnGeom,'=',P14))
       V_Bent11M.GroupOnGeom(V_Bent11)
    except:
       ERREUR=True
       print ("   =>ERROR WHILE GENERATING THE MESH!_")
       return
            


    if ListeV!=[]:
       _W=geompy.MakeWire(ListeV,1e-7)
       Pipe = geompy.MakePipe( FaceTube ,_W)
       Pipe.SetColor(SALOMEDS.Color(0.8,0.8,0.8))
       Pipe_id=geompy.addToStudy(Pipe,"Pipe")
       gg.createAndDisplayGO(Pipe_id)
       gg.setDisplayMode(Pipe_id,1)
       for x in Liste:
           geompy.addToStudyInFather(Pipe,x[0],x[1])
       Liste=[]
       ListeV=[]
    

    try:
      print("Add V12")
      V12= geompy.MakeVector(P15,P16)
      #Liste.append([P15,"P15"])
      geompy.addToStudy(V12,"V12" )
      Liste.append([V12,"V12"])
      ListeV.append(V12)
        

      _C1 = geompy.MakeCircle(P15, V12,35)
      _C2 = geompy.MakeCircle(P15, V12,31)
      FaceTube = geompy.MakeFaceWires([_C1, _C2], 1)
      Liste.append([_C1 ,"CercleExt"])
      Liste.append([_C2 ,"CercleInt"])
            

    except:
       ERREUR=True
       print ("   =>ERROR BUILDING THE GEOMETRY!")
       for x in Liste :
           geompy.addToStudy(x[0],x[1])
       return

    try:
       V12M = smesh.Mesh(V12)
       Decoupage = V12M.Segment()
       Decoupage.NumberOfSegments(8)
       Quadratic_Mesh = Decoupage.QuadraticMesh()

       smesh.SetName(V12M,'V12')
       V12M.Compute()
       V12M.Group(P15)
       V12M.Group(P16)
       V12M.GroupOnGeom(V12)
    except:
       ERREUR=True
       print ("   =>ERROR WHILE GENERATING THE MESH!_")
       return
        


    if ListeV!=[]:
       _W=geompy.MakeWire(ListeV,1e-7)
       Pipe = geompy.MakePipe( FaceTube ,_W)
       Pipe.SetColor(SALOMEDS.Color(0.8,0.8,0.8))
       Pipe_id=geompy.addToStudy(Pipe,"Pipe")
       gg.createAndDisplayGO(Pipe_id)
       gg.setDisplayMode(Pipe_id,1)
       for x in Liste:
           geompy.addToStudyInFather(Pipe,x[0],x[1])
       Liste=[]
       ListeV=[]
    

    try:
      print("Add  V_Bent13 ")
      Liste=[]
      V_Bent13 = geompy.MakeArcCenter(P16_17_center,P16,P17)
      geompy.addToStudy(V_Bent13,"V_Bent13")
      Liste.append([V_Bent13,"V_Bent13"])
      ListeV.append(V_Bent13)

         

      C1 = geompy.MakeCircle(P16,Vd2x_P16,35)
      C2 = geompy.MakeCircle(P16,Vd2x_P16,31)
      FaceTube = geompy.MakeFaceWires([C1, C2], 1)
      Liste.append([C1 ,"CercleExt"])
      Liste.append([C2 ,"CercleInt"])
            


    except:
       ERREUR=True
       print ("   =>ERROR BUILDING THE GEOMETRY!")
       for x in Liste :
           geompy.addToStudy(x[0],x[1])
       return

    try:
       V_Bent13M = smesh.Mesh(V_Bent13)
       Decoupage = V_Bent13M.Segment()
       Decoupage.NumberOfSegments(8)
       Quadratic_Mesh = Decoupage.QuadraticMesh()

       smesh.SetName(V_Bent13M,'V_Bent13')
       V_Bent13M.Compute()
       V_Bent13M.GroupOnFilter( SMESH.NODE,'P16', smesh.GetFilter( SMESH.NODE, SMESH.FT_LyingOnGeom,'=',P16))
       V_Bent13M.GroupOnFilter( SMESH.NODE,'P17', smesh.GetFilter( SMESH.NODE, SMESH.FT_LyingOnGeom,'=',P17))
       V_Bent13M.GroupOnGeom(V_Bent13)
    except:
       ERREUR=True
       print ("   =>ERROR WHILE GENERATING THE MESH!_")
       return
            


    if ListeV!=[]:
       _W=geompy.MakeWire(ListeV,1e-7)
       Pipe = geompy.MakePipe( FaceTube ,_W)
       Pipe.SetColor(SALOMEDS.Color(0.8,0.8,0.8))
       Pipe_id=geompy.addToStudy(Pipe,"Pipe")
       gg.createAndDisplayGO(Pipe_id)
       gg.setDisplayMode(Pipe_id,1)
       for x in Liste:
           geompy.addToStudyInFather(Pipe,x[0],x[1])
       Liste=[]
       ListeV=[]
    

    try:
      print("Add V14")
      V14= geompy.MakeVector(P17,P18)
      #Liste.append([P17,"P17"])
      geompy.addToStudy(V14,"V14" )
      Liste.append([V14,"V14"])
      ListeV.append(V14)
        

      _C1 = geompy.MakeCircle(P17, V14,35)
      _C2 = geompy.MakeCircle(P17, V14,31)
      FaceTube = geompy.MakeFaceWires([_C1, _C2], 1)
      Liste.append([_C1 ,"CercleExt"])
      Liste.append([_C2 ,"CercleInt"])
            

    except:
       ERREUR=True
       print ("   =>ERROR BUILDING THE GEOMETRY!")
       for x in Liste :
           geompy.addToStudy(x[0],x[1])
       return

    try:
       V14M = smesh.Mesh(V14)
       Decoupage = V14M.Segment()
       Decoupage.NumberOfSegments(8)
       Quadratic_Mesh = Decoupage.QuadraticMesh()

       smesh.SetName(V14M,'V14')
       V14M.Compute()
       V14M.Group(P17)
       V14M.Group(P18)
       V14M.GroupOnGeom(V14)
    except:
       ERREUR=True
       print ("   =>ERROR WHILE GENERATING THE MESH!_")
       return
        


    if ListeV!=[]:
       _W=geompy.MakeWire(ListeV,1e-7)
       Pipe = geompy.MakePipe( FaceTube ,_W)
       Pipe.SetColor(SALOMEDS.Color(0.8,0.8,0.8))
       Pipe_id=geompy.addToStudy(Pipe,"Pipe")
       gg.createAndDisplayGO(Pipe_id)
       gg.setDisplayMode(Pipe_id,1)
       for x in Liste:
           geompy.addToStudyInFather(Pipe,x[0],x[1])
       Liste=[]
       ListeV=[]
    

    try:
      print("Add  V_Bent15 ")
      Liste=[]
      V_Bent15 = geompy.MakeArcCenter(P18_19_center,P18,P19)
      geompy.addToStudy(V_Bent15,"V_Bent15")
      Liste.append([V_Bent15,"V_Bent15"])
      ListeV.append(V_Bent15)

         

      C1 = geompy.MakeCircle(P18,Vd2x_P18,35)
      C2 = geompy.MakeCircle(P18,Vd2x_P18,31)
      FaceTube = geompy.MakeFaceWires([C1, C2], 1)
      Liste.append([C1 ,"CercleExt"])
      Liste.append([C2 ,"CercleInt"])
            


    except:
       ERREUR=True
       print ("   =>ERROR BUILDING THE GEOMETRY!")
       for x in Liste :
           geompy.addToStudy(x[0],x[1])
       return

    try:
       V_Bent15M = smesh.Mesh(V_Bent15)
       Decoupage = V_Bent15M.Segment()
       Decoupage.NumberOfSegments(8)
       Quadratic_Mesh = Decoupage.QuadraticMesh()

       smesh.SetName(V_Bent15M,'V_Bent15')
       V_Bent15M.Compute()
       V_Bent15M.GroupOnFilter( SMESH.NODE,'P18', smesh.GetFilter( SMESH.NODE, SMESH.FT_LyingOnGeom,'=',P18))
       V_Bent15M.GroupOnFilter( SMESH.NODE,'P19', smesh.GetFilter( SMESH.NODE, SMESH.FT_LyingOnGeom,'=',P19))
       V_Bent15M.GroupOnGeom(V_Bent15)
    except:
       ERREUR=True
       print ("   =>ERROR WHILE GENERATING THE MESH!_")
       return
            


    if ListeV!=[]:
       _W=geompy.MakeWire(ListeV,1e-7)
       Pipe = geompy.MakePipe( FaceTube ,_W)
       Pipe.SetColor(SALOMEDS.Color(0.8,0.8,0.8))
       Pipe_id=geompy.addToStudy(Pipe,"Pipe")
       gg.createAndDisplayGO(Pipe_id)
       gg.setDisplayMode(Pipe_id,1)
       for x in Liste:
           geompy.addToStudyInFather(Pipe,x[0],x[1])
       Liste=[]
       ListeV=[]
    

    try:
      print("Add V16")
      V16= geompy.MakeVector(P20,P21)
      #Liste.append([P20,"P20"])
      geompy.addToStudy(V16,"V16" )
      Liste.append([V16,"V16"])
      ListeV.append(V16)
        

      _C1 = geompy.MakeCircle(P20, V16,35)
      _C2 = geompy.MakeCircle(P20, V16,31)
      FaceTube = geompy.MakeFaceWires([_C1, _C2], 1)
      Liste.append([_C1 ,"CercleExt"])
      Liste.append([_C2 ,"CercleInt"])
            

    except:
       ERREUR=True
       print ("   =>ERROR BUILDING THE GEOMETRY!")
       for x in Liste :
           geompy.addToStudy(x[0],x[1])
       return

    try:
       V16M = smesh.Mesh(V16)
       Decoupage = V16M.Segment()
       Decoupage.NumberOfSegments(8)
       Quadratic_Mesh = Decoupage.QuadraticMesh()

       smesh.SetName(V16M,'V16')
       V16M.Compute()
       V16M.Group(P20)
       V16M.Group(P21)
       V16M.GroupOnGeom(V16)
    except:
       ERREUR=True
       print ("   =>ERROR WHILE GENERATING THE MESH!_")
       return
        


    if ListeV!=[]:
       _W=geompy.MakeWire(ListeV,1e-7)
       Pipe = geompy.MakePipe( FaceTube ,_W)
       Pipe.SetColor(SALOMEDS.Color(0.8,0.8,0.8))
       Pipe_id=geompy.addToStudy(Pipe,"Pipe")
       gg.createAndDisplayGO(Pipe_id)
       gg.setDisplayMode(Pipe_id,1)
       for x in Liste:
           geompy.addToStudyInFather(Pipe,x[0],x[1])
       Liste=[]
       ListeV=[]
    

    try:
      print("Add  V_Bent17 ")
      Liste=[]
      V_Bent17 = geompy.MakeArcCenter(P21_22_center,P21,P22)
      geompy.addToStudy(V_Bent17,"V_Bent17")
      Liste.append([V_Bent17,"V_Bent17"])
      ListeV.append(V_Bent17)

         

      C1 = geompy.MakeCircle(P21,Vd2x_P21,35)
      C2 = geompy.MakeCircle(P21,Vd2x_P21,31)
      FaceTube = geompy.MakeFaceWires([C1, C2], 1)
      Liste.append([C1 ,"CercleExt"])
      Liste.append([C2 ,"CercleInt"])
            


    except:
       ERREUR=True
       print ("   =>ERROR BUILDING THE GEOMETRY!")
       for x in Liste :
           geompy.addToStudy(x[0],x[1])
       return

    try:
       V_Bent17M = smesh.Mesh(V_Bent17)
       Decoupage = V_Bent17M.Segment()
       Decoupage.NumberOfSegments(8)
       Quadratic_Mesh = Decoupage.QuadraticMesh()

       smesh.SetName(V_Bent17M,'V_Bent17')
       V_Bent17M.Compute()
       V_Bent17M.GroupOnFilter( SMESH.NODE,'P21', smesh.GetFilter( SMESH.NODE, SMESH.FT_LyingOnGeom,'=',P21))
       V_Bent17M.GroupOnFilter( SMESH.NODE,'P22', smesh.GetFilter( SMESH.NODE, SMESH.FT_LyingOnGeom,'=',P22))
       V_Bent17M.GroupOnGeom(V_Bent17)
    except:
       ERREUR=True
       print ("   =>ERROR WHILE GENERATING THE MESH!_")
       return
            


    if ListeV!=[]:
       _W=geompy.MakeWire(ListeV,1e-7)
       Pipe = geompy.MakePipe( FaceTube ,_W)
       Pipe.SetColor(SALOMEDS.Color(0.8,0.8,0.8))
       Pipe_id=geompy.addToStudy(Pipe,"Pipe")
       gg.createAndDisplayGO(Pipe_id)
       gg.setDisplayMode(Pipe_id,1)
       for x in Liste:
           geompy.addToStudyInFather(Pipe,x[0],x[1])
       Liste=[]
       ListeV=[]
    

    try:
      print("Add V18")
      V18= geompy.MakeVector(P22,P23)
      #Liste.append([P22,"P22"])
      geompy.addToStudy(V18,"V18" )
      Liste.append([V18,"V18"])
      ListeV.append(V18)
        

      _C1 = geompy.MakeCircle(P22, V18,35)
      _C2 = geompy.MakeCircle(P22, V18,31)
      FaceTube = geompy.MakeFaceWires([_C1, _C2], 1)
      Liste.append([_C1 ,"CercleExt"])
      Liste.append([_C2 ,"CercleInt"])
            

    except:
       ERREUR=True
       print ("   =>ERROR BUILDING THE GEOMETRY!")
       for x in Liste :
           geompy.addToStudy(x[0],x[1])
       return

    try:
       V18M = smesh.Mesh(V18)
       Decoupage = V18M.Segment()
       Decoupage.NumberOfSegments(8)
       Quadratic_Mesh = Decoupage.QuadraticMesh()

       smesh.SetName(V18M,'V18')
       V18M.Compute()
       V18M.Group(P22)
       V18M.Group(P23)
       V18M.GroupOnGeom(V18)
    except:
       ERREUR=True
       print ("   =>ERROR WHILE GENERATING THE MESH!_")
       return
        


    if ListeV!=[]:
       _W=geompy.MakeWire(ListeV,1e-7)
       Pipe = geompy.MakePipe( FaceTube ,_W)
       Pipe.SetColor(SALOMEDS.Color(0.8,0.8,0.8))
       Pipe_id=geompy.addToStudy(Pipe,"Pipe")
       gg.createAndDisplayGO(Pipe_id)
       gg.setDisplayMode(Pipe_id,1)
       for x in Liste:
           geompy.addToStudyInFather(Pipe,x[0],x[1])
       Liste=[]
       ListeV=[]
    

    try:
      print("Add  V_Bent19 ")
      Liste=[]
      V_Bent19 = geompy.MakeArcCenter(P23_24_center,P23,P24)
      geompy.addToStudy(V_Bent19,"V_Bent19")
      Liste.append([V_Bent19,"V_Bent19"])
      ListeV.append(V_Bent19)

         

      C1 = geompy.MakeCircle(P23,Vd2x_P23,35)
      C2 = geompy.MakeCircle(P23,Vd2x_P23,31)
      FaceTube = geompy.MakeFaceWires([C1, C2], 1)
      Liste.append([C1 ,"CercleExt"])
      Liste.append([C2 ,"CercleInt"])
            


    except:
       ERREUR=True
       print ("   =>ERROR BUILDING THE GEOMETRY!")
       for x in Liste :
           geompy.addToStudy(x[0],x[1])
       return

    try:
       V_Bent19M = smesh.Mesh(V_Bent19)
       Decoupage = V_Bent19M.Segment()
       Decoupage.NumberOfSegments(8)
       Quadratic_Mesh = Decoupage.QuadraticMesh()

       smesh.SetName(V_Bent19M,'V_Bent19')
       V_Bent19M.Compute()
       V_Bent19M.GroupOnFilter( SMESH.NODE,'P23', smesh.GetFilter( SMESH.NODE, SMESH.FT_LyingOnGeom,'=',P23))
       V_Bent19M.GroupOnFilter( SMESH.NODE,'P24', smesh.GetFilter( SMESH.NODE, SMESH.FT_LyingOnGeom,'=',P24))
       V_Bent19M.GroupOnGeom(V_Bent19)
    except:
       ERREUR=True
       print ("   =>ERROR WHILE GENERATING THE MESH!_")
       return
            


    if ListeV!=[]:
       _W=geompy.MakeWire(ListeV,1e-7)
       Pipe = geompy.MakePipe( FaceTube ,_W)
       Pipe.SetColor(SALOMEDS.Color(0.8,0.8,0.8))
       Pipe_id=geompy.addToStudy(Pipe,"Pipe")
       gg.createAndDisplayGO(Pipe_id)
       gg.setDisplayMode(Pipe_id,1)
       for x in Liste:
           geompy.addToStudyInFather(Pipe,x[0],x[1])
       Liste=[]
       ListeV=[]
    

    try:
      print("Add V20")
      V20= geompy.MakeVector(P25,P26)
      #Liste.append([P25,"P25"])
      geompy.addToStudy(V20,"V20" )
      Liste.append([V20,"V20"])
      ListeV.append(V20)
        

      _C1 = geompy.MakeCircle(P25, V20,35)
      _C2 = geompy.MakeCircle(P25, V20,31)
      FaceTube = geompy.MakeFaceWires([_C1, _C2], 1)
      Liste.append([_C1 ,"CercleExt"])
      Liste.append([_C2 ,"CercleInt"])
            

    except:
       ERREUR=True
       print ("   =>ERROR BUILDING THE GEOMETRY!")
       for x in Liste :
           geompy.addToStudy(x[0],x[1])
       return

    try:
       V20M = smesh.Mesh(V20)
       Decoupage = V20M.Segment()
       Decoupage.NumberOfSegments(8)
       Quadratic_Mesh = Decoupage.QuadraticMesh()

       smesh.SetName(V20M,'V20')
       V20M.Compute()
       V20M.Group(P25)
       V20M.Group(P26)
       V20M.GroupOnGeom(V20)
    except:
       ERREUR=True
       print ("   =>ERROR WHILE GENERATING THE MESH!_")
       return
        


    if ListeV!=[]:
       _W=geompy.MakeWire(ListeV,1e-7)
       Pipe = geompy.MakePipe( FaceTube ,_W)
       Pipe.SetColor(SALOMEDS.Color(0.8,0.8,0.8))
       Pipe_id=geompy.addToStudy(Pipe,"Pipe")
       gg.createAndDisplayGO(Pipe_id)
       gg.setDisplayMode(Pipe_id,1)
       for x in Liste:
           geompy.addToStudyInFather(Pipe,x[0],x[1])
       Liste=[]
       ListeV=[]
    

    try:
      print("Add  V_Bent21 ")
      Liste=[]
      V_Bent21 = geompy.MakeArcCenter(P26_27_center,P26,P27)
      geompy.addToStudy(V_Bent21,"V_Bent21")
      Liste.append([V_Bent21,"V_Bent21"])
      ListeV.append(V_Bent21)

         

      C1 = geompy.MakeCircle(P26,Vd2x_P26,35)
      C2 = geompy.MakeCircle(P26,Vd2x_P26,31)
      FaceTube = geompy.MakeFaceWires([C1, C2], 1)
      Liste.append([C1 ,"CercleExt"])
      Liste.append([C2 ,"CercleInt"])
            


    except:
       ERREUR=True
       print ("   =>ERROR BUILDING THE GEOMETRY!")
       for x in Liste :
           geompy.addToStudy(x[0],x[1])
       return

    try:
       V_Bent21M = smesh.Mesh(V_Bent21)
       Decoupage = V_Bent21M.Segment()
       Decoupage.NumberOfSegments(8)
       Quadratic_Mesh = Decoupage.QuadraticMesh()

       smesh.SetName(V_Bent21M,'V_Bent21')
       V_Bent21M.Compute()
       V_Bent21M.GroupOnFilter( SMESH.NODE,'P26', smesh.GetFilter( SMESH.NODE, SMESH.FT_LyingOnGeom,'=',P26))
       V_Bent21M.GroupOnFilter( SMESH.NODE,'P27', smesh.GetFilter( SMESH.NODE, SMESH.FT_LyingOnGeom,'=',P27))
       V_Bent21M.GroupOnGeom(V_Bent21)
    except:
       ERREUR=True
       print ("   =>ERROR WHILE GENERATING THE MESH!_")
       return
            


    if ListeV!=[]:
       _W=geompy.MakeWire(ListeV,1e-7)
       Pipe = geompy.MakePipe( FaceTube ,_W)
       Pipe.SetColor(SALOMEDS.Color(0.8,0.8,0.8))
       Pipe_id=geompy.addToStudy(Pipe,"Pipe")
       gg.createAndDisplayGO(Pipe_id)
       gg.setDisplayMode(Pipe_id,1)
       for x in Liste:
           geompy.addToStudyInFather(Pipe,x[0],x[1])
       Liste=[]
       ListeV=[]
    

    try:
      print("Add V22")
      V22= geompy.MakeVector(P27,P28)
      #Liste.append([P27,"P27"])
      geompy.addToStudy(V22,"V22" )
      Liste.append([V22,"V22"])
      ListeV.append(V22)
        

      _C1 = geompy.MakeCircle(P27, V22,35)
      _C2 = geompy.MakeCircle(P27, V22,31)
      FaceTube = geompy.MakeFaceWires([_C1, _C2], 1)
      Liste.append([_C1 ,"CercleExt"])
      Liste.append([_C2 ,"CercleInt"])
            

    except:
       ERREUR=True
       print ("   =>ERROR BUILDING THE GEOMETRY!")
       for x in Liste :
           geompy.addToStudy(x[0],x[1])
       return

    try:
       V22M = smesh.Mesh(V22)
       Decoupage = V22M.Segment()
       Decoupage.NumberOfSegments(8)
       Quadratic_Mesh = Decoupage.QuadraticMesh()

       smesh.SetName(V22M,'V22')
       V22M.Compute()
       V22M.Group(P27)
       V22M.Group(P28)
       V22M.GroupOnGeom(V22)
    except:
       ERREUR=True
       print ("   =>ERROR WHILE GENERATING THE MESH!_")
       return
        


    if ListeV!=[]:
       _W=geompy.MakeWire(ListeV,1e-7)
       Pipe = geompy.MakePipe( FaceTube ,_W)
       Pipe.SetColor(SALOMEDS.Color(0.8,0.8,0.8))
       Pipe_id=geompy.addToStudy(Pipe,"Pipe")
       gg.createAndDisplayGO(Pipe_id)
       gg.setDisplayMode(Pipe_id,1)
       for x in Liste:
           geompy.addToStudyInFather(Pipe,x[0],x[1])
       Liste=[]
       ListeV=[]
    

    try:
      print("Add  V_Bent23 ")
      Liste=[]
      V_Bent23 = geompy.MakeArcCenter(P28_29_center,P28,P29)
      geompy.addToStudy(V_Bent23,"V_Bent23")
      Liste.append([V_Bent23,"V_Bent23"])
      ListeV.append(V_Bent23)

         

      C1 = geompy.MakeCircle(P28,Vd2x_P28,35)
      C2 = geompy.MakeCircle(P28,Vd2x_P28,31)
      FaceTube = geompy.MakeFaceWires([C1, C2], 1)
      Liste.append([C1 ,"CercleExt"])
      Liste.append([C2 ,"CercleInt"])
            


    except:
       ERREUR=True
       print ("   =>ERROR BUILDING THE GEOMETRY!")
       for x in Liste :
           geompy.addToStudy(x[0],x[1])
       return

    try:
       V_Bent23M = smesh.Mesh(V_Bent23)
       Decoupage = V_Bent23M.Segment()
       Decoupage.NumberOfSegments(8)
       Quadratic_Mesh = Decoupage.QuadraticMesh()

       smesh.SetName(V_Bent23M,'V_Bent23')
       V_Bent23M.Compute()
       V_Bent23M.GroupOnFilter( SMESH.NODE,'P28', smesh.GetFilter( SMESH.NODE, SMESH.FT_LyingOnGeom,'=',P28))
       V_Bent23M.GroupOnFilter( SMESH.NODE,'P29', smesh.GetFilter( SMESH.NODE, SMESH.FT_LyingOnGeom,'=',P29))
       V_Bent23M.GroupOnGeom(V_Bent23)
    except:
       ERREUR=True
       print ("   =>ERROR WHILE GENERATING THE MESH!_")
       return
            


    if ListeV!=[]:
       _W=geompy.MakeWire(ListeV,1e-7)
       Pipe = geompy.MakePipe( FaceTube ,_W)
       Pipe.SetColor(SALOMEDS.Color(0.8,0.8,0.8))
       Pipe_id=geompy.addToStudy(Pipe,"Pipe")
       gg.createAndDisplayGO(Pipe_id)
       gg.setDisplayMode(Pipe_id,1)
       for x in Liste:
           geompy.addToStudyInFather(Pipe,x[0],x[1])
       Liste=[]
       ListeV=[]
    

    try:
      print("Add V24")
      V24= geompy.MakeVector(P30,P31)
      #Liste.append([P30,"P30"])
      geompy.addToStudy(V24,"V24" )
      Liste.append([V24,"V24"])
      ListeV.append(V24)
        

      _C1 = geompy.MakeCircle(P30, V24,35)
      _C2 = geompy.MakeCircle(P30, V24,31)
      FaceTube = geompy.MakeFaceWires([_C1, _C2], 1)
      Liste.append([_C1 ,"CercleExt"])
      Liste.append([_C2 ,"CercleInt"])
            

    except:
       ERREUR=True
       print ("   =>ERROR BUILDING THE GEOMETRY!")
       for x in Liste :
           geompy.addToStudy(x[0],x[1])
       return

    try:
       V24M = smesh.Mesh(V24)
       Decoupage = V24M.Segment()
       Decoupage.NumberOfSegments(8)
       Quadratic_Mesh = Decoupage.QuadraticMesh()

       smesh.SetName(V24M,'V24')
       V24M.Compute()
       V24M.Group(P30)
       V24M.Group(P31)
       V24M.GroupOnGeom(V24)
    except:
       ERREUR=True
       print ("   =>ERROR WHILE GENERATING THE MESH!_")
       return
        


    if ListeV!=[]:
       _W=geompy.MakeWire(ListeV,1e-7)
       Pipe = geompy.MakePipe( FaceTube ,_W)
       Pipe.SetColor(SALOMEDS.Color(0.8,0.8,0.8))
       Pipe_id=geompy.addToStudy(Pipe,"Pipe")
       gg.createAndDisplayGO(Pipe_id)
       gg.setDisplayMode(Pipe_id,1)
       for x in Liste:
           geompy.addToStudyInFather(Pipe,x[0],x[1])
       Liste=[]
       ListeV=[]
    

    try:
      print("Add  V_Bent25 ")
      Liste=[]
      V_Bent25 = geompy.MakeArcCenter(P31_32_center,P31,P32)
      geompy.addToStudy(V_Bent25,"V_Bent25")
      Liste.append([V_Bent25,"V_Bent25"])
      ListeV.append(V_Bent25)

         

      C1 = geompy.MakeCircle(P31,Vd2x_P31,35)
      C2 = geompy.MakeCircle(P31,Vd2x_P31,31)
      FaceTube = geompy.MakeFaceWires([C1, C2], 1)
      Liste.append([C1 ,"CercleExt"])
      Liste.append([C2 ,"CercleInt"])
            


    except:
       ERREUR=True
       print ("   =>ERROR BUILDING THE GEOMETRY!")
       for x in Liste :
           geompy.addToStudy(x[0],x[1])
       return

    try:
       V_Bent25M = smesh.Mesh(V_Bent25)
       Decoupage = V_Bent25M.Segment()
       Decoupage.NumberOfSegments(8)
       Quadratic_Mesh = Decoupage.QuadraticMesh()

       smesh.SetName(V_Bent25M,'V_Bent25')
       V_Bent25M.Compute()
       V_Bent25M.GroupOnFilter( SMESH.NODE,'P31', smesh.GetFilter( SMESH.NODE, SMESH.FT_LyingOnGeom,'=',P31))
       V_Bent25M.GroupOnFilter( SMESH.NODE,'P32', smesh.GetFilter( SMESH.NODE, SMESH.FT_LyingOnGeom,'=',P32))
       V_Bent25M.GroupOnGeom(V_Bent25)
    except:
       ERREUR=True
       print ("   =>ERROR WHILE GENERATING THE MESH!_")
       return
            


    if ListeV!=[]:
       _W=geompy.MakeWire(ListeV,1e-7)
       Pipe = geompy.MakePipe( FaceTube ,_W)
       Pipe.SetColor(SALOMEDS.Color(0.8,0.8,0.8))
       Pipe_id=geompy.addToStudy(Pipe,"Pipe")
       gg.createAndDisplayGO(Pipe_id)
       gg.setDisplayMode(Pipe_id,1)
       for x in Liste:
           geompy.addToStudyInFather(Pipe,x[0],x[1])
       Liste=[]
       ListeV=[]
    

    try:
      print("Add V26")
      V26= geompy.MakeVector(P32,P33)
      #Liste.append([P32,"P32"])
      geompy.addToStudy(V26,"V26" )
      Liste.append([V26,"V26"])
      ListeV.append(V26)
        

      _C1 = geompy.MakeCircle(P32, V26,35)
      _C2 = geompy.MakeCircle(P32, V26,31)
      FaceTube = geompy.MakeFaceWires([_C1, _C2], 1)
      Liste.append([_C1 ,"CercleExt"])
      Liste.append([_C2 ,"CercleInt"])
            

    except:
       ERREUR=True
       print ("   =>ERROR BUILDING THE GEOMETRY!")
       for x in Liste :
           geompy.addToStudy(x[0],x[1])
       return

    try:
       V26M = smesh.Mesh(V26)
       Decoupage = V26M.Segment()
       Decoupage.NumberOfSegments(8)
       Quadratic_Mesh = Decoupage.QuadraticMesh()

       smesh.SetName(V26M,'V26')
       V26M.Compute()
       V26M.Group(P32)
       V26M.Group(P33)
       V26M.GroupOnGeom(V26)
    except:
       ERREUR=True
       print ("   =>ERROR WHILE GENERATING THE MESH!_")
       return
        


    if ListeV!=[]:
       _W=geompy.MakeWire(ListeV,1e-7)
       Pipe = geompy.MakePipe( FaceTube ,_W)
       Pipe.SetColor(SALOMEDS.Color(0.8,0.8,0.8))
       Pipe_id=geompy.addToStudy(Pipe,"Pipe")
       gg.createAndDisplayGO(Pipe_id)
       gg.setDisplayMode(Pipe_id,1)
       for x in Liste:
           geompy.addToStudyInFather(Pipe,x[0],x[1])
       Liste=[]
       ListeV=[]
    

    try:
      print("Add  V_Bent27 ")
      Liste=[]
      V_Bent27 = geompy.MakeArcCenter(P33_34_center,P33,P34)
      geompy.addToStudy(V_Bent27,"V_Bent27")
      Liste.append([V_Bent27,"V_Bent27"])
      ListeV.append(V_Bent27)

         

      C1 = geompy.MakeCircle(P33,Vd2x_P33,35)
      C2 = geompy.MakeCircle(P33,Vd2x_P33,31)
      FaceTube = geompy.MakeFaceWires([C1, C2], 1)
      Liste.append([C1 ,"CercleExt"])
      Liste.append([C2 ,"CercleInt"])
            


    except:
       ERREUR=True
       print ("   =>ERROR BUILDING THE GEOMETRY!")
       for x in Liste :
           geompy.addToStudy(x[0],x[1])
       return

    try:
       V_Bent27M = smesh.Mesh(V_Bent27)
       Decoupage = V_Bent27M.Segment()
       Decoupage.NumberOfSegments(8)
       Quadratic_Mesh = Decoupage.QuadraticMesh()

       smesh.SetName(V_Bent27M,'V_Bent27')
       V_Bent27M.Compute()
       V_Bent27M.GroupOnFilter( SMESH.NODE,'P33', smesh.GetFilter( SMESH.NODE, SMESH.FT_LyingOnGeom,'=',P33))
       V_Bent27M.GroupOnFilter( SMESH.NODE,'P34', smesh.GetFilter( SMESH.NODE, SMESH.FT_LyingOnGeom,'=',P34))
       V_Bent27M.GroupOnGeom(V_Bent27)
    except:
       ERREUR=True
       print ("   =>ERROR WHILE GENERATING THE MESH!_")
       return
            


    if ListeV!=[]:
       _W=geompy.MakeWire(ListeV,1e-7)
       Pipe = geompy.MakePipe( FaceTube ,_W)
       Pipe.SetColor(SALOMEDS.Color(0.8,0.8,0.8))
       Pipe_id=geompy.addToStudy(Pipe,"Pipe")
       gg.createAndDisplayGO(Pipe_id)
       gg.setDisplayMode(Pipe_id,1)
       for x in Liste:
           geompy.addToStudyInFather(Pipe,x[0],x[1])
       Liste=[]
       ListeV=[]
    

    try:
      print("Add V28")
      V28= geompy.MakeVector(P35,P36)
      #Liste.append([P35,"P35"])
      geompy.addToStudy(V28,"V28" )
      Liste.append([V28,"V28"])
      ListeV.append(V28)
        

      _C1 = geompy.MakeCircle(P35, V28,35)
      _C2 = geompy.MakeCircle(P35, V28,31)
      FaceTube = geompy.MakeFaceWires([_C1, _C2], 1)
      Liste.append([_C1 ,"CercleExt"])
      Liste.append([_C2 ,"CercleInt"])
            

    except:
       ERREUR=True
       print ("   =>ERROR BUILDING THE GEOMETRY!")
       for x in Liste :
           geompy.addToStudy(x[0],x[1])
       return

    try:
       V28M = smesh.Mesh(V28)
       Decoupage = V28M.Segment()
       Decoupage.NumberOfSegments(8)
       Quadratic_Mesh = Decoupage.QuadraticMesh()

       smesh.SetName(V28M,'V28')
       V28M.Compute()
       V28M.Group(P35)
       V28M.Group(P36)
       V28M.GroupOnGeom(V28)
    except:
       ERREUR=True
       print ("   =>ERROR WHILE GENERATING THE MESH!_")
       return
        


    if ListeV!=[]:
       _W=geompy.MakeWire(ListeV,1e-7)
       Pipe = geompy.MakePipe( FaceTube ,_W)
       Pipe.SetColor(SALOMEDS.Color(0.8,0.8,0.8))
       Pipe_id=geompy.addToStudy(Pipe,"Pipe")
       gg.createAndDisplayGO(Pipe_id)
       gg.setDisplayMode(Pipe_id,1)
       for x in Liste:
           geompy.addToStudyInFather(Pipe,x[0],x[1])
       Liste=[]
       ListeV=[]
    

    try:
      print("Add  V_Bent29 ")
      Liste=[]
      V_Bent29 = geompy.MakeArcCenter(P36_37_center,P36,P37)
      geompy.addToStudy(V_Bent29,"V_Bent29")
      Liste.append([V_Bent29,"V_Bent29"])
      ListeV.append(V_Bent29)

         

      C1 = geompy.MakeCircle(P36,Vd2x_P36,35)
      C2 = geompy.MakeCircle(P36,Vd2x_P36,31)
      FaceTube = geompy.MakeFaceWires([C1, C2], 1)
      Liste.append([C1 ,"CercleExt"])
      Liste.append([C2 ,"CercleInt"])
            


    except:
       ERREUR=True
       print ("   =>ERROR BUILDING THE GEOMETRY!")
       for x in Liste :
           geompy.addToStudy(x[0],x[1])
       return

    try:
       V_Bent29M = smesh.Mesh(V_Bent29)
       Decoupage = V_Bent29M.Segment()
       Decoupage.NumberOfSegments(8)
       Quadratic_Mesh = Decoupage.QuadraticMesh()

       smesh.SetName(V_Bent29M,'V_Bent29')
       V_Bent29M.Compute()
       V_Bent29M.GroupOnFilter( SMESH.NODE,'P36', smesh.GetFilter( SMESH.NODE, SMESH.FT_LyingOnGeom,'=',P36))
       V_Bent29M.GroupOnFilter( SMESH.NODE,'P37', smesh.GetFilter( SMESH.NODE, SMESH.FT_LyingOnGeom,'=',P37))
       V_Bent29M.GroupOnGeom(V_Bent29)
    except:
       ERREUR=True
       print ("   =>ERROR WHILE GENERATING THE MESH!_")
       return
            


    if ListeV!=[]:
       _W=geompy.MakeWire(ListeV,1e-7)
       Pipe = geompy.MakePipe( FaceTube ,_W)
       Pipe.SetColor(SALOMEDS.Color(0.8,0.8,0.8))
       Pipe_id=geompy.addToStudy(Pipe,"Pipe")
       gg.createAndDisplayGO(Pipe_id)
       gg.setDisplayMode(Pipe_id,1)
       for x in Liste:
           geompy.addToStudyInFather(Pipe,x[0],x[1])
       Liste=[]
       ListeV=[]
    

    try:
      print("Add V30")
      V30= geompy.MakeVector(P37,P38)
      #Liste.append([P37,"P37"])
      geompy.addToStudy(V30,"V30" )
      Liste.append([V30,"V30"])
      ListeV.append(V30)
        

      _C1 = geompy.MakeCircle(P37, V30,35)
      _C2 = geompy.MakeCircle(P37, V30,31)
      FaceTube = geompy.MakeFaceWires([_C1, _C2], 1)
      Liste.append([_C1 ,"CercleExt"])
      Liste.append([_C2 ,"CercleInt"])
            

    except:
       ERREUR=True
       print ("   =>ERROR BUILDING THE GEOMETRY!")
       for x in Liste :
           geompy.addToStudy(x[0],x[1])
       return

    try:
       V30M = smesh.Mesh(V30)
       Decoupage = V30M.Segment()
       Decoupage.NumberOfSegments(8)
       Quadratic_Mesh = Decoupage.QuadraticMesh()

       smesh.SetName(V30M,'V30')
       V30M.Compute()
       V30M.Group(P37)
       V30M.Group(P38)
       V30M.GroupOnGeom(V30)
    except:
       ERREUR=True
       print ("   =>ERROR WHILE GENERATING THE MESH!_")
       return
        


    if ListeV!=[]:
       _W=geompy.MakeWire(ListeV,1e-7)
       Pipe = geompy.MakePipe( FaceTube ,_W)
       Pipe.SetColor(SALOMEDS.Color(0.8,0.8,0.8))
       Pipe_id=geompy.addToStudy(Pipe,"Pipe")
       gg.createAndDisplayGO(Pipe_id)
       gg.setDisplayMode(Pipe_id,1)
       for x in Liste:
           geompy.addToStudyInFather(Pipe,x[0],x[1])
       Liste=[]
       ListeV=[]
    

    try:
      print("Add  V_Bent31 ")
      Liste=[]
      V_Bent31 = geompy.MakeArcCenter(P38_39_center,P38,P39)
      geompy.addToStudy(V_Bent31,"V_Bent31")
      Liste.append([V_Bent31,"V_Bent31"])
      ListeV.append(V_Bent31)

         

      C1 = geompy.MakeCircle(P38,Vd2x_P38,35)
      C2 = geompy.MakeCircle(P38,Vd2x_P38,31)
      FaceTube = geompy.MakeFaceWires([C1, C2], 1)
      Liste.append([C1 ,"CercleExt"])
      Liste.append([C2 ,"CercleInt"])
            


    except:
       ERREUR=True
       print ("   =>ERROR BUILDING THE GEOMETRY!")
       for x in Liste :
           geompy.addToStudy(x[0],x[1])
       return

    try:
       V_Bent31M = smesh.Mesh(V_Bent31)
       Decoupage = V_Bent31M.Segment()
       Decoupage.NumberOfSegments(8)
       Quadratic_Mesh = Decoupage.QuadraticMesh()

       smesh.SetName(V_Bent31M,'V_Bent31')
       V_Bent31M.Compute()
       V_Bent31M.GroupOnFilter( SMESH.NODE,'P38', smesh.GetFilter( SMESH.NODE, SMESH.FT_LyingOnGeom,'=',P38))
       V_Bent31M.GroupOnFilter( SMESH.NODE,'P39', smesh.GetFilter( SMESH.NODE, SMESH.FT_LyingOnGeom,'=',P39))
       V_Bent31M.GroupOnGeom(V_Bent31)
    except:
       ERREUR=True
       print ("   =>ERROR WHILE GENERATING THE MESH!_")
       return
            


    if ListeV!=[]:
       _W=geompy.MakeWire(ListeV,1e-7)
       Pipe = geompy.MakePipe( FaceTube ,_W)
       Pipe.SetColor(SALOMEDS.Color(0.8,0.8,0.8))
       Pipe_id=geompy.addToStudy(Pipe,"Pipe")
       gg.createAndDisplayGO(Pipe_id)
       gg.setDisplayMode(Pipe_id,1)
       for x in Liste:
           geompy.addToStudyInFather(Pipe,x[0],x[1])
       Liste=[]
       ListeV=[]
    
        
    #Creates the mesh compound
    if not(ERREUR):
        Completed_Mesh = smesh.Concatenate([V0M.GetMesh() , V_Bent1M.GetMesh() , V2M.GetMesh() , 
           V_Bent3M.GetMesh() , V4M.GetMesh() , V_Bent5M.GetMesh() , V6M.GetMesh() , 
           V_Bent7M.GetMesh() , V8M.GetMesh() , V_Bent9M.GetMesh() , V10M.GetMesh() , 
           V_Bent11M.GetMesh() , V12M.GetMesh() , V_Bent13M.GetMesh() , V14M.GetMesh() , 
           V_Bent15M.GetMesh() , V16M.GetMesh() , V_Bent17M.GetMesh() , V18M.GetMesh() , 
           V_Bent19M.GetMesh() , V20M.GetMesh() , V_Bent21M.GetMesh() , V22M.GetMesh() , 
           V_Bent23M.GetMesh() , V24M.GetMesh() , V_Bent25M.GetMesh() , V26M.GetMesh() , 
           V_Bent27M.GetMesh() , V28M.GetMesh() , V_Bent29M.GetMesh() , V30M.GetMesh() , 
           V_Bent31M.GetMesh() ,], 1, 0, 1e-05)
        coincident_nodes = Completed_Mesh.FindCoincidentNodes( 1e-05 )
        Completed_Mesh.MergeNodes(coincident_nodes)
        equal_elements = Completed_Mesh.FindEqualElements(Completed_Mesh)    
        Completed_Mesh.MergeElements(equal_elements)   
        smesh.SetName(Completed_Mesh.GetMesh(), 'Completed_Mesh')
        

    if salome.sg.hasDesktop():
       salome.sg.updateObjBrowser(0)
    time2=time.time()
    dtime = time2 - time1
    print("------------------------")
    print("Duration of construction:"+str(round(dtime,2))+"s")

    
Project()