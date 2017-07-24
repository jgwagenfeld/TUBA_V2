#!/usr/bin/python 3
# -*- coding: iso-8859-1 -*-

import time
time1=time.time()
import sys
sys.path.append(' /home/jangeorg/TUBA/examples/000_Testing/001_TUBE_K_M_F ')

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

#from  salome.geom.structelem import StructuralElementManager
#structElemManager = StructuralElementManager()
#commandList=[]

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
    List_Visualization=[]
    List_ParaVis_Visualization=[]
    L1=[]
    L2=[]
    List_id=[]
    ERREUR=False

            

    P0= geompy.MakeVertex(0, 0, 0 )
    geompy.addToStudy(P0,"P0 ")
    Vd2x_P0 = geompy.MakeVectorDXDYDZ(1.0, 0.0, 0.0)
    P0_vd2x=    geompy.MakeTranslationVectorDistance(P0,Vd2x_P0,100)
    Vd2x_P0= geompy.MakeVector(P0,P0_vd2x)
    geompy.addToStudyInFather(P0,Vd2x_P0,"Vd2x_P0 " )

                
    P0_BLOCK_xyzrxryrz=geompy.MakeBox(70.0,70.0,70.0,-70.0,-70.0,-70.0)	
    P0_BLOCK_xyzrxryrz.SetColor(SALOMEDS.Color(1,1,0))
    P0_BLOCK_xyzrxryrz_id=geompy.addToStudyInFather( P0, P0_BLOCK_xyzrxryrz,'P0_BLOCK_xyzrxryrz' )
 #   B_id=geompy.addToStudy(P0_BLOCK_xyzrxryrz,'P0_BLOCK_xyzrxryrz' )
    
    
    
    List_ParaVis_Visualization.append(P0_BLOCK_xyzrxryrz)
    objId = geompy.getObjectID(P0_BLOCK_xyzrxryrz)    
    gg.createAndDisplayGO(objId)
    gg.setDisplayMode(objId,1)
    gg.setColor(objId,218,165,31)
  
    

    P1= geompy.MakeVertex(1000, 0, 0 )
    geompy.addToStudy(P1,"P1 ")
    Vd2x_P1 = geompy.MakeVectorDXDYDZ(1.0, 0.0, 0.0)
    P1_vd2x=    geompy.MakeTranslationVectorDistance(P1,Vd2x_P1,100)
    Vd2x_P1= geompy.MakeVector(P1,P1_vd2x)
    geompy.addToStudyInFather(P1,Vd2x_P1,"Vd2x_P1 " )


    Radius=35.0
        
    Pna=geompy.MakeVertexWithRef(P1,Radius*0.0,Radius*1.0,Radius*0.0)
    Pnb=geompy.MakeVertexWithRef(P1,1.5*Radius*0.0,1.5*Radius*1.0,1.5*Radius*0.0)
    Pnc=geompy.MakeVertexWithRef(P1,10*Radius*0.0,10*Radius*1.0,10*Radius*0.0) 
 
    V_force=geompy.MakeVector(Pna,Pnb)     

    Tip = geompy.MakeCone(Pnc,V_force,2*Radius,0,4*Radius)           
    Shaft = geompy.MakeCylinder(P1, V_force,0.5*Radius, 10*Radius)
    Arrow = geompy.MakeCompound([Tip,Shaft])  
               
    Arrow.SetColor(SALOMEDS.Color(1,0,0))
    B_id=geompy.addToStudyInFather( P1, Arrow,'P1_Arrow' )    

    List_ParaVis_Visualization.append(Arrow)
    gg.createAndDisplayGO(B_id)
    gg.setDisplayMode(B_id,1)
            

    P2= geompy.MakeVertex(2000, 0, 0 )
    geompy.addToStudy(P2,"P2 ")
    Vd2x_P2 = geompy.MakeVectorDXDYDZ(1.0, 0.0, 0.0)
    P2_vd2x=    geompy.MakeTranslationVectorDistance(P2,Vd2x_P2,100)
    Vd2x_P2= geompy.MakeVector(P2,P2_vd2x)
    geompy.addToStudyInFather(P2,Vd2x_P2,"Vd2x_P2 " )
        
 
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
    

    P3= geompy.MakeVertex(3000, 0, 0 )
    geompy.addToStudy(P3,"P3 ")
    Vd2x_P3 = geompy.MakeVectorDXDYDZ(1.0, 0.0, 0.0)
    P3_vd2x=    geompy.MakeTranslationVectorDistance(P3,Vd2x_P3,100)
    Vd2x_P3= geompy.MakeVector(P3,P3_vd2x)
    geompy.addToStudyInFather(P3,Vd2x_P3,"Vd2x_P3 " )
        
 
