#!/usr/bin/python 3
# -*- coding: iso-8859-1 -*-

import time
time1=time.time()
import sys
sys.path.append('/home/max/salome_meca/TUBA_2019/external/')

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


from salome.geom import geomBuilder
geompy = geomBuilder.New()

smesh = smeshBuilder.New()

from salome.geom import geomtools
geompy = geomtools.getGeompy()

from salome.kernel.studyedit import getStudyEditor
studyEditor = getStudyEditor()

#from  salome.geom.structelem import StructuralElementManager
from Section.structelem import StructuralElementManager

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
    P0= geompy.MakeVertex(0, 0, 0 )
    geompy.addToStudy(P0,"P0 ")
    geompy.PutToFolder(P0, Folder_Points)

    local_y_P0 = geompy.MakeVectorDXDYDZ(0, 1, 0)
    P0_local_y=    geompy.MakeTranslationVectorDistance(P0,local_y_P0,1000)
    local_y_P0= geompy.MakeVector(P0,P0_local_y)
    geompy.addToStudyInFather(P0,local_y_P0,"local_y_P0 " )
       
    local_x_P0 = geompy.MakeVectorDXDYDZ(1.0, 0.0, 0.0)
    P0_local_x=    geompy.MakeTranslationVectorDistance(P0,local_x_P0,1000)
    local_x_P0= geompy.MakeVector(P0,P0_local_x)
    geompy.addToStudyInFather(P0,local_x_P0,"local_x_P0 " )
    
    P0M = smesh.Mesh(P0)
    P0M.Compute()
    P0M.Group(P0)
    P0M.GroupOnGeom(P0)


    

    # Visualize a support(restriction DOF) at point P0
    #---------------------------------------------
    P0_BLOCK_xyzrxryrz=geompy.MakeBox(70.0,70.0,70.0,-70.0,-70.0,-70.0)	
    P0_BLOCK_xyzrxryrz.SetColor(SALOMEDS.Color(1,1,0))
    P0_BLOCK_xyzrxryrz_id=geompy.addToStudyInFather( P0, P0_BLOCK_xyzrxryrz,'P0_BLOCK_xyzrxryrz' )
 #   B_id=geompy.addToStudy(P0_BLOCK_xyzrxryrz,'P0_BLOCK_xyzrxryrz' )

    List_ParaVis_Visualization.append(P0_BLOCK_xyzrxryrz)
    objId = geompy.getObjectID(P0_BLOCK_xyzrxryrz)    
    gg.createAndDisplayGO(objId)
    gg.setDisplayMode(objId,1)
    gg.setColor(objId,218,165,31)

    


##_points##  
    P1= geompy.MakeVertex(1000, 0, 0 )
    geompy.addToStudy(P1,"P1 ")
    geompy.PutToFolder(P1, Folder_Points)

    local_y_P1 = geompy.MakeVectorDXDYDZ(0, 1, 0)
    P1_local_y=    geompy.MakeTranslationVectorDistance(P1,local_y_P1,1000)
    local_y_P1= geompy.MakeVector(P1,P1_local_y)
    geompy.addToStudyInFather(P1,local_y_P1,"local_y_P1 " )
       
    local_x_P1 = geompy.MakeVectorDXDYDZ(1.0, 0.0, 0.0)
    P1_local_x=    geompy.MakeTranslationVectorDistance(P1,local_x_P1,1000)
    local_x_P1= geompy.MakeVector(P1,P1_local_x)
    geompy.addToStudyInFather(P1,local_x_P1,"local_x_P1 " )
    
    P1M = smesh.Mesh(P1)
    P1M.Compute()
    P1M.Group(P1)
    P1M.GroupOnGeom(P1)


    


##_points##  
    P2= geompy.MakeVertex(2000, 0, 0 )
    geompy.addToStudy(P2,"P2 ")
    geompy.PutToFolder(P2, Folder_Points)

    local_y_P2 = geompy.MakeVectorDXDYDZ(0, 1, 0)
    P2_local_y=    geompy.MakeTranslationVectorDistance(P2,local_y_P2,1000)
    local_y_P2= geompy.MakeVector(P2,P2_local_y)
    geompy.addToStudyInFather(P2,local_y_P2,"local_y_P2 " )
       
    local_x_P2 = geompy.MakeVectorDXDYDZ(1.0, 0.0, 0.0)
    P2_local_x=    geompy.MakeTranslationVectorDistance(P2,local_x_P2,1000)
    local_x_P2= geompy.MakeVector(P2,P2_local_x)
    geompy.addToStudyInFather(P2,local_x_P2,"local_x_P2 " )
    
    P2M = smesh.Mesh(P2)
    P2M.Compute()
    P2M.Group(P2)
    P2M.GroupOnGeom(P2)


    


    Radius=35.0

    Pna=geompy.MakeVertexWithRef(P2,0,0,105.0)
    Pnb=geompy.MakeVertexWithRef(P2,0,0,70.0)  
    Vp=geompy.MakeVector(Pna,Pnb)
    Cone1 = geompy.MakeCone(Pna,Vp,Radius,0,2*Radius)

    P2a=geompy.MakeVertexWithRef(P2,0,0,-105.0)    
    P2b=geompy.MakeVertexWithRef(P2,0,0,-70.0)    
    Vm=geompy.MakeVector(P2a,P2b)
    Cone2 = geompy.MakeCone(P2a,Vm,Radius,0,2*Radius)

    BLOCK_z=geompy.MakeCompound([Cone1,Cone2])
    BLOCK_z.SetColor(SALOMEDS.Color(1,1,0))
    B_id=geompy.addToStudyInFather( P2, BLOCK_z,'P2_BLOCK_z' )    

    List_ParaVis_Visualization.append(BLOCK_z)
    gg.createAndDisplayGO(B_id)
    gg.setDisplayMode(B_id,1)
    


