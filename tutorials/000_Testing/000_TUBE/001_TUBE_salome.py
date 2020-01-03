#!/usr/bin/python 3
# -*- coding: iso-8859-1 -*-

import time
time1=time.time()
import sys
sys.path.append('/home/cae/TUBA_2019/external/')

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

#from max
def takeSecond(elem):
    return elem[1]

def SortFacesByAreas(all_faces):
    print("SortFacesByAreas from max ",len(all_faces))
    alist=[]
    index = []

    for idx,face in enumerate(all_faces) :
        l,a,v = geompy.BasicProperties( face )
        alist.append((idx,a))
        #print(idx," Area ",a)

    #print("alist ",alist)
    alist.sort(key=takeSecond,reverse=False)
    #print("sorted ",alist)
    for a in alist:
        index.append(a[0])

    #print("index ",index)
    return index
##

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

    local_y_a = geompy.MakeVectorDXDYDZ(0, 1, 0)
    a_local_y=    geompy.MakeTranslationVectorDistance(a,local_y_a,1000)
    local_y_a= geompy.MakeVector(a,a_local_y)
    geompy.addToStudyInFather(a,local_y_a,"local_y_a " )
       
    local_x_a = geompy.MakeVectorDXDYDZ(1.0, 0.0, 0.0)
    a_local_x=    geompy.MakeTranslationVectorDistance(a,local_x_a,1000)
    local_x_a= geompy.MakeVector(a,a_local_x)
    geompy.addToStudyInFather(a,local_x_a,"local_x_a " )
    
    aM = smesh.Mesh(a)
    aM.Compute()
    aM.Group(a)
    aM.GroupOnGeom(a)


    

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
    P1_2_center= geompy.MakeVertex(1000.0, 500.0, 0.0 )
    geompy.addToStudy(P1_2_center,"P1_2_center ")
    geompy.PutToFolder(P1_2_center, Folder_Points)

    local_y_P1_2_center = geompy.MakeVectorDXDYDZ(0, 1, 0)
    P1_2_center_local_y=    geompy.MakeTranslationVectorDistance(P1_2_center,local_y_P1_2_center,1000)
    local_y_P1_2_center= geompy.MakeVector(P1_2_center,P1_2_center_local_y)
    geompy.addToStudyInFather(P1_2_center,local_y_P1_2_center,"local_y_P1_2_center " )
       
    local_x_P1_2_center = geompy.MakeVectorDXDYDZ(1, 0, 0)
    P1_2_center_local_x=    geompy.MakeTranslationVectorDistance(P1_2_center,local_x_P1_2_center,1000)
    local_x_P1_2_center= geompy.MakeVector(P1_2_center,P1_2_center_local_x)
    geompy.addToStudyInFather(P1_2_center,local_x_P1_2_center,"local_x_P1_2_center " )
    
    P1_2_centerM = smesh.Mesh(P1_2_center)
    P1_2_centerM.Compute()
    P1_2_centerM.Group(P1_2_center)
    P1_2_centerM.GroupOnGeom(P1_2_center)


    


##_points##  
    P2= geompy.MakeVertex(1500.0, 499.99999999999994, 0.0 )
    geompy.addToStudy(P2,"P2 ")
    geompy.PutToFolder(P2, Folder_Points)

    local_y_P2 = geompy.MakeVectorDXDYDZ(-1.0, 6.123233995736766e-17, 0.0)
    P2_local_y=    geompy.MakeTranslationVectorDistance(P2,local_y_P2,1000)
    local_y_P2= geompy.MakeVector(P2,P2_local_y)
    geompy.addToStudyInFather(P2,local_y_P2,"local_y_P2 " )
       
    local_x_P2 = geompy.MakeVectorDXDYDZ(6.123233995736766e-17, 1.0, 0.0)
    P2_local_x=    geompy.MakeTranslationVectorDistance(P2,local_x_P2,1000)
    local_x_P2= geompy.MakeVector(P2,P2_local_x)
    geompy.addToStudyInFather(P2,local_x_P2,"local_x_P2 " )
    
    P2M = smesh.Mesh(P2)
    P2M.Compute()
    P2M.Group(P2)
    P2M.GroupOnGeom(P2)


    