#    try:
    Radius=35.0

    Pna=geompy.MakeVertexWithRef(P3,105.0,0,0)
    Pnb=geompy.MakeVertexWithRef(P3,70.0,0,0)  
    Vp=geompy.MakeVector(Pna,Pnb)  

    Torus_1 = geompy.MakeTorus(Pna, Vp, Radius, Radius/2) 
    Torus_2 = geompy.MakeTorus(Pnb, Vp, Radius, Radius/2)  
 
    P2a=geompy.MakeVertexWithRef(P3,-105.0,0,0)    
    P2b=geompy.MakeVertexWithRef(P3,-70.0,0,0)    
    Vm=geompy.MakeVector(P2a,P2b)  

    Torus_3 = geompy.MakeTorus(P2a, Vm, Radius, Radius/2) 
    Torus_4 = geompy.MakeTorus(P2b, Vm, Radius, Radius/2)  
    
    STIFFNESS_x=geompy.MakeCompound([Torus_1,Torus_2,Torus_3,Torus_4])
    STIFFNESS_x.SetColor(SALOMEDS.Color(0,0,1))
    S_id=geompy.addToStudyInFather( P3, STIFFNESS_x,'P3_STIFFNESS_x' )    

    List_ParaVis_Visualization.append(STIFFNESS_x)    
    gg.createAndDisplayGO(S_id)
    gg.setDisplayMode(S_id,1)
        
    
        
 
#    try:
    Radius=35.0

    Pna=geompy.MakeVertexWithRef(P3,0,105.0,0)
    Pnb=geompy.MakeVertexWithRef(P3,0,70.0,0)  
    Vp=geompy.MakeVector(Pna,Pnb)  

    Torus_1 = geompy.MakeTorus(Pna, Vp, Radius, Radius/2) 
    Torus_2 = geompy.MakeTorus(Pnb, Vp, Radius, Radius/2)  
 
    P2a=geompy.MakeVertexWithRef(P3,0,-105.0,0)    
    P2b=geompy.MakeVertexWithRef(P3,0,-70.0,0)    
    Vm=geompy.MakeVector(P2a,P2b)  

    Torus_3 = geompy.MakeTorus(P2a, Vm, Radius, Radius/2) 
    Torus_4 = geompy.MakeTorus(P2b, Vm, Radius, Radius/2)  
    
    STIFFNESS_y=geompy.MakeCompound([Torus_1,Torus_2,Torus_3,Torus_4])
    STIFFNESS_y.SetColor(SALOMEDS.Color(0,0,1))
    S_id=geompy.addToStudyInFather( P3, STIFFNESS_y,'P3_STIFFNESS_y' )    

    List_ParaVis_Visualization.append(STIFFNESS_y)    
    gg.createAndDisplayGO(S_id)
    gg.setDisplayMode(S_id,1)
        
    
        
 
#    try:
    Radius=35.0

    Pna=geompy.MakeVertexWithRef(P3,0,0,105.0)
    Pnb=geompy.MakeVertexWithRef(P3,0,0,70.0)  
    Vp=geompy.MakeVector(Pna,Pnb)  

    Torus_1 = geompy.MakeTorus(Pna, Vp, Radius, Radius/2) 
    Torus_2 = geompy.MakeTorus(Pnb, Vp, Radius, Radius/2)  
 
    P2a=geompy.MakeVertexWithRef(P3,0,0,-105.0)    
    P2b=geompy.MakeVertexWithRef(P3,0,0,-70.0)    
    Vm=geompy.MakeVector(P2a,P2b)  

    Torus_3 = geompy.MakeTorus(P2a, Vm, Radius, Radius/2) 
    Torus_4 = geompy.MakeTorus(P2b, Vm, Radius, Radius/2)  
    
    STIFFNESS_z=geompy.MakeCompound([Torus_1,Torus_2,Torus_3,Torus_4])
    STIFFNESS_z.SetColor(SALOMEDS.Color(0,0,1))
    S_id=geompy.addToStudyInFather( P3, STIFFNESS_z,'P3_STIFFNESS_z' )    

    List_ParaVis_Visualization.append(STIFFNESS_z)    
    gg.createAndDisplayGO(S_id)
    gg.setDisplayMode(S_id,1)
        
    
        
 
#    try:
    Radius=35.0

    Pna=geompy.MakeVertexWithRef(P3,105.0,0,0)
    Pnb=geompy.MakeVertexWithRef(P3,70.0,0,0)  
    Vp=geompy.MakeVector(Pna,Pnb)  

    Torus_1 = geompy.MakeTorus(Pna, Vp, Radius, Radius/2) 
    Torus_2 = geompy.MakeTorus(Pnb, Vp, Radius, Radius/2)  
 
    P2a=geompy.MakeVertexWithRef(P3,-105.0,0,0)    
    P2b=geompy.MakeVertexWithRef(P3,-70.0,0,0)    
    Vm=geompy.MakeVector(P2a,P2b)  

    Torus_3 = geompy.MakeTorus(P2a, Vm, Radius, Radius/2) 
    Torus_4 = geompy.MakeTorus(P2b, Vm, Radius, Radius/2)  
    
    STIFFNESS_x=geompy.MakeCompound([Torus_1,Torus_2,Torus_3,Torus_4])
    STIFFNESS_x.SetColor(SALOMEDS.Color(0,0,1))
    S_id=geompy.addToStudyInFather( P3, STIFFNESS_x,'P3_STIFFNESS_x' )    

    List_ParaVis_Visualization.append(STIFFNESS_x)    
    gg.createAndDisplayGO(S_id)
    gg.setDisplayMode(S_id,1)
        
    
        
 
