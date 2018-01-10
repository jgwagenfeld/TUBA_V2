#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 02:34:03 2016

"""
import collections
import numpy as np
import external.euclid as eu
import logging

import tuba_vars_and_funcs as tub
import tuba.define_geometry as tuba_geom
#import library_material


class Salome:

    def __init__(self, current_directory):
        self.current_directory=current_directory
        self.lines=[]
#==============================================================================
    def write(self,dict_tubavectors,dict_tubapoints):

        self._initialize()

        for tubapoint in dict_tubapoints:
            tubapoint.is_element_start()

        for tubapoint in dict_tubapoints:
            logging.debug("Processing TubaPoint: "+ tubapoint.name+ " \n ====")
            self._point(tubapoint)
            print("DDL", tubapoint.ddl)
            print("LastVector",str(tubapoint.get_last_vector())) 
            
            
            if tubapoint.get_last_vector():               
                section=tubapoint.get_last_vector().section
            elif tubapoint.get_next_vector():
                section=tubapoint.get_next_vector().section
            
            if section:
                self._visualize_stiffness(tubapoint,section)            
                self._visualize_ddl(tubapoint,section)
                self._visualize_stiffness(tubapoint,section)
                self._visualize_force(tubapoint,section)
                self._visualize_mass(tubapoint,section)                
            if not tubapoint.stiffness==[0.0, 0.0, 0.0, 0.0, 0.0, 0.0]:
                self._stiffness_mesh(tubapoint)
            if not tubapoint.friction_coefficient == 0.0:  
                self._friction_mesh(tubapoint)
                
        for tubavector in dict_tubavectors:
            print('Turbavector',tubavector.__class__.__name__)
            logging.debug("Processing TubaVector: "+tubavector.name+ " \n ====")
            self._vector(tubavector)
#            self._visualize_Pipe_1D(tubavector)

        self._create_paravis_geometry_compound()
        self._create_mesh_compound(dict_tubavectors,dict_tubapoints)
        self._finalize()


#==============================================================================
    def _initialize(self):
        self.lines=self.lines+(
"""#!/usr/bin/python 3
# -*- coding: iso-8859-1 -*-

import time
time1=time.time()
import sys
sys.path.append(' """+self.current_directory+""" ')

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

            """).split("\n")

#==============================================================================
    def _point(self,tubapoint):
        """Writes the python code to construct a point and the current direction-vector in Salome"""

        pos = str(tubapoint.pos.xyz).strip('()')
        name_point =tubapoint.name

        self.lines=self.lines+("""

##_points##  
    """+name_point+"""= geompy.MakeVertex("""+pos+ """ )
    geompy.addToStudy("""+name_point+",\""+ name_point+""" \")
    geompy.PutToFolder("""+name_point+""", Folder_Points)""").split("\n")
        
        #if not tubapoint.is_element_end():
        vd2x = str(tubapoint.vd2x.xyz).strip('()')
        vd1x = str(tubapoint.vd1x.xyz).strip('()')
        self.lines=self.lines+("""
    Vd1x_"""+name_point+" = geompy.MakeVectorDXDYDZ("+vd1x+""")
    """ +name_point+"_vd1x=    geompy.MakeTranslationVectorDistance("+name_point+",Vd1x_"+name_point+""",1000)
    Vd1x_"""+name_point+"= geompy.MakeVector("+name_point+","+name_point+"""_vd1x)
    geompy.addToStudyInFather("""+name_point+",Vd1x_"""+name_point+",\"Vd1x_"+ name_point+""" " )
       
    Vd2x_"""+name_point+" = geompy.MakeVectorDXDYDZ("+vd2x+""")
    """ +name_point+"_vd2x=    geompy.MakeTranslationVectorDistance("+name_point+",Vd2x_"+name_point+""",1000)
    Vd2x_"""+name_point+"= geompy.MakeVector("+name_point+","+name_point+"""_vd2x)
    geompy.addToStudyInFather("""+name_point+",Vd2x_"""+name_point+",\"Vd2x_"+ name_point+""" " )"""
    
    ).split("\n")

#==============================================================================
    def _stiffness_mesh(self,tubapoint):
        name_point = str(tubapoint.name)
        
        self.lines=self.lines+("""  
##_stiffness_mesh##  
    ### create dummy-gemoetry for a mesh to model stiffness in CodeAster at """+name_point+"""
    #----------------------------------------------------   
    """+name_point+ "K= geompy.MakeVertexWithRef("+name_point+""", 1, 1, 1)
    Spring"""+name_point+"= geompy.MakeLineTwoPnt("+name_point+", "+name_point+"""K)
    geompy.addToStudy( """+name_point+ "K, '"+name_point+ """K' )
    geompy.addToStudy( Spring"""+name_point+", 'Spring"""+name_point+"""' ) 

    Spring"""+name_point+"M = smesh.Mesh(Spring"+  name_point +""")
    Decoupage = Spring"""+ name_point+"""M.Segment()
    Decoupage.NumberOfSegments("""+str(1)+""")
    smesh.SetName(Spring"""+ name_point+"M,'Spring"+name_point+"""')
    Spring"""+name_point+"""M.Compute()
    Spring"""+name_point+"M.Group("+name_point+""")
    Spring"""+name_point+"M.Group("+name_point+"""K)
    Spring"""+name_point+"M.GroupOnGeom(Spring"+name_point+""")
      
""").split("\n")
            
