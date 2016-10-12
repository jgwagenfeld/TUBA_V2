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
import library_material


class Salome:

    def __init__(self, my_directory):
        self.my_directory=my_directory
        self.lines=[]
        logging.debug("Now in writeSalomeFile \n ====")

#==============================================================================
    def write(self,dict_tubavectors,dict_tubapoints):

        self._initialize()

        for tubapoint in dict_tubapoints:
            tubapoint.is_element_start()

        for tubapoint in dict_tubapoints:
            logging.debug("Processing TubaPoint: "+ tubapoint.name+ " \n ====")
            self._point(tubapoint)
            print("DDL", tubapoint.ddl)
                

        for tubavector in dict_tubavectors:
            logging.debug("Processing TubaVector: "+tubavector.name+ " \n ====")
            self._vector(tubavector)
            self._visualize_Pipe_1D(tubavector)

            self._visualize_stiffness(tubavector.start_tubapoint,tubavector.section)
            self._visualize_ddl(tubavector.start_tubapoint,tubavector.section)
            if tubavector.start_tubapoint.is_element_start:
                print(str(tubavector.name)+"is an element start")
                self._visualize_ddl(tubavector.start_tubapoint,tubavector.section)
                self._visualize_stiffness(tubavector.start_tubapoint,tubavector.section)
            
        
        self._create_mesh_compound(dict_tubavectors)
        self._finalize()

#==============================================================================
    def _point(self,tubapoint):
        """Writes the python code to construct a point and the current direction-vector in Salome"""

        pos = str(tubapoint.pos.xyz).strip('()')
        name_point =tubapoint.name



        self.lines=self.lines+("""
    """+name_point+"""= geompy.MakeVertex("""+pos+ """ )
    geompy.addToStudy("""+name_point+",\""+ name_point+" \")").split("\n")


        #if not tubapoint.is_element_end():
        vd2x = str(tubapoint.vd2x.xyz).strip('()')
        self.lines=self.lines+("    Vd2x_"+name_point+" = geompy.MakeVectorDXDYDZ("+vd2x+""")
    """ +name_point+"_vd2x=    geompy.MakeTranslationVectorDistance("+name_point+",Vd2x_"+name_point+""",100)
    Vd2x_"""+name_point+"= geompy.MakeVector("+name_point+","+name_point+"""_vd2x)
    geompy.addToStudyInFather("""+name_point+",Vd2x_"""+name_point+",\"Vd2x_"+ name_point+""" " )"""
        ).split("\n")

    

#==============================================================================
    def _vector(self,tubavector) :
        """Writes the python code to construct a Vector in Salome"""

        if isinstance(tubavector, tuba_geom.TubaBent):
            self._bent_1D(tubavector)

        elif isinstance(tubavector, tuba_geom.TubaTShape3D):
            self._TShape_3D(tubavector)

        elif isinstance(tubavector, tuba_geom.TubaVector):
            if tubavector.model == "3D":
                exec("self.Ajouter_V_"+self.forme+"_3D(A,nom,lien)")

            elif tubavector.model in ["TUBE","TUYAU"]:
                self._vector_round_1D(tubavector)

            elif tubavector.model in ["POUTRE_RECTANGLE", "RECTANGULAR"]:
                self._vector_rectangular_1D(tubavector)

            elif tubavector.model in ["POUTRE"]:
                self._vector_pout1D(tubavector)

            else:
                writeError(["Model is not defined"])