#    try:
    Radius=35.0

    Pna=geompy.MakeVertexWithRef(P3,0,105.0,0)
    Pnb=geompy.MakeVertexWithRef(P3,0,70.0,0)  
    Vp=geompy.MakeVector(Pna,Pnb)  

    Torus_1 = geompy.MakeTorus(Pna, Vp, Radius, Radius/2) 
    Torus_2 = geompy.MakeTorus(Pnb, Vp, Radius, Radius/2)  
 
    P2a=geompy.MakeVertexWithRef(P3,0,-105.0,0)    
    P2b=geompy.MakeVertexWithRef(P3,0,-70.0,0)    
    Vm=geompy.MakeVector(P2a,P2b)  

    Torus_3 = geompy.MakeTorus(P2a, Vm, Radius, Radius/2) 
    Torus_4 = geompy.MakeTorus(P2b, Vm, Radius, Radius/2)  
    
    STIFFNESS_y=geompy.MakeCompound([Torus_1,Torus_2,Torus_3,Torus_4])
    STIFFNESS_y.SetColor(SALOMEDS.Color(0,0,1))
    S_id=geompy.addToStudyInFather( P3, STIFFNESS_y,'P3_STIFFNESS_y' )    

    List_ParaVis_Visualization.append(STIFFNESS_y)    
    gg.createAndDisplayGO(S_id)
    gg.setDisplayMode(S_id,1)
        
    
        
 
