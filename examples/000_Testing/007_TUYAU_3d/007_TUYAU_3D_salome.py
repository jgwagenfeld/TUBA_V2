#!/usr/bin/python 3
# -*- coding: iso-8859-1 -*-

import time
time1=time.time()
import sys
sys.path.append(' /home/jangeorg/TUBA/examples/000_Testing/007_TUYAU_3d ')

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
    

    P3= geompy.MakeVertex(2850.0, 0.0, 0.0 )
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


    P3_4_center= geompy.MakeVertex(2850.0, 9.184850993605149e-15, 150.0 )
    geompy.addToStudy(P3_4_center,"P3_4_center ")
    Vd2x_P3_4_center = geompy.MakeVectorDXDYDZ(1, 0, 0)
    P3_4_center_vd2x=    geompy.MakeTranslationVectorDistance(P3_4_center,Vd2x_P3_4_center,100)
    Vd2x_P3_4_center= geompy.MakeVector(P3_4_center,P3_4_center_vd2x)
    geompy.addToStudyInFather(P3_4_center,Vd2x_P3_4_center,"Vd2x_P3_4_center " )

    P4= geompy.MakeVertex(3000.0, 9.184850993605149e-15, 150.0 )
    geompy.addToStudy(P4,"P4 ")
    Vd2x_P4 = geompy.MakeVectorDXDYDZ(6.123233995736766e-17, 6.123233995736766e-17, 1.0)
    P4_vd2x=    geompy.MakeTranslationVectorDistance(P4,Vd2x_P4,100)
    Vd2x_P4= geompy.MakeVector(P4,P4_vd2x)
    geompy.addToStudyInFather(P4,Vd2x_P4,"Vd2x_P4 " )

    P5= geompy.MakeVertex(3000.0, 6.429395695523604e-14, 1050.0 )
    geompy.addToStudy(P5,"P5 ")
    Vd2x_P5 = geompy.MakeVectorDXDYDZ(6.123233995736766e-17, 6.123233995736766e-17, 1.0)
    P5_vd2x=    geompy.MakeTranslationVectorDistance(P5,Vd2x_P5,100)
    Vd2x_P5= geompy.MakeVector(P5,P5_vd2x)
    geompy.addToStudyInFather(P5,Vd2x_P5,"Vd2x_P5 " )

    a= geompy.MakeVertex(2900.0, 7.654042494670958e-14, 1150.0 )
    geompy.addToStudy(a,"a ")
    Vd2x_a = geompy.MakeVectorDXDYDZ(-1.0, 6.123233995736766e-17, 1.224646799147353e-16)
    a_vd2x=    geompy.MakeTranslationVectorDistance(a,Vd2x_a,100)
    Vd2x_a= geompy.MakeVector(a,a_vd2x)
    geompy.addToStudyInFather(a,Vd2x_a,"Vd2x_a " )

    b= geompy.MakeVertex(3000.0, 7.654042494670957e-14, 1250.0 )
    geompy.addToStudy(b,"b ")
    Vd2x_b = geompy.MakeVectorDXDYDZ(6.123233995736766e-17, 6.123233995736766e-17, 1.0)
    b_vd2x=    geompy.MakeTranslationVectorDistance(b,Vd2x_b,100)
    Vd2x_b= geompy.MakeVector(b,b_vd2x)
    geompy.addToStudyInFather(b,Vd2x_b,"Vd2x_b " )

    P8= geompy.MakeVertex(3000.0, 1.3777276490407722e-13, 2250.0 )
    geompy.addToStudy(P8,"P8 ")
    Vd2x_P8 = geompy.MakeVectorDXDYDZ(6.123233995736766e-17, 6.123233995736766e-17, 1.0)
    P8_vd2x=    geompy.MakeTranslationVectorDistance(P8,Vd2x_P8,100)
    Vd2x_P8= geompy.MakeVector(P8,P8_vd2x)
    geompy.addToStudyInFather(P8,Vd2x_P8,"Vd2x_P8 " )


    100.0
    Radius=35.0
        
    Pna=geompy.MakeVertexWithRef(P8,-100,0,0)
   
    V_def=geompy.MakeVector(P8,Pna)

    Deform_P8 = geompy.MakeCone(P8,V_def,1*Radius,0,100.0)

               
    Deform_P8.SetColor(SALOMEDS.Color(1,0.5,0))
    B_id=geompy.addToStudyInFather( P8, Deform_P8,'P8_Deform' )    


    List_ParaVis_Visualization.append(Deform_P8)
    gg.createAndDisplayGO(B_id)
    gg.setDisplayMode(B_id,1)
    

    P9= geompy.MakeVertex(1900.0, 1.3777276490407724e-13, 1150.0000000000002 )
    geompy.addToStudy(P9,"P9 ")
    Vd2x_P9 = geompy.MakeVectorDXDYDZ(-1.0, 6.123233995736766e-17, 1.224646799147353e-16)
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
#    commandList.append(('CircularBeam', {'R': 35.0, 'Group_Maille': 'V0', 'EP': 4.0}))    
        


    if List_Visualization!=[]:
       _W=geompy.MakeWire(List_Visualization,1e-7)
       Pipe_V0 = geompy.MakePipe( FaceTube ,_W)
       Pipe_V0.SetColor(SALOMEDS.Color(0.9,0.9,0.9))
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
       Quadratic_Mesh = Decoupage.QuadraticMesh()

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
       Pipe_V1.SetColor(SALOMEDS.Color(0.9,0.9,0.9))
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
#    commandList.append(('CircularBeam', {'R': 35.0, 'Group_Maille': 'V2', 'EP': 4.0}))    
        


    if List_Visualization!=[]:
       _W=geompy.MakeWire(List_Visualization,1e-7)
       Pipe_V2 = geompy.MakePipe( FaceTube ,_W)
       Pipe_V2.SetColor(SALOMEDS.Color(0.9,0.9,0.9))
       Pipe_id=geompy.addToStudyInFather(V2,Pipe_V2,"Pipe_V2")
       gg.createAndDisplayGO(Pipe_id)
       gg.setDisplayMode(Pipe_id,1)

       List_ParaVis_Visualization.append(Pipe_V2)
       List_Visualization=[]
    

    try:
      print("Add  V_Bent3 ")
      Liste=[]
      V_Bent3 = geompy.MakeArcCenter(P3_4_center,P3,P4)
      geompy.addToStudy(V_Bent3,"V_Bent3")
      Liste.append([V_Bent3,"V_Bent3"])
      List_Visualization.append(V_Bent3)

         

      C1 = geompy.MakeCircle(P3,Vd2x_P3,35.0)
      C2 = geompy.MakeCircle(P3,Vd2x_P3,31.0)
      FaceTube = geompy.MakeFaceWires([C1, C2], 1)

            


    except:
       ERREUR=True
       print ("   =>ERROR BUILDING THE GEOMETRY!")

    try:
       V_Bent3M = smesh.Mesh(V_Bent3)
       Decoupage = V_Bent3M.Segment()
       Decoupage.NumberOfSegments(10)
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
            


    if List_Visualization!=[]:
       _W=geompy.MakeWire(List_Visualization,1e-7)
       Pipe_V_Bent3 = geompy.MakePipe( FaceTube ,_W)
       Pipe_V_Bent3.SetColor(SALOMEDS.Color(0.9,0.9,0.9))
       Pipe_id=geompy.addToStudyInFather(V_Bent3,Pipe_V_Bent3,"Pipe_V_Bent3")
       gg.createAndDisplayGO(Pipe_id)
       gg.setDisplayMode(Pipe_id,1)

       List_ParaVis_Visualization.append(Pipe_V_Bent3)
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
       Quadratic_Mesh = Decoupage.QuadraticMesh()

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
       Pipe_V4.SetColor(SALOMEDS.Color(0.9,0.9,0.9))
       Pipe_id=geompy.addToStudyInFather(V4,Pipe_V4,"Pipe_V4")
       gg.createAndDisplayGO(Pipe_id)
       gg.setDisplayMode(Pipe_id,1)

       List_ParaVis_Visualization.append(Pipe_V4)
       List_Visualization=[]
    

    try:
        print("Add  TShape ")

        [TShape, Junction_1, Junction_2, Junction_3, Thickness,
         Circular_quarter_of_pipe, Circular_quarter_of_pipe_1,Main_pipe_half_length,
         Flange, Incident_pipe_half_length, Internal_faces] =            geompy.MakePipeTShape(31.0,4.0,100.0,16.0,4.0,100.0, True,P5,b,a)
                                  

        geompy.addToStudy( TShape, 'TShape' )
