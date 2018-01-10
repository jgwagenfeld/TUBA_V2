#!/usr/bin/python 3
# -*- coding: iso-8859-1 -*-

import time
time1=time.time()
import sys
sys.path.append(' /home/jangeorg/TUBA/tutorials/000_Testing/009_BAR ')

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
       
    Vd2x_P0 = geompy.MakeVectorDXDYDZ(1.0, 0.0, 0.0)
    P0_vd2x=    geompy.MakeTranslationVectorDistance(P0,Vd2x_P0,1000)
    Vd2x_P0= geompy.MakeVector(P0,P0_vd2x)
    geompy.addToStudyInFather(P0,Vd2x_P0,"Vd2x_P0 " )
        
 
    Radius=35.0

    Pna=geompy.MakeVertexWithRef(P0,105.0,0,0)
    Pnb=geompy.MakeVertexWithRef(P0,70.0,0,0)  
    Vp=geompy.MakeVector(Pna,Pnb)  
    Cone1 = geompy.MakeCone(Pna,Vp,Radius,0,2*Radius)

   
    P2a=geompy.MakeVertexWithRef(P0,-105.0,0,0)    
    P2b=geompy.MakeVertexWithRef(P0,-70.0,0,0)    
    Vm=geompy.MakeVector(P2a,P2b)  
    Cone2 = geompy.MakeCone(P2a,Vm,Radius,0,2*Radius)
    
    BLOCK_x=geompy.MakeCompound([Cone1,Cone2])
    BLOCK_x.SetColor(SALOMEDS.Color(1,1,0))
    B_id=geompy.addToStudyInFather( P0, BLOCK_x,'P0_BLOCK_x' )    

    List_ParaVis_Visualization.append(BLOCK_x)
    gg.createAndDisplayGO(B_id)
    gg.setDisplayMode(B_id,1)
    
        
 
    Radius=35.0

    Pna=geompy.MakeVertexWithRef(P0,0,105.0,0)
    Pnb=geompy.MakeVertexWithRef(P0,0,70.0,0)  
    Vp=geompy.MakeVector(Pna,Pnb)  
    Cone1 = geompy.MakeCone(Pna,Vp,Radius,0,2*Radius)

   
    P2a=geompy.MakeVertexWithRef(P0,0,-105.0,0)    
    P2b=geompy.MakeVertexWithRef(P0,0,-70.0,0)    
    Vm=geompy.MakeVector(P2a,P2b)  
    Cone2 = geompy.MakeCone(P2a,Vm,Radius,0,2*Radius)
    
    BLOCK_y=geompy.MakeCompound([Cone1,Cone2])
    BLOCK_y.SetColor(SALOMEDS.Color(1,1,0))
    B_id=geompy.addToStudyInFather( P0, BLOCK_y,'P0_BLOCK_y' )    

    List_ParaVis_Visualization.append(BLOCK_y)
    gg.createAndDisplayGO(B_id)
    gg.setDisplayMode(B_id,1)
    
        
 
    Radius=35.0

    Pna=geompy.MakeVertexWithRef(P0,0,0,105.0)
    Pnb=geompy.MakeVertexWithRef(P0,0,0,70.0)  
    Vp=geompy.MakeVector(Pna,Pnb)  
    Cone1 = geompy.MakeCone(Pna,Vp,Radius,0,2*Radius)

   
    P2a=geompy.MakeVertexWithRef(P0,0,0,-105.0)    
    P2b=geompy.MakeVertexWithRef(P0,0,0,-70.0)    
    Vm=geompy.MakeVector(P2a,P2b)  
    Cone2 = geompy.MakeCone(P2a,Vm,Radius,0,2*Radius)
    
    BLOCK_z=geompy.MakeCompound([Cone1,Cone2])
    BLOCK_z.SetColor(SALOMEDS.Color(1,1,0))
    B_id=geompy.addToStudyInFather( P0, BLOCK_z,'P0_BLOCK_z' )    

    List_ParaVis_Visualization.append(BLOCK_z)
    gg.createAndDisplayGO(B_id)
    gg.setDisplayMode(B_id,1)
    