##_points##  
    P3= geompy.MakeVertex(2850.0, 0.0, 0.0 )
    geompy.addToStudy(P3,"P3 ")
    geompy.PutToFolder(P3, Folder_Points)

    local_y_P3 = geompy.MakeVectorDXDYDZ(0, 1, 0)
    P3_local_y=    geompy.MakeTranslationVectorDistance(P3,local_y_P3,1000)
    local_y_P3= geompy.MakeVector(P3,P3_local_y)
    geompy.addToStudyInFather(P3,local_y_P3,"local_y_P3 " )
       
    local_x_P3 = geompy.MakeVectorDXDYDZ(1.0, 0.0, 0.0)
    P3_local_x=    geompy.MakeTranslationVectorDistance(P3,local_x_P3,1000)
    local_x_P3= geompy.MakeVector(P3,P3_local_x)
    geompy.addToStudyInFather(P3,local_x_P3,"local_x_P3 " )
    
    P3M = smesh.Mesh(P3)
    P3M.Compute()
    P3M.Group(P3)
    P3M.GroupOnGeom(P3)


    


##_points##  
    P3_4_center= geompy.MakeVertex(2850.0, 9.184850993605149e-15, 150.0 )
    geompy.addToStudy(P3_4_center,"P3_4_center ")
    geompy.PutToFolder(P3_4_center, Folder_Points)

    local_y_P3_4_center = geompy.MakeVectorDXDYDZ(0, 1, 0)
    P3_4_center_local_y=    geompy.MakeTranslationVectorDistance(P3_4_center,local_y_P3_4_center,1000)
    local_y_P3_4_center= geompy.MakeVector(P3_4_center,P3_4_center_local_y)
    geompy.addToStudyInFather(P3_4_center,local_y_P3_4_center,"local_y_P3_4_center " )
       
    local_x_P3_4_center = geompy.MakeVectorDXDYDZ(1, 0, 0)
    P3_4_center_local_x=    geompy.MakeTranslationVectorDistance(P3_4_center,local_x_P3_4_center,1000)
    local_x_P3_4_center= geompy.MakeVector(P3_4_center,P3_4_center_local_x)
    geompy.addToStudyInFather(P3_4_center,local_x_P3_4_center,"local_x_P3_4_center " )
    
    P3_4_centerM = smesh.Mesh(P3_4_center)
    P3_4_centerM.Compute()
    P3_4_centerM.Group(P3_4_center)
    P3_4_centerM.GroupOnGeom(P3_4_center)


    


##_points##  
    P4= geompy.MakeVertex(3000.0, 9.184850993605149e-15, 150.0 )
    geompy.addToStudy(P4,"P4 ")
    geompy.PutToFolder(P4, Folder_Points)

    local_y_P4 = geompy.MakeVectorDXDYDZ(1.0, 0.0, 0.0)
    P4_local_y=    geompy.MakeTranslationVectorDistance(P4,local_y_P4,1000)
    local_y_P4= geompy.MakeVector(P4,P4_local_y)
    geompy.addToStudyInFather(P4,local_y_P4,"local_y_P4 " )
       
    local_x_P4 = geompy.MakeVectorDXDYDZ(6.123233995736766e-17, 6.123233995736766e-17, 1.0)
    P4_local_x=    geompy.MakeTranslationVectorDistance(P4,local_x_P4,1000)
    local_x_P4= geompy.MakeVector(P4,P4_local_x)
    geompy.addToStudyInFather(P4,local_x_P4,"local_x_P4 " )
    
    P4M = smesh.Mesh(P4)
    P4M.Compute()
    P4M.Group(P4)
    P4M.GroupOnGeom(P4)


    


##_points##  
    P5= geompy.MakeVertex(3000.0, 7.041719095097281e-14, 1150.0 )
    geompy.addToStudy(P5,"P5 ")
    geompy.PutToFolder(P5, Folder_Points)

    local_y_P5 = geompy.MakeVectorDXDYDZ(0, 1, 0)
    P5_local_y=    geompy.MakeTranslationVectorDistance(P5,local_y_P5,1000)
    local_y_P5= geompy.MakeVector(P5,P5_local_y)
    geompy.addToStudyInFather(P5,local_y_P5,"local_y_P5 " )
       
    local_x_P5 = geompy.MakeVectorDXDYDZ(6.123233995736766e-17, 6.123233995736766e-17, 1.0)
    P5_local_x=    geompy.MakeTranslationVectorDistance(P5,local_x_P5,1000)
    local_x_P5= geompy.MakeVector(P5,P5_local_x)
    geompy.addToStudyInFather(P5,local_x_P5,"local_x_P5 " )
    
    P5M = smesh.Mesh(P5)
    P5M.Compute()
    P5M.Group(P5)
    P5M.GroupOnGeom(P5)


    


##_points##  
    a= geompy.MakeVertex(2900.0, 8.266365894244635e-14, 1250.0 )
    geompy.addToStudy(a,"a ")
    geompy.PutToFolder(a, Folder_Points)

    local_y_a = geompy.MakeVectorDXDYDZ(6.123233995736766e-17, 6.123233995736766e-17, 1.0)
    a_local_y=    geompy.MakeTranslationVectorDistance(a,local_y_a,1000)
    local_y_a= geompy.MakeVector(a,a_local_y)
    geompy.addToStudyInFather(a,local_y_a,"local_y_a " )
       
    local_x_a = geompy.MakeVectorDXDYDZ(-1.0, 6.123233995736766e-17, 1.224646799147353e-16)
    a_local_x=    geompy.MakeTranslationVectorDistance(a,local_x_a,1000)
    local_x_a= geompy.MakeVector(a,a_local_x)
    geompy.addToStudyInFather(a,local_x_a,"local_x_a " )
    
    aM = smesh.Mesh(a)
    aM.Compute()
    aM.Group(a)
    aM.GroupOnGeom(a)


    


