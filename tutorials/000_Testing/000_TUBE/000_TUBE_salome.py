#!/usr/bin/python 3
# -*- coding: iso-8859-1 -*-

import time
time1=time.time()
import sys
sys.path.append(' /media/sf_Shared_Folder_Linux/TUBA/tutorials/000_Testing/000_TUBE ')

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

from  salome.geom.structelem import StructuralElementManager
structElemManager = StructuralElementManager()
structElemList=[]

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

    Folder_Points = geompy.NewFolder('Folder_Points')
    Folder_Vectors = geompy.NewFolder('Folder_Vectors')
    
    # List of elements which are added to the study
    List_ParaVis_Visualization=[]

            


##_points##  
    a= geompy.MakeVertex(0, 0, 0 )
    geompy.addToStudy(a,"a ")
    geompy.PutToFolder(a, Folder_Points)

    Vd1x_a = geompy.MakeVectorDXDYDZ(0, 1, 0)
    a_vd1x=    geompy.MakeTranslationVectorDistance(a,Vd1x_a,1000)
    Vd1x_a= geompy.MakeVector(a,a_vd1x)
    geompy.addToStudyInFather(a,Vd1x_a,"Vd1x_a " )
       
    Vd2x_a = geompy.MakeVectorDXDYDZ(1.0, 0.0, 0.0)
    a_vd2x=    geompy.MakeTranslationVectorDistance(a,Vd2x_a,1000)
    Vd2x_a= geompy.MakeVector(a,a_vd2x)
    geompy.addToStudyInFather(a,Vd2x_a,"Vd2x_a " )

    # Visualize a support(restriction DOF) at point a
    #---------------------------------------------               
    a_BLOCK_xyzrxryrz=geompy.MakeBox(70.0,70.0,70.0,-70.0,-70.0,-70.0)	
    a_BLOCK_xyzrxryrz.SetColor(SALOMEDS.Color(1,1,0))
    a_BLOCK_xyzrxryrz_id=geompy.addToStudyInFather( a, a_BLOCK_xyzrxryrz,'a_BLOCK_xyzrxryrz' )
 #   B_id=geompy.addToStudy(a_BLOCK_xyzrxryrz,'a_BLOCK_xyzrxryrz' )
    
    List_ParaVis_Visualization.append(a_BLOCK_xyzrxryrz)
    objId = geompy.getObjectID(a_BLOCK_xyzrxryrz)    
    gg.createAndDisplayGO(objId)
    gg.setDisplayMode(objId,1)
    gg.setColor(objId,218,165,31)
  
    


##_points##  
    P1= geompy.MakeVertex(2000.0, 0, 0 )
    geompy.addToStudy(P1,"P1 ")
    geompy.PutToFolder(P1, Folder_Points)

    Vd1x_P1 = geompy.MakeVectorDXDYDZ(0, 1, 0)
    P1_vd1x=    geompy.MakeTranslationVectorDistance(P1,Vd1x_P1,1000)
    Vd1x_P1= geompy.MakeVector(P1,P1_vd1x)
    geompy.addToStudyInFather(P1,Vd1x_P1,"Vd1x_P1 " )
       
    Vd2x_P1 = geompy.MakeVectorDXDYDZ(1.0, 0.0, 0.0)
    P1_vd2x=    geompy.MakeTranslationVectorDistance(P1,Vd2x_P1,1000)
    Vd2x_P1= geompy.MakeVector(P1,P1_vd2x)
    geompy.addToStudyInFather(P1,Vd2x_P1,"Vd2x_P1 " )


##_points##  
    P1_2_center= geompy.MakeVertex(2000.0, 2.4492935982947064e-14, 400.0 )
    geompy.addToStudy(P1_2_center,"P1_2_center ")
    geompy.PutToFolder(P1_2_center, Folder_Points)

    Vd1x_P1_2_center = geompy.MakeVectorDXDYDZ(0, 1, 0)
    P1_2_center_vd1x=    geompy.MakeTranslationVectorDistance(P1_2_center,Vd1x_P1_2_center,1000)
    Vd1x_P1_2_center= geompy.MakeVector(P1_2_center,P1_2_center_vd1x)
    geompy.addToStudyInFather(P1_2_center,Vd1x_P1_2_center,"Vd1x_P1_2_center " )
       
    Vd2x_P1_2_center = geompy.MakeVectorDXDYDZ(1, 0, 0)
    P1_2_center_vd2x=    geompy.MakeTranslationVectorDistance(P1_2_center,Vd2x_P1_2_center,1000)
    Vd2x_P1_2_center= geompy.MakeVector(P1_2_center,P1_2_center_vd2x)
    geompy.addToStudyInFather(P1_2_center,Vd2x_P1_2_center,"Vd2x_P1_2_center " )