##_points##  
    P1= geompy.MakeVertex(1000, 0, 0 )
    geompy.addToStudy(P1,"P1 ")
    geompy.PutToFolder(P1, Folder_Points)

    Vd1x_P1 = geompy.MakeVectorDXDYDZ(1.0, 0.0, 0.0)
    P1_vd1x=    geompy.MakeTranslationVectorDistance(P1,Vd1x_P1,1000)
    Vd1x_P1= geompy.MakeVector(P1,P1_vd1x)
    geompy.addToStudyInFather(P1,Vd1x_P1,"Vd1x_P1 " )
       
    Vd2x_P1 = geompy.MakeVectorDXDYDZ(-0.4472135954999579, 0.0, 0.8944271909999159)
    P1_vd2x=    geompy.MakeTranslationVectorDistance(P1,Vd2x_P1,1000)
    Vd2x_P1= geompy.MakeVector(P1,P1_vd2x)
    geompy.addToStudyInFather(P1,Vd2x_P1,"Vd2x_P1 " )
        
 
    Radius=35.0

    Pna=geompy.MakeVertexWithRef(P1,105.0,0,0)
    Pnb=geompy.MakeVertexWithRef(P1,70.0,0,0)  
    Vp=geompy.MakeVector(Pna,Pnb)  
    Cone1 = geompy.MakeCone(Pna,Vp,Radius,0,2*Radius)

   
    P2a=geompy.MakeVertexWithRef(P1,-105.0,0,0)    
    P2b=geompy.MakeVertexWithRef(P1,-70.0,0,0)    
    Vm=geompy.MakeVector(P2a,P2b)  
    Cone2 = geompy.MakeCone(P2a,Vm,Radius,0,2*Radius)
    
    BLOCK_x=geompy.MakeCompound([Cone1,Cone2])
    BLOCK_x.SetColor(SALOMEDS.Color(1,1,0))
    B_id=geompy.addToStudyInFather( P1, BLOCK_x,'P1_BLOCK_x' )    

    List_ParaVis_Visualization.append(BLOCK_x)
    gg.createAndDisplayGO(B_id)
    gg.setDisplayMode(B_id,1)
    
        
 
    Radius=35.0

    Pna=geompy.MakeVertexWithRef(P1,0,105.0,0)
    Pnb=geompy.MakeVertexWithRef(P1,0,70.0,0)  
    Vp=geompy.MakeVector(Pna,Pnb)  
    Cone1 = geompy.MakeCone(Pna,Vp,Radius,0,2*Radius)

   
    P2a=geompy.MakeVertexWithRef(P1,0,-105.0,0)    
    P2b=geompy.MakeVertexWithRef(P1,0,-70.0,0)    
    Vm=geompy.MakeVector(P2a,P2b)  
    Cone2 = geompy.MakeCone(P2a,Vm,Radius,0,2*Radius)
    
    BLOCK_y=geompy.MakeCompound([Cone1,Cone2])
    BLOCK_y.SetColor(SALOMEDS.Color(1,1,0))
    B_id=geompy.addToStudyInFather( P1, BLOCK_y,'P1_BLOCK_y' )    

    List_ParaVis_Visualization.append(BLOCK_y)
    gg.createAndDisplayGO(B_id)
    gg.setDisplayMode(B_id,1)
    
        
 
    Radius=35.0

    Pna=geompy.MakeVertexWithRef(P1,0,0,105.0)
    Pnb=geompy.MakeVertexWithRef(P1,0,0,70.0)  
    Vp=geompy.MakeVector(Pna,Pnb)  
    Cone1 = geompy.MakeCone(Pna,Vp,Radius,0,2*Radius)

   
    P2a=geompy.MakeVertexWithRef(P1,0,0,-105.0)    
    P2b=geompy.MakeVertexWithRef(P1,0,0,-70.0)    
    Vm=geompy.MakeVector(P2a,P2b)  
    Cone2 = geompy.MakeCone(P2a,Vm,Radius,0,2*Radius)
    
    BLOCK_z=geompy.MakeCompound([Cone1,Cone2])
    BLOCK_z.SetColor(SALOMEDS.Color(1,1,0))
    B_id=geompy.addToStudyInFather( P1, BLOCK_z,'P1_BLOCK_z' )    

    List_ParaVis_Visualization.append(BLOCK_z)
    gg.createAndDisplayGO(B_id)
    gg.setDisplayMode(B_id,1)
    