#==============================================================================
    def _vector_round_1D(self,tubavector):
        """This function creates a round tube-profile with the specified wall thickness as visualization
        The actual mesh is only one-dimensional. The crosssection is later specified in the Aster-File"""

        [radius,thickness]=tubavector.section
        model=tubavector.model
        Vx=tubavector.vector

        name_startpoint = tubavector.start_tubapoint.name
        name_endpoint=tubavector.end_tubapoint.name


        name_vector = str(tubavector.name)


        self.lines=self.lines+("""
    try:
      print(\"Add """+name_vector+"""\")
      """+name_vector+"= geompy.MakeVector("+name_startpoint+","+name_endpoint+""")
      #Liste.append(["""+name_startpoint+",\""+name_startpoint+"""\"])
      geompy.addToStudy("""+name_vector+",\""+name_vector+"""\" )
#     Liste.append(["""+name_vector+",\""+name_vector+"""\"])
      List_Visualization.append("""+name_vector+""")
        """).split("\n")

        self.lines=self.lines+("""
      _C1 = geompy.MakeCircle("""+name_startpoint+", "+name_vector+","+str(radius)+""")
      _C2 = geompy.MakeCircle("""+name_startpoint+", "+name_vector+","+str(radius-thickness)+""")
      FaceTube = geompy.MakeFaceWires([_C1, _C2], 1)
      Liste.append([_C1 ,\"CercleExt\"])
      Liste.append([_C2 ,\"CercleInt\"])
            """).split("\n")


        self.lines=self.lines+("""
    except:
       ERREUR=True
       print (\"   =>ERROR BUILDING THE GEOMETRY!\")
       for x in Liste :
           geompy.addToStudy(x[0],x[1])
       return

    try:
       """+name_vector+"M = smesh.Mesh("+  name_vector +""")
       Decoupage = """+ name_vector+"M.Segment()").split("\n")


        if model in ["BARRE","RESSORT"]:
            self.lines=self.lines+(
"       Decoupage.NumberOfSegments("""+str(1)+")").split("\n")


        else:
            self.lines=self.lines+(
"       Decoupage.NumberOfSegments("+str(tub.MeshNbElement)+")").split("\n")


        if model in ["TUYAU"]:
            self.lines=self.lines+(
"       Quadratic_Mesh = Decoupage.QuadraticMesh()").split("\n")




        self.lines=self.lines+("""
       smesh.SetName("""+ name_vector+"M,'"+name_vector+"""')
       """+name_vector+"""M.Compute()
       """+name_vector+"M.Group("+name_startpoint+""")
       """+name_vector+"M.Group("+name_endpoint+""")
       """+name_vector+"M.GroupOnGeom("+name_vector+""")
    except:
       ERREUR=True
       print (\"   =>ERROR WHILE GENERATING THE MESH!_\")
       return
        """).split("\n")

#==============================================================================
    def _vector_rectangular_1D(self,tubavector):
        """This function creates a rectangluar tube-profile with the specified wall thickness as visualization.
        If no wall thickness is specified, the profile is solid.
        The actual mesh is only one-dimensional. The crosssection is later specified in the Aster-File"""

        model=tubavector.model
        Vx=tubavector.vector.normalized()
        Vy=tubavector.vd1x
#        print("NAME",tubavector.name)
#        print("Vy",Vy)
#        print("Vx",Vx)
        Vz=Vx.cross(Vy)