##_points##  
    P2= geompy.MakeVertex(2282.842712474619, 7.173814858237196e-15, 117.15728752538098 )
    geompy.addToStudy(P2,"P2 ")
    geompy.PutToFolder(P2, Folder_Points)

    Vd1x_P2 = geompy.MakeVectorDXDYDZ(1.0, 0.0, 0.0)
    P2_vd1x=    geompy.MakeTranslationVectorDistance(P2,Vd1x_P2,1000)
    Vd1x_P2= geompy.MakeVector(P2,P2_vd1x)
    geompy.addToStudyInFather(P2,Vd1x_P2,"Vd1x_P2 " )
       
    Vd2x_P2 = geompy.MakeVectorDXDYDZ(0.7071067811865476, 4.329780281177466e-17, 0.7071067811865475)
    P2_vd2x=    geompy.MakeTranslationVectorDistance(P2,Vd2x_P2,1000)
    Vd2x_P2= geompy.MakeVector(P2,P2_vd2x)
    geompy.addToStudyInFather(P2,Vd2x_P2,"Vd2x_P2 " )


##_points##  
    P3= geompy.MakeVertex(2636.396103067893, 2.882271626412453e-14, 470.7106781186547 )
    geompy.addToStudy(P3,"P3 ")
    geompy.PutToFolder(P3, Folder_Points)

    Vd1x_P3 = geompy.MakeVectorDXDYDZ(0, 1, 0)
    P3_vd1x=    geompy.MakeTranslationVectorDistance(P3,Vd1x_P3,1000)
    Vd1x_P3= geompy.MakeVector(P3,P3_vd1x)
    geompy.addToStudyInFather(P3,Vd1x_P3,"Vd1x_P3 " )
       
    Vd2x_P3 = geompy.MakeVectorDXDYDZ(0.7071067811865476, 4.329780281177466e-17, 0.7071067811865475)
    P3_vd2x=    geompy.MakeTranslationVectorDistance(P3,Vd2x_P3,1000)
    Vd2x_P3= geompy.MakeVector(P3,P3_vd2x)
    geompy.addToStudyInFather(P3,Vd2x_P3,"Vd2x_P3 " )


##_points##  
    P4= geompy.MakeVertex(0, 100, 0 )
    geompy.addToStudy(P4,"P4 ")
    geompy.PutToFolder(P4, Folder_Points)

    Vd1x_P4 = geompy.MakeVectorDXDYDZ(0.7071067811865476, 4.329780281177466e-17, 0.7071067811865475)
    P4_vd1x=    geompy.MakeTranslationVectorDistance(P4,Vd1x_P4,1000)
    Vd1x_P4= geompy.MakeVector(P4,P4_vd1x)
    geompy.addToStudyInFather(P4,Vd1x_P4,"Vd1x_P4 " )
       
    Vd2x_P4 = geompy.MakeVectorDXDYDZ(1.0, 0.0, 0.0)
    P4_vd2x=    geompy.MakeTranslationVectorDistance(P4,Vd2x_P4,1000)
    Vd2x_P4= geompy.MakeVector(P4,P4_vd2x)
    geompy.addToStudyInFather(P4,Vd2x_P4,"Vd2x_P4 " )

    # Visualize a support(restriction DOF) at point P4
    #---------------------------------------------               
    P4_BLOCK_xyzrxryrz=geompy.MakeBox(70.0,170.0,70.0,-70.0,30.0,-70.0)	
    P4_BLOCK_xyzrxryrz.SetColor(SALOMEDS.Color(1,1,0))
    P4_BLOCK_xyzrxryrz_id=geompy.addToStudyInFather( P4, P4_BLOCK_xyzrxryrz,'P4_BLOCK_xyzrxryrz' )
 #   B_id=geompy.addToStudy(P4_BLOCK_xyzrxryrz,'P4_BLOCK_xyzrxryrz' )
    
    List_ParaVis_Visualization.append(P4_BLOCK_xyzrxryrz)
    objId = geompy.getObjectID(P4_BLOCK_xyzrxryrz)    
    gg.createAndDisplayGO(objId)
    gg.setDisplayMode(objId,1)
    gg.setColor(objId,218,165,31)
  
    


##_points##  
    P5= geompy.MakeVertex(1834.314575050762, 100.0, 0.0 )
    geompy.addToStudy(P5,"P5 ")
    geompy.PutToFolder(P5, Folder_Points)

    Vd1x_P5 = geompy.MakeVectorDXDYDZ(0, 1, 0)
    P5_vd1x=    geompy.MakeTranslationVectorDistance(P5,Vd1x_P5,1000)
    Vd1x_P5= geompy.MakeVector(P5,P5_vd1x)
    geompy.addToStudyInFather(P5,Vd1x_P5,"Vd1x_P5 " )
       
    Vd2x_P5 = geompy.MakeVectorDXDYDZ(1.0, 0.0, 0.0)
    P5_vd2x=    geompy.MakeTranslationVectorDistance(P5,Vd2x_P5,1000)
    Vd2x_P5= geompy.MakeVector(P5,P5_vd2x)
    geompy.addToStudyInFather(P5,Vd2x_P5,"Vd2x_P5 " )