##_points##  
    P2= geompy.MakeVertex(500, 0, 1000 )
    geompy.addToStudy(P2,"P2 ")
    geompy.PutToFolder(P2, Folder_Points)

    Vd1x_P2 = geompy.MakeVectorDXDYDZ(-0.4472135954999579, 0.0, 0.8944271909999159)
    P2_vd1x=    geompy.MakeTranslationVectorDistance(P2,Vd1x_P2,1000)
    Vd1x_P2= geompy.MakeVector(P2,P2_vd1x)
    geompy.addToStudyInFather(P2,Vd1x_P2,"Vd1x_P2 " )
       
    Vd2x_P2 = geompy.MakeVectorDXDYDZ(-0.4472135954999579, 0.0, -0.8944271909999159)
    P2_vd2x=    geompy.MakeTranslationVectorDistance(P2,Vd2x_P2,1000)
    Vd2x_P2= geompy.MakeVector(P2,P2_vd2x)
    geompy.addToStudyInFather(P2,Vd2x_P2,"Vd2x_P2 " )
        
 
    Radius=35.0

    Pna=geompy.MakeVertexWithRef(P2,105.0,0,0)
    Pnb=geompy.MakeVertexWithRef(P2,70.0,0,0)  
    Vp=geompy.MakeVector(Pna,Pnb)  
    Cone1 = geompy.MakeCone(Pna,Vp,Radius,0,2*Radius)

   
    P2a=geompy.MakeVertexWithRef(P2,-105.0,0,0)    
    P2b=geompy.MakeVertexWithRef(P2,-70.0,0,0)    
    Vm=geompy.MakeVector(P2a,P2b)  
    Cone2 = geompy.MakeCone(P2a,Vm,Radius,0,2*Radius)
    
    BLOCK_x=geompy.MakeCompound([Cone1,Cone2])
    BLOCK_x.SetColor(SALOMEDS.Color(1,1,0))
    B_id=geompy.addToStudyInFather( P2, BLOCK_x,'P2_BLOCK_x' )    

    List_ParaVis_Visualization.append(BLOCK_x)
    gg.createAndDisplayGO(B_id)
    gg.setDisplayMode(B_id,1)
    
        
 
    Radius=35.0

    Pna=geompy.MakeVertexWithRef(P2,0,105.0,0)
    Pnb=geompy.MakeVertexWithRef(P2,0,70.0,0)  
    Vp=geompy.MakeVector(Pna,Pnb)  
    Cone1 = geompy.MakeCone(Pna,Vp,Radius,0,2*Radius)

   
    P2a=geompy.MakeVertexWithRef(P2,0,-105.0,0)    
    P2b=geompy.MakeVertexWithRef(P2,0,-70.0,0)    
    Vm=geompy.MakeVector(P2a,P2b)  
    Cone2 = geompy.MakeCone(P2a,Vm,Radius,0,2*Radius)
    
    BLOCK_y=geompy.MakeCompound([Cone1,Cone2])
    BLOCK_y.SetColor(SALOMEDS.Color(1,1,0))
    B_id=geompy.addToStudyInFather( P2, BLOCK_y,'P2_BLOCK_y' )    

    List_ParaVis_Visualization.append(BLOCK_y)
    gg.createAndDisplayGO(B_id)
    gg.setDisplayMode(B_id,1)
    
        
 
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
    P3= geompy.MakeVertex(0, 0, 0 )
    geompy.addToStudy(P3,"P3 ")
    geompy.PutToFolder(P3, Folder_Points)

    Vd1x_P3 = geompy.MakeVectorDXDYDZ(0, 1, 0)
    P3_vd1x=    geompy.MakeTranslationVectorDistance(P3,Vd1x_P3,1000)
    Vd1x_P3= geompy.MakeVector(P3,P3_vd1x)
    geompy.addToStudyInFather(P3,Vd1x_P3,"Vd1x_P3 " )
       
    Vd2x_P3 = geompy.MakeVectorDXDYDZ(-0.4472135954999579, 0.0, -0.8944271909999159)
    P3_vd2x=    geompy.MakeTranslationVectorDistance(P3,Vd2x_P3,1000)
    Vd2x_P3= geompy.MakeVector(P3,P3_vd2x)
    geompy.addToStudyInFather(P3,Vd2x_P3,"Vd2x_P3 " )