#============================================================================== 
    def _friction_mesh(self,tubapoint):
        name_point = str(tubapoint.name)
        
        self.lines=self.lines+("""  
##_friction_mesh##
    ### create dummy-gemoetry for a mesh to model a friction-stiffness in CodeAster at """+name_point+"""
    #----------------------------------------------------   
    """+name_point+ "_f= geompy.MakeVertexWithRef("+name_point+""", -1, -1, -1)
    Friction"""+name_point+"= geompy.MakeLineTwoPnt("+name_point+", "+name_point+"""_f)
    geompy.addToStudy( """+name_point+ "_f, '"+name_point+ """_f' )
    geompy.addToStudy( Friction"""+name_point+", 'Friction"""+name_point+"""' ) 

    Friction"""+name_point+"M = smesh.Mesh(Friction"+  name_point +""")
    Decoupage = Friction"""+ name_point+"""M.Segment()
    Decoupage.NumberOfSegments("""+str(1)+""")
    smesh.SetName(Friction"""+ name_point+"M,'Friction"+name_point+"""')
    Friction"""+name_point+"""M.Compute()
    Friction"""+name_point+"M.Group("+name_point+""")
    Friction"""+name_point+"M.Group("+name_point+"""_f)
    Friction"""+name_point+"M.GroupOnGeom(Friction"+name_point+""")
    
""").split("\n")
            

           
#==============================================================================
    def _vector(self,tubavector) :
        """Writes the python code to construct a Vector in Salome"""

        if isinstance(tubavector, tuba_geom.TubaBent):
            if tubavector.model in ["VOLUME"]:
                self._bent_3D(tubavector)
            else:    
                self._bent_1D(tubavector)
                
        elif isinstance(tubavector, tuba_geom.TubaTShape3D):
            self._TShape_3D(tubavector)

        elif isinstance(tubavector, tuba_geom.TubaVector):
            if tubavector.model in ["VOLUME"]:
                self._vector_round_3D(tubavector)

            elif tubavector.model in ["TUBE","TUYAU","BAR"]:
                self._vector_round_1D(tubavector)

            elif tubavector.model in ["POUTRE_RECTANGLE", "RECTANGULAR"]:
                self._vector_rectangular_1D(tubavector)

            else:
                print("Model is not defined")

#==============================================================================
    def _vector_round_1D(self,tubavector):
        """This function creates a round tube-profile with the specified wall thickness as visualization
        The actual mesh is only one-dimensional. The crosssection is later specified in the Aster-File"""

        [radius,thickness]=tubavector.section
        model=tubavector.model

        name_startpoint = tubavector.start_tubapoint.name
        name_endpoint=tubavector.end_tubapoint.name

        name_vector = str(tubavector.name)

        self.lines=self.lines+("""
##_vector_round_1D##
    ### geometry generation for  """+ name_vector +""" ###
    #----------------------------------------------------
    print(\"Add """+name_vector+"""\")
    """+name_vector+"= geompy.MakeVector("+name_startpoint+","+name_endpoint+""")
    geompy.addToStudy("""+name_vector+",\""+name_vector+"""\" )
    geompy.PutToFolder("""+name_vector+""", Folder_Vectors)

    _C1 = geompy.MakeCircle("""+name_startpoint+", "+name_vector+","+str(radius)+""")
    _C2 = geompy.MakeCircle("""+name_startpoint+", "+name_vector+","+str(radius-thickness)+""")
    FaceTube = geompy.MakeFaceWires([_C1, _C2], 1) 
           
    ### mesh generation for  """+ name_vector +""" ###
    #----------------------------------------------------    
    """+name_vector+"M = smesh.Mesh("+  name_vector +""")
    Regular_1D = """+ name_vector+"M.Segment()").split("\n")

        if model in ["BAR","RESSORT"]:
            self.lines=self.lines+("    Regular_1D.NumberOfSegments("""+str(1)+")").split("\n")
        else:
            self.lines=self.lines+("    Regular_1D.NumberOfSegments("+str(tub.Mesh_NbElement1D)+")").split("\n")

        if model in ["TUYAU"]:
            self.lines=self.lines+("    Quadratic_Mesh = Regular_1D.QuadraticMesh()").split("\n")

        self.lines=self.lines+("""
    smesh.SetName("""+ name_vector+"M,'"+name_vector+"""')
    """+name_vector+"""M.Compute()
    """+name_vector+"M.Group("+name_startpoint+""")
    """+name_vector+"M.Group("+name_endpoint+""")
    """+name_vector+"M.GroupOnGeom("+name_vector+""")

    structElemList.append(('CircularBeam', {'R': """+str(radius)+""", 'Group_Maille': '"""+name_vector+"""', 'EP': """+str(thickness)+"""}))    
    List_ParaVis_Visualization.append(\"Beam_"""+name_vector+"""\")
        """).split("\n")