##_points##  
    b= geompy.MakeVertex(3000.0, 8.266365894244634e-14, 1350.0 )
    geompy.addToStudy(b,"b ")
    geompy.PutToFolder(b, Folder_Points)

    local_y_b = geompy.MakeVectorDXDYDZ(0, 1, 0)
    b_local_y=    geompy.MakeTranslationVectorDistance(b,local_y_b,1000)
    local_y_b= geompy.MakeVector(b,b_local_y)
    geompy.addToStudyInFather(b,local_y_b,"local_y_b " )
       
    local_x_b = geompy.MakeVectorDXDYDZ(6.123233995736766e-17, 6.123233995736766e-17, 1.0)
    b_local_x=    geompy.MakeTranslationVectorDistance(b,local_x_b,1000)
    local_x_b= geompy.MakeVector(b,b_local_x)
    geompy.addToStudyInFather(b,local_x_b,"local_x_b " )
    
    bM = smesh.Mesh(b)
    bM.Compute()
    bM.Group(b)
    bM.GroupOnGeom(b)


    


##_points##  
    P8= geompy.MakeVertex(3000.0, 1.43895998899814e-13, 2350.0 )
    geompy.addToStudy(P8,"P8 ")
    geompy.PutToFolder(P8, Folder_Points)

    local_y_P8 = geompy.MakeVectorDXDYDZ(0, 1, 0)
    P8_local_y=    geompy.MakeTranslationVectorDistance(P8,local_y_P8,1000)
    local_y_P8= geompy.MakeVector(P8,P8_local_y)
    geompy.addToStudyInFather(P8,local_y_P8,"local_y_P8 " )
       
    local_x_P8 = geompy.MakeVectorDXDYDZ(6.123233995736766e-17, 6.123233995736766e-17, 1.0)
    P8_local_x=    geompy.MakeTranslationVectorDistance(P8,local_x_P8,1000)
    local_x_P8= geompy.MakeVector(P8,P8_local_x)
    geompy.addToStudyInFather(P8,local_x_P8,"local_x_P8 " )
    
    P8M = smesh.Mesh(P8)
    P8M.Compute()
    P8M.Group(P8)
    P8M.GroupOnGeom(P8)


    


