#!/usr/bin/python 3
# -*- coding: iso-8859-1 -*-

import time
time1=time.time()
import sys
sys.path.append(' /home/jangeorg/TUBA/tutorials/007_Pyramide ')

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
    A= geompy.MakeVertex(0, 0, 0 )
    geompy.addToStudy(A,"A ")
    geompy.PutToFolder(A, Folder_Points)

    Vd1x_A = geompy.MakeVectorDXDYDZ(0, 1, 0)
    A_vd1x=    geompy.MakeTranslationVectorDistance(A,Vd1x_A,1000)
    Vd1x_A= geompy.MakeVector(A,A_vd1x)
    geompy.addToStudyInFather(A,Vd1x_A,"Vd1x_A " )
       
    Vd2x_A = geompy.MakeVectorDXDYDZ(-0.23570226039551587, -0.23570226039551587, -0.9428090415820635)
    A_vd2x=    geompy.MakeTranslationVectorDistance(A,Vd2x_A,1000)
    Vd2x_A= geompy.MakeVector(A,A_vd2x)
    geompy.addToStudyInFather(A,Vd2x_A,"Vd2x_A " )

    # Visualize a support(restriction DOF) at point A
    #---------------------------------------------               
    A_BLOCK_xyzrxryrz=geompy.MakeBox(120,120,120,-120,-120,-120)	
    A_BLOCK_xyzrxryrz.SetColor(SALOMEDS.Color(1,1,0))
    A_BLOCK_xyzrxryrz_id=geompy.addToStudyInFather( A, A_BLOCK_xyzrxryrz,'A_BLOCK_xyzrxryrz' )
 #   B_id=geompy.addToStudy(A_BLOCK_xyzrxryrz,'A_BLOCK_xyzrxryrz' )
    
    List_ParaVis_Visualization.append(A_BLOCK_xyzrxryrz)
    objId = geompy.getObjectID(A_BLOCK_xyzrxryrz)    
    gg.createAndDisplayGO(objId)
    gg.setDisplayMode(objId,1)
    gg.setColor(objId,218,165,31)
  
    


##_points##  
    P1= geompy.MakeVertex(1000, 0, 0 )
    geompy.addToStudy(P1,"P1 ")
    geompy.PutToFolder(P1, Folder_Points)

    Vd1x_P1 = geompy.MakeVectorDXDYDZ(-0.23570226039551587, -0.23570226039551587, -0.9428090415820635)
    P1_vd1x=    geompy.MakeTranslationVectorDistance(P1,Vd1x_P1,1000)
    Vd1x_P1= geompy.MakeVector(P1,P1_vd1x)
    geompy.addToStudyInFather(P1,Vd1x_P1,"Vd1x_P1 " )
       
    Vd2x_P1 = geompy.MakeVectorDXDYDZ(-0.23570226039551587, 0.23570226039551587, 0.9428090415820635)
    P1_vd2x=    geompy.MakeTranslationVectorDistance(P1,Vd2x_P1,1000)
    Vd2x_P1= geompy.MakeVector(P1,P1_vd2x)
    geompy.addToStudyInFather(P1,Vd2x_P1,"Vd2x_P1 " )
        
 
    Radius=60

    Pna=geompy.MakeVertexWithRef(P1,0,0,180)
    Pnb=geompy.MakeVertexWithRef(P1,0,0,120)  
    Vp=geompy.MakeVector(Pna,Pnb)  
    Cone1 = geompy.MakeCone(Pna,Vp,Radius,0,2*Radius)

   
    P2a=geompy.MakeVertexWithRef(P1,0,0,-180)    
    P2b=geompy.MakeVertexWithRef(P1,0,0,-120)    
    Vm=geompy.MakeVector(P2a,P2b)  
    Cone2 = geompy.MakeCone(P2a,Vm,Radius,0,2*Radius)
    
    BLOCK_z=geompy.MakeCompound([Cone1,Cone2])
    BLOCK_z.SetColor(SALOMEDS.Color(1,1,0))
    B_id=geompy.addToStudyInFather( P1, BLOCK_z,'P1_BLOCK_z' )    

    List_ParaVis_Visualization.append(BLOCK_z)
    gg.createAndDisplayGO(B_id)
    gg.setDisplayMode(B_id,1)
    