#==============================================================================
    def _vector_rectangular_1D(self,tubavector):
        """This function creates a rectangluar tube-profile with the specified wall thickness as visualization.
        If no wall thickness is specified, the profile is solid.
        The actual mesh is only one-dimensional. The crosssection is later specified in the Aster-File"""

        model=tubavector.model
        Vx=tubavector.vector.normalized()
        Vy=tubavector.vd1x
        Vz=Vx.cross(Vy)

        print("Section",tubavector.section)
        [height_y,height_z,thickness_y,thickness_z]=tubavector.section
        
        solid_crosssection=False
        if thickness_y==0 and thickness_z==0 : solid_crosssection=True
        
        L1=height_y/2
        L2=height_z/2
        
        L1s=str(L1)
        L2s=str(L2)
        
        Li1s=str(L1-thickness_y)
        Li2s=str(L2-thickness_z)

        name_startpoint = tubavector.start_tubapoint.name
        name_endpoint=tubavector.end_tubapoint.name
        name_vector = str(tubavector.name)

        self.lines=self.lines+("""
##_vector_rectangular_1D##
    ### geometry generation for  """+ name_vector +""" ###
    #----------------------------------------------------
    print(\"Add: """+name_vector+"""\")
    """+name_vector+"= geompy.MakeVector("+name_startpoint+","+name_endpoint+""")
    geompy.addToStudy("""+name_vector+",\""+name_vector+"""\" )
    geompy.PutToFolder("""+name_vector+""", Folder_Vectors)""").split("\n")      


        if solid_crosssection:
            self.lines=self.lines+("""
    _W1 = geompy.MakeSketcher(\"Sketcher: F """+L1s+" "+L2s+": TT -"+L1s+" "+L2s+": TT -"+L1s+" -"+L2s+": TT "+L1s+" -"+L2s+""": WW\",
          [   """+str(tubavector.start_tubapoint.pos.x)+","+str(tubavector.start_tubapoint.pos.y)+","+str(tubavector.start_tubapoint.pos.z)+""",
              """+str(Vy.x)+","+str(Vy.y)+","+str(Vy.z)+""",
              """+str(Vz.x)+","+str(Vz.y)+","+str(Vz.z)+"""])
      
    _W1  = geompy.MakeRotation(_W1,"""+name_vector+""", """+str(tubavector.section_orientation)+"""*math.pi/180.0)
      FaceTube = geompy.MakeFaceWires([_W1], 1)
      Liste.append([_W1 ,\"_W1\"])""").split("\n")
        
        else:
            self.lines=self.lines+("""
    _W1 = geompy.MakeSketcher(\"Sketcher: F """+L1s+" "+L2s+": TT -"+L1s+" "+L2s+": TT -"+L1s+" -"+L2s+": TT "+L1s+" -"+L2s+""": WW\",
          [   """+str(tubavector.start_tubapoint.pos.x)+","+str(tubavector.start_tubapoint.pos.y)+","+str(tubavector.start_tubapoint.pos.z)+""",
              """+str(Vx.x)+","+str(Vx.y)+","+str(Vx.z)+""",
              """+str(Vz.x)+","+str(Vz.y)+","+str(Vz.z)+"""])

    _W2 = geompy.MakeSketcher(\"Sketcher: F """+Li1s+" "+Li2s+": TT -"+Li1s+" "+Li2s+": TT -"+Li1s+" -"+Li2s+": TT "+Li1s+" -"+Li2s+""": WW\",
          [   """+str(tubavector.start_tubapoint.pos.x)+","+str(tubavector.start_tubapoint.pos.y)+","+str(tubavector.start_tubapoint.pos.z)+""",
              """+str(Vx.x)+","+str(Vx.y)+","+str(Vx.z)+""",
              """+str(Vz.x)+","+str(Vz.y)+","+str(Vz.z)+"""])
      
    _W1  = geompy.MakeRotation(_W1,"""+name_vector+""", """+str(tubavector.section_orientation)+"""*math.pi/180.0)
    _W2  = geompy.MakeRotation(_W2,"""+name_vector+""", """+str(tubavector.section_orientation)+"""*math.pi/180.0)      
    FaceTube= geompy.MakeFaceWires([_W1, _W2], 1)   


 
            """).split("\n")


        self.lines=self.lines+("""
    ### mesh generation for  """+ name_vector +""" ###
    #----------------------------------------------------    

    """+name_vector+"M = smesh.Mesh("+  name_vector +""")
    Decoupage = """+ name_vector+"M.Segment()").split("\n")


        if model in ["BARRE","RESSORT"]:
            self.lines=self.lines+("    Decoupage.NumberOfSegments("""+str(1)+")").split("\n")
        else:
            self.lines=self.lines+("    Decoupage.NumberOfSegments("+str(tub.Mesh_NbElement1D)+")").split("\n")

        self.lines=self.lines+("""
    smesh.SetName("""+ name_vector+"M,'"+name_vector+"""')
    """+name_vector+"""M.Compute()
    """+name_vector+"M.Group("+name_startpoint+""")
    """+name_vector+"M.Group("+name_endpoint+""")
    """+name_vector+"M.GroupOnGeom("+name_vector+""")

    structElemList.append(('Orientation', {'MeshGroups': '"""+name_vector+"""',
                                        'ANGL_VRIL': """+str(tubavector.section_orientation)+"""}),)
    structElemList.append(('RectangularBeam', {'HY1': """+str(height_y)+""",'HY2': """+str(height_y)+""",
                                                'HZ1': """+str(height_z)+""",'HZ2': """+str(height_z)+""",
                                                'EPY1': """+str(thickness_y)+""",'EPY2': """+str(thickness_y)+""",    
                                                'EPZ1': """+str(thickness_z)+""",'EPZ2': """+str(thickness_z)+""",    
                                                'MeshGroups': '"""+name_vector+"""'}))

    List_ParaVis_Visualization.append(\"Beam_"""+name_vector+"""\")
        """).split("\n")

#==============================================================================
    def _vector_round_3D(self,tubavector):
        """This function creates a round tube-profile with the specified wall thickness as visualization
        The actual mesh is only one-dimensional. The crosssection is later specified in the Aster-File"""

        [radius,thickness]=tubavector.section
        model=tubavector.model

        name_startpoint = tubavector.start_tubapoint.name
        name_endpoint=tubavector.end_tubapoint.name

        name_vector = str(tubavector.name)

        self.lines=self.lines+("""
##_vector_round_3D##
    ### geometry generation for  """+ name_vector +""" ###
    #----------------------------------------------------
    print(\"Add  """+ name_vector +""" \")    

    """+name_vector+"= geompy.MakeVector("+name_startpoint+","+name_endpoint+""")

    C1 = geompy.MakeCircle("""+name_startpoint+",Vd2x_"+name_startpoint+","+str(radius)+""")                                                    
    C2 = geompy.MakeCircle("""+name_startpoint+",Vd2x_"+name_startpoint+","+str(radius-thickness)+""")
                                         
    FaceTube = geompy.MakeFaceWires([C1, C2], 1)

    #For the Hexahedron to work, the pipe has to be partioned
    Pipe= geompy.MakePipe( FaceTube ,"""+name_vector+""")
    cuttingPlane = geompy.MakePlane("""+name_startpoint+",Vd1x_"+name_startpoint+","+str(tubavector.vector.magnitude()*5)+""")
    """+name_vector+""" = geompy.MakePartition([Pipe], [cuttingPlane], [], [], geompy.ShapeType["SOLID"], 0, [], 0)
    thickness = geompy.Propagate("""+name_vector+""")[1]

    """+name_vector+""".SetColor(SALOMEDS.Color("""+tub.colors[model]+"""))

    geompy.addToStudy("""+name_vector+""",\""""+name_vector+"""\")
    geompy.addToStudyInFather( """+name_vector+""", thickness, 'thickness' )
    geompy.PutToFolder("""+name_vector+""", Folder_Vectors)

    L_Start = geompy.GetShapesOnPlane("""+name_vector+""",geompy.ShapeType[\"FACE\"],Vd2x_"""+tubavector.start_tubapoint.name+""",GEOM.ST_ON)
    """+name_vector+"""_StartFace = geompy.MakeCompound(L_Start)
    geompy.addToStudyInFather("""+name_vector+""","""+name_vector+"""_StartFace,\""""+name_vector+"""_StartFace\")

    L_End = geompy.GetShapesOnPlane("""+name_vector+""",geompy.ShapeType[\"FACE\"],Vd2x_"""+tubavector.end_tubapoint.name+""",GEOM.ST_ON)
    """+name_vector+"""_EndFace = geompy.MakeCompound(L_End)
    geompy.addToStudyInFather("""+name_vector+""","""+name_vector+"""_EndFace,\""""+name_vector+"""_EndFace\")


    List_ParaVis_Visualization.append("""+name_vector+""")

    ### mesh generation for  """+ name_vector +""" ###
    #----------------------------------------------------    
    """+name_vector+"M = smesh.Mesh("""+name_vector+""")

    """+ name_vector+"""M.Segment().NumberOfSegments("""+str(tub.Mesh_NbElement3D)+""")
    """+ name_vector+"""M.Segment(geom=thickness).NumberOfSegments("""+str(tub.Mesh_NbElement3D_thickness)+""")
    """+ name_vector+"""M.Quadrangle()
    """+ name_vector+"""M.Hexahedron()

    smesh.SetName("""+ name_vector+"M,'"+name_vector+"""')
    """+name_vector+"""M.Compute()
    """+name_vector+"M.Group("+name_startpoint+""")
    """+name_vector+"M.Group("+name_endpoint+""")
    """+name_vector+"M.GroupOnGeom("+name_vector+"_StartFace" """)
    """+name_vector+"M.GroupOnGeom("+name_vector+"_EndFace" """)
    """+name_vector+"M.GroupOnGeom("+name_vector+""")

           """).split("\n")