#        print("Vz",Vz)

        
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
    try:
      print(\"Add: """+name_vector+"""\")
      """+name_vector+"= geompy.MakeVector("+name_startpoint+","+name_endpoint+""")
      #Liste.append(["""+name_startpoint+",\""+name_startpoint+"""\"])
      geompy.addToStudy("""+name_vector+",\""+name_vector+"""\" )
#      Liste.append(["""+name_vector+",\""+name_vector+"""\"])
      List_Visualization.append("""+name_vector+""")
        """).split("\n")

        if solid_crosssection:
            self.lines=self.lines+("""
      _W1 = geompy.MakeSketcher(\"Sketcher: F """+L1s+" "+L2s+": TT -"+L1s+" "+L2s+": TT -"+L1s+" -"+L2s+": TT "+L1s+" -"+L2s+""": WW\",
          [   """+str(tubavector.start_tubapoint.pos.x)+","+str(tubavector.start_tubapoint.pos.y)+","+str(tubavector.start_tubapoint.pos.z)+""",
              """+str(Vy.x)+","+str(Vy.y)+","+str(Vy.z)+""",
              """+str(Vz.x)+","+str(Vz.y)+","+str(Vz.z)+"""]
      )
      FaceTube = geompy.MakeFaceWires([_W1], 1)
      Liste.append([_W1 ,\"_W1\"])
        """).split("\n")
        else:
            self.lines=self.lines+("""
      _W1 = geompy.MakeSketcher(\"Sketcher: F """+L1s+" "+L2s+": TT -"+L1s+" "+L2s+": TT -"+L1s+" -"+L2s+": TT "+L1s+" -"+L2s+""": WW\",
          [   """+str(tubavector.start_tubapoint.pos.x)+","+str(tubavector.start_tubapoint.pos.y)+","+str(tubavector.start_tubapoint.pos.z)+""",
              """+str(Vx.x)+","+str(Vx.y)+","+str(Vx.z)+""",
              """+str(Vz.x)+","+str(Vz.y)+","+str(Vz.z)+"""]
      )

      _W2 = geompy.MakeSketcher(\"Sketcher: F """+Li1s+" "+Li2s+": TT -"+Li1s+" "+Li2s+": TT -"+Li1s+" -"+Li2s+": TT "+Li1s+" -"+Li2s+""": WW\",
          [   """+str(tubavector.start_tubapoint.pos.x)+","+str(tubavector.start_tubapoint.pos.y)+","+str(tubavector.start_tubapoint.pos.z)+""",
              """+str(Vx.x)+","+str(Vx.y)+","+str(Vx.z)+""",
              """+str(Vz.x)+","+str(Vz.y)+","+str(Vz.z)+"""]
      )
      FaceTube= geompy.MakeFaceWires([_W1, _W2], 1)
      Liste.append([_W1 ,\"_W1\"])
      Liste.append([_W2 ,\"_W2\"])
#      Pipe = geompy.MakePipe( S ,"""+name_vector+""")
#      Pipe.SetColor(SALOMEDS.Color("""+tub.colors["TUBE"]+"""))
#      Pipe_id=geompy.addToStudy(Pipe,\" """+ name_vector +"""_3D\")
#      gg.createAndDisplayGO(Pipe_id)
#      gg.setDisplayMode(Pipe_id,1)       
 
            """).split("\n")


        self.lines=self.lines+("""
    except:
       ERREUR=True
       print (\"   =>ERROR BUILDING THE GEOMETRY!\")
       for x in Liste :
           geompy.addToStudy(x[0],x[1])
       return

    try:
       """+name_vector+"M = smesh.Mesh("+  name_vector +""")
       Decoupage = """+ name_vector+"M.Segment()").split("\n")


        if model in ["BARRE","RESSORT"]:
            self.lines=self.lines+(
"       Decoupage.NumberOfSegments("""+str(1)+")").split("\n")


        else:
            self.lines=self.lines+(
"       Decoupage.NumberOfSegments("+str(tub.MeshNbElement)+")").split("\n")


        self.lines=self.lines+("""
       smesh.SetName("""+ name_vector+"M,'"+name_vector+"""')
       """+name_vector+"""M.Compute()
       """+name_vector+"M.Group("+name_startpoint+""")
       """+name_vector+"M.Group("+name_endpoint+""")
       """+name_vector+"M.GroupOnGeom("+name_vector+""")
    except:
       ERREUR=True
       print (\"   =>ERROR WHILE GENERATING THE MESH!_\")
       return
        """).split("\n")


#==============================================================================
    def _visualize_Pipe_1D(self, tubavector):
        model=tubavector.model
        self.lines=self.lines+("""

    if List_Visualization!=[]:
       _W=geompy.MakeWire(List_Visualization,1e-7)
       Pipe = geompy.MakePipe( FaceTube ,_W)
       Pipe.SetColor(SALOMEDS.Color("""+tub.colors[model]+"""))
       Pipe_id=geompy.addToStudyInFather("""+tubavector.name+""",Pipe,\"Pipe\")
       gg.createAndDisplayGO(Pipe_id)
       gg.setDisplayMode(Pipe_id,"""+"1"+""")
       for x in Liste:
           geompy.addToStudyInFather(Pipe,x[0],x[1])
       Liste=[]
       List_Visualization=[]
    """).split("\n")



