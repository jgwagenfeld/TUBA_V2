#!/usr/bin/python 3
# -*- coding: iso-8859-1 -*-

import time
time1=time.time()
import sys
sys.path.append('/home/caelinux/TUBAV2')
sys.path.append(' /home/jangeorg/TUBA/tutorial/001 ')

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

    P1= geompy.MakeVertex(1000, 0, 0 )
    geompy.addToStudy(P1,"P1 ")
    Vd2x_P1 = geompy.MakeVectorDXDYDZ(1.0, 0.0, 0.0)
    P1_vd2x=    geompy.MakeTranslationVectorDistance(P1,Vd2x_P1,100)
    Vd2x_P1= geompy.MakeVector(P1,P1_vd2x)
    geompy.addToStudy(Vd2x_P1,"Vd2x_P1 " )

    P2= geompy.MakeVertex(2000.0, 0.0, 0.0 )
    geompy.addToStudy(P2,"P2 ")
    Vd2x_P2 = geompy.MakeVectorDXDYDZ(1.0, 0.0, 0.0)
    P2_vd2x=    geompy.MakeTranslationVectorDistance(P2,Vd2x_P2,100)
    Vd2x_P2= geompy.MakeVector(P2,P2_vd2x)
    geompy.addToStudy(Vd2x_P2,"Vd2x_P2 " )

    P3= geompy.MakeVertex(3000.0, 0.0, 0.0 )
    geompy.addToStudy(P3,"P3 ")
    Vd2x_P3 = geompy.MakeVectorDXDYDZ(1.0, 0.0, 0.0)
    P3_vd2x=    geompy.MakeTranslationVectorDistance(P3,Vd2x_P3,100)
    Vd2x_P3= geompy.MakeVector(P3,P3_vd2x)
    geompy.addToStudy(Vd2x_P3,"Vd2x_P3 " )

    P4= geompy.MakeVertex(4000.0, 0.0, 0.0 )
    geompy.addToStudy(P4,"P4 ")
    Vd2x_P4 = geompy.MakeVectorDXDYDZ(1.0, 0.0, 0.0)
    P4_vd2x=    geompy.MakeTranslationVectorDistance(P4,Vd2x_P4,100)
    Vd2x_P4= geompy.MakeVector(P4,P4_vd2x)
    geompy.addToStudy(Vd2x_P4,"Vd2x_P4 " )

    P5= geompy.MakeVertex(5000.0, 0.0, 0.0 )
    geompy.addToStudy(P5,"P5 ")
    Vd2x_P5 = geompy.MakeVectorDXDYDZ(1.0, 0.0, 0.0)
    P5_vd2x=    geompy.MakeTranslationVectorDistance(P5,Vd2x_P5,100)
    Vd2x_P5= geompy.MakeVector(P5,P5_vd2x)
    geompy.addToStudy(Vd2x_P5,"Vd2x_P5 " )

    P6= geompy.MakeVertex(5850.0, 0.0, 0.0 )
    geompy.addToStudy(P6,"P6 ")
    Vd2x_P6 = geompy.MakeVectorDXDYDZ(1.0, 0.0, 0.0)
    P6_vd2x=    geompy.MakeTranslationVectorDistance(P6,Vd2x_P6,100)
    Vd2x_P6= geompy.MakeVector(P6,P6_vd2x)
    geompy.addToStudy(Vd2x_P6,"Vd2x_P6 " )

    P6_7_center= geompy.MakeVertex(5850.0, 150.0, 0.0 )
    geompy.addToStudy(P6_7_center,"P6_7_center ")
    Vd2x_P6_7_center = geompy.MakeVectorDXDYDZ(1, 0, 0)
    P6_7_center_vd2x=    geompy.MakeTranslationVectorDistance(P6_7_center,Vd2x_P6_7_center,100)
    Vd2x_P6_7_center= geompy.MakeVector(P6_7_center,P6_7_center_vd2x)
    geompy.addToStudy(Vd2x_P6_7_center,"Vd2x_P6_7_center " )

    P7= geompy.MakeVertex(6000.0, 150.0, 0.0 )
    geompy.addToStudy(P7,"P7 ")
    Vd2x_P7 = geompy.MakeVectorDXDYDZ(6.123233995736766e-17, 1.0, 0.0)
    P7_vd2x=    geompy.MakeTranslationVectorDistance(P7,Vd2x_P7,100)
    Vd2x_P7= geompy.MakeVector(P7,P7_vd2x)
    geompy.addToStudy(Vd2x_P7,"Vd2x_P7 " )

    P8= geompy.MakeVertex(6000.0, 1150.0, 0.0 )
    geompy.addToStudy(P8,"P8 ")
    Vd2x_P8 = geompy.MakeVectorDXDYDZ(6.123233995736766e-17, 1.0, 0.0)
    P8_vd2x=    geompy.MakeTranslationVectorDistance(P8,Vd2x_P8,100)
    Vd2x_P8= geompy.MakeVector(P8,P8_vd2x)
    geompy.addToStudy(Vd2x_P8,"Vd2x_P8 " )

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
      print("Add V1")
      V1= geompy.MakeVector(P1,P2)
      #Liste.append([P1,"P1"])
      geompy.addToStudy(V1,"V1" )
      Liste.append([V1,"V1"])
      ListeV.append(V1)
        

      _C1 = geompy.MakeCircle(P1, V1,35)
      _C2 = geompy.MakeCircle(P1, V1,31)
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
       V1M = smesh.Mesh(V1)
       Decoupage = V1M.Segment()
       Decoupage.NumberOfSegments(8)
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
      print("Add V3")
      V3= geompy.MakeVector(P3,P4)
      #Liste.append([P3,"P3"])
      geompy.addToStudy(V3,"V3" )
      Liste.append([V3,"V3"])
      ListeV.append(V3)
        

      _C1 = geompy.MakeCircle(P3, V3,35)
      _C2 = geompy.MakeCircle(P3, V3,31)
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
       V3M = smesh.Mesh(V3)
       Decoupage = V3M.Segment()
       Decoupage.NumberOfSegments(8)
       Quadratic_Mesh = Decoupage.QuadraticMesh()

       smesh.SetName(V3M,'V3')
       V3M.Compute()
       V3M.Group(P3)
       V3M.Group(P4)
       V3M.GroupOnGeom(V3)
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
      V4= geompy.MakeVector(P4,P5)
      #Liste.append([P4,"P4"])
      geompy.addToStudy(V4,"V4" )
      Liste.append([V4,"V4"])
      ListeV.append(V4)
        

      _C1 = geompy.MakeCircle(P4, V4,35)
      _C2 = geompy.MakeCircle(P4, V4,31)
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
       V4M.Group(P4)
       V4M.Group(P5)
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
      print("Add V5")
      V5= geompy.MakeVector(P5,P6)
      #Liste.append([P5,"P5"])
      geompy.addToStudy(V5,"V5" )
      Liste.append([V5,"V5"])
      ListeV.append(V5)
        

      _C1 = geompy.MakeCircle(P5, V5,35)
      _C2 = geompy.MakeCircle(P5, V5,31)
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
       V5M = smesh.Mesh(V5)
       Decoupage = V5M.Segment()
       Decoupage.NumberOfSegments(8)
       Quadratic_Mesh = Decoupage.QuadraticMesh()

       smesh.SetName(V5M,'V5')
       V5M.Compute()
       V5M.Group(P5)
       V5M.Group(P6)
       V5M.GroupOnGeom(V5)
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
      print("Add  V_Bent6 ")
      Liste=[]
      V_Bent6 = geompy.MakeArcCenter(P6_7_center,P6,P7)
      geompy.addToStudy(V_Bent6,"V_Bent6")
      Liste.append([V_Bent6,"V_Bent6"])
      ListeV.append(V_Bent6)

         

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
       V_Bent6M = smesh.Mesh(V_Bent6)
       Decoupage = V_Bent6M.Segment()
       Decoupage.NumberOfSegments(8)
       Quadratic_Mesh = Decoupage.QuadraticMesh()

       smesh.SetName(V_Bent6M,'V_Bent6')
       V_Bent6M.Compute()
       V_Bent6M.GroupOnFilter( SMESH.NODE,'P6', smesh.GetFilter( SMESH.NODE, SMESH.FT_LyingOnGeom,'=',P6))
       V_Bent6M.GroupOnFilter( SMESH.NODE,'P7', smesh.GetFilter( SMESH.NODE, SMESH.FT_LyingOnGeom,'=',P7))
       V_Bent6M.GroupOnGeom(V_Bent6)
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
      print("Add V7")
      V7= geompy.MakeVector(P7,P8)
      #Liste.append([P7,"P7"])
      geompy.addToStudy(V7,"V7" )
      Liste.append([V7,"V7"])
      ListeV.append(V7)
        

      _C1 = geompy.MakeCircle(P7, V7,35)
      _C2 = geompy.MakeCircle(P7, V7,31)
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
       V7M = smesh.Mesh(V7)
       Decoupage = V7M.Segment()
       Decoupage.NumberOfSegments(8)
       Quadratic_Mesh = Decoupage.QuadraticMesh()

       smesh.SetName(V7M,'V7')
       V7M.Compute()
       V7M.Group(P7)
       V7M.Group(P8)
       V7M.GroupOnGeom(V7)
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
        Completed_Mesh = smesh.Concatenate([V0M.GetMesh() , V1M.GetMesh() , V2M.GetMesh() , V3M.GetMesh() , 
           V4M.GetMesh() , V5M.GetMesh() , V_Bent6M.GetMesh() , V7M.GetMesh() ,], 1, 0, 1e-05)
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