#==============================================================================
##obsolete
#    def _visualize_Pipe_1D(self, tubavector):
#        model=tubavector.model
#                
#        self.lines=self.lines+("""
#    if List_Visualization!=[]:
#       _W=geompy.MakeWire(List_Visualization,1e-7)
#       Pipe_"""+tubavector.name+""" = geompy.MakePipe( FaceTube ,_W)
#       Pipe_"""+tubavector.name+""".SetColor(SALOMEDS.Color("""+tub.colors[model]+"""))
#       Pipe_id=geompy.addToStudyInFather("""+tubavector.name+""",Pipe_"""+tubavector.name+""",\"Pipe_"""+tubavector.name+"""\")
#       gg.createAndDisplayGO(Pipe_id)
#       gg.setDisplayMode(Pipe_id,1)
#
#       List_ParaVis_Visualization.append(Pipe_"""+tubavector.name+""")
#       List_Visualization=[]
#    """).split("\n")
#obsolete
#==============================================================================

    def _visualize_force(self,tubapoint,section):
        outerRadius=section[0]
        name_point=tubapoint.name
        for force in tubapoint.force:
            force_direction=[force.normalized().x,force.normalized().y,force.normalized().z]
            print("force direction",str(force_direction))
           
            self.lines=self.lines+("""
    # Visualize a forces at point """+name_point+"""
    #---------------------------------------------           
    Radius="""+str(outerRadius)+"""
        
    Pna=geompy.MakeVertexWithRef("""+name_point+",Radius*"+str(force_direction[0])+",Radius*"+str(force_direction[1])+",Radius*"+str(force_direction[2])+""")
    Pnb=geompy.MakeVertexWithRef("""+name_point+",1.5*Radius*"+str(force_direction[0])+",1.5*Radius*"+str(force_direction[1])+",1.5*Radius*"+str(force_direction[2])+""")
    Pnc=geompy.MakeVertexWithRef("""+name_point+",10*Radius*"+str(force_direction[0])+",10*Radius*"+str(force_direction[1])+",10*Radius*"+str(force_direction[2])+""") 
 
    V_force=geompy.MakeVector(Pna,Pnb)     

    Tip = geompy.MakeCone(Pnc,V_force,2*Radius,0,4*Radius)           
    Shaft = geompy.MakeCylinder("""+name_point+""", V_force,0.5*Radius, 10*Radius)
    Arrow = geompy.MakeCompound([Tip,Shaft])  
               
    Arrow.SetColor(SALOMEDS.Color("""+tub.colors["FORCE"]+"""))
    B_id=geompy.addToStudyInFather( """+ name_point +""", Arrow,'"""+name_point+"""_Arrow' )    

    List_ParaVis_Visualization.append(Arrow)
    gg.createAndDisplayGO(B_id)
    gg.setDisplayMode(B_id,1)
            """).split("\n")

