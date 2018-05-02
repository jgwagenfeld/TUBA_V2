#!/usr/bin/python 3
# -*- coding: iso-8859-1 -*-

import time
time1=time.time()
import sys
sys.path.append(' /home/jangeorg/TUBA/tutorials/000_Testing/011_CABLE ')

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
    P0= geompy.MakeVertex(0, 0, 0 )
    geompy.addToStudy(P0,"P0 ")
    geompy.PutToFolder(P0, Folder_Points)

    Vd1x_P0 = geompy.MakeVectorDXDYDZ(0, 1, 0)
    P0_vd1x=    geompy.MakeTranslationVectorDistance(P0,Vd1x_P0,1000)
    Vd1x_P0= geompy.MakeVector(P0,P0_vd1x)
    geompy.addToStudyInFather(P0,Vd1x_P0,"Vd1x_P0 " )
       
    Vd2x_P0 = geompy.MakeVectorDXDYDZ(0.0, 0.0, 1.0)
    P0_vd2x=    geompy.MakeTranslationVectorDistance(P0,Vd2x_P0,1000)
    Vd2x_P0= geompy.MakeVector(P0,P0_vd2x)
    geompy.addToStudyInFather(P0,Vd2x_P0,"Vd2x_P0 " )

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
    top= geompy.MakeVertex(0, 0, 1000 )
    geompy.addToStudy(top,"top ")
    geompy.PutToFolder(top, Folder_Points)

    Vd1x_top = geompy.MakeVectorDXDYDZ(-0.5773502691896258, 0.5773502691896258, -0.5773502691896258)
    top_vd1x=    geompy.MakeTranslationVectorDistance(top,Vd1x_top,1000)
    Vd1x_top= geompy.MakeVector(top,top_vd1x)
    geompy.addToStudyInFather(top,Vd1x_top,"Vd1x_top " )
       
    Vd2x_top = geompy.MakeVectorDXDYDZ(-0.5773502691896258, -0.5773502691896258, -0.5773502691896258)
    top_vd2x=    geompy.MakeTranslationVectorDistance(top,Vd2x_top,1000)
    Vd2x_top= geompy.MakeVector(top,top_vd2x)
    geompy.addToStudyInFather(top,Vd2x_top,"Vd2x_top " )


##_points##  
    P2= geompy.MakeVertex(1000, 1000, 0 )
    geompy.addToStudy(P2,"P2 ")
    geompy.PutToFolder(P2, Folder_Points)

    Vd1x_P2 = geompy.MakeVectorDXDYDZ(0, 1, 0)
    P2_vd1x=    geompy.MakeTranslationVectorDistance(P2,Vd1x_P2,1000)
    Vd1x_P2= geompy.MakeVector(P2,P2_vd1x)
    geompy.addToStudyInFather(P2,Vd1x_P2,"Vd1x_P2 " )
       
    Vd2x_P2 = geompy.MakeVectorDXDYDZ(0.5773502691896258, 0.5773502691896258, -0.5773502691896258)
    P2_vd2x=    geompy.MakeTranslationVectorDistance(P2,Vd2x_P2,1000)
    Vd2x_P2= geompy.MakeVector(P2,P2_vd2x)
    geompy.addToStudyInFather(P2,Vd2x_P2,"Vd2x_P2 " )

    # Visualize a support(restriction DOF) at point P2
    #---------------------------------------------               
    P2_BLOCK_xyzrxryrz=geompy.MakeBox(1070.0,1070.0,70.0,930.0,930.0,-70.0)	
    P2_BLOCK_xyzrxryrz.SetColor(SALOMEDS.Color(1,1,0))
    P2_BLOCK_xyzrxryrz_id=geompy.addToStudyInFather( P2, P2_BLOCK_xyzrxryrz,'P2_BLOCK_xyzrxryrz' )
 #   B_id=geompy.addToStudy(P2_BLOCK_xyzrxryrz,'P2_BLOCK_xyzrxryrz' )
    
    List_ParaVis_Visualization.append(P2_BLOCK_xyzrxryrz)
    objId = geompy.getObjectID(P2_BLOCK_xyzrxryrz)    
    gg.createAndDisplayGO(objId)
    gg.setDisplayMode(objId,1)
    gg.setColor(objId,218,165,31)
  
    