##_points##  
    P2= geompy.MakeVertex(1000, 1000, 0 )
    geompy.addToStudy(P2,"P2 ")
    geompy.PutToFolder(P2, Folder_Points)

    Vd1x_P2 = geompy.MakeVectorDXDYDZ(-0.23570226039551587, 0.23570226039551587, 0.9428090415820635)
    P2_vd1x=    geompy.MakeTranslationVectorDistance(P2,Vd1x_P2,1000)
    Vd1x_P2= geompy.MakeVector(P2,P2_vd1x)
    geompy.addToStudyInFather(P2,Vd1x_P2,"Vd1x_P2 " )
       
    Vd2x_P2 = geompy.MakeVectorDXDYDZ(-0.23570226039551587, -0.23570226039551587, 0.9428090415820635)
    P2_vd2x=    geompy.MakeTranslationVectorDistance(P2,Vd2x_P2,1000)
    Vd2x_P2= geompy.MakeVector(P2,P2_vd2x)
    geompy.addToStudyInFather(P2,Vd2x_P2,"Vd2x_P2 " )
        
 
    Radius=60

    Pna=geompy.MakeVertexWithRef(P2,0,0,180)
    Pnb=geompy.MakeVertexWithRef(P2,0,0,120)  
    Vp=geompy.MakeVector(Pna,Pnb)  
    Cone1 = geompy.MakeCone(Pna,Vp,Radius,0,2*Radius)

   
    P2a=geompy.MakeVertexWithRef(P2,0,0,-180)    
    P2b=geompy.MakeVertexWithRef(P2,0,0,-120)    
    Vm=geompy.MakeVector(P2a,P2b)  
    Cone2 = geompy.MakeCone(P2a,Vm,Radius,0,2*Radius)
    
    BLOCK_z=geompy.MakeCompound([Cone1,Cone2])
    BLOCK_z.SetColor(SALOMEDS.Color(1,1,0))
    B_id=geompy.addToStudyInFather( P2, BLOCK_z,'P2_BLOCK_z' )    

    List_ParaVis_Visualization.append(BLOCK_z)
    gg.createAndDisplayGO(B_id)
    gg.setDisplayMode(B_id,1)
    


##_points##  
    P3= geompy.MakeVertex(0, 1000, 0 )
    geompy.addToStudy(P3,"P3 ")
    geompy.PutToFolder(P3, Folder_Points)

    Vd1x_P3 = geompy.MakeVectorDXDYDZ(-0.23570226039551587, -0.23570226039551587, 0.9428090415820635)
    P3_vd1x=    geompy.MakeTranslationVectorDistance(P3,Vd1x_P3,1000)
    Vd1x_P3= geompy.MakeVector(P3,P3_vd1x)
    geompy.addToStudyInFather(P3,Vd1x_P3,"Vd1x_P3 " )
       
    Vd2x_P3 = geompy.MakeVectorDXDYDZ(0.23570226039551587, -0.23570226039551587, 0.9428090415820635)
    P3_vd2x=    geompy.MakeTranslationVectorDistance(P3,Vd2x_P3,1000)
    Vd2x_P3= geompy.MakeVector(P3,P3_vd2x)
    geompy.addToStudyInFather(P3,Vd2x_P3,"Vd2x_P3 " )
        
 
    Radius=60

    Pna=geompy.MakeVertexWithRef(P3,0,0,180)
    Pnb=geompy.MakeVertexWithRef(P3,0,0,120)  
    Vp=geompy.MakeVector(Pna,Pnb)  
    Cone1 = geompy.MakeCone(Pna,Vp,Radius,0,2*Radius)

   
    P2a=geompy.MakeVertexWithRef(P3,0,0,-180)    
    P2b=geompy.MakeVertexWithRef(P3,0,0,-120)    
    Vm=geompy.MakeVector(P2a,P2b)  
    Cone2 = geompy.MakeCone(P2a,Vm,Radius,0,2*Radius)
    
    BLOCK_z=geompy.MakeCompound([Cone1,Cone2])
    BLOCK_z.SetColor(SALOMEDS.Color(1,1,0))
    B_id=geompy.addToStudyInFather( P3, BLOCK_z,'P3_BLOCK_z' )    

    List_ParaVis_Visualization.append(BLOCK_z)
    gg.createAndDisplayGO(B_id)
    gg.setDisplayMode(B_id,1)
    