#==============================================================================

    def _visualize_ddl(self,tubapoint,section):
        """Creates a visualization element in the Code Aster GEOM-Module. 
        The created geometry is not part of the actual simulation"""
        outerRadius=section[0]
        name_point=tubapoint.name
        
    
        
        if tubapoint.ddl==[0,0,0,0,0,0]:
            self.lines=self.lines+("""
    # Visualize a support(restriction DOF) at point """+name_point+"""
    #---------------------------------------------               
    """+name_point+"""_BLOCK_xyzrxryrz=geompy.MakeBox("""+str(tubapoint.pos.x+2*outerRadius)+""","""+str(tubapoint.pos.y+2*outerRadius)+""","""+str(tubapoint.pos.z+2*outerRadius)+""","""+str(tubapoint.pos.x-2*outerRadius)+""","""+str(tubapoint.pos.y-2*outerRadius)+""","""+str(tubapoint.pos.z-2*outerRadius)+""")	
    """+name_point+"""_BLOCK_xyzrxryrz.SetColor(SALOMEDS.Color("""+tub.colors["BLOCK"]+"""))
    """+name_point+"""_BLOCK_xyzrxryrz_id=geompy.addToStudyInFather( """+ name_point +""", """+name_point+"""_BLOCK_xyzrxryrz,'"""+name_point+"""_BLOCK_xyzrxryrz' )
 #   B_id=geompy.addToStudy("""+name_point+"""_BLOCK_xyzrxryrz,'"""+name_point+"""_BLOCK_xyzrxryrz' )
    
    List_ParaVis_Visualization.append("""+name_point+"""_BLOCK_xyzrxryrz)
    objId = geompy.getObjectID("""+name_point+"""_BLOCK_xyzrxryrz)    
    gg.createAndDisplayGO(objId)
    gg.setDisplayMode(objId,1)
    gg.setColor(objId,218,165,31)
  
    """).split("\n")  	            

        else:
            V1s_list=[]
            if not tubapoint.ddl[0]=="x" and tubapoint.ddl[0]==0:
                V1s_list.append([[3*outerRadius,0,0],[2*outerRadius,0,0],[-3*outerRadius,0,0],[-2*outerRadius,0,0],"x"])
            if not tubapoint.ddl[1]=="x" and tubapoint.ddl[1]==0:
                V1s_list.append([[0,3*outerRadius,0],[0,2*outerRadius,0],[0,-3*outerRadius,0],[0,-2*outerRadius,0],"y"])          
            if not tubapoint.ddl[2]=="x" and tubapoint.ddl[2]==0:
                V1s_list.append([[0,0,3*outerRadius],[0,0,2*outerRadius],[0,0,-3*outerRadius],[0,0,-2*outerRadius],"z"])            
    
            for V1s in V1s_list:
                self.lines=self.lines+("""        
 
    Radius="""+str(outerRadius)+"""

    Pna=geompy.MakeVertexWithRef("""+name_point+","+str(V1s[0][0])+","+str(V1s[0][1])+","+str(V1s[0][2])+""")
    Pnb=geompy.MakeVertexWithRef("""+name_point+","+str(V1s[1][0])+","+str(V1s[1][1])+","+str(V1s[1][2])+""")  
    Vp=geompy.MakeVector(Pna,Pnb)  
    Cone1 = geompy.MakeCone(Pna,Vp,Radius,0,2*Radius)

   
    P2a=geompy.MakeVertexWithRef("""+name_point+","+str(V1s[2][0])+","+str(V1s[2][1])+","+str(V1s[2][2])+""")    
    P2b=geompy.MakeVertexWithRef("""+name_point+","+str(V1s[3][0])+","+str(V1s[3][1])+","+str(V1s[3][2])+""")    
    Vm=geompy.MakeVector(P2a,P2b)  
    Cone2 = geompy.MakeCone(P2a,Vm,Radius,0,2*Radius)
    
    BLOCK_"""+V1s[4]+"""=geompy.MakeCompound([Cone1,Cone2])
    BLOCK_"""+V1s[4]+""".SetColor(SALOMEDS.Color("""+tub.colors["BLOCK"]+"""))
    B_id=geompy.addToStudyInFather( """+ name_point +""", BLOCK_"""+str(V1s[4])+",'"+name_point+"_BLOCK_"""+str(V1s[4])+"""' )    

    List_ParaVis_Visualization.append(BLOCK_"""+V1s[4]+""")
    gg.createAndDisplayGO(B_id)
    gg.setDisplayMode(B_id,1)
    """).split("\n")  



            deform = eu.Vector3(0, 0, 0) 
            if not tubapoint.ddl[0]=="x" and  not tubapoint.ddl[0]==0:
                deform.x=tubapoint.ddl[0]
            if not tubapoint.ddl[1]=="x" and  not tubapoint.ddl[1]==0:
                deform.y=tubapoint.ddl[1]                              
            if not tubapoint.ddl[2]=="x" and  not tubapoint.ddl[2]==0:
                deform.z=tubapoint.ddl[2]                
               
            print("deform", deform)    
#            deform=deform.normalized() 
            if abs(deform):
                self.lines=self.lines+("""

    """+str(abs(deform))+"""
    Radius="""+str(outerRadius)+"""
        
    Pna=geompy.MakeVertexWithRef("""+name_point+","+str(deform.x)+","+str(deform.y)+","+str(deform.z)+""")   
    V_def=geompy.MakeVector("""+name_point+""",Pna)
    Deform_"""+name_point+""" = geompy.MakeCone("""+name_point+""",V_def,1*Radius,0,"""+str(deform.__abs__())+""")
    Deform_"""+name_point+""".SetColor(SALOMEDS.Color("""+tub.colors["BLOCK_DEFORMATION"]+"""))
    B_id=geompy.addToStudyInFather( """+ name_point +""", Deform_"""+name_point+""",'"""+name_point+"""_Deform' )    

    List_ParaVis_Visualization.append(Deform_"""+name_point+""")
    gg.createAndDisplayGO(B_id)
    gg.setDisplayMode(B_id,1)
    
    """).split("\n")  