##_points##  
    P9= geompy.MakeVertex(1900.0, 1.4389599889981403e-13, 1250.0000000000002 )
    geompy.addToStudy(P9,"P9 ")
    geompy.PutToFolder(P9, Folder_Points)

    local_y_P9 = geompy.MakeVectorDXDYDZ(0, 1, 0)
    P9_local_y=    geompy.MakeTranslationVectorDistance(P9,local_y_P9,1000)
    local_y_P9= geompy.MakeVector(P9,P9_local_y)
    geompy.addToStudyInFather(P9,local_y_P9,"local_y_P9 " )
       
    local_x_P9 = geompy.MakeVectorDXDYDZ(-1.0, 6.123233995736766e-17, 1.224646799147353e-16)
    P9_local_x=    geompy.MakeTranslationVectorDistance(P9,local_x_P9,1000)
    local_x_P9= geompy.MakeVector(P9,P9_local_x)
    geompy.addToStudyInFather(P9,local_x_P9,"local_x_P9 " )
    
    P9M = smesh.Mesh(P9)
    P9M.Compute()
    P9M.Group(P9)
    P9M.GroupOnGeom(P9)


    

    # Visualize springs/stiffness at point P9
    #---------------------------------------------
    Radius=20.0

    Pna=geompy.MakeVertexWithRef(P9,60.0,0,0)
    Pnb=geompy.MakeVertexWithRef(P9,40.0,0,0)  
    Vp=geompy.MakeVector(Pna,Pnb)  

    Torus_1 = geompy.MakeTorus(Pna, Vp, Radius, Radius/2) 
    Torus_2 = geompy.MakeTorus(Pnb, Vp, Radius, Radius/2)  

    P2a=geompy.MakeVertexWithRef(P9,-60.0,0,0)    
    P2b=geompy.MakeVertexWithRef(P9,-40.0,0,0)    
    Vm=geompy.MakeVector(P2a,P2b)  

    Torus_3 = geompy.MakeTorus(P2a, Vm, Radius, Radius/2)
    Torus_4 = geompy.MakeTorus(P2b, Vm, Radius, Radius/2)

    STIFFNESS_x=geompy.MakeCompound([Torus_1,Torus_2,Torus_3,Torus_4])
    STIFFNESS_x.SetColor(SALOMEDS.Color(0,0,1))
    S_id=geompy.addToStudyInFather( P9, STIFFNESS_x,'P9_STIFFNESS_x' )    

    List_ParaVis_Visualization.append(STIFFNESS_x)
    gg.createAndDisplayGO(S_id)
    gg.setDisplayMode(S_id,1)

    

    # Visualize springs/stiffness at point P9
    #---------------------------------------------
    Radius=20.0

    Pna=geompy.MakeVertexWithRef(P9,0,60.0,0)
    Pnb=geompy.MakeVertexWithRef(P9,0,40.0,0)  
    Vp=geompy.MakeVector(Pna,Pnb)  

    Torus_1 = geompy.MakeTorus(Pna, Vp, Radius, Radius/2) 
    Torus_2 = geompy.MakeTorus(Pnb, Vp, Radius, Radius/2)  

    P2a=geompy.MakeVertexWithRef(P9,0,-60.0,0)    
    P2b=geompy.MakeVertexWithRef(P9,0,-40.0,0)    
    Vm=geompy.MakeVector(P2a,P2b)  

    Torus_3 = geompy.MakeTorus(P2a, Vm, Radius, Radius/2)
    Torus_4 = geompy.MakeTorus(P2b, Vm, Radius, Radius/2)

    STIFFNESS_y=geompy.MakeCompound([Torus_1,Torus_2,Torus_3,Torus_4])
    STIFFNESS_y.SetColor(SALOMEDS.Color(0,0,1))
    S_id=geompy.addToStudyInFather( P9, STIFFNESS_y,'P9_STIFFNESS_y' )    

    List_ParaVis_Visualization.append(STIFFNESS_y)
    gg.createAndDisplayGO(S_id)
    gg.setDisplayMode(S_id,1)

    

    # Visualize springs/stiffness at point P9
    #---------------------------------------------
    Radius=20.0

    Pna=geompy.MakeVertexWithRef(P9,0,0,60.0)
    Pnb=geompy.MakeVertexWithRef(P9,0,0,40.0)  
    Vp=geompy.MakeVector(Pna,Pnb)  

    Torus_1 = geompy.MakeTorus(Pna, Vp, Radius, Radius/2) 
    Torus_2 = geompy.MakeTorus(Pnb, Vp, Radius, Radius/2)  

    P2a=geompy.MakeVertexWithRef(P9,0,0,-60.0)    
    P2b=geompy.MakeVertexWithRef(P9,0,0,-40.0)    
    Vm=geompy.MakeVector(P2a,P2b)  

    Torus_3 = geompy.MakeTorus(P2a, Vm, Radius, Radius/2)
    Torus_4 = geompy.MakeTorus(P2b, Vm, Radius, Radius/2)

    STIFFNESS_z=geompy.MakeCompound([Torus_1,Torus_2,Torus_3,Torus_4])
    STIFFNESS_z.SetColor(SALOMEDS.Color(0,0,1))
    S_id=geompy.addToStudyInFather( P9, STIFFNESS_z,'P9_STIFFNESS_z' )    

    List_ParaVis_Visualization.append(STIFFNESS_z)
    gg.createAndDisplayGO(S_id)
    gg.setDisplayMode(S_id,1)

    

    # Visualize springs/stiffness at point P9
    #---------------------------------------------
    Radius=20.0

    Pna=geompy.MakeVertexWithRef(P9,60.0,0,0)
    Pnb=geompy.MakeVertexWithRef(P9,40.0,0,0)  
    Vp=geompy.MakeVector(Pna,Pnb)  

    Torus_1 = geompy.MakeTorus(Pna, Vp, Radius, Radius/2) 
    Torus_2 = geompy.MakeTorus(Pnb, Vp, Radius, Radius/2)  

    P2a=geompy.MakeVertexWithRef(P9,-60.0,0,0)    
    P2b=geompy.MakeVertexWithRef(P9,-40.0,0,0)    
    Vm=geompy.MakeVector(P2a,P2b)  

    Torus_3 = geompy.MakeTorus(P2a, Vm, Radius, Radius/2)
    Torus_4 = geompy.MakeTorus(P2b, Vm, Radius, Radius/2)

    STIFFNESS_x=geompy.MakeCompound([Torus_1,Torus_2,Torus_3,Torus_4])
    STIFFNESS_x.SetColor(SALOMEDS.Color(0,0,1))
    S_id=geompy.addToStudyInFather( P9, STIFFNESS_x,'P9_STIFFNESS_x' )    

    List_ParaVis_Visualization.append(STIFFNESS_x)
    gg.createAndDisplayGO(S_id)
    gg.setDisplayMode(S_id,1)

    

    # Visualize springs/stiffness at point P9
    #---------------------------------------------
    Radius=20.0

    Pna=geompy.MakeVertexWithRef(P9,0,60.0,0)
    Pnb=geompy.MakeVertexWithRef(P9,0,40.0,0)  
    Vp=geompy.MakeVector(Pna,Pnb)  

    Torus_1 = geompy.MakeTorus(Pna, Vp, Radius, Radius/2) 
    Torus_2 = geompy.MakeTorus(Pnb, Vp, Radius, Radius/2)  

    P2a=geompy.MakeVertexWithRef(P9,0,-60.0,0)    
    P2b=geompy.MakeVertexWithRef(P9,0,-40.0,0)    
    Vm=geompy.MakeVector(P2a,P2b)  

    Torus_3 = geompy.MakeTorus(P2a, Vm, Radius, Radius/2)
    Torus_4 = geompy.MakeTorus(P2b, Vm, Radius, Radius/2)

    STIFFNESS_y=geompy.MakeCompound([Torus_1,Torus_2,Torus_3,Torus_4])
    STIFFNESS_y.SetColor(SALOMEDS.Color(0,0,1))
    S_id=geompy.addToStudyInFather( P9, STIFFNESS_y,'P9_STIFFNESS_y' )    

    List_ParaVis_Visualization.append(STIFFNESS_y)
    gg.createAndDisplayGO(S_id)
    gg.setDisplayMode(S_id,1)

    

    # Visualize springs/stiffness at point P9
    #---------------------------------------------
    Radius=20.0

    Pna=geompy.MakeVertexWithRef(P9,0,0,60.0)
    Pnb=geompy.MakeVertexWithRef(P9,0,0,40.0)  
    Vp=geompy.MakeVector(Pna,Pnb)  

    Torus_1 = geompy.MakeTorus(Pna, Vp, Radius, Radius/2) 
    Torus_2 = geompy.MakeTorus(Pnb, Vp, Radius, Radius/2)  

    P2a=geompy.MakeVertexWithRef(P9,0,0,-60.0)    
    P2b=geompy.MakeVertexWithRef(P9,0,0,-40.0)    
    Vm=geompy.MakeVector(P2a,P2b)  

    Torus_3 = geompy.MakeTorus(P2a, Vm, Radius, Radius/2)
    Torus_4 = geompy.MakeTorus(P2b, Vm, Radius, Radius/2)

    STIFFNESS_z=geompy.MakeCompound([Torus_1,Torus_2,Torus_3,Torus_4])
    STIFFNESS_z.SetColor(SALOMEDS.Color(0,0,1))
    S_id=geompy.addToStudyInFather( P9, STIFFNESS_z,'P9_STIFFNESS_z' )    

    List_ParaVis_Visualization.append(STIFFNESS_z)
    gg.createAndDisplayGO(S_id)
    gg.setDisplayMode(S_id,1)

    
  
##_stiffness_mesh##  
    ### create dummy-gemoetry for a mesh to model stiffness in CodeAster at P9
    #----------------------------------------------------   
    P9K= geompy.MakeVertexWithRef(P9, 1, 1, 1)
    SpringP9= geompy.MakeLineTwoPnt(P9, P9K)
    geompy.addToStudy( P9K, 'P9K' )
    geompy.addToStudy( SpringP9, 'SpringP9' ) 

    SpringP9M = smesh.Mesh(SpringP9)
    Decoupage = SpringP9M.Segment()
    Decoupage.NumberOfSegments(1)
    smesh.SetName(SpringP9M,'SpringP9')
    SpringP9M.Compute()
    SpringP9M.Group(P9)
    SpringP9M.Group(P9K)
    SpringP9M.GroupOnGeom(SpringP9)
      