#==============================================================================

    def _visualize_Arrow(self):
        Arrow="Arrow_"+Pn
        As=VectString2(An)
        Cs=VectString2(c)

        self.lines=self.lines+("""
    try:
      Liste=[]
      Pf="+Pn"
      Liste.append([Pf,\"Pf\"])
      Rf="+str(Rf)"
      P2=geompy.MakeVertexWithRef(Pf,"+As+")
      Liste.append([P2,\"P2\"])
      V=geompy.MakeVector(Pf,P2)
      Liste.append([V,\"V\"])
      S=geompy.MakeCircle(Pf,V,Rf)
      Liste.append([S,\"S\"])
      Tige = geompy.MakePipe( S , V )
      Liste.append([Tige,\"Tige\"])
      Pointe = geompy.MakeCone(P2 ,V,2*Rf,0,5*Rf)
      Liste.append([Pointe,\"Pointe\"])
      Fleche = geompy.MakeCompound([Tige,Pointe])
      "+Fleche+" =Fleche
      Fleche.SetColor(SALOMEDS.Color("+Cs+"))
      Fleche_id=geompy.addToStudy(Fleche ,\""+ Fleche +"\")
      gg.createAndDisplayGO(Fleche_id)
      gg.setDisplayMode(Fleche_id,1)
    #    "  for x in Liste:
    #    "    geompy.addToStudyInFather(Fleche,x[0],x[1])
    except:
       print\"Erreur fleche effort!\"
       for x in Liste:
           geompy.addToStudy(x[0],x[1])
       gg.createAndDisplayGO(O_id)
       gg.setDisplayMode(O_id,1)
       return
        """.split("\n"))

#==============================================================================

    def _visualize_ddl(self,tubapoint,section):
        outerRadius=section[0]
        name_point=tubapoint.name
           
        if tubapoint.ddl==[0,0,0,0,0,0]:
            self.lines=self.lines+("""
                
    """+name_point+"""_BLOCK_xyzrxryrz=geompy.MakeBox("""+str(tubapoint.pos.x+2*outerRadius)+""","""+str(tubapoint.pos.y+2*outerRadius)+""","""+str(tubapoint.pos.z+2*outerRadius)+""","""+str(tubapoint.pos.x-2*outerRadius)+""","""+str(tubapoint.pos.y-2*outerRadius)+""","""+str(tubapoint.pos.z-2*outerRadius)+""")	
    """+name_point+"""_BLOCK_xyzrxryrz.SetColor(SALOMEDS.Color("""+tub.colors["BLOCK"]+"""))
    B_id=geompy.addToStudyInFather( """+ name_point +""", """+name_point+"""_BLOCK_xyzrxryrz,'"""+name_point+"""_BLOCK_xyzrxryrz' )

    gg.createAndDisplayGO(B_id)
    gg.setDisplayMode(B_id,1)



 

#        
    """).split("\n")  	            
      
        else:    
        
            V1s_list=[]        
            if not tubapoint.ddl[0]=="x":
                V1s_list.append([[3*outerRadius,0,0],[2*outerRadius,0,0],[-3*outerRadius,0,0],[-2*outerRadius,0,0],"x"])
            if not tubapoint.ddl[1]=="x":
                V1s_list.append([[0,3*outerRadius,0],[0,2*outerRadius,0],[0,-3*outerRadius,0],[0,-2*outerRadius,0],"y"])          
            if not tubapoint.ddl[2]=="x":
                V1s_list.append([[0,0,3*outerRadius],[0,0,2*outerRadius],[0,0,-3*outerRadius],[0,0,-2*outerRadius],"z"])            
    
            

    
            for V1s in V1s_list:
                self.lines=self.lines+("""        
 
#    try:
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
    
#   B_id=geompy.addToStudy(B,"B")
    gg.createAndDisplayGO(B_id)
    gg.setDisplayMode(B_id,1)
 
    
#    for x in Liste:
#        geompy.addToStudyInFather(B,x[0],x[1])
#        
#    except:
#        print("DDL wasnt visualized")
#        for x in Liste:
#            geompy.addToStudy(x[0],x[1])
#            return
        
    """).split("\n")        
        

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
 