#==============================================================================

    def _visualize_stiffness(self,tubapoint,section):
        outerRadius=section[0]
        name_point=tubapoint.name

        V1s_list=[]        
        if not tubapoint.stiffness[0]==0:
            V1s_list.append([[3*outerRadius,0,0],[2*outerRadius,0,0],[-3*outerRadius,0,0],[-2*outerRadius,0,0],"x"])
        if not tubapoint.stiffness[1]==0:
            V1s_list.append([[0,3*outerRadius,0],[0,2*outerRadius,0],[0,-3*outerRadius,0],[0,-2*outerRadius,0],"y"])          
        if not tubapoint.stiffness[2]==0:
            V1s_list.append([[0,0,3*outerRadius],[0,0,2*outerRadius],[0,0,-3*outerRadius],[0,0,-2*outerRadius],"z"])            
  
        for V1s in V1s_list:
                self.lines=self.lines+("""        
    # Visualize springs/stiffness at point """+name_point+"""
    #---------------------------------------------
    Radius="""+str(outerRadius)+"""

    Pna=geompy.MakeVertexWithRef("""+name_point+","+str(V1s[0][0])+","+str(V1s[0][1])+","+str(V1s[0][2])+""")
    Pnb=geompy.MakeVertexWithRef("""+name_point+","+str(V1s[1][0])+","+str(V1s[1][1])+","+str(V1s[1][2])+""")  
    Vp=geompy.MakeVector(Pna,Pnb)  

    Torus_1 = geompy.MakeTorus(Pna, Vp, Radius, Radius/2) 
    Torus_2 = geompy.MakeTorus(Pnb, Vp, Radius, Radius/2)  
 
    P2a=geompy.MakeVertexWithRef("""+name_point+","+str(V1s[2][0])+","+str(V1s[2][1])+","+str(V1s[2][2])+""")    
    P2b=geompy.MakeVertexWithRef("""+name_point+","+str(V1s[3][0])+","+str(V1s[3][1])+","+str(V1s[3][2])+""")    
    Vm=geompy.MakeVector(P2a,P2b)  

    Torus_3 = geompy.MakeTorus(P2a, Vm, Radius, Radius/2) 
    Torus_4 = geompy.MakeTorus(P2b, Vm, Radius, Radius/2)  
    
    STIFFNESS_"""+V1s[4]+"""=geompy.MakeCompound([Torus_1,Torus_2,Torus_3,Torus_4])
    STIFFNESS_"""+V1s[4]+""".SetColor(SALOMEDS.Color("""+tub.colors["STIFFNESS"]+"""))
    S_id=geompy.addToStudyInFather( """+ name_point +""", STIFFNESS_"""+str(V1s[4])+",'"+name_point+"_STIFFNESS_"""+str(V1s[4])+"""' )    

    List_ParaVis_Visualization.append(STIFFNESS_"""+V1s[4]+""")    
    gg.createAndDisplayGO(S_id)
    gg.setDisplayMode(S_id,1)
        
    """).split("\n") 

#==============================================================================
    def _visualize_mass(self,tubapoint,section):
        """Creates a visualization element in the Code Aster GEOM-Module. 
        The created geometry is not part of the actual simulation"""
        outerRadius=section[0]
        name_point=tubapoint.name
         
        if not tubapoint.mass ==0:
            self.lines=self.lines+("""
    # Visualize mass at point """+name_point+"""
    #---------------------------------------------
    """+name_point+"""_MASS=geompy.MakeSpherePntR("""+name_point+""","""+str(2*outerRadius)+""")	
    """+name_point+"""_MASS.SetColor(SALOMEDS.Color("""+tub.colors["STIFFNESS"]+"""))
    """+name_point+"""_MASS_id=geompy.addToStudyInFather( """+ name_point +""", """+name_point+"""_MASS,'"""+name_point+"""_MASS' )
#   B_id=geompy.addToStudy("""+name_point+"""_MASS,'"""+name_point+"""_MASS' )
    
    List_ParaVis_Visualization.append("""+name_point+"""_MASS)
    objId = geompy.getObjectID("""+name_point+"""_MASS)    
    gg.createAndDisplayGO(objId)
    gg.setDisplayMode(objId,1)
    gg.setColor(objId,218,165,31)
  
    """).split("\n")              
#==============================================================================
    def _create_mesh_compound(self,dict_tubavectors,dict_tubapoints): 
        print("Text---------------------------",dict_tubavectors)
        text = "["
        character_count=0
        for tubavector in dict_tubavectors :
            name_vector = str(tubavector.name)#+tubavector.model[:3]
            character_count+=len(tubavector.name)+10
            if character_count>50:
                text += "\n"
                character_count=0
                text += "           "
            text += ""+name_vector+"M.GetMesh() , "
        text = text[:-1]
        print("Text---------------------------"+text)
        for tubapoint in dict_tubapoints :           
            if not tubapoint.stiffness==[0.0, 0.0, 0.0, 0.0, 0.0, 0.0]:
                    name_point = str(tubapoint.name)
                    text += "Spring"+name_point+"M.GetMesh() , "
            if not tubapoint.friction_coefficient==0.0:
                    name_point = str(tubapoint.name)
                    text += "Friction"+name_point+"M.GetMesh() , "
        text += "]"
        
        self.lines=self.lines+("""        
    #Creates the final mesh compound
    #----------------------------------------------------

    Completed_Mesh = smesh.Concatenate("""+text+""", 1, 0, 1e-05)
    coincident_nodes = Completed_Mesh.FindCoincidentNodes( 1e-05 )
    Completed_Mesh.MergeNodes(coincident_nodes)
    equal_elements = Completed_Mesh.FindEqualElements(Completed_Mesh)    
    Completed_Mesh.MergeElements(equal_elements)   
    smesh.SetName(Completed_Mesh.GetMesh(), 'Completed_Mesh')
        """).split("\n")



#==============================================================================
    def _bent_1D(self,tubavector) :
        [radius,thickness]=tubavector.section
        name_vector=name_vector = str(tubavector.name)#+tubavector.model[:3]
        model=tubavector.model
        logging.debug("Bent: "+str(name_vector))
        name_centerpoint=tubavector.center_tubapoint.name
        name_startpoint=tubavector.start_tubapoint.name
        name_endpoint=tubavector.end_tubapoint.name

        self.lines=self.lines+("""
##_bent_1D##
    ### geometry generation for  """+ name_vector +""" ###
    #----------------------------------------------------

    print(\"Add  """+ name_vector +""" \")
    """+name_vector+" = geompy.MakeArcCenter("+name_centerpoint+","+name_startpoint+","+name_endpoint+""")
    geompy.addToStudy("""+name_vector+""",\""""+name_vector+ """\")

    ### mesh generation for  """+ name_vector +""" ###
    #----------------------------------------------------    

    """+name_vector+"M = smesh.Mesh("+  name_vector +""")
    Regular_1D = """+ name_vector+"M.Segment()").split("\n")

        if model in ["BARRE","RESSORT"]:
            self.lines=self.lines+("    Regular_1D.NumberOfSegments("""+str(1)+")").split("\n")
        elif model in ["TUBE"]:
            self.lines=self.lines+("    Regular_1D.NumberOfSegments("+str(tub.Mesh_NbElement1D)+")").split("\n")
        elif model in ["TUYAU"]:
            self.lines=self.lines+("    Regular_1D.NumberOfSegments("+str(tub.Mesh_NbElement1D)+")").split("\n")
            self.lines=self.lines+("    Quadratic_Mesh = Regular_1D.QuadraticMesh()").split("\n")

        self.lines=self.lines+("""
    smesh.SetName("""+ name_vector+"M,'"+name_vector+"""')
    """+name_vector+"""M.Compute()
    """+name_vector+"M.Group("+name_startpoint+""")
    """+name_vector+"M.Group("+name_endpoint+""")
    """+name_vector+"M.GroupOnGeom("+name_vector+""")


    structElemList.append(('CircularBeam', {'R': """+str(radius)+""", 'Group_Maille': '"""+name_vector+"""', 'EP': """+str(thickness)+"""}))             
    List_ParaVis_Visualization.append(\"Beam_"""+name_vector+"""\")

            """).split("\n")

