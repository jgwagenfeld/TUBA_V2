#!/usr/bin/python 3
# -*- coding: iso-8859-1 -*-

import time
time1=time.time()
import sys
sys.path.append('/home/caelinux/TUBAV2')
sys.path.append(' /home/jangeorg/TUBA/examples/000_Testing/008_RECANGULAR ')

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

                
    P0_BLOCK_xyzrxryrz=geompy.MakeBox(120,120,120,-120,-120,-120)	
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
    Vd2x_P1 = geompy.MakeVectorDXDYDZ(-0.4472135954999579, 0.0, 0.8944271909999159)
    P1_vd2x=    geompy.MakeTranslationVectorDistance(P1,Vd2x_P1,100)
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
    

    P2= geompy.MakeVertex(500, 0, 1000 )
    geompy.addToStudy(P2,"P2 ")
    Vd2x_P2 = geompy.MakeVectorDXDYDZ(-0.4472135954999579, 0.0, -0.8944271909999159)
    P2_vd2x=    geompy.MakeTranslationVectorDistance(P2,Vd2x_P2,100)
    Vd2x_P2= geompy.MakeVector(P2,P2_vd2x)
    geompy.addToStudyInFather(P2,Vd2x_P2,"Vd2x_P2 " )

    P3= geompy.MakeVertex(0, 0, 0 )
    geompy.addToStudy(P3,"P3 ")
    Vd2x_P3 = geompy.MakeVectorDXDYDZ(-0.4472135954999579, 0.0, -0.8944271909999159)
    P3_vd2x=    geompy.MakeTranslationVectorDistance(P3,Vd2x_P3,100)
    Vd2x_P3= geompy.MakeVector(P3,P3_vd2x)
    geompy.addToStudyInFather(P3,Vd2x_P3,"Vd2x_P3 " )

    try:
      print("Add: V0")
      V0= geompy.MakeVector(P0,P1)
      #Liste.append([P0,"P0"])
      geompy.addToStudy(V0,"V0" )
#      Liste.append([V0,"V0"])
      List_Visualization.append(V0)
        

      _W1 = geompy.MakeSketcher("Sketcher: F 30 30: TT -30 30: TT -30 -30: TT 30 -30: WW",
          [   0,0,0,
              1.0,0.0,0.0,
              0.0,0.0,1.0]
      )

      _W2 = geompy.MakeSketcher("Sketcher: F 27 27: TT -27 27: TT -27 -27: TT 27 -27: WW",
          [   0,0,0,
              1.0,0.0,0.0,
              0.0,0.0,1.0]
      )
      FaceTube= geompy.MakeFaceWires([_W1, _W2], 1)
      Liste.append([_W1 ,"_W1"])
      Liste.append([_W2 ,"_W2"])
#      Pipe = geompy.MakePipe( S ,V0)
#      Pipe.SetColor(SALOMEDS.Color(0.6,0.6,0.6))
#      Pipe_id=geompy.addToStudy(Pipe," V0_3D")
#      gg.createAndDisplayGO(Pipe_id)
#      gg.setDisplayMode(Pipe_id,1)       
 
            

    except:
       ERREUR=True
       print ("   =>ERROR BUILDING THE GEOMETRY!")
       for x in Liste :
           geompy.addToStudy(x[0],x[1])
       return

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
        


    if List_Visualization!=[]:
       _W=geompy.MakeWire(List_Visualization,1e-7)
       Pipe_V0 = geompy.MakePipe( FaceTube ,_W)
       Pipe_V0.SetColor(SALOMEDS.Color(0.8,0.8,0.8))
       Pipe_id=geompy.addToStudyInFather(V0,Pipe_V0,"Pipe_V0")
       gg.createAndDisplayGO(Pipe_id)
       gg.setDisplayMode(Pipe_id,1)

       List_ParaVis_Visualization.append(Pipe_V0)
       List_Visualization=[]
    

    try:
      print("Add: V1")
      V1= geompy.MakeVector(P1,P2)
      #Liste.append([P1,"P1"])
      geompy.addToStudy(V1,"V1" )
#      Liste.append([V1,"V1"])
      List_Visualization.append(V1)
        

      _W1 = geompy.MakeSketcher("Sketcher: F 30 30: TT -30 30: TT -30 -30: TT 30 -30: WW",
          [   1000,0,0,
              -0.4472135955,0.0,0.894427191,
              0.0,0.894427191,-0.0]
      )

      _W2 = geompy.MakeSketcher("Sketcher: F 27 27: TT -27 27: TT -27 -27: TT 27 -27: WW",
          [   1000,0,0,
              -0.4472135955,0.0,0.894427191,
              0.0,0.894427191,-0.0]
      )
      FaceTube= geompy.MakeFaceWires([_W1, _W2], 1)
      Liste.append([_W1 ,"_W1"])
      Liste.append([_W2 ,"_W2"])