#    try:
    Radius=35.0

    Pna=geompy.MakeVertexWithRef(P3,0,0,105.0)
    Pnb=geompy.MakeVertexWithRef(P3,0,0,70.0)  
    Vp=geompy.MakeVector(Pna,Pnb)  

    Torus_1 = geompy.MakeTorus(Pna, Vp, Radius, Radius/2) 
    Torus_2 = geompy.MakeTorus(Pnb, Vp, Radius, Radius/2)  
 
    P2a=geompy.MakeVertexWithRef(P3,0,0,-105.0)    
    P2b=geompy.MakeVertexWithRef(P3,0,0,-70.0)    
    Vm=geompy.MakeVector(P2a,P2b)  

    Torus_3 = geompy.MakeTorus(P2a, Vm, Radius, Radius/2) 
    Torus_4 = geompy.MakeTorus(P2b, Vm, Radius, Radius/2)  
    
    STIFFNESS_z=geompy.MakeCompound([Torus_1,Torus_2,Torus_3,Torus_4])
    STIFFNESS_z.SetColor(SALOMEDS.Color(0,0,1))
    S_id=geompy.addToStudyInFather( P3, STIFFNESS_z,'P3_STIFFNESS_z' )    

    List_ParaVis_Visualization.append(STIFFNESS_z)    
    gg.createAndDisplayGO(S_id)
    gg.setDisplayMode(S_id,1)
        
    
  
    P3K= geompy.MakeVertexWithRef(P3, 1, 1, 1)
    SpringP3= geompy.MakeLineTwoPnt(P3, P3K)
    geompy.addToStudy( P3K, 'P3K' )
    geompy.addToStudy( SpringP3, 'SpringP3' ) 

    try:
       SpringP3M = smesh.Mesh(SpringP3)
       Decoupage = SpringP3M.Segment()
       Decoupage.NumberOfSegments(1)
       smesh.SetName(SpringP3M,'SpringP3')
       SpringP3M.Compute()
       SpringP3M.Group(P3)
       SpringP3M.Group(P3K)
       SpringP3M.GroupOnGeom(SpringP3)
    except:
       ERREUR=True
       print ("   =>ERROR WHILE GENERATING THE MESH!_")
       return        


    P4= geompy.MakeVertex(4000, 0, 0 )
    geompy.addToStudy(P4,"P4 ")
    Vd2x_P4 = geompy.MakeVectorDXDYDZ(1.0, 0.0, 0.0)
    P4_vd2x=    geompy.MakeTranslationVectorDistance(P4,Vd2x_P4,100)
    Vd2x_P4= geompy.MakeVector(P4,P4_vd2x)
    geompy.addToStudyInFather(P4,Vd2x_P4,"Vd2x_P4 " )

                
    P4_MASS=geompy.MakeSpherePntR(P4,70.0)	
    P4_MASS.SetColor(SALOMEDS.Color(0,0,1))
    P4_MASS_id=geompy.addToStudyInFather( P4, P4_MASS,'P4_MASS' )
 #   B_id=geompy.addToStudy(P4_MASS,'P4_MASS' )
    
    
    
    List_ParaVis_Visualization.append(P4_MASS)
    objId = geompy.getObjectID(P4_MASS)    
    gg.createAndDisplayGO(objId)
    gg.setDisplayMode(objId,1)
    gg.setColor(objId,218,165,31)
  
    

    P5= geompy.MakeVertex(5000.0, 0.0, 0.0 )
    geompy.addToStudy(P5,"P5 ")
    Vd2x_P5 = geompy.MakeVectorDXDYDZ(1.0, 0.0, 0.0)
    P5_vd2x=    geompy.MakeTranslationVectorDistance(P5,Vd2x_P5,100)
    Vd2x_P5= geompy.MakeVector(P5,P5_vd2x)
    geompy.addToStudyInFather(P5,Vd2x_P5,"Vd2x_P5 " )


    5.0
    Radius=35.0
        
    Pna=geompy.MakeVertexWithRef(P5,0,-5,0)
   
    V_def=geompy.MakeVector(P5,Pna)

    Deform_P5 = geompy.MakeCone(P5,V_def,1*Radius,0,5.0)

               
    Deform_P5.SetColor(SALOMEDS.Color(1,0.5,0))
    B_id=geompy.addToStudyInFather( P5, Deform_P5,'P5_Deform' )    


    List_ParaVis_Visualization.append(Deform_P5)
    gg.createAndDisplayGO(B_id)
    gg.setDisplayMode(B_id,1)
    

    P6= geompy.MakeVertex(5850.0, 0.0, 0.0 )
    geompy.addToStudy(P6,"P6 ")
    Vd2x_P6 = geompy.MakeVectorDXDYDZ(1.0, 0.0, 0.0)
    P6_vd2x=    geompy.MakeTranslationVectorDistance(P6,Vd2x_P6,100)
    Vd2x_P6= geompy.MakeVector(P6,P6_vd2x)
    geompy.addToStudyInFather(P6,Vd2x_P6,"Vd2x_P6 " )

    P6_7_center= geompy.MakeVertex(5850.0, 9.184850993605149e-15, 150.0 )
    geompy.addToStudy(P6_7_center,"P6_7_center ")
    Vd2x_P6_7_center = geompy.MakeVectorDXDYDZ(1, 0, 0)
    P6_7_center_vd2x=    geompy.MakeTranslationVectorDistance(P6_7_center,Vd2x_P6_7_center,100)
    Vd2x_P6_7_center= geompy.MakeVector(P6_7_center,P6_7_center_vd2x)
    geompy.addToStudyInFather(P6_7_center,Vd2x_P6_7_center,"Vd2x_P6_7_center " )

    P7= geompy.MakeVertex(6000.0, 9.184850993605149e-15, 150.0 )
    geompy.addToStudy(P7,"P7 ")
    Vd2x_P7 = geompy.MakeVectorDXDYDZ(6.123233995736766e-17, 6.123233995736766e-17, 1.0)
    P7_vd2x=    geompy.MakeTranslationVectorDistance(P7,Vd2x_P7,100)
    Vd2x_P7= geompy.MakeVector(P7,P7_vd2x)
    geompy.addToStudyInFather(P7,Vd2x_P7,"Vd2x_P7 " )

    P8= geompy.MakeVertex(6000.0, 7.041719095097281e-14, 1150.0 )
    geompy.addToStudy(P8,"P8 ")
    Vd2x_P8 = geompy.MakeVectorDXDYDZ(6.123233995736766e-17, 6.123233995736766e-17, 1.0)
    P8_vd2x=    geompy.MakeTranslationVectorDistance(P8,Vd2x_P8,100)
    Vd2x_P8= geompy.MakeVector(P8,P8_vd2x)
    geompy.addToStudyInFather(P8,Vd2x_P8,"Vd2x_P8 " )
        
 
    Radius=35.0


    
    Pna=geompy.MakeVertexWithRef(P8,105.0,0,0)
    Pnb=geompy.MakeVertexWithRef(P8,70.0,0,0)  
    Vp=geompy.MakeVector(Pna,Pnb)  
    Cone1 = geompy.MakeCone(Pna,Vp,Radius,0,2*Radius)

   
    P2a=geompy.MakeVertexWithRef(P8,-105.0,0,0)    
    P2b=geompy.MakeVertexWithRef(P8,-70.0,0,0)    
    Vm=geompy.MakeVector(P2a,P2b)  
    Cone2 = geompy.MakeCone(P2a,Vm,Radius,0,2*Radius)
    
    BLOCK_x=geompy.MakeCompound([Cone1,Cone2])
    BLOCK_x.SetColor(SALOMEDS.Color(1,1,0))
    B_id=geompy.addToStudyInFather( P8, BLOCK_x,'P8_BLOCK_x' )    

    List_ParaVis_Visualization.append(BLOCK_x)
    gg.createAndDisplayGO(B_id)
    gg.setDisplayMode(B_id,1)
    
        
 
    Radius=35.0


    
    Pna=geompy.MakeVertexWithRef(P8,0,105.0,0)
    Pnb=geompy.MakeVertexWithRef(P8,0,70.0,0)  
    Vp=geompy.MakeVector(Pna,Pnb)  
    Cone1 = geompy.MakeCone(Pna,Vp,Radius,0,2*Radius)

   
    P2a=geompy.MakeVertexWithRef(P8,0,-105.0,0)    
    P2b=geompy.MakeVertexWithRef(P8,0,-70.0,0)    
    Vm=geompy.MakeVector(P2a,P2b)  
    Cone2 = geompy.MakeCone(P2a,Vm,Radius,0,2*Radius)
    
    BLOCK_y=geompy.MakeCompound([Cone1,Cone2])
    BLOCK_y.SetColor(SALOMEDS.Color(1,1,0))
    B_id=geompy.addToStudyInFather( P8, BLOCK_y,'P8_BLOCK_y' )    

    List_ParaVis_Visualization.append(BLOCK_y)
    gg.createAndDisplayGO(B_id)
    gg.setDisplayMode(B_id,1)
    

    P9= geompy.MakeVertex(6000.0, 1.3164953090834046e-13, 2150.0 )
    geompy.addToStudy(P9,"P9 ")
    Vd2x_P9 = geompy.MakeVectorDXDYDZ(6.123233995736766e-17, 6.123233995736766e-17, 1.0)
    P9_vd2x=    geompy.MakeTranslationVectorDistance(P9,Vd2x_P9,100)
    Vd2x_P9= geompy.MakeVector(P9,P9_vd2x)
    geompy.addToStudyInFather(P9,Vd2x_P9,"Vd2x_P9 " )

           
    try:
      print("Add V0")
      V0= geompy.MakeVector(P0,P1)
      #Liste.append([P0,"P0"])
      geompy.addToStudy(V0,"V0" )
      List_Visualization.append(V0)
        

      _C1 = geompy.MakeCircle(P0, V0,35.0)
      _C2 = geompy.MakeCircle(P0, V0,31.0)
      FaceTube = geompy.MakeFaceWires([_C1, _C2], 1)

            

    except:
       ERREUR=True
       print ("   =>ERROR BUILDING THE GEOMETRY!")

    try:
       V0M = smesh.Mesh(V0)
       Decoupage = V0M.Segment()
       Decoupage.NumberOfSegments(10)

       smesh.SetName(V0M,'V0')
       V0M.Compute()
       V0M.Group(P0)
       V0M.Group(P1)
       V0M.GroupOnGeom(V0)
    except:
       ERREUR=True
       print ("   =>ERROR WHILE GENERATING THE MESH!_")
       return