#==============================================================================
    def _bent_3D(self,tubavector) :
        [radius,thickness]=tubavector.section
        name_vector = str(tubavector.name)#+tubavector.model[:3]
        model=tubavector.model
        logging.debug("Bent: "+str(name_vector))
        name_centerpoint=tubavector.center_tubapoint.name
        name_startpoint=tubavector.start_tubapoint.name
        name_endpoint=tubavector.end_tubapoint.name

        self.lines=self.lines+("""
##_bent_3D##
    ### geometry generation for  """+ name_vector +""" ###
    #----------------------------------------------------

    print(\"Add  """+ name_vector +""" \")
    """+name_vector+" = geompy.MakeArcCenter("+name_centerpoint+","+name_startpoint+","+name_endpoint+""")
                  

    C1 = geompy.MakeCircle("""+name_startpoint+",Vd2x_"+name_startpoint+","+str(radius)+""")                                                    
    C2 = geompy.MakeCircle("""+name_startpoint+",Vd2x_"+name_startpoint+","+str(radius-thickness)+""")                                            
    FaceTube = geompy.MakeFaceWires([C1, C2], 1)
    
    #For the Hexahedron to work, the pipe has to be partioned
    Pipe = geompy.MakePipe( FaceTube ,"""+name_vector+""")                     
    cuttingPlane = geompy.MakePlaneThreePnt("""+name_centerpoint+","+name_startpoint+","+name_endpoint+","+str(tubavector.bending_radius*5)+""")
    """+name_vector+""" = geompy.MakePartition([Pipe], [cuttingPlane], [], [], geompy.ShapeType["SOLID"], 0, [], 0)
    thickness = geompy.Propagate("""+name_vector+""")[1]

    """+name_vector+""".SetColor(SALOMEDS.Color("""+tub.colors[model]+"""))

    geompy.addToStudy("""+name_vector+""",\""""+name_vector+"""\")
    geompy.addToStudyInFather( """+name_vector+""", thickness, 'thickness' )
    geompy.PutToFolder("""+name_vector+""", Folder_Vectors)
    
    L_Start = geompy.GetShapesOnPlane("""+name_vector+""",geompy.ShapeType[\"FACE\"],Vd2x_"""+tubavector.start_tubapoint.name+""",GEOM.ST_ON)
    """+name_vector+"""_StartFace = geompy.MakeCompound(L_Start)
    geompy.addToStudyInFather("""+name_vector+""","""+name_vector+"""_StartFace,\""""+name_vector+"""_StartFace\")

    L_End = geompy.GetShapesOnPlane("""+name_vector+""",geompy.ShapeType[\"FACE\"],Vd2x_"""+tubavector.end_tubapoint.name+""",GEOM.ST_ON)
    """+name_vector+"""_EndFace = geompy.MakeCompound(L_End)
    geompy.addToStudyInFather("""+name_vector+""","""+name_vector+"""_EndFace,\""""+name_vector+"""_EndFace\")

    List_ParaVis_Visualization.append("""+name_vector+""")

    ### mesh generation for  """+ name_vector +""" ###
    #----------------------------------------------------    

    """+ name_vector+"M = smesh.Mesh("""+name_vector+""")
    """+ name_vector+"""M.Segment().NumberOfSegments("""+str(tub.Mesh_NbElement3D)+""")
    """+ name_vector+"""M.Segment(geom=thickness).NumberOfSegments("""+str(tub.Mesh_NbElement3D_thickness)+""")
    """+ name_vector+"""M.Quadrangle()
    """+ name_vector+"""M.Hexahedron()
    
    smesh.SetName("""+ name_vector+"M,'"+name_vector+"""')
    """+name_vector+"""M.Compute()
    """+name_vector+"M.Group("+name_startpoint+""")
    """+name_vector+"M.Group("+name_endpoint+""")
    """+name_vector+"M.GroupOnGeom("+name_vector+"_StartFace" """)
    """+name_vector+"M.GroupOnGeom("+name_vector+"_EndFace" """)
    """+name_vector+"M.GroupOnGeom("+name_vector+""")""").split("\n")