##_vector_round_1D##
    ### geometry generation for  V0 ###
    #----------------------------------------------------
    print("Add V0")
    V0= geompy.MakeVector(P0,P1)
    geompy.addToStudy(V0,"V0" )
    geompy.PutToFolder(V0, Folder_Vectors)

    ### mesh generation for  V0 ###
    #----------------------------------------------------    
    V0M = smesh.Mesh(V0)
    Regular_1D = V0M.Segment()
    Regular_1D.NumberOfSegments(10)
    Quadratic_Mesh = Regular_1D.QuadraticMesh()

    smesh.SetName(V0M,'V0')
    V0M.Compute()
    V0M.Group(P0)
    V0M.Group(P1)
    V0M.GroupOnGeom(V0)

    structElemList.append(('CircularBeam', {'R': 35.0, 'Group_Maille': 'V0', 'EP': 4.0}))    
    List_ParaVis_Visualization.append("Beam_V0")
        

##_vector_round_3D##
    ### geometry generation for  V1 ###
    #----------------------------------------------------
    print("Add  V1 ")    

    V1= geompy.MakeVector(P1,P2)

    C1 = geompy.MakeCircle(P1,local_x_P1,35.0)                                                    
    C2 = geompy.MakeCircle(P1,local_x_P1,31.0)
                                         
    FaceTube = geompy.MakeFaceWires([C1, C2], 1)

    #For the Hexahedron to work, the pipe has to be partioned
    Pipe= geompy.MakePipe( FaceTube ,V1)
    cuttingPlane = geompy.MakePlane(P1,local_y_P1,5000.0)
    V1_3D = geompy.MakePartition([Pipe], [cuttingPlane], [], [], geompy.ShapeType["SOLID"], 0, [], 0)
    thickness = geompy.Propagate(V1_3D)[1]

    V1_3D.SetColor(SALOMEDS.Color(0.5,0.8,0.8))

    geompy.addToStudy(V1_3D,"V1")
    geompy.addToStudyInFather( V1_3D, thickness, 'thickness' )
    geompy.PutToFolder(V1_3D, Folder_Vectors)

    L_Start = geompy.GetShapesOnPlane(V1_3D,geompy.ShapeType["FACE"],local_x_P1,GEOM.ST_ON)
    V1_StartFace = geompy.MakeCompound(L_Start)
    geompy.addToStudyInFather(V1_3D,V1_StartFace,"V1_StartFace")

    L_End = geompy.GetShapesOnPlane(V1_3D,geompy.ShapeType["FACE"],local_x_P2,GEOM.ST_ON)
    V1_EndFace = geompy.MakeCompound(L_End)
    geompy.addToStudyInFather(V1_3D,V1_EndFace,"V1_EndFace")

    L_Inner = geompy.GetShapesOnCylinder(V1_3D,geompy.ShapeType["FACE"],V1,31.0,GEOM.ST_ON)
    V1_InnerFace = geompy.MakeCompound(L_Inner)
    geompy.addToStudyInFather(V1_3D,V1_InnerFace,"V1_InnerFace")

    L_Outer = geompy.GetShapesOnCylinder(V1_3D,geompy.ShapeType["FACE"],V1,35.0,GEOM.ST_ON)
    V1_OuterFace = geompy.MakeCompound(L_Outer)
    geompy.addToStudyInFather(V1_3D,V1_OuterFace,"V1_OuterFace")

    print(L_Outer)
    List_ParaVis_Visualization.append(V1)

    ### mesh generation for  V1 ###
    #----------------------------------------------------    
    V1M = smesh.Mesh(V1_3D)

    V1M.Segment().NumberOfSegments(10)
    V1M.Segment(geom=thickness).NumberOfSegments(3)
    V1M.Quadrangle()
    V1M.Hexahedron()

    smesh.SetName(V1M,'V1')
    V1M.Compute()
    V1M.Group(P1)
    V1M.Group(P2)
    V1M.GroupOnGeom(V1_StartFace)
    V1M.GroupOnGeom(V1_EndFace)
    V1M.GroupOnGeom(V1_InnerFace)
    V1M.GroupOnGeom(V1_OuterFace)

    V1M.GroupOnGeom(V1_3D)
           

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
    Quadratic_Mesh = Regular_1D.QuadraticMesh()

    smesh.SetName(V2M,'V2')
    V2M.Compute()
    V2M.Group(P2)
    V2M.Group(P3)
    V2M.GroupOnGeom(V2)

    structElemList.append(('CircularBeam', {'R': 35.0, 'Group_Maille': 'V2', 'EP': 4.0}))    
    List_ParaVis_Visualization.append("Beam_V2")
        