##_points##  
    P5_6_center= geompy.MakeVertex(1834.314575050762, 100.00000000000003, 400.0 )
    geompy.addToStudy(P5_6_center,"P5_6_center ")
    geompy.PutToFolder(P5_6_center, Folder_Points)

    Vd1x_P5_6_center = geompy.MakeVectorDXDYDZ(0, 1, 0)
    P5_6_center_vd1x=    geompy.MakeTranslationVectorDistance(P5_6_center,Vd1x_P5_6_center,1000)
    Vd1x_P5_6_center= geompy.MakeVector(P5_6_center,P5_6_center_vd1x)
    geompy.addToStudyInFather(P5_6_center,Vd1x_P5_6_center,"Vd1x_P5_6_center " )
       
    Vd2x_P5_6_center = geompy.MakeVectorDXDYDZ(1, 0, 0)
    P5_6_center_vd2x=    geompy.MakeTranslationVectorDistance(P5_6_center,Vd2x_P5_6_center,1000)
    Vd2x_P5_6_center= geompy.MakeVector(P5_6_center,P5_6_center_vd2x)
    geompy.addToStudyInFather(P5_6_center,Vd2x_P5_6_center,"Vd2x_P5_6_center " )


##_points##  
    P6= geompy.MakeVertex(2117.157287525381, 100.00000000000001, 117.15728752538098 )
    geompy.addToStudy(P6,"P6 ")
    geompy.PutToFolder(P6, Folder_Points)

    Vd1x_P6 = geompy.MakeVectorDXDYDZ(1.0, 0.0, 0.0)
    P6_vd1x=    geompy.MakeTranslationVectorDistance(P6,Vd1x_P6,1000)
    Vd1x_P6= geompy.MakeVector(P6,P6_vd1x)
    geompy.addToStudyInFather(P6,Vd1x_P6,"Vd1x_P6 " )
       
    Vd2x_P6 = geompy.MakeVectorDXDYDZ(0.7071067811865476, 4.329780281177466e-17, 0.7071067811865475)
    P6_vd2x=    geompy.MakeTranslationVectorDistance(P6,Vd2x_P6,1000)
    Vd2x_P6= geompy.MakeVector(P6,P6_vd2x)
    geompy.addToStudyInFather(P6,Vd2x_P6,"Vd2x_P6 " )


##_points##  
    P7= geompy.MakeVertex(2470.710678118655, 100.00000000000004, 470.7106781186547 )
    geompy.addToStudy(P7,"P7 ")
    geompy.PutToFolder(P7, Folder_Points)

    Vd1x_P7 = geompy.MakeVectorDXDYDZ(0, 1, 0)
    P7_vd1x=    geompy.MakeTranslationVectorDistance(P7,Vd1x_P7,1000)
    Vd1x_P7= geompy.MakeVector(P7,P7_vd1x)
    geompy.addToStudyInFather(P7,Vd1x_P7,"Vd1x_P7 " )
       
    Vd2x_P7 = geompy.MakeVectorDXDYDZ(0.7071067811865476, 4.329780281177466e-17, 0.7071067811865475)
    P7_vd2x=    geompy.MakeTranslationVectorDistance(P7,Vd2x_P7,1000)
    Vd2x_P7= geompy.MakeVector(P7,P7_vd2x)
    geompy.addToStudyInFather(P7,Vd2x_P7,"Vd2x_P7 " )


##_points##  
    c= geompy.MakeVertex(0, 1000, 0 )
    geompy.addToStudy(c,"c ")
    geompy.PutToFolder(c, Folder_Points)

    Vd1x_c = geompy.MakeVectorDXDYDZ(6.123233995736766e-17, 0.0, 1.0)
    c_vd1x=    geompy.MakeTranslationVectorDistance(c,Vd1x_c,1000)
    Vd1x_c= geompy.MakeVector(c,c_vd1x)
    geompy.addToStudyInFather(c,Vd1x_c,"Vd1x_c " )
       
    Vd2x_c = geompy.MakeVectorDXDYDZ(0.0, 0.0, 1.0)
    c_vd2x=    geompy.MakeTranslationVectorDistance(c,Vd2x_c,1000)
    Vd2x_c= geompy.MakeVector(c,c_vd2x)
    geompy.addToStudyInFather(c,Vd2x_c,"Vd2x_c " )

    # Visualize a support(restriction DOF) at point c
    #---------------------------------------------               
    c_BLOCK_xyzrxryrz=geompy.MakeBox(70.0,1070.0,70.0,-70.0,930.0,-70.0)	
    c_BLOCK_xyzrxryrz.SetColor(SALOMEDS.Color(1,1,0))
    c_BLOCK_xyzrxryrz_id=geompy.addToStudyInFather( c, c_BLOCK_xyzrxryrz,'c_BLOCK_xyzrxryrz' )
 #   B_id=geompy.addToStudy(c_BLOCK_xyzrxryrz,'c_BLOCK_xyzrxryrz' )
    
    List_ParaVis_Visualization.append(c_BLOCK_xyzrxryrz)
    objId = geompy.getObjectID(c_BLOCK_xyzrxryrz)    
    gg.createAndDisplayGO(objId)
    gg.setDisplayMode(objId,1)
    gg.setColor(objId,218,165,31)
  
    