##_points##  
    P3= geompy.MakeVertex(1500.0, 550.0, 0.0 )
    geompy.addToStudy(P3,"P3 ")
    geompy.PutToFolder(P3, Folder_Points)

    local_y_P3 = geompy.MakeVectorDXDYDZ(6.123233995736766e-17, 1.0, 0.0)
    P3_local_y=    geompy.MakeTranslationVectorDistance(P3,local_y_P3,1000)
    local_y_P3= geompy.MakeVector(P3,P3_local_y)
    geompy.addToStudyInFather(P3,local_y_P3,"local_y_P3 " )
       
    local_x_P3 = geompy.MakeVectorDXDYDZ(6.123233995736766e-17, 1.0, 0.0)
    P3_local_x=    geompy.MakeTranslationVectorDistance(P3,local_x_P3,1000)
    local_x_P3= geompy.MakeVector(P3,P3_local_x)
    geompy.addToStudyInFather(P3,local_x_P3,"local_x_P3 " )
    
    P3M = smesh.Mesh(P3)
    P3M.Compute()
    P3M.Group(P3)
    P3M.GroupOnGeom(P3)


    

    # Visualize a support(restriction DOF) at point P3
    #---------------------------------------------
    P3_BLOCK_xyzrxryrz=geompy.MakeBox(1570.0,620.0,70.0,1430.0,480.0,-70.0)	
    P3_BLOCK_xyzrxryrz.SetColor(SALOMEDS.Color(1,1,0))
    P3_BLOCK_xyzrxryrz_id=geompy.addToStudyInFather( P3, P3_BLOCK_xyzrxryrz,'P3_BLOCK_xyzrxryrz' )
 #   B_id=geompy.addToStudy(P3_BLOCK_xyzrxryrz,'P3_BLOCK_xyzrxryrz' )

    List_ParaVis_Visualization.append(P3_BLOCK_xyzrxryrz)
    objId = geompy.getObjectID(P3_BLOCK_xyzrxryrz)    
    gg.createAndDisplayGO(objId)
    gg.setDisplayMode(objId,1)
    gg.setColor(objId,218,165,31)

    


##_points##  
    P4= geompy.MakeVertex(1500.0, 1050.0, 0.0 )
    geompy.addToStudy(P4,"P4 ")
    geompy.PutToFolder(P4, Folder_Points)

    local_y_P4 = geompy.MakeVectorDXDYDZ(0, 1, 0)
    P4_local_y=    geompy.MakeTranslationVectorDistance(P4,local_y_P4,1000)
    local_y_P4= geompy.MakeVector(P4,P4_local_y)
    geompy.addToStudyInFather(P4,local_y_P4,"local_y_P4 " )
       
    local_x_P4 = geompy.MakeVectorDXDYDZ(6.123233995736766e-17, 1.0, 0.0)
    P4_local_x=    geompy.MakeTranslationVectorDistance(P4,local_x_P4,1000)
    local_x_P4= geompy.MakeVector(P4,P4_local_x)
    geompy.addToStudyInFather(P4,local_x_P4,"local_x_P4 " )
    
    P4M = smesh.Mesh(P4)
    P4M.Compute()
    P4M.Group(P4)
    P4M.GroupOnGeom(P4)


    


##_points##  
    P4_5_center= geompy.MakeVertex(500.0, 1050.0, 0.0 )
    geompy.addToStudy(P4_5_center,"P4_5_center ")
    geompy.PutToFolder(P4_5_center, Folder_Points)

    local_y_P4_5_center = geompy.MakeVectorDXDYDZ(0, 1, 0)
    P4_5_center_local_y=    geompy.MakeTranslationVectorDistance(P4_5_center,local_y_P4_5_center,1000)
    local_y_P4_5_center= geompy.MakeVector(P4_5_center,P4_5_center_local_y)
    geompy.addToStudyInFather(P4_5_center,local_y_P4_5_center,"local_y_P4_5_center " )
       
    local_x_P4_5_center = geompy.MakeVectorDXDYDZ(1, 0, 0)
    P4_5_center_local_x=    geompy.MakeTranslationVectorDistance(P4_5_center,local_x_P4_5_center,1000)
    local_x_P4_5_center= geompy.MakeVector(P4_5_center,P4_5_center_local_x)
    geompy.addToStudyInFather(P4_5_center,local_x_P4_5_center,"local_x_P4_5_center " )
    
    P4_5_centerM = smesh.Mesh(P4_5_center)
    P4_5_centerM.Compute()
    P4_5_centerM.Group(P4_5_center)
    P4_5_centerM.GroupOnGeom(P4_5_center)


    