##_points##  
    top= geompy.MakeVertex(500, 500, 2000 )
    geompy.addToStudy(top,"top ")
    geompy.PutToFolder(top, Folder_Points)

    Vd1x_top = geompy.MakeVectorDXDYDZ(1.0, 0.0, 0.0)
    top_vd1x=    geompy.MakeTranslationVectorDistance(top,Vd1x_top,1000)
    Vd1x_top= geompy.MakeVector(top,top_vd1x)
    geompy.addToStudyInFather(top,Vd1x_top,"Vd1x_top " )
       
    Vd2x_top = geompy.MakeVectorDXDYDZ(0.23570226039551587, -0.23570226039551587, 0.9428090415820635)
    top_vd2x=    geompy.MakeTranslationVectorDistance(top,Vd2x_top,1000)
    Vd2x_top= geompy.MakeVector(top,top_vd2x)
    geompy.addToStudyInFather(top,Vd2x_top,"Vd2x_top " )

    # Visualize a forces at point top
    #---------------------------------------------           
    Radius=30
        
    Pna=geompy.MakeVertexWithRef(top,Radius*0.0,Radius*0.0,Radius*-1.0)
    Pnb=geompy.MakeVertexWithRef(top,1.5*Radius*0.0,1.5*Radius*0.0,1.5*Radius*-1.0)
    Pnc=geompy.MakeVertexWithRef(top,10*Radius*0.0,10*Radius*0.0,10*Radius*-1.0) 
 
    V_force=geompy.MakeVector(Pna,Pnb)     

    Tip = geompy.MakeCone(Pnc,V_force,2*Radius,0,4*Radius)           
    Shaft = geompy.MakeCylinder(top, V_force,0.5*Radius, 10*Radius)
    Arrow = geompy.MakeCompound([Tip,Shaft])  
               
    Arrow.SetColor(SALOMEDS.Color(1,0,0))
    B_id=geompy.addToStudyInFather( top, Arrow,'top_Arrow' )    

    List_ParaVis_Visualization.append(Arrow)
    gg.createAndDisplayGO(B_id)
    gg.setDisplayMode(B_id,1)
            

##_vector_rectangular_1D##
    ### geometry generation for  V0 ###
    #----------------------------------------------------
    print("Add: V0")
    V0= geompy.MakeVector(P3,A)
    geompy.addToStudy(V0,"V0" )
    geompy.PutToFolder(V0, Folder_Vectors)

    _W1 = geompy.MakeSketcher("Sketcher: F 30 30: TT -30 30: TT -30 -30: TT 30 -30: WW",
          [   0,1000,0,
              0.0,-1.0,0.0,
              -0.0,0.0,1.0])

    _W2 = geompy.MakeSketcher("Sketcher: F 27 27: TT -27 27: TT -27 -27: TT 27 -27: WW",
          [   0,1000,0,
              0.0,-1.0,0.0,
              -0.0,0.0,1.0])
      
    _W1  = geompy.MakeRotation(_W1,V0, 0*math.pi/180.0)
    _W2  = geompy.MakeRotation(_W2,V0, 0*math.pi/180.0)      
    FaceTube= geompy.MakeFaceWires([_W1, _W2], 1)   
            

    ### mesh generation for  V0 ###
    #----------------------------------------------------    

    V0M = smesh.Mesh(V0)
    Decoupage = V0M.Segment()
    Decoupage.NumberOfSegments(10)

    smesh.SetName(V0M,'V0')
    V0M.Compute()
    V0M.Group(P3)
    V0M.Group(A)
    V0M.GroupOnGeom(V0)

    structElemList.append(('Orientation', {'MeshGroups': 'V0',
                                        'ANGL_VRIL': 0}),)
    structElemList.append(('RectangularBeam', {'HY1': 60,'HY2': 60,
                                                'HZ1': 60,'HZ2': 60,
                                                'EPY1': 3,'EPY2': 3,    
                                                'EPZ1': 3,'EPZ2': 3,    
                                                'MeshGroups': 'V0'}))

    List_ParaVis_Visualization.append("Beam_V0")
        