##_points##  
    d= geompy.MakeVertex(1800.0, 1000.0, 0.0 )
    geompy.addToStudy(d,"d ")
    geompy.PutToFolder(d, Folder_Points)

    Vd1x_d = geompy.MakeVectorDXDYDZ(0, 1, 0)
    d_vd1x=    geompy.MakeTranslationVectorDistance(d,Vd1x_d,1000)
    Vd1x_d= geompy.MakeVector(d,d_vd1x)
    geompy.addToStudyInFather(d,Vd1x_d,"Vd1x_d " )
       
    Vd2x_d = geompy.MakeVectorDXDYDZ(1.0, 0.0, 0.0)
    d_vd2x=    geompy.MakeTranslationVectorDistance(d,Vd2x_d,1000)
    Vd2x_d= geompy.MakeVector(d,d_vd2x)
    geompy.addToStudyInFather(d,Vd2x_d,"Vd2x_d " )


##_points##  
    P9_10_center= geompy.MakeVertex(1800.0, 1000.0, 200.0 )
    geompy.addToStudy(P9_10_center,"P9_10_center ")
    geompy.PutToFolder(P9_10_center, Folder_Points)

    Vd1x_P9_10_center = geompy.MakeVectorDXDYDZ(0, 1, 0)
    P9_10_center_vd1x=    geompy.MakeTranslationVectorDistance(P9_10_center,Vd1x_P9_10_center,1000)
    Vd1x_P9_10_center= geompy.MakeVector(P9_10_center,P9_10_center_vd1x)
    geompy.addToStudyInFather(P9_10_center,Vd1x_P9_10_center,"Vd1x_P9_10_center " )
       
    Vd2x_P9_10_center = geompy.MakeVectorDXDYDZ(1, 0, 0)
    P9_10_center_vd2x=    geompy.MakeTranslationVectorDistance(P9_10_center,Vd2x_P9_10_center,1000)
    Vd2x_P9_10_center= geompy.MakeVector(P9_10_center,P9_10_center_vd2x)
    geompy.addToStudyInFather(P9_10_center,Vd2x_P9_10_center,"Vd2x_P9_10_center " )


##_points##  
    P10= geompy.MakeVertex(2000.0, 1000.0, 200.0 )
    geompy.addToStudy(P10,"P10 ")
    geompy.PutToFolder(P10, Folder_Points)

    Vd1x_P10 = geompy.MakeVectorDXDYDZ(1.0, 0.0, 0.0)
    P10_vd1x=    geompy.MakeTranslationVectorDistance(P10,Vd1x_P10,1000)
    Vd1x_P10= geompy.MakeVector(P10,P10_vd1x)
    geompy.addToStudyInFather(P10,Vd1x_P10,"Vd1x_P10 " )
       
    Vd2x_P10 = geompy.MakeVectorDXDYDZ(6.123233995736766e-17, 0.0, 1.0)
    P10_vd2x=    geompy.MakeTranslationVectorDistance(P10,Vd2x_P10,1000)
    Vd2x_P10= geompy.MakeVector(P10,P10_vd2x)
    geompy.addToStudyInFather(P10,Vd2x_P10,"Vd2x_P10 " )


##_points##  
    P11= geompy.MakeVertex(2000.0, 1000.0, 700.0 )
    geompy.addToStudy(P11,"P11 ")
    geompy.PutToFolder(P11, Folder_Points)

    Vd1x_P11 = geompy.MakeVectorDXDYDZ(0, 1, 0)
    P11_vd1x=    geompy.MakeTranslationVectorDistance(P11,Vd1x_P11,1000)
    Vd1x_P11= geompy.MakeVector(P11,P11_vd1x)
    geompy.addToStudyInFather(P11,Vd1x_P11,"Vd1x_P11 " )
       
    Vd2x_P11 = geompy.MakeVectorDXDYDZ(6.123233995736766e-17, 0.0, 1.0)
    P11_vd2x=    geompy.MakeTranslationVectorDistance(P11,Vd2x_P11,1000)
    Vd2x_P11= geompy.MakeVector(P11,P11_vd2x)
    geompy.addToStudyInFather(P11,Vd2x_P11,"Vd2x_P11 " )

    # Visualize a forces at point P11
    #---------------------------------------------           
    Radius=35.0
        
    Pna=geompy.MakeVertexWithRef(P11,Radius*0.0,Radius*0.707106781187,Radius*0.707106781187)
    Pnb=geompy.MakeVertexWithRef(P11,1.5*Radius*0.0,1.5*Radius*0.707106781187,1.5*Radius*0.707106781187)
    Pnc=geompy.MakeVertexWithRef(P11,10*Radius*0.0,10*Radius*0.707106781187,10*Radius*0.707106781187) 
 
    V_force=geompy.MakeVector(Pna,Pnb)     

    Tip = geompy.MakeCone(Pnc,V_force,2*Radius,0,4*Radius)           
    Shaft = geompy.MakeCylinder(P11, V_force,0.5*Radius, 10*Radius)
    Arrow = geompy.MakeCompound([Tip,Shaft])  
               
    Arrow.SetColor(SALOMEDS.Color(1,0,0))
    B_id=geompy.addToStudyInFather( P11, Arrow,'P11_Arrow' )    

    List_ParaVis_Visualization.append(Arrow)
    gg.createAndDisplayGO(B_id)
    gg.setDisplayMode(B_id,1)
            