##_points##  
    P5= geompy.MakeVertex(500.0000000000001, 2050.0, 0.0 )
    geompy.addToStudy(P5,"P5 ")
    geompy.PutToFolder(P5, Folder_Points)

    local_y_P5 = geompy.MakeVectorDXDYDZ(-1.0, 6.123233995736766e-17, 0.0)
    P5_local_y=    geompy.MakeTranslationVectorDistance(P5,local_y_P5,1000)
    local_y_P5= geompy.MakeVector(P5,P5_local_y)
    geompy.addToStudyInFather(P5,local_y_P5,"local_y_P5 " )
       
    local_x_P5 = geompy.MakeVectorDXDYDZ(-1.0, 1.2246467991473532e-16, 0.0)
    P5_local_x=    geompy.MakeTranslationVectorDistance(P5,local_x_P5,1000)
    local_x_P5= geompy.MakeVector(P5,P5_local_x)
    geompy.addToStudyInFather(P5,local_x_P5,"local_x_P5 " )
    
    P5M = smesh.Mesh(P5)
    P5M.Compute()
    P5M.Group(P5)
    P5M.GroupOnGeom(P5)


    

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
        
        
    structElemList.append(('CircularBeam', {'R1': 35.0,'R2': 135.0, 'Group_Maille': 'V2', 'EP1': 4.0, 'EP2': 4.0}))    
    List_ParaVis_Visualization.append("Beam_V2")
        

##_vector_round_1D##
    ### geometry generation for  V3 ###
    #----------------------------------------------------
    print("Add V3")
    V3= geompy.MakeVector(P3,P4)
    geompy.addToStudy(V3,"V3" )
    geompy.PutToFolder(V3, Folder_Vectors)

    ### mesh generation for  V3 ###
    #----------------------------------------------------    
    V3M = smesh.Mesh(V3)
    Regular_1D = V3M.Segment()
    Regular_1D.NumberOfSegments(10)

    smesh.SetName(V3M,'V3')
    V3M.Compute()
    V3M.Group(P3)
    V3M.Group(P4)
    V3M.GroupOnGeom(V3)
        
        
    structElemList.append(('CircularBeam', {'R': 135.0, 'Group_Maille': 'V3', 'EP': 4.0}))    
    List_ParaVis_Visualization.append("Beam_V3")
        

##_bent_1D##
    ### geometry generation for  V4_Bent ###
    #----------------------------------------------------

    print("Add  V4_Bent ")
    V4_Bent = geompy.MakeArcCenter(P4_5_center,P4,P5)
    geompy.addToStudy(V4_Bent,"V4_Bent")

    ### mesh generation for  V4_Bent ###
    #----------------------------------------------------    

    V4_BentM = smesh.Mesh(V4_Bent)
    Regular_1D = V4_BentM.Segment()
    Regular_1D.NumberOfSegments(10)

    smesh.SetName(V4_BentM,'V4_Bent')
    V4_BentM.Compute()
    V4_BentM.Group(P4)
    V4_BentM.Group(P5)
    V4_BentM.GroupOnGeom(V4_Bent)


    structElemList.append(('CircularBeam', {'R': 135.0, 'Group_Maille': 'V4_Bent', 'EP': 4.0}))             
    List_ParaVis_Visualization.append("Beam_V4_Bent")

            

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

    Completed_Mesh = smesh.Concatenate([V0M.GetMesh() ,V1_BentM.GetMesh() ,V2M.GetMesh() ,
           V3M.GetMesh() ,V4_BentM.GetMesh() ,aM.GetMesh() ,P1M.GetMesh() ,
           P1_2_centerM.GetMesh() ,P2M.GetMesh() ,P3M.GetMesh() ,P4M.GetMesh() ,
           P4_5_centerM.GetMesh() ,P5M.GetMesh() ,], 1, 0, 1e-05)
    coincident_nodes = Completed_Mesh.FindCoincidentNodes( 1e-05 )
    Completed_Mesh.MergeNodes(coincident_nodes)
    equal_elements = Completed_Mesh.FindEqualElements(Completed_Mesh)    
    Completed_Mesh.MergeElements(equal_elements)   
    smesh.SetName(Completed_Mesh.GetMesh(), 'Completed_Mesh')
        


##_finalize##
    #exports the created mesh compound 
    try:
        Completed_Mesh.ExportMED( r'/home/cae/TUBA_2019/tutorials/000_Testing/000_TUBE/001_TUBE.mmed', 0)
    except:
        print ('ExportPartToMED() failed')

    #exports visualizations (structural elements, forces, etc) as a grouped geometry to be used in Paravis
    try:
        geompy.ExportVTK(compound_paravis, '/home/cae/TUBA_2019/tutorials/000_Testing/000_TUBE/compound_paravis.vtk', 0.001)     
    except:
        print ('ExportVTK of the visualization compound failed')

    if salome.sg.hasDesktop():
       salome.sg.updateObjBrowser()
    time2=time.time()
    dtime = time2 - time1
    print("------------------------")
    print("Duration of construction:"+str(round(dtime,2))+"s")







    
Project()