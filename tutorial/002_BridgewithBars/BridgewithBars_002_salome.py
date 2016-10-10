#!/usr/bin/python 3
# -*- coding: iso-8859-1 -*-

import time
time1=time.time()
import sys
sys.path.append('/home/caelinux/TUBAV2')
sys.path.append(' /home/jangeorg/TUBA/tutorial/002_BridgewithBars ')

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
    Vd2x_P0 = geompy.MakeVectorDXDYDZ(-0.4472135954999579, 0.0, -0.8944271909999159)
    P0_vd2x=    geompy.MakeTranslationVectorDistance(P0,Vd2x_P0,100)
    Vd2x_P0= geompy.MakeVector(P0,P0_vd2x)
    geompy.addToStudy(Vd2x_P0,"Vd2x_P0 " )

    P1= geompy.MakeVertex(1000, 0, 0 )
    geompy.addToStudy(P1,"P1 ")
    Vd2x_P1 = geompy.MakeVectorDXDYDZ(-0.4472135954999579, 0.0, -0.8944271909999159)
    P1_vd2x=    geompy.MakeTranslationVectorDistance(P1,Vd2x_P1,100)
    Vd2x_P1= geompy.MakeVector(P1,P1_vd2x)
    geompy.addToStudy(Vd2x_P1,"Vd2x_P1 " )

    P2= geompy.MakeVertex(2000, 0, 0 )
    geompy.addToStudy(P2,"P2 ")
    Vd2x_P2 = geompy.MakeVectorDXDYDZ(-0.4472135954999579, 0.0, -0.8944271909999159)
    P2_vd2x=    geompy.MakeTranslationVectorDistance(P2,Vd2x_P2,100)
    Vd2x_P2= geompy.MakeVector(P2,P2_vd2x)
    geompy.addToStudy(Vd2x_P2,"Vd2x_P2 " )

    P3= geompy.MakeVertex(3000, 0, 0 )
    geompy.addToStudy(P3,"P3 ")
    Vd2x_P3 = geompy.MakeVectorDXDYDZ(-0.4472135954999579, 0.0, -0.8944271909999159)
    P3_vd2x=    geompy.MakeTranslationVectorDistance(P3,Vd2x_P3,100)
    Vd2x_P3= geompy.MakeVector(P3,P3_vd2x)
    geompy.addToStudy(Vd2x_P3,"Vd2x_P3 " )

    P4= geompy.MakeVertex(4000, 0, 0 )
    geompy.addToStudy(P4,"P4 ")
    Vd2x_P4 = geompy.MakeVectorDXDYDZ(-0.4472135954999579, 0.0, 0.8944271909999159)
    P4_vd2x=    geompy.MakeTranslationVectorDistance(P4,Vd2x_P4,100)
    Vd2x_P4= geompy.MakeVector(P4,P4_vd2x)
    geompy.addToStudy(Vd2x_P4,"Vd2x_P4 " )

    P5= geompy.MakeVertex(3500, 0, 1000 )
    geompy.addToStudy(P5,"P5 ")
    Vd2x_P5 = geompy.MakeVectorDXDYDZ(0.4472135954999579, 0.0, -0.8944271909999159)
    P5_vd2x=    geompy.MakeTranslationVectorDistance(P5,Vd2x_P5,100)
    Vd2x_P5= geompy.MakeVector(P5,P5_vd2x)
    geompy.addToStudy(Vd2x_P5,"Vd2x_P5 " )

    P6= geompy.MakeVertex(2500, 0, 1000 )
    geompy.addToStudy(P6,"P6 ")
    Vd2x_P6 = geompy.MakeVectorDXDYDZ(0.4472135954999579, 0.0, -0.8944271909999159)
    P6_vd2x=    geompy.MakeTranslationVectorDistance(P6,Vd2x_P6,100)
    Vd2x_P6= geompy.MakeVector(P6,P6_vd2x)
    geompy.addToStudy(Vd2x_P6,"Vd2x_P6 " )

    P7= geompy.MakeVertex(1500, 0, 1000 )
    geompy.addToStudy(P7,"P7 ")
    Vd2x_P7 = geompy.MakeVectorDXDYDZ(0.4472135954999579, 0.0, -0.8944271909999159)
    P7_vd2x=    geompy.MakeTranslationVectorDistance(P7,Vd2x_P7,100)
    Vd2x_P7= geompy.MakeVector(P7,P7_vd2x)
    geompy.addToStudy(Vd2x_P7,"Vd2x_P7 " )

    P8= geompy.MakeVertex(500, 0, 1000 )
    geompy.addToStudy(P8,"P8 ")
    Vd2x_P8 = geompy.MakeVectorDXDYDZ(-0.4472135954999579, 0.0, 0.8944271909999159)
    P8_vd2x=    geompy.MakeTranslationVectorDistance(P8,Vd2x_P8,100)
    Vd2x_P8= geompy.MakeVector(P8,P8_vd2x)
    geompy.addToStudy(Vd2x_P8,"Vd2x_P8 " )

    P9= geompy.MakeVertex(1000, 0, 2000 )
    geompy.addToStudy(P9,"P9 ")
    Vd2x_P9 = geompy.MakeVectorDXDYDZ(-0.4472135954999579, 0.0, -0.8944271909999159)
    P9_vd2x=    geompy.MakeTranslationVectorDistance(P9,Vd2x_P9,100)
    Vd2x_P9= geompy.MakeVector(P9,P9_vd2x)
    geompy.addToStudy(Vd2x_P9,"Vd2x_P9 " )

    P10= geompy.MakeVertex(2000, 0, 2000 )
    geompy.addToStudy(P10,"P10 ")
    Vd2x_P10 = geompy.MakeVectorDXDYDZ(-0.4472135954999579, 0.0, -0.8944271909999159)
    P10_vd2x=    geompy.MakeTranslationVectorDistance(P10,Vd2x_P10,100)
    Vd2x_P10= geompy.MakeVector(P10,P10_vd2x)
    geompy.addToStudy(Vd2x_P10,"Vd2x_P10 " )

    P11= geompy.MakeVertex(3000, 0, 2000 )
    geompy.addToStudy(P11,"P11 ")
    Vd2x_P11 = geompy.MakeVectorDXDYDZ(0.4472135954999579, 0.0, 0.8944271909999159)
    P11_vd2x=    geompy.MakeTranslationVectorDistance(P11,Vd2x_P11,100)
    Vd2x_P11= geompy.MakeVector(P11,P11_vd2x)
    geompy.addToStudy(Vd2x_P11,"Vd2x_P11 " )

    P12= geompy.MakeVertex(2500, 0, 3000 )
    geompy.addToStudy(P12,"P12 ")
    Vd2x_P12 = geompy.MakeVectorDXDYDZ(-0.4472135954999579, 0.0, -0.8944271909999159)
    P12_vd2x=    geompy.MakeTranslationVectorDistance(P12,Vd2x_P12,100)
    Vd2x_P12= geompy.MakeVector(P12,P12_vd2x)
    geompy.addToStudy(Vd2x_P12,"Vd2x_P12 " )

    P13= geompy.MakeVertex(1500, 0, 3000 )
    geompy.addToStudy(P13,"P13 ")
    Vd2x_P13 = geompy.MakeVectorDXDYDZ(-0.4472135954999579, 0.0, 0.8944271909999159)
    P13_vd2x=    geompy.MakeTranslationVectorDistance(P13,Vd2x_P13,100)
    Vd2x_P13= geompy.MakeVector(P13,P13_vd2x)
    geompy.addToStudy(Vd2x_P13,"Vd2x_P13 " )

    try:
      print("Add V0")
      V0= geompy.MakeVector(P0,P1)
      #Liste.append([P0,"P0"])
      geompy.addToStudy(V0,"V0" )
      Liste.append([V0,"V0"])
      ListeV.append(V0)
        

      _C1 = geompy.MakeCircle(P0, V0,60)
      _C2 = geompy.MakeCircle(P0, V0,57)
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
        

      _C1 = geompy.MakeCircle(P1, V1,60)
      _C2 = geompy.MakeCircle(P1, V1,57)
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
        

      _C1 = geompy.MakeCircle(P2, V2,60)
      _C2 = geompy.MakeCircle(P2, V2,57)
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
        

      _C1 = geompy.MakeCircle(P3, V3,60)
      _C2 = geompy.MakeCircle(P3, V3,57)
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
        

      _C1 = geompy.MakeCircle(P4, V4,60)
      _C2 = geompy.MakeCircle(P4, V4,57)
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
        

      _C1 = geompy.MakeCircle(P5, V5,60)
      _C2 = geompy.MakeCircle(P5, V5,57)
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
      print("Add V6")
      V6= geompy.MakeVector(P6,P7)
      #Liste.append([P6,"P6"])
      geompy.addToStudy(V6,"V6" )
      Liste.append([V6,"V6"])
      ListeV.append(V6)
        

      _C1 = geompy.MakeCircle(P6, V6,60)
      _C2 = geompy.MakeCircle(P6, V6,57)
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

       smesh.SetName(V6M,'V6')
       V6M.Compute()
       V6M.Group(P6)
       V6M.Group(P7)
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
      print("Add V7")
      V7= geompy.MakeVector(P7,P8)
      #Liste.append([P7,"P7"])
      geompy.addToStudy(V7,"V7" )
      Liste.append([V7,"V7"])
      ListeV.append(V7)
        

      _C1 = geompy.MakeCircle(P7, V7,60)
      _C2 = geompy.MakeCircle(P7, V7,57)
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
    

    try:
      print("Add V8")
      V8= geompy.MakeVector(P8,P9)
      #Liste.append([P8,"P8"])
      geompy.addToStudy(V8,"V8" )
      Liste.append([V8,"V8"])
      ListeV.append(V8)
        

      _C1 = geompy.MakeCircle(P8, V8,60)
      _C2 = geompy.MakeCircle(P8, V8,57)
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

       smesh.SetName(V8M,'V8')
       V8M.Compute()
       V8M.Group(P8)
       V8M.Group(P9)
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
      print("Add V9")
      V9= geompy.MakeVector(P9,P10)
      #Liste.append([P9,"P9"])
      geompy.addToStudy(V9,"V9" )
      Liste.append([V9,"V9"])
      ListeV.append(V9)
        

      _C1 = geompy.MakeCircle(P9, V9,60)
      _C2 = geompy.MakeCircle(P9, V9,57)
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
       V9M = smesh.Mesh(V9)
       Decoupage = V9M.Segment()
       Decoupage.NumberOfSegments(8)

       smesh.SetName(V9M,'V9')
       V9M.Compute()
       V9M.Group(P9)
       V9M.Group(P10)
       V9M.GroupOnGeom(V9)
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
      V10= geompy.MakeVector(P10,P11)
      #Liste.append([P10,"P10"])
      geompy.addToStudy(V10,"V10" )
      Liste.append([V10,"V10"])
      ListeV.append(V10)
        

      _C1 = geompy.MakeCircle(P10, V10,60)
      _C2 = geompy.MakeCircle(P10, V10,57)
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

       smesh.SetName(V10M,'V10')
       V10M.Compute()
       V10M.Group(P10)
       V10M.Group(P11)
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
      print("Add V11")
      V11= geompy.MakeVector(P11,P12)
      #Liste.append([P11,"P11"])
      geompy.addToStudy(V11,"V11" )
      Liste.append([V11,"V11"])
      ListeV.append(V11)
        

      _C1 = geompy.MakeCircle(P11, V11,60)
      _C2 = geompy.MakeCircle(P11, V11,57)
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
       V11M = smesh.Mesh(V11)
       Decoupage = V11M.Segment()
       Decoupage.NumberOfSegments(8)

       smesh.SetName(V11M,'V11')
       V11M.Compute()
       V11M.Group(P11)
       V11M.Group(P12)
       V11M.GroupOnGeom(V11)
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
      V12= geompy.MakeVector(P12,P13)
      #Liste.append([P12,"P12"])
      geompy.addToStudy(V12,"V12" )
      Liste.append([V12,"V12"])
      ListeV.append(V12)
        

      _C1 = geompy.MakeCircle(P12, V12,60)
      _C2 = geompy.MakeCircle(P12, V12,57)
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

       smesh.SetName(V12M,'V12')
       V12M.Compute()
       V12M.Group(P12)
       V12M.Group(P13)
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
      print("Add V13")
      V13= geompy.MakeVector(P8,P0)
      #Liste.append([P8,"P8"])
      geompy.addToStudy(V13,"V13" )
      Liste.append([V13,"V13"])
      ListeV.append(V13)
        

      _C1 = geompy.MakeCircle(P8, V13,60)
      _C2 = geompy.MakeCircle(P8, V13,57)
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
       V13M = smesh.Mesh(V13)
       Decoupage = V13M.Segment()
       Decoupage.NumberOfSegments(8)

       smesh.SetName(V13M,'V13')
       V13M.Compute()
       V13M.Group(P8)
       V13M.Group(P0)
       V13M.GroupOnGeom(V13)
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
      V14= geompy.MakeVector(P1,P8)
      #Liste.append([P1,"P1"])
      geompy.addToStudy(V14,"V14" )
      Liste.append([V14,"V14"])
      ListeV.append(V14)
        

      _C1 = geompy.MakeCircle(P1, V14,60)
      _C2 = geompy.MakeCircle(P1, V14,57)
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

       smesh.SetName(V14M,'V14')
       V14M.Compute()
       V14M.Group(P1)
       V14M.Group(P8)
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
      print("Add V15")
      V15= geompy.MakeVector(P7,P1)
      #Liste.append([P7,"P7"])
      geompy.addToStudy(V15,"V15" )
      Liste.append([V15,"V15"])
      ListeV.append(V15)
        

      _C1 = geompy.MakeCircle(P7, V15,60)
      _C2 = geompy.MakeCircle(P7, V15,57)
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
       V15M = smesh.Mesh(V15)
       Decoupage = V15M.Segment()
       Decoupage.NumberOfSegments(8)

       smesh.SetName(V15M,'V15')
       V15M.Compute()
       V15M.Group(P7)
       V15M.Group(P1)
       V15M.GroupOnGeom(V15)
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
      V16= geompy.MakeVector(P2,P7)
      #Liste.append([P2,"P2"])
      geompy.addToStudy(V16,"V16" )
      Liste.append([V16,"V16"])
      ListeV.append(V16)
        

      _C1 = geompy.MakeCircle(P2, V16,60)
      _C2 = geompy.MakeCircle(P2, V16,57)
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

       smesh.SetName(V16M,'V16')
       V16M.Compute()
       V16M.Group(P2)
       V16M.Group(P7)
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
      print("Add V17")
      V17= geompy.MakeVector(P6,P2)
      #Liste.append([P6,"P6"])
      geompy.addToStudy(V17,"V17" )
      Liste.append([V17,"V17"])
      ListeV.append(V17)
        

      _C1 = geompy.MakeCircle(P6, V17,60)
      _C2 = geompy.MakeCircle(P6, V17,57)
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
       V17M = smesh.Mesh(V17)
       Decoupage = V17M.Segment()
       Decoupage.NumberOfSegments(8)

       smesh.SetName(V17M,'V17')
       V17M.Compute()
       V17M.Group(P6)
       V17M.Group(P2)
       V17M.GroupOnGeom(V17)
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
      V18= geompy.MakeVector(P3,P6)
      #Liste.append([P3,"P3"])
      geompy.addToStudy(V18,"V18" )
      Liste.append([V18,"V18"])
      ListeV.append(V18)
        

      _C1 = geompy.MakeCircle(P3, V18,60)
      _C2 = geompy.MakeCircle(P3, V18,57)
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

       smesh.SetName(V18M,'V18')
       V18M.Compute()
       V18M.Group(P3)
       V18M.Group(P6)
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
      print("Add V19")
      V19= geompy.MakeVector(P5,P3)
      #Liste.append([P5,"P5"])
      geompy.addToStudy(V19,"V19" )
      Liste.append([V19,"V19"])
      ListeV.append(V19)
        

      _C1 = geompy.MakeCircle(P5, V19,60)
      _C2 = geompy.MakeCircle(P5, V19,57)
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
       V19M = smesh.Mesh(V19)
       Decoupage = V19M.Segment()
       Decoupage.NumberOfSegments(8)

       smesh.SetName(V19M,'V19')
       V19M.Compute()
       V19M.Group(P5)
       V19M.Group(P3)
       V19M.GroupOnGeom(V19)
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
      V20= geompy.MakeVector(P11,P5)
      #Liste.append([P11,"P11"])
      geompy.addToStudy(V20,"V20" )
      Liste.append([V20,"V20"])
      ListeV.append(V20)
        

      _C1 = geompy.MakeCircle(P11, V20,60)
      _C2 = geompy.MakeCircle(P11, V20,57)
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

       smesh.SetName(V20M,'V20')
       V20M.Compute()
       V20M.Group(P11)
       V20M.Group(P5)
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
      print("Add V21")
      V21= geompy.MakeVector(P6,P11)
      #Liste.append([P6,"P6"])
      geompy.addToStudy(V21,"V21" )
      Liste.append([V21,"V21"])
      ListeV.append(V21)
        

      _C1 = geompy.MakeCircle(P6, V21,60)
      _C2 = geompy.MakeCircle(P6, V21,57)
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
       V21M = smesh.Mesh(V21)
       Decoupage = V21M.Segment()
       Decoupage.NumberOfSegments(8)

       smesh.SetName(V21M,'V21')
       V21M.Compute()
       V21M.Group(P6)
       V21M.Group(P11)
       V21M.GroupOnGeom(V21)
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
      V22= geompy.MakeVector(P10,P6)
      #Liste.append([P10,"P10"])
      geompy.addToStudy(V22,"V22" )
      Liste.append([V22,"V22"])
      ListeV.append(V22)
        

      _C1 = geompy.MakeCircle(P10, V22,60)
      _C2 = geompy.MakeCircle(P10, V22,57)
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

       smesh.SetName(V22M,'V22')
       V22M.Compute()
       V22M.Group(P10)
       V22M.Group(P6)
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
      print("Add V23")
      V23= geompy.MakeVector(P7,P10)
      #Liste.append([P7,"P7"])
      geompy.addToStudy(V23,"V23" )
      Liste.append([V23,"V23"])
      ListeV.append(V23)
        

      _C1 = geompy.MakeCircle(P7, V23,60)
      _C2 = geompy.MakeCircle(P7, V23,57)
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
       V23M = smesh.Mesh(V23)
       Decoupage = V23M.Segment()
       Decoupage.NumberOfSegments(8)

       smesh.SetName(V23M,'V23')
       V23M.Compute()
       V23M.Group(P7)
       V23M.Group(P10)
       V23M.GroupOnGeom(V23)
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
      V24= geompy.MakeVector(P9,P7)
      #Liste.append([P9,"P9"])
      geompy.addToStudy(V24,"V24" )
      Liste.append([V24,"V24"])
      ListeV.append(V24)
        

      _C1 = geompy.MakeCircle(P9, V24,60)
      _C2 = geompy.MakeCircle(P9, V24,57)
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

       smesh.SetName(V24M,'V24')
       V24M.Compute()
       V24M.Group(P9)
       V24M.Group(P7)
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
      print("Add V25")
      V25= geompy.MakeVector(P13,P9)
      #Liste.append([P13,"P13"])
      geompy.addToStudy(V25,"V25" )
      Liste.append([V25,"V25"])
      ListeV.append(V25)
        

      _C1 = geompy.MakeCircle(P13, V25,60)
      _C2 = geompy.MakeCircle(P13, V25,57)
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
       V25M = smesh.Mesh(V25)
       Decoupage = V25M.Segment()
       Decoupage.NumberOfSegments(8)

       smesh.SetName(V25M,'V25')
       V25M.Compute()
       V25M.Group(P13)
       V25M.Group(P9)
       V25M.GroupOnGeom(V25)
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
      V26= geompy.MakeVector(P10,P13)
      #Liste.append([P10,"P10"])
      geompy.addToStudy(V26,"V26" )
      Liste.append([V26,"V26"])
      ListeV.append(V26)
        

      _C1 = geompy.MakeCircle(P10, V26,60)
      _C2 = geompy.MakeCircle(P10, V26,57)
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

       smesh.SetName(V26M,'V26')
       V26M.Compute()
       V26M.Group(P10)
       V26M.Group(P13)
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
      print("Add V27")
      V27= geompy.MakeVector(P12,P10)
      #Liste.append([P12,"P12"])
      geompy.addToStudy(V27,"V27" )
      Liste.append([V27,"V27"])
      ListeV.append(V27)
        

      _C1 = geompy.MakeCircle(P12, V27,60)
      _C2 = geompy.MakeCircle(P12, V27,57)
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
       V27M = smesh.Mesh(V27)
       Decoupage = V27M.Segment()
       Decoupage.NumberOfSegments(8)

       smesh.SetName(V27M,'V27')
       V27M.Compute()
       V27M.Group(P12)
       V27M.Group(P10)
       V27M.GroupOnGeom(V27)
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
           V4M.GetMesh() , V5M.GetMesh() , V6M.GetMesh() , V7M.GetMesh() , V8M.GetMesh() , 
           V9M.GetMesh() , V10M.GetMesh() , V11M.GetMesh() , V12M.GetMesh() , 
           V13M.GetMesh() , V14M.GetMesh() , V15M.GetMesh() , V16M.GetMesh() , 
           V17M.GetMesh() , V18M.GetMesh() , V19M.GetMesh() , V20M.GetMesh() , 
           V21M.GetMesh() , V22M.GetMesh() , V23M.GetMesh() , V24M.GetMesh() , 
           V25M.GetMesh() , V26M.GetMesh() , V27M.GetMesh() ,], 1, 0, 1e-05)
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