##_points##  
    P12= geompy.MakeVertex(0, 1000, 100 )
    geompy.addToStudy(P12,"P12 ")
    geompy.PutToFolder(P12, Folder_Points)

    Vd1x_P12 = geompy.MakeVectorDXDYDZ(0, 1, 0)
    P12_vd1x=    geompy.MakeTranslationVectorDistance(P12,Vd1x_P12,1000)
    Vd1x_P12= geompy.MakeVector(P12,P12_vd1x)
    geompy.addToStudyInFather(P12,Vd1x_P12,"Vd1x_P12 " )
       
    Vd2x_P12 = geompy.MakeVectorDXDYDZ(0.0, 0.0, 1.0)
    P12_vd2x=    geompy.MakeTranslationVectorDistance(P12,Vd2x_P12,1000)
    Vd2x_P12= geompy.MakeVector(P12,P12_vd2x)
    geompy.addToStudyInFather(P12,Vd2x_P12,"Vd2x_P12 " )


##_points##  
    P13= geompy.MakeVertex(0, 1000, 200 )
    geompy.addToStudy(P13,"P13 ")
    geompy.PutToFolder(P13, Folder_Points)

    Vd1x_P13 = geompy.MakeVectorDXDYDZ(0, 1, 0)
    P13_vd1x=    geompy.MakeTranslationVectorDistance(P13,Vd1x_P13,1000)
    Vd1x_P13= geompy.MakeVector(P13,P13_vd1x)
    geompy.addToStudyInFather(P13,Vd1x_P13,"Vd1x_P13 " )
       
    Vd2x_P13 = geompy.MakeVectorDXDYDZ(0.0, 0.0, 1.0)
    P13_vd2x=    geompy.MakeTranslationVectorDistance(P13,Vd2x_P13,1000)
    Vd2x_P13= geompy.MakeVector(P13,P13_vd2x)
    geompy.addToStudyInFather(P13,Vd2x_P13,"Vd2x_P13 " )


##_points##  
    P14= geompy.MakeVertex(0, 1000, 300 )
    geompy.addToStudy(P14,"P14 ")
    geompy.PutToFolder(P14, Folder_Points)

    Vd1x_P14 = geompy.MakeVectorDXDYDZ(0, 1, 0)
    P14_vd1x=    geompy.MakeTranslationVectorDistance(P14,Vd1x_P14,1000)
    Vd1x_P14= geompy.MakeVector(P14,P14_vd1x)
    geompy.addToStudyInFather(P14,Vd1x_P14,"Vd1x_P14 " )
       
    Vd2x_P14 = geompy.MakeVectorDXDYDZ(0.0, 0.0, 1.0)
    P14_vd2x=    geompy.MakeTranslationVectorDistance(P14,Vd2x_P14,1000)
    Vd2x_P14= geompy.MakeVector(P14,P14_vd2x)
    geompy.addToStudyInFather(P14,Vd2x_P14,"Vd2x_P14 " )


##_points##  
    P15= geompy.MakeVertex(0, 1000, 400 )
    geompy.addToStudy(P15,"P15 ")
    geompy.PutToFolder(P15, Folder_Points)

    Vd1x_P15 = geompy.MakeVectorDXDYDZ(0, 1, 0)
    P15_vd1x=    geompy.MakeTranslationVectorDistance(P15,Vd1x_P15,1000)
    Vd1x_P15= geompy.MakeVector(P15,P15_vd1x)
    geompy.addToStudyInFather(P15,Vd1x_P15,"Vd1x_P15 " )
       
    Vd2x_P15 = geompy.MakeVectorDXDYDZ(0.0, 0.0, 1.0)
    P15_vd2x=    geompy.MakeTranslationVectorDistance(P15,Vd2x_P15,1000)
    Vd2x_P15= geompy.MakeVector(P15,P15_vd2x)
    geompy.addToStudyInFather(P15,Vd2x_P15,"Vd2x_P15 " )


##_points##  
    P16= geompy.MakeVertex(0, 1000, 500 )
    geompy.addToStudy(P16,"P16 ")
    geompy.PutToFolder(P16, Folder_Points)

    Vd1x_P16 = geompy.MakeVectorDXDYDZ(0, 1, 0)
    P16_vd1x=    geompy.MakeTranslationVectorDistance(P16,Vd1x_P16,1000)
    Vd1x_P16= geompy.MakeVector(P16,P16_vd1x)
    geompy.addToStudyInFather(P16,Vd1x_P16,"Vd1x_P16 " )
       
    Vd2x_P16 = geompy.MakeVectorDXDYDZ(0.0, 0.0, 1.0)
    P16_vd2x=    geompy.MakeTranslationVectorDistance(P16,Vd2x_P16,1000)
    Vd2x_P16= geompy.MakeVector(P16,P16_vd2x)
    geompy.addToStudyInFather(P16,Vd2x_P16,"Vd2x_P16 " )