##_bent_3D##
    ### geometry generation for  V3_Bent ###
    #----------------------------------------------------

    print("Add  V3_Bent ")
    V3_Bent = geompy.MakeArcCenter(P3_4_center,P3,P4)

    C1 = geompy.MakeCircle(P3,local_x_P3,35.0)                                                    
    C2 = geompy.MakeCircle(P3,local_x_P3,31.0)                                            
    FaceTube = geompy.MakeFaceWires([C1, C2], 1)

    #For the Hexahedron to work, the pipe has to be partioned
    Pipe = geompy.MakePipe( FaceTube ,V3_Bent)                     
    cuttingPlane = geompy.MakePlaneThreePnt(P3_4_center,P3,P4,750)
    V3_Bent_3D= geompy.MakePartition([Pipe], [cuttingPlane], [], [], geompy.ShapeType["SOLID"], 0, [], 0)
    thickness = geompy.Propagate(V3_Bent_3D)[1]

    #Union unwanted faces
    V3_Bent_3D = geompy.UnionFaces(V3_Bent_3D)  

    V3_Bent_3D.SetColor(SALOMEDS.Color(0.5,0.8,0.8))

    geompy.addToStudy(V3_Bent_3D,"V3_Bent")
    geompy.addToStudyInFather( V3_Bent_3D, thickness, 'thickness' )
    geompy.PutToFolder(V3_Bent_3D, Folder_Vectors)

    L_Start = geompy.GetShapesOnPlane(V3_Bent_3D,geompy.ShapeType["FACE"],local_x_P3,GEOM.ST_ON)
    V3_Bent_StartFace = geompy.MakeCompound(L_Start)
    geompy.addToStudyInFather(V3_Bent_3D,V3_Bent_StartFace,"V3_Bent_StartFace")

    L_End = geompy.GetShapesOnPlane(V3_Bent_3D,geompy.ShapeType["FACE"],local_x_P4,GEOM.ST_ON)
    V3_Bent_EndFace = geompy.MakeCompound(L_End)
    geompy.addToStudyInFather(V3_Bent_3D,V3_Bent_EndFace,"V3_Bent_EndFace")

    all_faces = geompy.SubShapeAllSorted(V3_Bent_3D, geompy.ShapeType["FACE"])
    index=SortFacesByAreas(all_faces) 

    L_Inner = geompy.GetShapesOnCylinder(V3_Bent_3D,geompy.ShapeType["FACE"],V3_Bent,31.0,GEOM.ST_ON)
    V3_Bent_InnerFace = geompy.MakeCompound([all_faces[index[6]],all_faces[index[7]]])
    geompy.addToStudyInFather(V3_Bent_3D,V3_Bent_InnerFace,"V3_Bent_InnerFace")

    L_Outer = geompy.GetShapesOnCylinder(V3_Bent_3D,geompy.ShapeType["FACE"],V3_Bent,35.0,GEOM.ST_ON)
    V3_Bent_OuterFace = geompy.MakeCompound([all_faces[index[8]],all_faces[index[9]]])
    geompy.addToStudyInFather(V3_Bent_3D,V3_Bent_OuterFace,"V3_Bent_OuterFace")

    List_ParaVis_Visualization.append(V3_Bent)

    ### mesh generation for  V3_Bent ###
    #----------------------------------------------------    

    V3_BentM = smesh.Mesh(V3_Bent_3D)
    V3_BentM.Segment().NumberOfSegments(10)
    V3_BentM.Segment(geom=thickness).NumberOfSegments(3)
    V3_BentM.Quadrangle()
    V3_BentM.Hexahedron()

    smesh.SetName(V3_BentM,'V3_Bent')
    V3_BentM.Compute()
    V3_BentM.Group(P3)
    V3_BentM.Group(P4)
    V3_BentM.GroupOnGeom(V3_Bent_StartFace)
    V3_BentM.GroupOnGeom(V3_Bent_EndFace)
    V3_BentM.GroupOnGeom(V3_Bent_InnerFace)
    V3_BentM.GroupOnGeom(V3_Bent_OuterFace)
    V3_BentM.GroupOnGeom(V3_Bent_3D)