##_vector_round_1D##
    ### geometry generation for  V0 ###
    #----------------------------------------------------
    print("Add V0")
    V0= geompy.MakeVector(P0,P1)
    geompy.addToStudy(V0,"V0" )
    geompy.PutToFolder(V0, Folder_Vectors)

    _C1 = geompy.MakeCircle(P0, V0,35.0)
    _C2 = geompy.MakeCircle(P0, V0,31.0)
    FaceTube = geompy.MakeFaceWires([_C1, _C2], 1) 
           
    ### mesh generation for  V0 ###
    #----------------------------------------------------    
    V0M = smesh.Mesh(V0)
    Regular_1D = V0M.Segment()
    Regular_1D.NumberOfSegments(1)

    smesh.SetName(V0M,'V0')
    V0M.Compute()
    V0M.Group(P0)
    V0M.Group(P1)
    V0M.GroupOnGeom(V0)

    structElemList.append(('CircularBeam', {'R': 35.0, 'Group_Maille': 'V0', 'EP': 4.0}))    
    List_ParaVis_Visualization.append("Beam_V0")
        

##_vector_round_1D##
    ### geometry generation for  V1 ###
    #----------------------------------------------------
    print("Add V1")
    V1= geompy.MakeVector(P1,P2)
    geompy.addToStudy(V1,"V1" )
    geompy.PutToFolder(V1, Folder_Vectors)

    _C1 = geompy.MakeCircle(P1, V1,35.0)
    _C2 = geompy.MakeCircle(P1, V1,31.0)
    FaceTube = geompy.MakeFaceWires([_C1, _C2], 1) 
           
    ### mesh generation for  V1 ###
    #----------------------------------------------------    
    V1M = smesh.Mesh(V1)
    Regular_1D = V1M.Segment()
    Regular_1D.NumberOfSegments(1)

    smesh.SetName(V1M,'V1')
    V1M.Compute()
    V1M.Group(P1)
    V1M.Group(P2)
    V1M.GroupOnGeom(V1)

    structElemList.append(('CircularBeam', {'R': 35.0, 'Group_Maille': 'V1', 'EP': 4.0}))    
    List_ParaVis_Visualization.append("Beam_V1")
        

##_vector_round_1D##
    ### geometry generation for  V2 ###
    #----------------------------------------------------
    print("Add V2")
    V2= geompy.MakeVector(P2,P3)
    geompy.addToStudy(V2,"V2" )
    geompy.PutToFolder(V2, Folder_Vectors)

    _C1 = geompy.MakeCircle(P2, V2,35.0)
    _C2 = geompy.MakeCircle(P2, V2,31.0)
    FaceTube = geompy.MakeFaceWires([_C1, _C2], 1) 
           
    ### mesh generation for  V2 ###
    #----------------------------------------------------    
    V2M = smesh.Mesh(V2)
    Regular_1D = V2M.Segment()
    Regular_1D.NumberOfSegments(1)

    smesh.SetName(V2M,'V2')
    V2M.Compute()
    V2M.Group(P2)
    V2M.Group(P3)
    V2M.GroupOnGeom(V2)

    structElemList.append(('CircularBeam', {'R': 35.0, 'Group_Maille': 'V2', 'EP': 4.0}))    
    List_ParaVis_Visualization.append("Beam_V2")
        

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

    Completed_Mesh = smesh.Concatenate([V0M.GetMesh() , V1M.GetMesh() , V2M.GetMesh() ,], 1, 0, 1e-05)
    coincident_nodes = Completed_Mesh.FindCoincidentNodes( 1e-05 )
    Completed_Mesh.MergeNodes(coincident_nodes)
    equal_elements = Completed_Mesh.FindEqualElements(Completed_Mesh)    
    Completed_Mesh.MergeElements(equal_elements)   
    smesh.SetName(Completed_Mesh.GetMesh(), 'Completed_Mesh')
        

                               
##_finalize##                
    #exports the created mesh compound 
    try:
        Completed_Mesh.ExportMED( r'/home/jangeorg/TUBA/tutorials/000_Testing/009_BAR/Completed_Mesh.mmed', 0)
    except:
        print ('ExportPartToMED() failed')


    #exports visualizations (structural elements, forces, etc) as a grouped geometry to be used in Paravis
    try:    
        geompy.ExportVTK(compound_paravis, '/home/jangeorg/TUBA/tutorials/000_Testing/009_BAR/compound_paravis.vtk', 0.001)     
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