##_vector_round_1D##
    ### geometry generation for  V0 ###
    #----------------------------------------------------
    print("Add V0")
    V0= geompy.MakeVector(a,P1)
    geompy.addToStudy(V0,"V0" )
    geompy.PutToFolder(V0, Folder_Vectors)

    ### mesh generation for  V0 ###
    #----------------------------------------------------    
    V0M = smesh.Mesh(V0)
    Regular_1D = V0M.Segment()
    Regular_1D.NumberOfSegments(10)

    smesh.SetName(V0M,'V0')
    V0M.Compute()
    V0M.Group(a)
    V0M.Group(P1)
    V0M.GroupOnGeom(V0)

    structElemList.append(('CircularBeam', {'R': 35.0, 'Group_Maille': 'V0', 'EP': 4.0}))    
    List_ParaVis_Visualization.append("Beam_V0")
        

##_bent_1D##
    ### geometry generation for  V1_Bent ###
    #----------------------------------------------------

    print("Add  V1_Bent ")
    V1_Bent = geompy.MakeArcCenter(P1_2_center,P1,P2)
    geompy.addToStudy(V1_Bent,"V1_Bent")

    ### mesh generation for  V1_Bent ###
    #----------------------------------------------------    

    V1_BentM = smesh.Mesh(V1_Bent)
    Regular_1D = V1_BentM.Segment()
    Regular_1D.NumberOfSegments(10)

    smesh.SetName(V1_BentM,'V1_Bent')
    V1_BentM.Compute()
    V1_BentM.Group(P1)
    V1_BentM.Group(P2)
    V1_BentM.GroupOnGeom(V1_Bent)


    structElemList.append(('CircularBeam', {'R': 35.0, 'Group_Maille': 'V1_Bent', 'EP': 4.0}))             
    List_ParaVis_Visualization.append("Beam_V1_Bent")

            

##_vector_round_1D##
    ### geometry generation for  V2 ###
    #----------------------------------------------------
    print("Add V2")
    V2= geompy.MakeVector(P2,P3)
    geompy.addToStudy(V2,"V2" )
    geompy.PutToFolder(V2, Folder_Vectors)

    ### mesh generation for  V2 ###
    #----------------------------------------------------    
    V2M = smesh.Mesh(V2)
    Regular_1D = V2M.Segment()
    Regular_1D.NumberOfSegments(10)

    smesh.SetName(V2M,'V2')
    V2M.Compute()
    V2M.Group(P2)
    V2M.Group(P3)
    V2M.GroupOnGeom(V2)

    structElemList.append(('CircularBeam', {'R': 35.0, 'Group_Maille': 'V2', 'EP': 4.0}))    
    List_ParaVis_Visualization.append("Beam_V2")
        

##_vector_round_1D##
    ### geometry generation for  V3 ###
    #----------------------------------------------------
    print("Add V3")
    V3= geompy.MakeVector(P4,P5)
    geompy.addToStudy(V3,"V3" )
    geompy.PutToFolder(V3, Folder_Vectors)

    ### mesh generation for  V3 ###
    #----------------------------------------------------    
    V3M = smesh.Mesh(V3)
    Regular_1D = V3M.Segment()
    Regular_1D.NumberOfSegments(10)

    smesh.SetName(V3M,'V3')
    V3M.Compute()
    V3M.Group(P4)
    V3M.Group(P5)
    V3M.GroupOnGeom(V3)

    structElemList.append(('CircularBeam', {'R': 35.0, 'Group_Maille': 'V3', 'EP': 4.0}))    
    List_ParaVis_Visualization.append("Beam_V3")
        

##_bent_1D##
    ### geometry generation for  V4_Bent ###
    #----------------------------------------------------

    print("Add  V4_Bent ")
    V4_Bent = geompy.MakeArcCenter(P5_6_center,P5,P6)
    geompy.addToStudy(V4_Bent,"V4_Bent")

    ### mesh generation for  V4_Bent ###
    #----------------------------------------------------    

    V4_BentM = smesh.Mesh(V4_Bent)
    Regular_1D = V4_BentM.Segment()
    Regular_1D.NumberOfSegments(10)

    smesh.SetName(V4_BentM,'V4_Bent')
    V4_BentM.Compute()
    V4_BentM.Group(P5)
    V4_BentM.Group(P6)
    V4_BentM.GroupOnGeom(V4_Bent)


    structElemList.append(('CircularBeam', {'R': 35.0, 'Group_Maille': 'V4_Bent', 'EP': 4.0}))             
    List_ParaVis_Visualization.append("Beam_V4_Bent")

            

##_vector_round_1D##
    ### geometry generation for  V5 ###
    #----------------------------------------------------
    print("Add V5")
    V5= geompy.MakeVector(P6,P7)
    geompy.addToStudy(V5,"V5" )
    geompy.PutToFolder(V5, Folder_Vectors)

    ### mesh generation for  V5 ###
    #----------------------------------------------------    
    V5M = smesh.Mesh(V5)
    Regular_1D = V5M.Segment()
    Regular_1D.NumberOfSegments(10)

    smesh.SetName(V5M,'V5')
    V5M.Compute()
    V5M.Group(P6)
    V5M.Group(P7)
    V5M.GroupOnGeom(V5)

    structElemList.append(('CircularBeam', {'R': 35.0, 'Group_Maille': 'V5', 'EP': 4.0}))    
    List_ParaVis_Visualization.append("Beam_V5")
        