##_vector_rectangular_1D##
    ### geometry generation for  V1 ###
    #----------------------------------------------------
    print("Add: V1")
    V1= geompy.MakeVector(P1,A)
    geompy.addToStudy(V1,"V1" )
    geompy.PutToFolder(V1, Folder_Vectors)

    _W1 = geompy.MakeSketcher("Sketcher: F 30 30: TT -30 30: TT -30 -30: TT 30 -30: WW",
          [   1000,0,0,
              -1.0,0.0,0.0,
              0.0,0.0,1.0])

    _W2 = geompy.MakeSketcher("Sketcher: F 27 27: TT -27 27: TT -27 -27: TT 27 -27: WW",
          [   1000,0,0,
              -1.0,0.0,0.0,
              0.0,0.0,1.0])
      
    _W1  = geompy.MakeRotation(_W1,V1, 0*math.pi/180.0)
    _W2  = geompy.MakeRotation(_W2,V1, 0*math.pi/180.0)      
    FaceTube= geompy.MakeFaceWires([_W1, _W2], 1)   
            

    ### mesh generation for  V1 ###
    #----------------------------------------------------    

    V1M = smesh.Mesh(V1)
    Decoupage = V1M.Segment()
    Decoupage.NumberOfSegments(10)

    smesh.SetName(V1M,'V1')
    V1M.Compute()
    V1M.Group(P1)
    V1M.Group(A)
    V1M.GroupOnGeom(V1)

    structElemList.append(('Orientation', {'MeshGroups': 'V1',
                                        'ANGL_VRIL': 0}),)
    structElemList.append(('RectangularBeam', {'HY1': 60,'HY2': 60,
                                                'HZ1': 60,'HZ2': 60,
                                                'EPY1': 3,'EPY2': 3,    
                                                'EPZ1': 3,'EPZ2': 3,    
                                                'MeshGroups': 'V1'}))

    List_ParaVis_Visualization.append("Beam_V1")
        

##_vector_rectangular_1D##
    ### geometry generation for  V2 ###
    #----------------------------------------------------
    print("Add: V2")
    V2= geompy.MakeVector(P2,P1)
    geompy.addToStudy(V2,"V2" )
    geompy.PutToFolder(V2, Folder_Vectors)

    _W1 = geompy.MakeSketcher("Sketcher: F 30 30: TT -30 30: TT -30 -30: TT 30 -30: WW",
          [   1000,1000,0,
              0.0,-1.0,0.0,
              -0.0,-0.0,-1.0])

    _W2 = geompy.MakeSketcher("Sketcher: F 27 27: TT -27 27: TT -27 -27: TT 27 -27: WW",
          [   1000,1000,0,
              0.0,-1.0,0.0,
              -0.0,-0.0,-1.0])
      
    _W1  = geompy.MakeRotation(_W1,V2, 0*math.pi/180.0)
    _W2  = geompy.MakeRotation(_W2,V2, 0*math.pi/180.0)      
    FaceTube= geompy.MakeFaceWires([_W1, _W2], 1)   
            

    ### mesh generation for  V2 ###
    #----------------------------------------------------    

    V2M = smesh.Mesh(V2)
    Decoupage = V2M.Segment()
    Decoupage.NumberOfSegments(10)

    smesh.SetName(V2M,'V2')
    V2M.Compute()
    V2M.Group(P2)
    V2M.Group(P1)
    V2M.GroupOnGeom(V2)

    structElemList.append(('Orientation', {'MeshGroups': 'V2',
                                        'ANGL_VRIL': 0}),)
    structElemList.append(('RectangularBeam', {'HY1': 60,'HY2': 60,
                                                'HZ1': 60,'HZ2': 60,
                                                'EPY1': 3,'EPY2': 3,    
                                                'EPZ1': 3,'EPZ2': 3,    
                                                'MeshGroups': 'V2'}))

    List_ParaVis_Visualization.append("Beam_V2")
        