##_vector_round_1D##
    ### geometry generation for  V4 ###
    #----------------------------------------------------
    print("Add V4")
    V4= geompy.MakeVector(P4,P5)
    geompy.addToStudy(V4,"V4" )
    geompy.PutToFolder(V4, Folder_Vectors)

    ### mesh generation for  V4 ###
    #----------------------------------------------------    
    V4M = smesh.Mesh(V4)
    Regular_1D = V4M.Segment()
    Regular_1D.NumberOfSegments(10)
    Quadratic_Mesh = Regular_1D.QuadraticMesh()

    smesh.SetName(V4M,'V4')
    V4M.Compute()
    V4M.Group(P4)
    V4M.Group(P5)
    V4M.GroupOnGeom(V4)

    structElemList.append(('CircularBeam', {'R': 35.0, 'Group_Maille': 'V4', 'EP': 4.0}))    
    List_ParaVis_Visualization.append("Beam_V4")
        


    ### geometry generation for  V5_TShape ###
    #----------------------------------------------------
    print("Add  V5_TShape ")

    [V5_TShape,Junction_1,Junction_2,Junction_3,Thickness,
     Circular_quarter_of_pipe, Circular_quarter_of_pipe_1,Main_pipe_half_length,
     Flange,Incident_pipe_half_length,Internal_faces] =        geompy.MakePipeTShape(31.0,4.0,100.0,16.0,4.0,100.0, True,P5,b,a)

    V5_TShape.SetColor(SALOMEDS.Color(0.5,0.8,0.8))
    geompy.addToStudy( V5_TShape, 'V5_TShape' )
    geompy.PutToFolder(V5_TShape, Folder_Vectors)

    L_Start = geompy.GetShapesOnPlane(V5_TShape,geompy.ShapeType["FACE"],local_x_P5,GEOM.ST_ON)
    V5_TShape_StartFace = geompy.MakeCompound(L_Start)
    geompy.addToStudyInFather(V5_TShape,V5_TShape_StartFace,"V5_TShape_StartFace")

    L_Incident = geompy.GetShapesOnPlane(V5_TShape,geompy.ShapeType["FACE"],local_x_a,GEOM.ST_ON)
    V5_TShape_IncidentFace = geompy.MakeCompound(L_Incident)
    geompy.addToStudyInFather(V5_TShape,V5_TShape_IncidentFace,"V5_TShape_IncidentFace")

    L_End = geompy.GetShapesOnPlane(V5_TShape,geompy.ShapeType["FACE"],local_x_b,GEOM.ST_ON)
    V5_TShape_EndFace = geompy.MakeCompound(L_End)
    geompy.addToStudyInFather(V5_TShape,V5_TShape_EndFace,"V5_TShape_EndFace")


    all_faces = geompy.SubShapeAll(V5_TShape, geompy.ShapeType["FACE"])
    V5_TShape_InnerFace = geompy.MakeCompound([all_faces[1],all_faces[7],
                                all_faces[11],all_faces[16],all_faces[22],all_faces[28],
                                all_faces[31],all_faces[35],all_faces[40],all_faces[45],
                                all_faces[48],all_faces[52],all_faces[57],all_faces[62],
                                all_faces[64],all_faces[67]])

    geompy.addToStudyInFather(V5_TShape,V5_TShape_InnerFace,"V5_TShape_InnerFace")
    V5_TShape_OuterFace = geompy.MakeCompound([all_faces[3],all_faces[9],
                                all_faces[15],all_faces[20],all_faces[24],all_faces[30],
                                all_faces[34],all_faces[38],all_faces[42],all_faces[46],
                                all_faces[51],all_faces[55],all_faces[59],all_faces[63],
                                all_faces[66],all_faces[69]])
    
    geompy.addToStudyInFather(V5_TShape,V5_TShape_OuterFace,"V5_TShape_OuterFace")

    List_ParaVis_Visualization.append(V5_TShape)

    ### mesh generation for  V5_TShape ###
    #----------------------------------------------------    

    V5_TShapeM = smesh.Mesh(V5_TShape)
    Regular_1D = V5_TShapeM.Segment()
    Nb_Segments_1 = Regular_1D.NumberOfSegments(4)
    Nb_Segments_1.SetDistrType( 0 )
    Quadrangle_2D = V5_TShapeM.Quadrangle(algo=smeshBuilder.QUADRANGLE)
    Hexa_3D = V5_TShapeM.Hexahedron(algo=smeshBuilder.Hexa)
    Nb_Segments_2 = smesh.CreateHypothesis('NumberOfSegments')
    Nb_Segments_2.SetNumberOfSegments( 4 )
    Nb_Segments_2.SetDistrType( 0 )
    status = V5_TShapeM.AddHypothesis(Regular_1D,Thickness)
    status = V5_TShapeM.AddHypothesis(Nb_Segments_2,Thickness)
    isDone = V5_TShapeM.Compute()
    [ Sub_mesh_1 ] = V5_TShapeM.GetMesh().GetSubMeshes()
    Sub_mesh_1 = V5_TShapeM.GetSubMesh(Thickness, 'Sub-mesh_1' )

    ## Set names of Mesh objects
    smesh.SetName(V5_TShapeM,'V5_TShape')
    V5_TShapeM.Compute()
    V5_TShapeM.Group(P5)
    V5_TShapeM.Group(b)
    V5_TShapeM.Group(a)

    V5_TShapeM.GroupOnGeom(V5_TShape)
    V5_TShapeM.GroupOnGeom(V5_TShape_StartFace)
    V5_TShapeM.GroupOnGeom(V5_TShape_IncidentFace)
    V5_TShapeM.GroupOnGeom(V5_TShape_EndFace)
    V5_TShapeM.GroupOnGeom(V5_TShape_InnerFace)
    V5_TShapeM.GroupOnGeom(V5_TShape_OuterFace)


    smesh.SetName(Regular_1D.GetAlgorithm(), 'Regular_1D')
    smesh.SetName(Hexa_3D.GetAlgorithm(), 'Hexa_3D')
    smesh.SetName(Quadrangle_2D.GetAlgorithm(), 'Quadrangle_2D')
    smesh.SetName(Nb_Segments_2, 'Nb. Segments_2')
    smesh.SetName(Nb_Segments_1, 'Nb. Segments_1')
    smesh.SetName(V5_TShapeM.GetMesh()," V5_TShapeM")
    smesh.SetName(Sub_mesh_1, 'Sub-mesh_1')

            

##_vector_round_3D##
    ### geometry generation for  V6 ###
    #----------------------------------------------------
    print("Add  V6 ")    

    V6= geompy.MakeVector(b,P8)

    C1 = geompy.MakeCircle(b,local_x_b,35.0)                                                    
    C2 = geompy.MakeCircle(b,local_x_b,31.0)
                                         
    FaceTube = geompy.MakeFaceWires([C1, C2], 1)

    #For the Hexahedron to work, the pipe has to be partioned
    Pipe= geompy.MakePipe( FaceTube ,V6)
    cuttingPlane = geompy.MakePlane(b,local_y_b,5000.0)
    V6_3D = geompy.MakePartition([Pipe], [cuttingPlane], [], [], geompy.ShapeType["SOLID"], 0, [], 0)
    thickness = geompy.Propagate(V6_3D)[1]

    V6_3D.SetColor(SALOMEDS.Color(0.5,0.8,0.8))

    geompy.addToStudy(V6_3D,"V6")
    geompy.addToStudyInFather( V6_3D, thickness, 'thickness' )
    geompy.PutToFolder(V6_3D, Folder_Vectors)

    L_Start = geompy.GetShapesOnPlane(V6_3D,geompy.ShapeType["FACE"],local_x_b,GEOM.ST_ON)
    V6_StartFace = geompy.MakeCompound(L_Start)
    geompy.addToStudyInFather(V6_3D,V6_StartFace,"V6_StartFace")

    L_End = geompy.GetShapesOnPlane(V6_3D,geompy.ShapeType["FACE"],local_x_P8,GEOM.ST_ON)
    V6_EndFace = geompy.MakeCompound(L_End)
    geompy.addToStudyInFather(V6_3D,V6_EndFace,"V6_EndFace")

    L_Inner = geompy.GetShapesOnCylinder(V6_3D,geompy.ShapeType["FACE"],V6,31.0,GEOM.ST_ON)
    V6_InnerFace = geompy.MakeCompound(L_Inner)
    geompy.addToStudyInFather(V6_3D,V6_InnerFace,"V6_InnerFace")

    L_Outer = geompy.GetShapesOnCylinder(V6_3D,geompy.ShapeType["FACE"],V6,35.0,GEOM.ST_ON)
    V6_OuterFace = geompy.MakeCompound(L_Outer)
    geompy.addToStudyInFather(V6_3D,V6_OuterFace,"V6_OuterFace")

    print(L_Outer)
    List_ParaVis_Visualization.append(V6)

    ### mesh generation for  V6 ###
    #----------------------------------------------------    
    V6M = smesh.Mesh(V6_3D)

    V6M.Segment().NumberOfSegments(10)
    V6M.Segment(geom=thickness).NumberOfSegments(3)
    V6M.Quadrangle()
    V6M.Hexahedron()

    smesh.SetName(V6M,'V6')
    V6M.Compute()
    V6M.Group(b)
    V6M.Group(P8)
    V6M.GroupOnGeom(V6_StartFace)
    V6M.GroupOnGeom(V6_EndFace)
    V6M.GroupOnGeom(V6_InnerFace)
    V6M.GroupOnGeom(V6_OuterFace)

    V6M.GroupOnGeom(V6_3D)
           