##_vector_round_1D##
    ### geometry generation for  V6 ###
    #----------------------------------------------------
    print("Add V6")
    V6= geompy.MakeVector(c,d)
    geompy.addToStudy(V6,"V6" )
    geompy.PutToFolder(V6, Folder_Vectors)

    ### mesh generation for  V6 ###
    #----------------------------------------------------    
    V6M = smesh.Mesh(V6)
    Regular_1D = V6M.Segment()
    Regular_1D.NumberOfSegments(10)

    smesh.SetName(V6M,'V6')
    V6M.Compute()
    V6M.Group(c)
    V6M.Group(d)
    V6M.GroupOnGeom(V6)

    structElemList.append(('CircularBeam', {'R': 35.0, 'Group_Maille': 'V6', 'EP': 4.0}))    
    List_ParaVis_Visualization.append("Beam_V6")
        

##_bent_1D##
    ### geometry generation for  V7_Bent ###
    #----------------------------------------------------

    print("Add  V7_Bent ")
    V7_Bent = geompy.MakeArcCenter(P9_10_center,d,P10)
    geompy.addToStudy(V7_Bent,"V7_Bent")

    ### mesh generation for  V7_Bent ###
    #----------------------------------------------------    

    V7_BentM = smesh.Mesh(V7_Bent)
    Regular_1D = V7_BentM.Segment()
    Regular_1D.NumberOfSegments(10)

    smesh.SetName(V7_BentM,'V7_Bent')
    V7_BentM.Compute()
    V7_BentM.Group(d)
    V7_BentM.Group(P10)
    V7_BentM.GroupOnGeom(V7_Bent)


    structElemList.append(('CircularBeam', {'R': 35.0, 'Group_Maille': 'V7_Bent', 'EP': 4.0}))             
    List_ParaVis_Visualization.append("Beam_V7_Bent")

            

##_vector_round_1D##
    ### geometry generation for  V8 ###
    #----------------------------------------------------
    print("Add V8")
    V8= geompy.MakeVector(P10,P11)
    geompy.addToStudy(V8,"V8" )
    geompy.PutToFolder(V8, Folder_Vectors)

    ### mesh generation for  V8 ###
    #----------------------------------------------------    
    V8M = smesh.Mesh(V8)
    Regular_1D = V8M.Segment()
    Regular_1D.NumberOfSegments(10)

    smesh.SetName(V8M,'V8')
    V8M.Compute()
    V8M.Group(P10)
    V8M.Group(P11)
    V8M.GroupOnGeom(V8)

    structElemList.append(('CircularBeam', {'R': 35.0, 'Group_Maille': 'V8', 'EP': 4.0}))    
    List_ParaVis_Visualization.append("Beam_V8")
        

##_vector_round_1D##
    ### geometry generation for  V9 ###
    #----------------------------------------------------
    print("Add V9")
    V9= geompy.MakeVector(c,P12)
    geompy.addToStudy(V9,"V9" )
    geompy.PutToFolder(V9, Folder_Vectors)

    ### mesh generation for  V9 ###
    #----------------------------------------------------    
    V9M = smesh.Mesh(V9)
    Regular_1D = V9M.Segment()
    Regular_1D.NumberOfSegments(10)

    smesh.SetName(V9M,'V9')
    V9M.Compute()
    V9M.Group(c)
    V9M.Group(P12)
    V9M.GroupOnGeom(V9)

    structElemList.append(('CircularBeam', {'R': 35.0, 'Group_Maille': 'V9', 'EP': 4.0}))    
    List_ParaVis_Visualization.append("Beam_V9")
        

##_vector_round_1D##
    ### geometry generation for  V10 ###
    #----------------------------------------------------
    print("Add V10")
    V10= geompy.MakeVector(P12,P13)
    geompy.addToStudy(V10,"V10" )
    geompy.PutToFolder(V10, Folder_Vectors)

    ### mesh generation for  V10 ###
    #----------------------------------------------------    
    V10M = smesh.Mesh(V10)
    Regular_1D = V10M.Segment()
    Regular_1D.NumberOfSegments(10)

    smesh.SetName(V10M,'V10')
    V10M.Compute()
    V10M.Group(P12)
    V10M.Group(P13)
    V10M.GroupOnGeom(V10)

    structElemList.append(('CircularBeam', {'R': 35.0, 'Group_Maille': 'V10', 'EP': 4.0}))    
    List_ParaVis_Visualization.append("Beam_V10")
        