#    try:
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
    
    gg.createAndDisplayGO(S_id)
    gg.setDisplayMode(S_id,1)
 
    
       
    """).split("\n") 

#==============================================================================
    def _initialize(self):
        self.lines=self.lines+(
"""#!/usr/bin/python 3
# -*- coding: iso-8859-1 -*-

import time
time1=time.time()
import sys
sys.path.append('/home/caelinux/TUBAV2')
sys.path.append(' """+self.my_directory+""" ')

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
    List_Visualization=[]
    L1=[]
    L2=[]
    List_id=[]
    ERREUR=False

    #gst.deleteShape(Obj)
            """).split("\n")
            
#==============================================================================
    def _create_mesh_compound(self,dict_tubavectors): 

            

                


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
        text += "]"
        
        self.lines=self.lines+("""        
    #Creates the mesh compound
    if not(ERREUR):
        Completed_Mesh = smesh.Concatenate("""+text+""", 1, 0, 1e-05)
        coincident_nodes = Completed_Mesh.FindCoincidentNodes( 1e-05 )
        Completed_Mesh.MergeNodes(coincident_nodes)
        equal_elements = Completed_Mesh.FindEqualElements(Completed_Mesh)    
        Completed_Mesh.MergeElements(equal_elements)   
        smesh.SetName(Completed_Mesh.GetMesh(), 'Completed_Mesh')
        """).split("\n")

            
            
#==============================================================================
    def _finalize(self):
        self.lines=self.lines+("""
    if salome.sg.hasDesktop():
       salome.sg.updateObjBrowser(0)
    time2=time.time()
    dtime = time2 - time1
    print(\"------------------------\")
    print(\"Duration of construction:\"+str(round(dtime,2))+\"s\")

    """).split("\n")


        self.lines=self.lines+"Project()".split()

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
    try:
      print(\"Add  """+ name_vector +""" \")
      Liste=[]
      """+name_vector+""" = geompy.MakeArcCenter("""+name_centerpoint+
                      ""","""+name_startpoint+""","""+name_endpoint+""")
      geompy.addToStudy("""+name_vector+""",\""""+name_vector+ """\")
      Liste.append(["""+name_vector+""",\""""+name_vector+"""\"])
      List_Visualization.append("""+name_vector+""")

         """).split("\n")


        self.lines=self.lines+("""
      C1 = geompy.MakeCircle("""+name_startpoint+",Vd2x_"+name_startpoint+
                                                      ","+str(radius)+""")
      C2 = geompy.MakeCircle("""+name_startpoint+",Vd2x_"+name_startpoint+
                                             ","+str(radius-thickness)+""")
      FaceTube = geompy.MakeFaceWires([C1, C2], 1)
      Liste.append([C1 ,\"CercleExt\"])
      Liste.append([C2 ,\"CercleInt\"])
            """).split("\n")

        self.lines=self.lines+("""

    except:
       ERREUR=True
       print (\"   =>ERROR BUILDING THE GEOMETRY!\")
       for x in Liste :
           geompy.addToStudy(x[0],x[1])
       return

    try:
       """+name_vector+"M = smesh.Mesh("+  name_vector +""")
       Decoupage = """+ name_vector+"M.Segment()").split("\n")


        if model in ["BARRE","RESSORT"]:
            self.lines=self.lines+(
"       Decoupage.NumberOfSegments("""+str(1)+")").split("\n")

        else:
            self.lines=self.lines+(
"       Decoupage.NumberOfSegments("+str(tub.MeshNbElement)+")").split("\n")

        if model in ["TUYAU"]:
            self.lines=self.lines+(
"       Quadratic_Mesh = Decoupage.QuadraticMesh()").split("\n")

        self.lines=self.lines+("""
       smesh.SetName("""+ name_vector+"M,'"+name_vector+"""')
       """+name_vector+"""M.Compute()
       """+name_vector+"M.GroupOnFilter( SMESH.NODE,'"+name_startpoint+"""', smesh.GetFilter( SMESH.NODE, SMESH.FT_LyingOnGeom,'=',"""+name_startpoint+"""))
       """+name_vector+"M.GroupOnFilter( SMESH.NODE,'"+name_endpoint+"""', smesh.GetFilter( SMESH.NODE, SMESH.FT_LyingOnGeom,'=',"""+name_endpoint+"""))
       """+name_vector+"M.GroupOnGeom("+name_vector+""")
    except:
       ERREUR=True
       print (\"   =>ERROR WHILE GENERATING THE MESH!_\")
       return
            """).split("\n")

#==============================================================================
    def _TShape_3D(self,tubavector) :
        [radius,thickness]=tubavector.section
        [incident_radius,incident_thickness]=tubavector.incident_section
        name_vector=name_vector = str(tubavector.name)#+tubavector.model[:3]

        name_incidentpoint=tubavector.incident_end_tubapoint.name
        name_startpoint=tubavector.start_tubapoint.name
        name_endpoint=tubavector.end_tubapoint.name
        
        
        main_halflength=str(tubavector.vector.magnitude()/2)
        
        incident_halflength=str(tubavector.incident_vector.magnitude())
        print(name_vector,type(name_vector))
        self.lines=self.lines+("""
    try:
        print(\"Add  """+ name_vector +""" \")
#            Vertex_1 = geompy.MakeVertex(0, 0, 0)
#            Vertex_3 = geompy.MakeVertex(280, 0, 0)
#            Vertex_4 = geompy.MakeVertex(140, 100, 0)
        ["""+ name_vector +""", Junction_1, Junction_2, Junction_3, Thickness,
         Circular_quarter_of_pipe, Circular_quarter_of_pipe_1,Main_pipe_half_length,
         Flange, Incident_pipe_half_length, Internal_faces] =\
            geompy.MakePipeTShape("""+str(radius-thickness)+","+str(thickness)+","+ main_halflength+","+
                                  str(incident_radius-incident_thickness)+","+str(incident_thickness)+","+
                                  incident_halflength+", True,"
                                  +name_startpoint+","+ name_endpoint+
                                  ","+name_incidentpoint+""")
                                  

#            geompy.addToStudy( Vertex_1, 'Vertex_1' )
#            geompy.addToStudy( Vertex_3, 'Vertex_3' )
#            geompy.addToStudy( Vertex_4, 'Vertex_4' )
        geompy.addToStudy( """+ name_vector +""", '"""+ name_vector +"""' )
        geompy.addToStudyInFather( """+ name_vector +""", Junction_1, 'Junction 1' )
        geompy.addToStudyInFather( """+ name_vector +""", Junction_2, 'Junction 2' )
        geompy.addToStudyInFather( """+ name_vector +""", Junction_3, 'Junction 3' )
        geompy.addToStudyInFather( """+ name_vector +""", Thickness, 'Thickness' )
        geompy.addToStudyInFather( """+ name_vector +""", Circular_quarter_of_pipe, 'Circular quarter of pipe' )
        geompy.addToStudyInFather( """+ name_vector +""", Circular_quarter_of_pipe_1, 'Circular quarter of pipe' )
        geompy.addToStudyInFather( """+ name_vector +""", Main_pipe_half_length, 'Main pipe half length' )
        geompy.addToStudyInFather( """+ name_vector +""", Flange, 'Flange' )
        geompy.addToStudyInFather( """+ name_vector +""", Incident_pipe_half_length, 'Incident pipe half length' )
        geompy.addToStudyInFather("""+ name_vector +""", Internal_faces, 'Internal faces' )

        L_Start = geompy.GetShapesOnPlane("""+name_vector+""",geompy.ShapeType[\"FACE\"],Vd2x_"""+tubavector.start_tubapoint.name+""",GEOM.ST_ON)
        """+name_vector+"""StartFace = geompy.MakeCompound(L_Start)
        geompy.addToStudy("""+name_vector+"""StartFace,\""""+name_vector+"""StartFace\")
        Liste.append([ """+name_vector+"""StartFace,\""""+name_vector+"""StartFace\"]) 

        L_Incident = geompy.GetShapesOnPlane("""+name_vector+""",geompy.ShapeType[\"FACE\"],Vd2x_"""+tubavector.incident_end_tubapoint.name+""",GEOM.ST_ON)
        """+name_vector+"""IncidentFace = geompy.MakeCompound(L_Incident)
        geompy.addToStudy("""+name_vector+"""IncidentFace,\""""+name_vector+"""IncidentFace\")
        Liste.append([ """+name_vector+"""IncidentFace,\""""+name_vector+"""IncidentFace\"]) 
        
        L_End = geompy.GetShapesOnPlane("""+name_vector+""",geompy.ShapeType[\"FACE\"],Vd2x_"""+tubavector.end_tubapoint.name+""",GEOM.ST_ON)
        """+name_vector+"""EndFace = geompy.MakeCompound(L_End)
        geompy.addToStudy("""+name_vector+"""EndFace,\""""+name_vector+"""EndFace\")
        Liste.append([ """+name_vector+"""EndFace,\""""+name_vector+"""EndFace\"]) 


        
    except:
       ERREUR=True
       print (\"   =>ERROR BUILDING THE GEOMETRY!\")
       for x in Liste :
           geompy.addToStudy(x[0],x[1])
    ###
    ### SMESH component
    ###

    try:
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
        """+name_vector+"M.GroupOnGeom("+name_vector+"StartFace" """)
        """+name_vector+"M.GroupOnGeom("+name_vector+"IncidentFace" """)
        """+name_vector+"M.GroupOnGeom("+name_vector+"EndFace" """)

        smesh.SetName(Regular_1D.GetAlgorithm(), 'Regular_1D')
        smesh.SetName(Hexa_3D.GetAlgorithm(), 'Hexa_3D')
        smesh.SetName(Quadrangle_2D.GetAlgorithm(), 'Quadrangle_2D')
        smesh.SetName(Nb_Segments_2, 'Nb. Segments_2')
        smesh.SetName(Nb_Segments_1, 'Nb. Segments_1')
        smesh.SetName("""+ name_vector +"""M.GetMesh()," """+name_vector+"""M")
        smesh.SetName(Sub_mesh_1, 'Sub-mesh_1')
    except:
       ERREUR=True
       print (\"   =>ERROR BUILDING THE MESH!\")
       for x in Liste :
           geompy.addToStudy(x[0],x[1])
            """).split("\n")
#==============================================================================
    def _stiffness(self,tubapoint):
        Ks="Ressort"+str(self.nP)

        CodeAppend(self.CodeS,[
        "R="+str(R),
        "print(\"Ajout d'un ressort\")", 
        "Cercle = geompy.MakeCircle("+self.Px+",Vd2x,R*1.1)",
        "Surface = geompy.MakeFaceWires([Cercle], 1)",
        Ks+" = geompy.MakePrismVecH2Ways(Surface, Vd2x,R/2)",
        Ks+".SetColor(SALOMEDS.Color("+tub.colors[model]+"))",
        "P_id = geompy.addToStudy("+Ks+",\""+Ks+"\")",
        "gg.createAndDisplayGO(P_id)",
        "gg.setDisplayMode(P_id,1)",
        ])