##_vector_rectangular_1D##
    ### geometry generation for  V3 ###
    #----------------------------------------------------
    print("Add: V3")
    V3= geompy.MakeVector(P3,P2)
    geompy.addToStudy(V3,"V3" )
    geompy.PutToFolder(V3, Folder_Vectors)

    _W1 = geompy.MakeSketcher("Sketcher: F 30 30: TT -30 30: TT -30 -30: TT 30 -30: WW",
          [   0,1000,0,
              1.0,0.0,0.0,
              0.0,0.0,-1.0])

    _W2 = geompy.MakeSketcher("Sketcher: F 27 27: TT -27 27: TT -27 -27: TT 27 -27: WW",
          [   0,1000,0,
              1.0,0.0,0.0,
              0.0,0.0,-1.0])
      
    _W1  = geompy.MakeRotation(_W1,V3, 0*math.pi/180.0)
    _W2  = geompy.MakeRotation(_W2,V3, 0*math.pi/180.0)      
    FaceTube= geompy.MakeFaceWires([_W1, _W2], 1)   
            

    ### mesh generation for  V3 ###
    #----------------------------------------------------    

    V3M = smesh.Mesh(V3)
    Decoupage = V3M.Segment()
    Decoupage.NumberOfSegments(10)

    smesh.SetName(V3M,'V3')
    V3M.Compute()
    V3M.Group(P3)
    V3M.Group(P2)
    V3M.GroupOnGeom(V3)

    structElemList.append(('Orientation', {'MeshGroups': 'V3',
                                        'ANGL_VRIL': 0}),)
    structElemList.append(('RectangularBeam', {'HY1': 60,'HY2': 60,
                                                'HZ1': 60,'HZ2': 60,
                                                'EPY1': 3,'EPY2': 3,    
                                                'EPZ1': 3,'EPZ2': 3,    
                                                'MeshGroups': 'V3'}))

    List_ParaVis_Visualization.append("Beam_V3")
        

##_vector_rectangular_1D##
    ### geometry generation for  V4 ###
    #----------------------------------------------------
    print("Add: V4")
    V4= geompy.MakeVector(top,A)
    geompy.addToStudy(V4,"V4" )
    geompy.PutToFolder(V4, Folder_Vectors)

    _W1 = geompy.MakeSketcher("Sketcher: F 15 15: TT -15 15: TT -15 -15: TT 15 -15: WW",
          [   500,500,2000,
              -0.235702260396,-0.235702260396,-0.942809041582,
              0.0,-0.942809041582,0.235702260396])

    _W2 = geompy.MakeSketcher("Sketcher: F 12 12: TT -12 12: TT -12 -12: TT 12 -12: WW",
          [   500,500,2000,
              -0.235702260396,-0.235702260396,-0.942809041582,
              0.0,-0.942809041582,0.235702260396])
      
    _W1  = geompy.MakeRotation(_W1,V4, 0*math.pi/180.0)
    _W2  = geompy.MakeRotation(_W2,V4, 0*math.pi/180.0)      
    FaceTube= geompy.MakeFaceWires([_W1, _W2], 1)   
            

    ### mesh generation for  V4 ###
    #----------------------------------------------------    

    V4M = smesh.Mesh(V4)
    Decoupage = V4M.Segment()
    Decoupage.NumberOfSegments(10)

    smesh.SetName(V4M,'V4')
    V4M.Compute()
    V4M.Group(top)
    V4M.Group(A)
    V4M.GroupOnGeom(V4)

    structElemList.append(('Orientation', {'MeshGroups': 'V4',
                                        'ANGL_VRIL': 0}),)
    structElemList.append(('RectangularBeam', {'HY1': 30,'HY2': 30,
                                                'HZ1': 30,'HZ2': 30,
                                                'EPY1': 3,'EPY2': 3,    
                                                'EPZ1': 3,'EPZ2': 3,    
                                                'MeshGroups': 'V4'}))

    List_ParaVis_Visualization.append("Beam_V4")
        