#    commandList.append(('CircularBeam', {'R': 35.0, 'Group_Maille': 'V0', 'EP': 4.0}))    
        


    if List_Visualization!=[]:
       _W=geompy.MakeWire(List_Visualization,1e-7)
       Pipe_V0 = geompy.MakePipe( FaceTube ,_W)
       Pipe_V0.SetColor(SALOMEDS.Color(0.6,0.6,0.6))
       Pipe_id=geompy.addToStudyInFather(V0,Pipe_V0,"Pipe_V0")
       gg.createAndDisplayGO(Pipe_id)
       gg.setDisplayMode(Pipe_id,1)

       List_ParaVis_Visualization.append(Pipe_V0)
       List_Visualization=[]
    

           
    try:
      print("Add V1")
      V1= geompy.MakeVector(P1,P2)
      #Liste.append([P1,"P1"])
      geompy.addToStudy(V1,"V1" )
      List_Visualization.append(V1)
        

      _C1 = geompy.MakeCircle(P1, V1,35.0)
      _C2 = geompy.MakeCircle(P1, V1,31.0)
      FaceTube = geompy.MakeFaceWires([_C1, _C2], 1)

            

    except:
       ERREUR=True
       print ("   =>ERROR BUILDING THE GEOMETRY!")

    try:
       V1M = smesh.Mesh(V1)
       Decoupage = V1M.Segment()
       Decoupage.NumberOfSegments(10)

       smesh.SetName(V1M,'V1')
       V1M.Compute()
       V1M.Group(P1)
       V1M.Group(P2)
       V1M.GroupOnGeom(V1)
    except:
       ERREUR=True
       print ("   =>ERROR WHILE GENERATING THE MESH!_")
       return