##_vector_round_3D##
    ### geometry generation for  V7 ###
    #----------------------------------------------------
    print("Add  V7 ")    

    V7= geompy.MakeVector(a,P9)

    C1 = geompy.MakeCircle(a,local_x_a,20)                                                    
    C2 = geompy.MakeCircle(a,local_x_a,16.0)
                                         
    FaceTube = geompy.MakeFaceWires([C1, C2], 1)

    #For the Hexahedron to work, the pipe has to be partioned
    Pipe= geompy.MakePipe( FaceTube ,V7)
    cuttingPlane = geompy.MakePlane(a,local_y_a,5000.0)
    V7_3D = geompy.MakePartition([Pipe], [cuttingPlane], [], [], geompy.ShapeType["SOLID"], 0, [], 0)
    thickness = geompy.Propagate(V7_3D)[1]

    V7_3D.SetColor(SALOMEDS.Color(0.5,0.8,0.8))

    geompy.addToStudy(V7_3D,"V7")
    geompy.addToStudyInFather( V7_3D, thickness, 'thickness' )
    geompy.PutToFolder(V7_3D, Folder_Vectors)

    L_Start = geompy.GetShapesOnPlane(V7_3D,geompy.ShapeType["FACE"],local_x_a,GEOM.ST_ON)
    V7_StartFace = geompy.MakeCompound(L_Start)
    geompy.addToStudyInFather(V7_3D,V7_StartFace,"V7_StartFace")

    L_End = geompy.GetShapesOnPlane(V7_3D,geompy.ShapeType["FACE"],local_x_P9,GEOM.ST_ON)
    V7_EndFace = geompy.MakeCompound(L_End)
    geompy.addToStudyInFather(V7_3D,V7_EndFace,"V7_EndFace")

    L_Inner = geompy.GetShapesOnCylinder(V7_3D,geompy.ShapeType["FACE"],V7,16.0,GEOM.ST_ON)
    V7_InnerFace = geompy.MakeCompound(L_Inner)
    geompy.addToStudyInFather(V7_3D,V7_InnerFace,"V7_InnerFace")

    L_Outer = geompy.GetShapesOnCylinder(V7_3D,geompy.ShapeType["FACE"],V7,20,GEOM.ST_ON)
    V7_OuterFace = geompy.MakeCompound(L_Outer)
    geompy.addToStudyInFather(V7_3D,V7_OuterFace,"V7_OuterFace")

    print(L_Outer)
    List_ParaVis_Visualization.append(V7)

    ### mesh generation for  V7 ###
    #----------------------------------------------------    
    V7M = smesh.Mesh(V7_3D)

    V7M.Segment().NumberOfSegments(10)
    V7M.Segment(geom=thickness).NumberOfSegments(3)
    V7M.Quadrangle()
    V7M.Hexahedron()

    smesh.SetName(V7M,'V7')
    V7M.Compute()
    V7M.Group(a)
    V7M.Group(P9)
    V7M.GroupOnGeom(V7_StartFace)
    V7M.GroupOnGeom(V7_EndFace)
    V7M.GroupOnGeom(V7_InnerFace)
    V7M.GroupOnGeom(V7_OuterFace)

    V7M.GroupOnGeom(V7_3D)
           

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

    Completed_Mesh = smesh.Concatenate([V0M.GetMesh() ,V1M.GetMesh() ,V2M.GetMesh() ,
           V3_BentM.GetMesh() ,V4M.GetMesh() ,V5_TShapeM.GetMesh() ,V6M.GetMesh() ,
           V7M.GetMesh() ,P0M.GetMesh() ,P1M.GetMesh() ,P2M.GetMesh() ,P3M.GetMesh() ,
           P3_4_centerM.GetMesh() ,P4M.GetMesh() ,P5M.GetMesh() ,aM.GetMesh() ,bM.GetMesh() ,
           P8M.GetMesh() ,P9M.GetMesh() ,SpringP9M.GetMesh() , ], 1, 0, 1e-05)
    coincident_nodes = Completed_Mesh.FindCoincidentNodes( 1e-05 )
    Completed_Mesh.MergeNodes(coincident_nodes)
    equal_elements = Completed_Mesh.FindEqualElements(Completed_Mesh)    
    Completed_Mesh.MergeElements(equal_elements)   
    smesh.SetName(Completed_Mesh.GetMesh(), 'Completed_Mesh')
        


##_finalize##
    #exports the created mesh compound 
    try:
        Completed_Mesh.ExportMED( r'/home/max/salome_meca/TUBA_2019/tutorials/000_Testing/x_008_TUYAU_3d/008_TUYAU_3D_K_M_F.mmed', 0)
    except:
        print ('ExportPartToMED() failed')

    #exports visualizations (structural elements, forces, etc) as a grouped geometry to be used in Paravis
    try:
        geompy.ExportVTK(compound_paravis, '/home/max/salome_meca/TUBA_2019/tutorials/000_Testing/x_008_TUYAU_3d/compound_paravis.vtk', 0.001)     
    except:
        print ('ExportVTK of the visualization compound failed')

    if salome.sg.hasDesktop():
       salome.sg.updateObjBrowser()
    time2=time.time()
    dtime = time2 - time1
    print("------------------------")
    print("Duration of construction:"+str(round(dtime,2))+"s")







    
Project()