#        geompy.addToStudyInFather( TShape, Junction_1, 'Junction 1' )
#        geompy.addToStudyInFather( TShape, Junction_2, 'Junction 2' )
#        geompy.addToStudyInFather( TShape, Junction_3, 'Junction 3' )
#        geompy.addToStudyInFather( TShape, Thickness, 'Thickness' )
#        geompy.addToStudyInFather( TShape, Circular_quarter_of_pipe, 'Circular quarter of pipe' )
#        geompy.addToStudyInFather( TShape, Circular_quarter_of_pipe_1, 'Circular quarter of pipe' )
#        geompy.addToStudyInFather( TShape, Main_pipe_half_length, 'Main pipe half length' )
#        geompy.addToStudyInFather( TShape, Flange, 'Flange' )
#        geompy.addToStudyInFather( TShape, Incident_pipe_half_length, 'Incident pipe half length' )
#        geompy.addToStudyInFather(TShape, Internal_faces, 'Internal faces' )

        L_Start = geompy.GetShapesOnPlane(TShape,geompy.ShapeType["FACE"],Vd2x_P5,GEOM.ST_ON)
        TShapeStartFace = geompy.MakeCompound(L_Start)
        geompy.addToStudyInFather(TShape,TShapeStartFace,"TShapeStartFace")

        List_ParaVis_Visualization.append(TShape) 

        L_Incident = geompy.GetShapesOnPlane(TShape,geompy.ShapeType["FACE"],Vd2x_a,GEOM.ST_ON)
        TShapeIncidentFace = geompy.MakeCompound(L_Incident)
        geompy.addToStudyInFather(TShape,TShapeIncidentFace,"TShapeIncidentFace")
 
        
        L_End = geompy.GetShapesOnPlane(TShape,geompy.ShapeType["FACE"],Vd2x_b,GEOM.ST_ON)
        TShapeEndFace = geompy.MakeCompound(L_End)
        geompy.addToStudyInFather(TShape,TShapeEndFace,"TShapeEndFace")

    
    except:
       ERREUR=True
       print ("   =>ERROR BUILDING THE GEOMETRY!")

    ###
    ### SMESH component
    ###

    try:
        TShapeM = smesh.Mesh(TShape)
        Regular_1D = TShapeM.Segment()
        Nb_Segments_1 = Regular_1D.NumberOfSegments(4)
        Nb_Segments_1.SetDistrType( 0 )
        Quadrangle_2D = TShapeM.Quadrangle(algo=smeshBuilder.QUADRANGLE)
        Hexa_3D = TShapeM.Hexahedron(algo=smeshBuilder.Hexa)
        Nb_Segments_2 = smesh.CreateHypothesis('NumberOfSegments')
        Nb_Segments_2.SetNumberOfSegments( 4 )
        Nb_Segments_2.SetDistrType( 0 )
        status = TShapeM.AddHypothesis(Regular_1D,Thickness)
        status = TShapeM.AddHypothesis(Nb_Segments_2,Thickness)
        isDone = TShapeM.Compute()
        [ Sub_mesh_1 ] = TShapeM.GetMesh().GetSubMeshes()
        Sub_mesh_1 = TShapeM.GetSubMesh( Thickness, 'Sub-mesh_1' )


        ## Set names of Mesh objects
        smesh.SetName(TShapeM,'TShape')
        TShapeM.Compute()
        TShapeM.Group(P5)
        TShapeM.Group(b)
        TShapeM.Group(a)
        
        TShapeM.GroupOnGeom(TShape)
        TShapeM.GroupOnGeom(TShapeStartFace)
        TShapeM.GroupOnGeom(TShapeIncidentFace)
        TShapeM.GroupOnGeom(TShapeEndFace)

        smesh.SetName(Regular_1D.GetAlgorithm(), 'Regular_1D')
        smesh.SetName(Hexa_3D.GetAlgorithm(), 'Hexa_3D')
        smesh.SetName(Quadrangle_2D.GetAlgorithm(), 'Quadrangle_2D')
        smesh.SetName(Nb_Segments_2, 'Nb. Segments_2')
        smesh.SetName(Nb_Segments_1, 'Nb. Segments_1')
        smesh.SetName(TShapeM.GetMesh()," TShapeM")
        smesh.SetName(Sub_mesh_1, 'Sub-mesh_1')
    except:
       ERREUR=True
       print ("   =>ERROR BUILDING THE MESH!")
       for x in Liste :
           geompy.addToStudy(x[0],x[1])
            


    if List_Visualization!=[]:
       _W=geompy.MakeWire(List_Visualization,1e-7)
       Pipe_TShape = geompy.MakePipe( FaceTube ,_W)
       Pipe_TShape.SetColor(SALOMEDS.Color(0.5,0.8,0.8))
       Pipe_id=geompy.addToStudyInFather(TShape,Pipe_TShape,"Pipe_TShape")
       gg.createAndDisplayGO(Pipe_id)
       gg.setDisplayMode(Pipe_id,1)

       List_ParaVis_Visualization.append(Pipe_TShape)
       List_Visualization=[]
    

           
    try:
      print("Add V6")
      V6= geompy.MakeVector(b,P8)
      #Liste.append([b,"b"])
      geompy.addToStudy(V6,"V6" )
      List_Visualization.append(V6)
        

      _C1 = geompy.MakeCircle(b, V6,35.0)
      _C2 = geompy.MakeCircle(b, V6,31.0)
      FaceTube = geompy.MakeFaceWires([_C1, _C2], 1)

            

    except:
       ERREUR=True
       print ("   =>ERROR BUILDING THE GEOMETRY!")

    try:
       V6M = smesh.Mesh(V6)
       Decoupage = V6M.Segment()
       Decoupage.NumberOfSegments(10)
       Quadratic_Mesh = Decoupage.QuadraticMesh()

       smesh.SetName(V6M,'V6')
       V6M.Compute()
       V6M.Group(b)
       V6M.Group(P8)
       V6M.GroupOnGeom(V6)
    except:
       ERREUR=True
       print ("   =>ERROR WHILE GENERATING THE MESH!_")
       return