#    commandList.append(('CircularBeam', {'R': 35.0, 'Group_Maille': 'V1', 'EP': 4.0}))    
        


    if List_Visualization!=[]:
       _W=geompy.MakeWire(List_Visualization,1e-7)
       Pipe_V1 = geompy.MakePipe( FaceTube ,_W)
       Pipe_V1.SetColor(SALOMEDS.Color(0.6,0.6,0.6))
       Pipe_id=geompy.addToStudyInFather(V1,Pipe_V1,"Pipe_V1")
       gg.createAndDisplayGO(Pipe_id)
       gg.setDisplayMode(Pipe_id,1)

       List_ParaVis_Visualization.append(Pipe_V1)
       List_Visualization=[]
    

           
    try:
      print("Add V2")
      V2= geompy.MakeVector(P2,P3)
      #Liste.append([P2,"P2"])
      geompy.addToStudy(V2,"V2" )
      List_Visualization.append(V2)
        

      _C1 = geompy.MakeCircle(P2, V2,35.0)
      _C2 = geompy.MakeCircle(P2, V2,31.0)
      FaceTube = geompy.MakeFaceWires([_C1, _C2], 1)

            

    except:
       ERREUR=True
       print ("   =>ERROR BUILDING THE GEOMETRY!")

    try:
       V2M = smesh.Mesh(V2)
       Decoupage = V2M.Segment()
       Decoupage.NumberOfSegments(10)

       smesh.SetName(V2M,'V2')
       V2M.Compute()
       V2M.Group(P2)
       V2M.Group(P3)
       V2M.GroupOnGeom(V2)
    except:
       ERREUR=True
       print ("   =>ERROR WHILE GENERATING THE MESH!_")
       return
#    commandList.append(('CircularBeam', {'R': 35.0, 'Group_Maille': 'V2', 'EP': 4.0}))    
        


    if List_Visualization!=[]:
       _W=geompy.MakeWire(List_Visualization,1e-7)
       Pipe_V2 = geompy.MakePipe( FaceTube ,_W)
       Pipe_V2.SetColor(SALOMEDS.Color(0.6,0.6,0.6))
       Pipe_id=geompy.addToStudyInFather(V2,Pipe_V2,"Pipe_V2")
       gg.createAndDisplayGO(Pipe_id)
       gg.setDisplayMode(Pipe_id,1)

       List_ParaVis_Visualization.append(Pipe_V2)
       List_Visualization=[]
    

           
    try:
      print("Add V3")
      V3= geompy.MakeVector(P3,P4)
      #Liste.append([P3,"P3"])
      geompy.addToStudy(V3,"V3" )
      List_Visualization.append(V3)
        

      _C1 = geompy.MakeCircle(P3, V3,35.0)
      _C2 = geompy.MakeCircle(P3, V3,31.0)
      FaceTube = geompy.MakeFaceWires([_C1, _C2], 1)

            

    except:
       ERREUR=True
       print ("   =>ERROR BUILDING THE GEOMETRY!")

    try:
       V3M = smesh.Mesh(V3)
       Decoupage = V3M.Segment()
       Decoupage.NumberOfSegments(10)

       smesh.SetName(V3M,'V3')
       V3M.Compute()
       V3M.Group(P3)
       V3M.Group(P4)
       V3M.GroupOnGeom(V3)
    except:
       ERREUR=True
       print ("   =>ERROR WHILE GENERATING THE MESH!_")
       return
#    commandList.append(('CircularBeam', {'R': 35.0, 'Group_Maille': 'V3', 'EP': 4.0}))    
        


    if List_Visualization!=[]:
       _W=geompy.MakeWire(List_Visualization,1e-7)
       Pipe_V3 = geompy.MakePipe( FaceTube ,_W)
       Pipe_V3.SetColor(SALOMEDS.Color(0.6,0.6,0.6))
       Pipe_id=geompy.addToStudyInFather(V3,Pipe_V3,"Pipe_V3")
       gg.createAndDisplayGO(Pipe_id)
       gg.setDisplayMode(Pipe_id,1)

       List_ParaVis_Visualization.append(Pipe_V3)
       List_Visualization=[]
    

           
    try:
      print("Add V4")
      V4= geompy.MakeVector(P4,P5)
      #Liste.append([P4,"P4"])
      geompy.addToStudy(V4,"V4" )
      List_Visualization.append(V4)
        

      _C1 = geompy.MakeCircle(P4, V4,35.0)
      _C2 = geompy.MakeCircle(P4, V4,31.0)
      FaceTube = geompy.MakeFaceWires([_C1, _C2], 1)

            

    except:
       ERREUR=True
       print ("   =>ERROR BUILDING THE GEOMETRY!")

    try:
       V4M = smesh.Mesh(V4)
       Decoupage = V4M.Segment()
       Decoupage.NumberOfSegments(10)

       smesh.SetName(V4M,'V4')
       V4M.Compute()
       V4M.Group(P4)
       V4M.Group(P5)
       V4M.GroupOnGeom(V4)
    except:
       ERREUR=True
       print ("   =>ERROR WHILE GENERATING THE MESH!_")
       return