##_vector_rectangular_1D##
    ### geometry generation for  V5 ###
    #----------------------------------------------------
    print("Add: V5")
    V5= geompy.MakeVector(P1,top)
    geompy.addToStudy(V5,"V5" )
    geompy.PutToFolder(V5, Folder_Vectors)

    _W1 = geompy.MakeSketcher("Sketcher: F 15 15: TT -15 15: TT -15 -15: TT 15 -15: WW",
          [   1000,0,0,
              -0.235702260396,0.235702260396,0.942809041582,
              0.0,-0.444444444444,0.111111111111])

    _W2 = geompy.MakeSketcher("Sketcher: F 12 12: TT -12 12: TT -12 -12: TT 12 -12: WW",
          [   1000,0,0,
              -0.235702260396,0.235702260396,0.942809041582,
              0.0,-0.444444444444,0.111111111111])
      
    _W1  = geompy.MakeRotation(_W1,V5, 0*math.pi/180.0)
    _W2  = geompy.MakeRotation(_W2,V5, 0*math.pi/180.0)      
    FaceTube= geompy.MakeFaceWires([_W1, _W2], 1)   
            

    ### mesh generation for  V5 ###
    #----------------------------------------------------    

    V5M = smesh.Mesh(V5)
    Decoupage = V5M.Segment()
    Decoupage.NumberOfSegments(10)

    smesh.SetName(V5M,'V5')
    V5M.Compute()
    V5M.Group(P1)
    V5M.Group(top)
    V5M.GroupOnGeom(V5)

    structElemList.append(('Orientation', {'MeshGroups': 'V5',
                                        'ANGL_VRIL': 0}),)
    structElemList.append(('RectangularBeam', {'HY1': 30,'HY2': 30,
                                                'HZ1': 30,'HZ2': 30,
                                                'EPY1': 3,'EPY2': 3,    
                                                'EPZ1': 3,'EPZ2': 3,    
                                                'MeshGroups': 'V5'}))

    List_ParaVis_Visualization.append("Beam_V5")
        

##_vector_rectangular_1D##
    ### geometry generation for  V6 ###
    #----------------------------------------------------
    print("Add: V6")
    V6= geompy.MakeVector(P2,top)
    geompy.addToStudy(V6,"V6" )
    geompy.PutToFolder(V6, Folder_Vectors)

    _W1 = geompy.MakeSketcher("Sketcher: F 15 15: TT -15 15: TT -15 -15: TT 15 -15: WW",
          [   1000,1000,0,
              -0.235702260396,-0.235702260396,0.942809041582,
              -0.444444444444,0.0,-0.111111111111])

    _W2 = geompy.MakeSketcher("Sketcher: F 12 12: TT -12 12: TT -12 -12: TT 12 -12: WW",
          [   1000,1000,0,
              -0.235702260396,-0.235702260396,0.942809041582,
              -0.444444444444,0.0,-0.111111111111])
      
    _W1  = geompy.MakeRotation(_W1,V6, 0*math.pi/180.0)
    _W2  = geompy.MakeRotation(_W2,V6, 0*math.pi/180.0)      
    FaceTube= geompy.MakeFaceWires([_W1, _W2], 1)   
            

    ### mesh generation for  V6 ###
    #----------------------------------------------------    

    V6M = smesh.Mesh(V6)
    Decoupage = V6M.Segment()
    Decoupage.NumberOfSegments(10)

    smesh.SetName(V6M,'V6')
    V6M.Compute()
    V6M.Group(P2)
    V6M.Group(top)
    V6M.GroupOnGeom(V6)

    structElemList.append(('Orientation', {'MeshGroups': 'V6',
                                        'ANGL_VRIL': 0}),)
    structElemList.append(('RectangularBeam', {'HY1': 30,'HY2': 30,
                                                'HZ1': 30,'HZ2': 30,
                                                'EPY1': 3,'EPY2': 3,    
                                                'EPZ1': 3,'EPZ2': 3,    
                                                'MeshGroups': 'V6'}))

    List_ParaVis_Visualization.append("Beam_V6")
        