#    commandList.append(('CircularBeam', {'R': 35.0, 'Group_Maille': 'V6', 'EP': 4.0}))    
        


    if List_Visualization!=[]:
       _W=geompy.MakeWire(List_Visualization,1e-7)
       Pipe_V6 = geompy.MakePipe( FaceTube ,_W)
       Pipe_V6.SetColor(SALOMEDS.Color(0.9,0.9,0.9))
       Pipe_id=geompy.addToStudyInFather(V6,Pipe_V6,"Pipe_V6")
       gg.createAndDisplayGO(Pipe_id)
       gg.setDisplayMode(Pipe_id,1)

       List_ParaVis_Visualization.append(Pipe_V6)
       List_Visualization=[]
    

           
    try:
      print("Add V7")
      V7= geompy.MakeVector(a,P9)
      #Liste.append([a,"a"])
      geompy.addToStudy(V7,"V7" )
      List_Visualization.append(V7)
        

      _C1 = geompy.MakeCircle(a, V7,20)
      _C2 = geompy.MakeCircle(a, V7,16.0)
      FaceTube = geompy.MakeFaceWires([_C1, _C2], 1)

            

    except:
       ERREUR=True
       print ("   =>ERROR BUILDING THE GEOMETRY!")

    try:
       V7M = smesh.Mesh(V7)
       Decoupage = V7M.Segment()
       Decoupage.NumberOfSegments(10)
       Quadratic_Mesh = Decoupage.QuadraticMesh()

       smesh.SetName(V7M,'V7')
       V7M.Compute()
       V7M.Group(a)
       V7M.Group(P9)
       V7M.GroupOnGeom(V7)
    except:
       ERREUR=True
       print ("   =>ERROR WHILE GENERATING THE MESH!_")
       return