#    commandList.append(('CircularBeam', {'R': 35.0, 'Group_Maille': 'V4', 'EP': 4.0}))    
        


    if List_Visualization!=[]:
       _W=geompy.MakeWire(List_Visualization,1e-7)
       Pipe_V4 = geompy.MakePipe( FaceTube ,_W)
       Pipe_V4.SetColor(SALOMEDS.Color(0.6,0.6,0.6))
       Pipe_id=geompy.addToStudyInFather(V4,Pipe_V4,"Pipe_V4")
       gg.createAndDisplayGO(Pipe_id)
       gg.setDisplayMode(Pipe_id,1)

       List_ParaVis_Visualization.append(Pipe_V4)
       List_Visualization=[]
    

           
    try:
      print("Add V5")
      V5= geompy.MakeVector(P5,P6)
      #Liste.append([P5,"P5"])
      geompy.addToStudy(V5,"V5" )
      List_Visualization.append(V5)
        

      _C1 = geompy.MakeCircle(P5, V5,35.0)
      _C2 = geompy.MakeCircle(P5, V5,31.0)
      FaceTube = geompy.MakeFaceWires([_C1, _C2], 1)

            

    except:
       ERREUR=True
       print ("   =>ERROR BUILDING THE GEOMETRY!")

    try:
       V5M = smesh.Mesh(V5)
       Decoupage = V5M.Segment()
       Decoupage.NumberOfSegments(10)

       smesh.SetName(V5M,'V5')
       V5M.Compute()
       V5M.Group(P5)
       V5M.Group(P6)
       V5M.GroupOnGeom(V5)
    except:
       ERREUR=True
       print ("   =>ERROR WHILE GENERATING THE MESH!_")
       return
#    commandList.append(('CircularBeam', {'R': 35.0, 'Group_Maille': 'V5', 'EP': 4.0}))    
        


    if List_Visualization!=[]:
       _W=geompy.MakeWire(List_Visualization,1e-7)
       Pipe_V5 = geompy.MakePipe( FaceTube ,_W)
       Pipe_V5.SetColor(SALOMEDS.Color(0.6,0.6,0.6))
       Pipe_id=geompy.addToStudyInFather(V5,Pipe_V5,"Pipe_V5")
       gg.createAndDisplayGO(Pipe_id)
       gg.setDisplayMode(Pipe_id,1)

       List_ParaVis_Visualization.append(Pipe_V5)
       List_Visualization=[]
    

    try:
      print("Add  V_Bent6 ")
      Liste=[]
      V_Bent6 = geompy.MakeArcCenter(P6_7_center,P6,P7)
      geompy.addToStudy(V_Bent6,"V_Bent6")
      Liste.append([V_Bent6,"V_Bent6"])
      List_Visualization.append(V_Bent6)

         

      C1 = geompy.MakeCircle(P6,Vd2x_P6,35.0)
      C2 = geompy.MakeCircle(P6,Vd2x_P6,31.0)
      FaceTube = geompy.MakeFaceWires([C1, C2], 1)

            


    except:
       ERREUR=True
       print ("   =>ERROR BUILDING THE GEOMETRY!")

    try:
       V_Bent6M = smesh.Mesh(V_Bent6)
       Decoupage = V_Bent6M.Segment()
       Decoupage.NumberOfSegments(10)

       smesh.SetName(V_Bent6M,'V_Bent6')
       V_Bent6M.Compute()
       V_Bent6M.GroupOnFilter( SMESH.NODE,'P6', smesh.GetFilter( SMESH.NODE, SMESH.FT_LyingOnGeom,'=',P6))
       V_Bent6M.GroupOnFilter( SMESH.NODE,'P7', smesh.GetFilter( SMESH.NODE, SMESH.FT_LyingOnGeom,'=',P7))
       V_Bent6M.GroupOnGeom(V_Bent6)
    except:
       ERREUR=True
       print ("   =>ERROR WHILE GENERATING THE MESH!_")
       return
            


    if List_Visualization!=[]:
       _W=geompy.MakeWire(List_Visualization,1e-7)
       Pipe_V_Bent6 = geompy.MakePipe( FaceTube ,_W)
       Pipe_V_Bent6.SetColor(SALOMEDS.Color(0.6,0.6,0.6))
       Pipe_id=geompy.addToStudyInFather(V_Bent6,Pipe_V_Bent6,"Pipe_V_Bent6")
       gg.createAndDisplayGO(Pipe_id)
       gg.setDisplayMode(Pipe_id,1)

       List_ParaVis_Visualization.append(Pipe_V_Bent6)
       List_Visualization=[]
    

           
    try:
      print("Add V7")
      V7= geompy.MakeVector(P7,P8)
      #Liste.append([P7,"P7"])
      geompy.addToStudy(V7,"V7" )
      List_Visualization.append(V7)
        

      _C1 = geompy.MakeCircle(P7, V7,35.0)
      _C2 = geompy.MakeCircle(P7, V7,31.0)
      FaceTube = geompy.MakeFaceWires([_C1, _C2], 1)

            

    except:
       ERREUR=True
       print ("   =>ERROR BUILDING THE GEOMETRY!")

    try:
       V7M = smesh.Mesh(V7)
       Decoupage = V7M.Segment()
       Decoupage.NumberOfSegments(10)

       smesh.SetName(V7M,'V7')
       V7M.Compute()
       V7M.Group(P7)
       V7M.Group(P8)
       V7M.GroupOnGeom(V7)
    except:
       ERREUR=True
       print ("   =>ERROR WHILE GENERATING THE MESH!_")
       return