##_vector_round_1D##
    ### geometry generation for  V11 ###
    #----------------------------------------------------
    print("Add V11")
    V11= geompy.MakeVector(P13,P14)
    geompy.addToStudy(V11,"V11" )
    geompy.PutToFolder(V11, Folder_Vectors)

    ### mesh generation for  V11 ###
    #----------------------------------------------------    
    V11M = smesh.Mesh(V11)
    Regular_1D = V11M.Segment()
    Regular_1D.NumberOfSegments(10)

    smesh.SetName(V11M,'V11')
    V11M.Compute()
    V11M.Group(P13)
    V11M.Group(P14)
    V11M.GroupOnGeom(V11)

    structElemList.append(('CircularBeam', {'R': 35.0, 'Group_Maille': 'V11', 'EP': 4.0}))    
    List_ParaVis_Visualization.append("Beam_V11")
        

##_vector_round_1D##
    ### geometry generation for  V12 ###
    #----------------------------------------------------
    print("Add V12")
    V12= geompy.MakeVector(P14,P15)
    geompy.addToStudy(V12,"V12" )
    geompy.PutToFolder(V12, Folder_Vectors)

    ### mesh generation for  V12 ###
    #----------------------------------------------------    
    V12M = smesh.Mesh(V12)
    Regular_1D = V12M.Segment()
    Regular_1D.NumberOfSegments(10)

    smesh.SetName(V12M,'V12')
    V12M.Compute()
    V12M.Group(P14)
    V12M.Group(P15)
    V12M.GroupOnGeom(V12)

    structElemList.append(('CircularBeam', {'R': 35.0, 'Group_Maille': 'V12', 'EP': 4.0}))    
    List_ParaVis_Visualization.append("Beam_V12")
        

##_vector_round_1D##
    ### geometry generation for  V13 ###
    #----------------------------------------------------
    print("Add V13")
    V13= geompy.MakeVector(P15,P16)
    geompy.addToStudy(V13,"V13" )
    geompy.PutToFolder(V13, Folder_Vectors)

    ### mesh generation for  V13 ###
    #----------------------------------------------------    
    V13M = smesh.Mesh(V13)
    Regular_1D = V13M.Segment()
    Regular_1D.NumberOfSegments(10)

    smesh.SetName(V13M,'V13')
    V13M.Compute()
    V13M.Group(P15)
    V13M.Group(P16)
    V13M.GroupOnGeom(V13)

    structElemList.append(('CircularBeam', {'R': 35.0, 'Group_Maille': 'V13', 'EP': 4.0}))    
    List_ParaVis_Visualization.append("Beam_V13")
        

    #Creates a visualization for 1D structural elements (Beams, Pipe etc)                           
    elem = structElemManager.createElement(structElemList)
    elem.display() 

    for i,item in enumerate(List_ParaVis_Visualization):    
        if isinstance(item, str):
            List_ParaVis_Visualization[i]=salome.myStudy.FindObject(item).GetObject()                         

    try:  
        compound_paravis=geompy.MakeCompound(List_ParaVis_Visualization)
    except:
        print("No compound could be created",str(List_ParaVis_Visualization))
        
        
    #Creates the final mesh compound
    #----------------------------------------------------

    Completed_Mesh = smesh.Concatenate([V0M.GetMesh() , V1_BentM.GetMesh() , V2M.GetMesh() , 
           V3M.GetMesh() , V4_BentM.GetMesh() , V5M.GetMesh() , V6M.GetMesh() , 
           V7_BentM.GetMesh() , V8M.GetMesh() , V9M.GetMesh() , V10M.GetMesh() , V11M.GetMesh() , 
           V12M.GetMesh() , V13M.GetMesh() ,], 1, 0, 1e-05)
    coincident_nodes = Completed_Mesh.FindCoincidentNodes( 1e-05 )
    Completed_Mesh.MergeNodes(coincident_nodes)
    equal_elements = Completed_Mesh.FindEqualElements(Completed_Mesh)    
    Completed_Mesh.MergeElements(equal_elements)   
    smesh.SetName(Completed_Mesh.GetMesh(), 'Completed_Mesh')
        

                               
##_finalize##                
    #exports the created mesh compound 
    try:
        Completed_Mesh.ExportMED( r'/media/sf_Shared_Folder_Linux/TUBA/tutorials/000_Testing/000_TUBE/Completed_Mesh.mmed', 0)
    except:
        print ('ExportPartToMED() failed')


    #exports visualizations (structural elements, forces, etc) as a grouped geometry to be used in Paravis
    try:    
        geompy.ExportVTK(compound_paravis, '/media/sf_Shared_Folder_Linux/TUBA/tutorials/000_Testing/000_TUBE/compound_paravis.vtk', 0.001)     
    except:
        print ('ExportVTK of the visualization compound failed')

    if salome.sg.hasDesktop():
       salome.sg.updateObjBrowser(0)
    time2=time.time()
    dtime = time2 - time1
    print("------------------------")
    print("Duration of construction:"+str(round(dtime,2))+"s")

#    import SalomePyQt
#    sg = SalomePyQt.SalomePyQt()
#    sg.activateModule("Geometry")
#    if salome.sg.hasDesktop():
#      salome.sg.updateObjBrowser(1)
#    sg.activateModule("AsterStudy")

    
Project()