#    commandList.append(('CircularBeam', {'R': 20, 'Group_Maille': 'V7', 'EP': 4.0}))    
        


    if List_Visualization!=[]:
       _W=geompy.MakeWire(List_Visualization,1e-7)
       Pipe_V7 = geompy.MakePipe( FaceTube ,_W)
       Pipe_V7.SetColor(SALOMEDS.Color(0.9,0.9,0.9))
       Pipe_id=geompy.addToStudyInFather(V7,Pipe_V7,"Pipe_V7")
       gg.createAndDisplayGO(Pipe_id)
       gg.setDisplayMode(Pipe_id,1)

       List_ParaVis_Visualization.append(Pipe_V7)
       List_Visualization=[]
    

    try:  

        compound_paravis=geompy.MakeCompound(List_ParaVis_Visualization)
     #   compound_id=geompy.addToStudy(compound_paravis,'compound_paravis')
    except:
        print("No compound could be created",str(List_ParaVis_Visualization))
        
        
    #Creates the mesh compound
    if not(ERREUR):
        Completed_Mesh = smesh.Concatenate([V0M.GetMesh() , V1M.GetMesh() , V2M.GetMesh() , 
           V_Bent3M.GetMesh() , V4M.GetMesh() , TShapeM.GetMesh() , V6M.GetMesh() , 
           V7M.GetMesh() ,SpringP3M.GetMesh() , ], 1, 0, 1e-05)
        coincident_nodes = Completed_Mesh.FindCoincidentNodes( 1e-05 )
        Completed_Mesh.MergeNodes(coincident_nodes)
        equal_elements = Completed_Mesh.FindEqualElements(Completed_Mesh)    
        Completed_Mesh.MergeElements(equal_elements)   
        smesh.SetName(Completed_Mesh.GetMesh(), 'Completed_Mesh')
        

#    elem = structElemManager.createElement(commandList)
#    elem.display()    



#    try:
#      Completed_Mesh.ExportMED( r'/home/jangeorg/TUBA/examples/000_Testing/007_TUYAU_3d/Completed_Mesh.mmed', 0)
#    except:
#      print ('ExportPartToMED() failed')


    try:    
        geompy.ExportVTK(compound_paravis, '/home/jangeorg/TUBA/examples/000_Testing/007_TUYAU_3d/compound_paravis.vtk', 0.001)     
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