#    commandList.append(('CircularBeam', {'R': 35.0, 'Group_Maille': 'V7', 'EP': 4.0}))    
        


    if List_Visualization!=[]:
       _W=geompy.MakeWire(List_Visualization,1e-7)
       Pipe_V7 = geompy.MakePipe( FaceTube ,_W)
       Pipe_V7.SetColor(SALOMEDS.Color(0.6,0.6,0.6))
       Pipe_id=geompy.addToStudyInFather(V7,Pipe_V7,"Pipe_V7")
       gg.createAndDisplayGO(Pipe_id)
       gg.setDisplayMode(Pipe_id,1)

       List_ParaVis_Visualization.append(Pipe_V7)
       List_Visualization=[]
    

           
    try:
      print("Add V8")
      V8= geompy.MakeVector(P8,P9)
      #Liste.append([P8,"P8"])
      geompy.addToStudy(V8,"V8" )
      List_Visualization.append(V8)
        

      _C1 = geompy.MakeCircle(P8, V8,35.0)
      _C2 = geompy.MakeCircle(P8, V8,31.0)
      FaceTube = geompy.MakeFaceWires([_C1, _C2], 1)

            

    except:
       ERREUR=True
       print ("   =>ERROR BUILDING THE GEOMETRY!")

    try:
       V8M = smesh.Mesh(V8)
       Decoupage = V8M.Segment()
       Decoupage.NumberOfSegments(10)

       smesh.SetName(V8M,'V8')
       V8M.Compute()
       V8M.Group(P8)
       V8M.Group(P9)
       V8M.GroupOnGeom(V8)
    except:
       ERREUR=True
       print ("   =>ERROR WHILE GENERATING THE MESH!_")
       return
#    commandList.append(('CircularBeam', {'R': 35.0, 'Group_Maille': 'V8', 'EP': 4.0}))    
        


    if List_Visualization!=[]:
       _W=geompy.MakeWire(List_Visualization,1e-7)
       Pipe_V8 = geompy.MakePipe( FaceTube ,_W)
       Pipe_V8.SetColor(SALOMEDS.Color(0.6,0.6,0.6))
       Pipe_id=geompy.addToStudyInFather(V8,Pipe_V8,"Pipe_V8")
       gg.createAndDisplayGO(Pipe_id)
       gg.setDisplayMode(Pipe_id,1)

       List_ParaVis_Visualization.append(Pipe_V8)
       List_Visualization=[]
    

    try:  

        compound_paravis=geompy.MakeCompound(List_ParaVis_Visualization)
     #   compound_id=geompy.addToStudy(compound_paravis,'compound_paravis')
    except:
        print("No compound could be created",str(List_ParaVis_Visualization))
        
        
    #Creates the mesh compound
    if not(ERREUR):
        Completed_Mesh = smesh.Concatenate([V0M.GetMesh() , V1M.GetMesh() , V2M.GetMesh() , V3M.GetMesh() , 
           V4M.GetMesh() , V5M.GetMesh() , V_Bent6M.GetMesh() , V7M.GetMesh() , 
           V8M.GetMesh() ,SpringP3M.GetMesh() , ], 1, 0, 1e-05)
        coincident_nodes = Completed_Mesh.FindCoincidentNodes( 1e-05 )
        Completed_Mesh.MergeNodes(coincident_nodes)
        equal_elements = Completed_Mesh.FindEqualElements(Completed_Mesh)    
        Completed_Mesh.MergeElements(equal_elements)   
        smesh.SetName(Completed_Mesh.GetMesh(), 'Completed_Mesh')
        

#    elem = structElemManager.createElement(commandList)
#    elem.display()    



#    try:
#      Completed_Mesh.ExportMED( r'/home/jangeorg/TUBA/examples/000_Testing/001_TUBE_K_M_F/Completed_Mesh.mmed', 0)
#    except:
#      print ('ExportPartToMED() failed')


    try:    
        geompy.ExportVTK(compound_paravis, '/home/jangeorg/TUBA/examples/000_Testing/001_TUBE_K_M_F/compound_paravis.vtk', 0.001)     
    except:
      print ('ExportVTK of the visualization compound failed')



    if salome.sg.hasDesktop():
       salome.sg.updateObjBrowser(0)
    time2=time.time()
    dtime = time2 - time1
    print("------------------------")
    print("Duration of construction:"+str(round(dtime,2))+"s")



    import SalomePyQt
    sg = SalomePyQt.SalomePyQt()
    sg.activateModule("Geometry")
    if salome.sg.hasDesktop():
      salome.sg.updateObjBrowser(1)
    sg.activateModule("Aster")

    
Project()