#      Pipe = geompy.MakePipe( S ,V1)
#      Pipe.SetColor(SALOMEDS.Color(0.6,0.6,0.6))
#      Pipe_id=geompy.addToStudy(Pipe," V1_3D")
#      gg.createAndDisplayGO(Pipe_id)
#      gg.setDisplayMode(Pipe_id,1)       
 
            

    except:
       ERREUR=True
       print ("   =>ERROR BUILDING THE GEOMETRY!")
       for x in Liste :
           geompy.addToStudy(x[0],x[1])
       return

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
        


    if List_Visualization!=[]:
       _W=geompy.MakeWire(List_Visualization,1e-7)
       Pipe_V1 = geompy.MakePipe( FaceTube ,_W)
       Pipe_V1.SetColor(SALOMEDS.Color(0.8,0.8,0.8))
       Pipe_id=geompy.addToStudyInFather(V1,Pipe_V1,"Pipe_V1")
       gg.createAndDisplayGO(Pipe_id)
       gg.setDisplayMode(Pipe_id,1)

       List_ParaVis_Visualization.append(Pipe_V1)
       List_Visualization=[]
    

    try:
      print("Add: V2")
      V2= geompy.MakeVector(P2,P3)
      #Liste.append([P2,"P2"])
      geompy.addToStudy(V2,"V2" )
#      Liste.append([V2,"V2"])
      List_Visualization.append(V2)
        

      _W1 = geompy.MakeSketcher("Sketcher: F 30 30: TT -30 30: TT -30 -30: TT 30 -30: WW",
          [   500,0,1000,
              -0.4472135955,0.0,-0.894427191,
              0.0,0.8,0.0]
      )

      _W2 = geompy.MakeSketcher("Sketcher: F 27 27: TT -27 27: TT -27 -27: TT 27 -27: WW",
          [   500,0,1000,
              -0.4472135955,0.0,-0.894427191,
              0.0,0.8,0.0]
      )
      FaceTube= geompy.MakeFaceWires([_W1, _W2], 1)
      Liste.append([_W1 ,"_W1"])
      Liste.append([_W2 ,"_W2"])
#      Pipe = geompy.MakePipe( S ,V2)
#      Pipe.SetColor(SALOMEDS.Color(0.6,0.6,0.6))
#      Pipe_id=geompy.addToStudy(Pipe," V2_3D")
#      gg.createAndDisplayGO(Pipe_id)
#      gg.setDisplayMode(Pipe_id,1)       
 
            

    except:
       ERREUR=True
       print ("   =>ERROR BUILDING THE GEOMETRY!")
       for x in Liste :
           geompy.addToStudy(x[0],x[1])
       return

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
        


    if List_Visualization!=[]:
       _W=geompy.MakeWire(List_Visualization,1e-7)
       Pipe_V2 = geompy.MakePipe( FaceTube ,_W)
       Pipe_V2.SetColor(SALOMEDS.Color(0.8,0.8,0.8))
       Pipe_id=geompy.addToStudyInFather(V2,Pipe_V2,"Pipe_V2")
       gg.createAndDisplayGO(Pipe_id)
       gg.setDisplayMode(Pipe_id,1)

       List_ParaVis_Visualization.append(Pipe_V2)
       List_Visualization=[]
    

    try:  

        compound_paravis=geompy.MakeCompound(List_ParaVis_Visualization)
     #   compound_id=geompy.addToStudy(compound_paravis,'compound_paravis')
    except:
        print("No compound could be created",str(List_ParaVis_Visualization))
        
        
    #Creates the mesh compound
    if not(ERREUR):
        Completed_Mesh = smesh.Concatenate([V0M.GetMesh() , V1M.GetMesh() , V2M.GetMesh() ,], 1, 0, 1e-05)
        coincident_nodes = Completed_Mesh.FindCoincidentNodes( 1e-05 )
        Completed_Mesh.MergeNodes(coincident_nodes)
        equal_elements = Completed_Mesh.FindEqualElements(Completed_Mesh)    
        Completed_Mesh.MergeElements(equal_elements)   
        smesh.SetName(Completed_Mesh.GetMesh(), 'Completed_Mesh')
        

#    elem = structElemManager.createElement(commandList)
#    elem.display()    



#    try:
#      Completed_Mesh.ExportMED( r'/home/jangeorg/TUBA/examples/000_Testing/008_RECANGULAR/Completed_Mesh.mmed', 0)
#    except:
#      print ('ExportPartToMED() failed')


    try:    
        geompy.ExportVTK(compound_paravis, '/home/jangeorg/TUBA/examples/000_Testing/008_RECANGULAR/compound_paravis.vtk', 0.001)     
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