#==============================================================================
    def _TShape_3D(self,tubavector) :
        [radius,thickness]=tubavector.section
        [incident_radius,incident_thickness]=tubavector.incident_section
        model=tubavector.model
        name_vector= str(tubavector.name)#+tubavector.model[:3]
        name_incidentpoint=tubavector.incident_end_tubapoint.name
        name_startpoint=tubavector.start_tubapoint.name
        name_endpoint=tubavector.end_tubapoint.name
               
        main_halflength=str(tubavector.vector.magnitude()/2)        
        incident_halflength=str(tubavector.incident_vector.magnitude())
        print(name_vector,type(name_vector))
        self.lines=self.lines+("""

    ### geometry generation for  """+ name_vector +""" ###
    #----------------------------------------------------
    print(\"Add  """+ name_vector +""" \")

    ["""+ name_vector +""", Junction_1, Junction_2, Junction_3, Thickness,
     Circular_quarter_of_pipe, Circular_quarter_of_pipe_1,Main_pipe_half_length,
     Flange, Incident_pipe_half_length, Internal_faces] =\
        geompy.MakePipeTShape("""+str(radius-thickness)+","+str(thickness)+","+ main_halflength+","+
                              str(incident_radius-incident_thickness)+","+str(incident_thickness)+","+
                              incident_halflength+", True,"
                              +name_startpoint+","+ name_endpoint+
                              ","+name_incidentpoint+""")
                              
    """+name_vector+""".SetColor(SALOMEDS.Color("""+tub.colors[model]+"""))
    geompy.addToStudy( """+ name_vector +""", '"""+ name_vector +"""' )
    geompy.PutToFolder("""+name_vector+""", Folder_Vectors)


    L_Start = geompy.GetShapesOnPlane("""+name_vector+""",geompy.ShapeType[\"FACE\"],Vd2x_"""+tubavector.start_tubapoint.name+""",GEOM.ST_ON)
    """+name_vector+"""_StartFace = geompy.MakeCompound(L_Start)
    geompy.addToStudyInFather("""+name_vector+""","""+name_vector+"""_StartFace,\""""+name_vector+"""_StartFace\")

    L_Incident = geompy.GetShapesOnPlane("""+name_vector+""",geompy.ShapeType[\"FACE\"],Vd2x_"""+tubavector.incident_end_tubapoint.name+""",GEOM.ST_ON)
    """+name_vector+"""_IncidentFace = geompy.MakeCompound(L_Incident)
    geompy.addToStudyInFather("""+ name_vector +""","""+name_vector+"""_IncidentFace,\""""+name_vector+"""_IncidentFace\")
 
    
    L_End = geompy.GetShapesOnPlane("""+name_vector+""",geompy.ShapeType[\"FACE\"],Vd2x_"""+tubavector.end_tubapoint.name+""",GEOM.ST_ON)
    """+name_vector+"""_EndFace = geompy.MakeCompound(L_End)
    geompy.addToStudyInFather("""+ name_vector +""","""+name_vector+"""_EndFace,\""""+name_vector+"""_EndFace\")

    List_ParaVis_Visualization.append("""+name_vector+""")

    ### mesh generation for  """+ name_vector +""" ###
    #----------------------------------------------------    

    """+ name_vector +"""M = smesh.Mesh("""+ name_vector +""")
    Regular_1D = """+ name_vector +"""M.Segment()
    Nb_Segments_1 = Regular_1D.NumberOfSegments(4)
    Nb_Segments_1.SetDistrType( 0 )
    Quadrangle_2D = """+ name_vector +"""M.Quadrangle(algo=smeshBuilder.QUADRANGLE)
    Hexa_3D = """+ name_vector +"""M.Hexahedron(algo=smeshBuilder.Hexa)
    Nb_Segments_2 = smesh.CreateHypothesis('NumberOfSegments')
    Nb_Segments_2.SetNumberOfSegments( 4 )
    Nb_Segments_2.SetDistrType( 0 )
    status = """+ name_vector +"""M.AddHypothesis(Regular_1D,Thickness)
    status = """+ name_vector +"""M.AddHypothesis(Nb_Segments_2,Thickness)
    isDone = """+ name_vector +"""M.Compute()
    [ Sub_mesh_1 ] = """+ name_vector +"""M.GetMesh().GetSubMeshes()
    Sub_mesh_1 = """+ name_vector +"""M.GetSubMesh( Thickness, 'Sub-mesh_1' )

    ## Set names of Mesh objects
    smesh.SetName("""+ name_vector+"M,'"+name_vector+"""')
    """+name_vector+"""M.Compute()
    """+name_vector+"M.Group("+name_startpoint+""")
    """+name_vector+"M.Group("+name_endpoint+""")
    """+name_vector+"M.Group("+name_incidentpoint+""")
    
    """+name_vector+"M.GroupOnGeom("+ name_vector + """)
    """+name_vector+"M.GroupOnGeom("+name_vector+"_StartFace" """)
    """+name_vector+"M.GroupOnGeom("+name_vector+"_IncidentFace" """)
    """+name_vector+"M.GroupOnGeom("+name_vector+"_EndFace" """)

    smesh.SetName(Regular_1D.GetAlgorithm(), 'Regular_1D')
    smesh.SetName(Hexa_3D.GetAlgorithm(), 'Hexa_3D')
    smesh.SetName(Quadrangle_2D.GetAlgorithm(), 'Quadrangle_2D')
    smesh.SetName(Nb_Segments_2, 'Nb. Segments_2')
    smesh.SetName(Nb_Segments_1, 'Nb. Segments_1')
    smesh.SetName("""+ name_vector +"""M.GetMesh()," """+name_vector+"""M")
    smesh.SetName(Sub_mesh_1, 'Sub-mesh_1')

            """).split("\n")



#==============================================================================            
    def _create_paravis_geometry_compound(self): 
        self.lines=self.lines+("""
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
        """).split("\n")
            
#==============================================================================
    def _finalize(self):
        self.lines=self.lines+("""
                               
##_finalize##                
    #exports the created mesh compound 
    try:
        Completed_Mesh.ExportMED( r'"""+self.current_directory+"""/Completed_Mesh.mmed', 0)
    except:
        print ('ExportPartToMED() failed')


    #exports visualizations (structural elements, forces, etc) as a grouped geometry to be used in Paravis
    try:    
        geompy.ExportVTK(compound_paravis, '"""+self.current_directory+"""/compound_paravis.vtk', 0.001)     
    except:
        print ('ExportVTK of the visualization compound failed')

    if salome.sg.hasDesktop():
       salome.sg.updateObjBrowser(0)
    time2=time.time()
    dtime = time2 - time1
    print(\"------------------------\")
    print(\"Duration of construction:\"+str(round(dtime,2))+\"s\")

#    import SalomePyQt
#    sg = SalomePyQt.SalomePyQt()
#    sg.activateModule("Geometry")
#    if salome.sg.hasDesktop():
#      salome.sg.updateObjBrowser(1)
#    sg.activateModule("AsterStudy")

    """).split("\n")

        self.lines=self.lines+"Project()".split()