##_points##  
    P3= geompy.MakeVertex(1000, -1000, 0 )
    geompy.addToStudy(P3,"P3 ")
    geompy.PutToFolder(P3, Folder_Points)

    Vd1x_P3 = geompy.MakeVectorDXDYDZ(0, 1, 0)
    P3_vd1x=    geompy.MakeTranslationVectorDistance(P3,Vd1x_P3,1000)
    Vd1x_P3= geompy.MakeVector(P3,P3_vd1x)
    geompy.addToStudyInFather(P3,Vd1x_P3,"Vd1x_P3 " )
       
    Vd2x_P3 = geompy.MakeVectorDXDYDZ(0.5773502691896258, -0.5773502691896258, -0.5773502691896258)
    P3_vd2x=    geompy.MakeTranslationVectorDistance(P3,Vd2x_P3,1000)
    Vd2x_P3= geompy.MakeVector(P3,P3_vd2x)
    geompy.addToStudyInFather(P3,Vd2x_P3,"Vd2x_P3 " )

    # Visualize a support(restriction DOF) at point P3
    #---------------------------------------------               
    P3_BLOCK_xyzrxryrz=geompy.MakeBox(1070.0,-930.0,70.0,930.0,-1070.0,-70.0)	
    P3_BLOCK_xyzrxryrz.SetColor(SALOMEDS.Color(1,1,0))
    P3_BLOCK_xyzrxryrz_id=geompy.addToStudyInFather( P3, P3_BLOCK_xyzrxryrz,'P3_BLOCK_xyzrxryrz' )
 #   B_id=geompy.addToStudy(P3_BLOCK_xyzrxryrz,'P3_BLOCK_xyzrxryrz' )
    
    List_ParaVis_Visualization.append(P3_BLOCK_xyzrxryrz)
    objId = geompy.getObjectID(P3_BLOCK_xyzrxryrz)    
    gg.createAndDisplayGO(objId)
    gg.setDisplayMode(objId,1)
    gg.setColor(objId,218,165,31)
  
    


##_points##  
    P4= geompy.MakeVertex(-1000, 1000, 0 )
    geompy.addToStudy(P4,"P4 ")
    geompy.PutToFolder(P4, Folder_Points)

    Vd1x_P4 = geompy.MakeVectorDXDYDZ(0, 1, 0)
    P4_vd1x=    geompy.MakeTranslationVectorDistance(P4,Vd1x_P4,1000)
    Vd1x_P4= geompy.MakeVector(P4,P4_vd1x)
    geompy.addToStudyInFather(P4,Vd1x_P4,"Vd1x_P4 " )
       
    Vd2x_P4 = geompy.MakeVectorDXDYDZ(-0.5773502691896258, 0.5773502691896258, -0.5773502691896258)
    P4_vd2x=    geompy.MakeTranslationVectorDistance(P4,Vd2x_P4,1000)
    Vd2x_P4= geompy.MakeVector(P4,P4_vd2x)
    geompy.addToStudyInFather(P4,Vd2x_P4,"Vd2x_P4 " )

    # Visualize a support(restriction DOF) at point P4
    #---------------------------------------------               
    P4_BLOCK_xyzrxryrz=geompy.MakeBox(-930.0,1070.0,70.0,-1070.0,930.0,-70.0)	
    P4_BLOCK_xyzrxryrz.SetColor(SALOMEDS.Color(1,1,0))
    P4_BLOCK_xyzrxryrz_id=geompy.addToStudyInFather( P4, P4_BLOCK_xyzrxryrz,'P4_BLOCK_xyzrxryrz' )
 #   B_id=geompy.addToStudy(P4_BLOCK_xyzrxryrz,'P4_BLOCK_xyzrxryrz' )
    
    List_ParaVis_Visualization.append(P4_BLOCK_xyzrxryrz)
    objId = geompy.getObjectID(P4_BLOCK_xyzrxryrz)    
    gg.createAndDisplayGO(objId)
    gg.setDisplayMode(objId,1)
    gg.setColor(objId,218,165,31)
  
    