##_vector_rectangular_1D##
    ### geometry generation for  V7 ###
    #----------------------------------------------------
    print("Add: V7")
    V7= geompy.MakeVector(P3,top)
    geompy.addToStudy(V7,"V7" )
    geompy.PutToFolder(V7, Folder_Vectors)

    _W1 = geompy.MakeSketcher("Sketcher: F 15 15: TT -15 15: TT -15 -15: TT 15 -15: WW",
          [   0,1000,0,
              0.235702260396,-0.235702260396,0.942809041582,
              0.0,-0.444444444444,-0.111111111111])

    _W2 = geompy.MakeSketcher("Sketcher: F 12 12: TT -12 12: TT -12 -12: TT 12 -12: WW",
          [   0,1000,0,
              0.235702260396,-0.235702260396,0.942809041582,
              0.0,-0.444444444444,-0.111111111111])
      
    _W1  = geompy.MakeRotation(_W1,V7, 0*math.pi/180.0)
    _W2  = geompy.MakeRotation(_W2,V7, 0*math.pi/180.0)      
    FaceTube= geompy.MakeFaceWires([_W1, _W2], 1)   
            

    ### mesh generation for  V7 ###
    #----------------------------------------------------    

    V7M = smesh.Mesh(V7)
    Decoupage = V7M.Segment()
    Decoupage.NumberOfSegments(10)

    smesh.SetName(V7M,'V7')
    V7M.Compute()
    V7M.Group(P3)
    V7M.Group(top)
    V7M.GroupOnGeom(V7)

    structElemList.append(('Orientation', {'MeshGroups': 'V7',
                                        'ANGL_VRIL': 0}),)
    structElemList.append(('RectangularBeam', {'HY1': 30,'HY2': 30,
                                                'HZ1': 30,'HZ2': 30,
                                                'EPY1': 3,'EPY2': 3,    
                                                'EPZ1': 3,'EPZ2': 3,    
                                                'MeshGroups': 'V7'}))

    List_ParaVis_Visualization.append("Beam_V7")
        

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

    Completed_Mesh = smesh.Concatenate([V0M.GetMesh() , V1M.GetMesh() , V2M.GetMesh() , V3M.GetMesh() , 
           V4M.GetMesh() , V5M.GetMesh() , V6M.GetMesh() , V7M.GetMesh() ,], 1, 0, 1e-05)
    coincident_nodes = Completed_Mesh.FindCoincidentNodes( 1e-05 )
    Completed_Mesh.MergeNodes(coincident_nodes)
    equal_elements = Completed_Mesh.FindEqualElements(Completed_Mesh)    
    Completed_Mesh.MergeElements(equal_elements)   
    smesh.SetName(Completed_Mesh.GetMesh(), 'Completed_Mesh')
        

                               
##_finalize##                
    #exports the created mesh compound 
    try:
        Completed_Mesh.ExportMED( r'/home/jangeorg/TUBA/tutorials/007_Pyramide/Completed_Mesh.mmed', 0)
    except:
        print ('ExportPartToMED() failed')


    #exports visualizations (structural elements, forces, etc) as a grouped geometry to be used in Paravis
    try:    
        geompy.ExportVTK(compound_paravis, '/home/jangeorg/TUBA/tutorials/007_Pyramide/compound_paravis.vtk', 0.001)     
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