##_points##  
    P5= geompy.MakeVertex(-1000, -1000, 0 )
    geompy.addToStudy(P5,"P5 ")
    geompy.PutToFolder(P5, Folder_Points)

    Vd1x_P5 = geompy.MakeVectorDXDYDZ(0, 1, 0)
    P5_vd1x=    geompy.MakeTranslationVectorDistance(P5,Vd1x_P5,1000)
    Vd1x_P5= geompy.MakeVector(P5,P5_vd1x)
    geompy.addToStudyInFather(P5,Vd1x_P5,"Vd1x_P5 " )
       
    Vd2x_P5 = geompy.MakeVectorDXDYDZ(-0.5773502691896258, -0.5773502691896258, -0.5773502691896258)
    P5_vd2x=    geompy.MakeTranslationVectorDistance(P5,Vd2x_P5,1000)
    Vd2x_P5= geompy.MakeVector(P5,P5_vd2x)
    geompy.addToStudyInFather(P5,Vd2x_P5,"Vd2x_P5 " )

    # Visualize a support(restriction DOF) at point P5
    #---------------------------------------------               
    P5_BLOCK_xyzrxryrz=geompy.MakeBox(-930.0,-930.0,70.0,-1070.0,-1070.0,-70.0)	
    P5_BLOCK_xyzrxryrz.SetColor(SALOMEDS.Color(1,1,0))
    P5_BLOCK_xyzrxryrz_id=geompy.addToStudyInFather( P5, P5_BLOCK_xyzrxryrz,'P5_BLOCK_xyzrxryrz' )
 #   B_id=geompy.addToStudy(P5_BLOCK_xyzrxryrz,'P5_BLOCK_xyzrxryrz' )
    
    List_ParaVis_Visualization.append(P5_BLOCK_xyzrxryrz)
    objId = geompy.getObjectID(P5_BLOCK_xyzrxryrz)    
    gg.createAndDisplayGO(objId)
    gg.setDisplayMode(objId,1)
    gg.setColor(objId,218,165,31)
  
    

##_vector_round_1D##
    ### geometry generation for  V0 ###
    #----------------------------------------------------
    print("Add V0")
    V0= geompy.MakeVector(P0,top)
    geompy.addToStudy(V0,"V0" )
    geompy.PutToFolder(V0, Folder_Vectors)

    _C1 = geompy.MakeCircle(P0, V0,35.0)
    _C2 = geompy.MakeCircle(P0, V0,31.0)
    FaceTube = geompy.MakeFaceWires([_C1, _C2], 1) 
           
    ### mesh generation for  V0 ###
    #----------------------------------------------------    
    V0M = smesh.Mesh(V0)
    Regular_1D = V0M.Segment()
    Regular_1D.NumberOfSegments(10)

    smesh.SetName(V0M,'V0')
    V0M.Compute()
    V0M.Group(P0)
    V0M.Group(top)
    V0M.GroupOnGeom(V0)

    structElemList.append(('CircularBeam', {'R': 35.0, 'Group_Maille': 'V0', 'EP': 4.0}))    
    List_ParaVis_Visualization.append("Beam_V0")
        

##_vector_round_1D##
    ### geometry generation for  V1 ###
    #----------------------------------------------------
    print("Add V1")
    V1= geompy.MakeVector(top,P2)
    geompy.addToStudy(V1,"V1" )
    geompy.PutToFolder(V1, Folder_Vectors)

    _C1 = geompy.MakeCircle(top, V1,35.0)
    _C2 = geompy.MakeCircle(top, V1,31.0)
    FaceTube = geompy.MakeFaceWires([_C1, _C2], 1) 
           
    ### mesh generation for  V1 ###
    #----------------------------------------------------    
    V1M = smesh.Mesh(V1)
    Regular_1D = V1M.Segment()
    Regular_1D.NumberOfSegments(10)

    smesh.SetName(V1M,'V1')
    V1M.Compute()
    V1M.Group(top)
    V1M.Group(P2)
    V1M.GroupOnGeom(V1)

    structElemList.append(('CircularBeam', {'R': 35.0, 'Group_Maille': 'V1', 'EP': 4.0}))    
    List_ParaVis_Visualization.append("Beam_V1")
        

##_vector_round_1D##
    ### geometry generation for  V2 ###
    #----------------------------------------------------
    print("Add V2")
    V2= geompy.MakeVector(top,P3)
    geompy.addToStudy(V2,"V2" )
    geompy.PutToFolder(V2, Folder_Vectors)

    _C1 = geompy.MakeCircle(top, V2,35.0)
    _C2 = geompy.MakeCircle(top, V2,31.0)
    FaceTube = geompy.MakeFaceWires([_C1, _C2], 1) 
           
    ### mesh generation for  V2 ###
    #----------------------------------------------------    
    V2M = smesh.Mesh(V2)
    Regular_1D = V2M.Segment()
    Regular_1D.NumberOfSegments(10)

    smesh.SetName(V2M,'V2')
    V2M.Compute()
    V2M.Group(top)
    V2M.Group(P3)
    V2M.GroupOnGeom(V2)

    structElemList.append(('CircularBeam', {'R': 35.0, 'Group_Maille': 'V2', 'EP': 4.0}))    
    List_ParaVis_Visualization.append("Beam_V2")
        

##_vector_round_1D##
    ### geometry generation for  V3 ###
    #----------------------------------------------------
    print("Add V3")
    V3= geompy.MakeVector(top,P4)
    geompy.addToStudy(V3,"V3" )
    geompy.PutToFolder(V3, Folder_Vectors)

    _C1 = geompy.MakeCircle(top, V3,35.0)
    _C2 = geompy.MakeCircle(top, V3,31.0)
    FaceTube = geompy.MakeFaceWires([_C1, _C2], 1) 
           
    ### mesh generation for  V3 ###
    #----------------------------------------------------    
    V3M = smesh.Mesh(V3)
    Regular_1D = V3M.Segment()
    Regular_1D.NumberOfSegments(10)

    smesh.SetName(V3M,'V3')
    V3M.Compute()
    V3M.Group(top)
    V3M.Group(P4)
    V3M.GroupOnGeom(V3)

    structElemList.append(('CircularBeam', {'R': 35.0, 'Group_Maille': 'V3', 'EP': 4.0}))    
    List_ParaVis_Visualization.append("Beam_V3")
        

##_vector_round_1D##
    ### geometry generation for  V4 ###
    #----------------------------------------------------
    print("Add V4")
    V4= geompy.MakeVector(top,P5)
    geompy.addToStudy(V4,"V4" )
    geompy.PutToFolder(V4, Folder_Vectors)

    _C1 = geompy.MakeCircle(top, V4,35.0)
    _C2 = geompy.MakeCircle(top, V4,31.0)
    FaceTube = geompy.MakeFaceWires([_C1, _C2], 1) 
           
    ### mesh generation for  V4 ###
    #----------------------------------------------------    
    V4M = smesh.Mesh(V4)
    Regular_1D = V4M.Segment()
    Regular_1D.NumberOfSegments(10)

    smesh.SetName(V4M,'V4')
    V4M.Compute()
    V4M.Group(top)
    V4M.Group(P5)
    V4M.GroupOnGeom(V4)

    structElemList.append(('CircularBeam', {'R': 35.0, 'Group_Maille': 'V4', 'EP': 4.0}))    
    List_ParaVis_Visualization.append("Beam_V4")
        

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
           V4M.GetMesh() ,], 1, 0, 1e-05)
    coincident_nodes = Completed_Mesh.FindCoincidentNodes( 1e-05 )
    Completed_Mesh.MergeNodes(coincident_nodes)
    equal_elements = Completed_Mesh.FindEqualElements(Completed_Mesh)    
    Completed_Mesh.MergeElements(equal_elements)   
    smesh.SetName(Completed_Mesh.GetMesh(), 'Completed_Mesh')
        

                               
##_finalize##                
    #exports the created mesh compound 
    try:
        Completed_Mesh.ExportMED( r'/home/jangeorg/TUBA/tutorials/000_Testing/011_CABLE/Completed_Mesh.mmed', 0)
    except:
        print ('ExportPartToMED() failed')


    #exports visualizations (structural elements, forces, etc) as a grouped geometry to be used in Paravis
    try:    
        geompy.ExportVTK(compound_paravis, '/home/jangeorg/TUBA/tutorials/000_Testing/011_CABLE/compound_paravis.vtk', 0.001)     
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