#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""

"""
import numpy as np
import external.euclid as eu
import logging

import tuba_vars_and_funcs as tub
import tuba.define_geometry as tuba_geom

class ParaPost:
    def __init__(self,my_directory):
        self.my_directory=my_directory
        self.lines=[]
        self.BAR_flag=False
        self.TUBE_flag=False
        self.TUYAU_flag=False
        self.VOLUME_flag=False
        self.SPRING_flag=False
        self.FRICTION_flag=False
        self.CONTINUOUS_VOLUME_flag=False

    def write(self,dict_tubavectors,dict_tubapoints,resultfile_aster):

        self._initialize(resultfile_aster)

        for tubavector in dict_tubavectors:
            if tubavector.model=="TUYAU":
                 self.TUYAU_flag=True
            if tubavector.model in ["TUBE","RECTANGULAR"]:
                 self.TUBE_flag=True
            if tubavector.model in ["VOLUME"]:
                 self.VOLUME_flag=True
            if tubavector.model in ["BAR"]:
                 self.BAR_flag=True

        for tubavector in dict_tubavectors:
            if not tubavector.start_tubapoint.is_element_start(): 
                if tubavector.start_tubapoint.get_last_vector().model=="VOLUME" and tubavector.model=="VOLUME":
                    self.CONTINUOUS_VOLUME_flag=True

        for tubapoint in dict_tubapoints:
            if not tubapoint.friction_coefficient==0.0:
                 self.FRICTION_flag=True
            if not tubapoint.stiffness == [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]: 
                 self.SPRING_flag=True

        flags=("""
#Flags set by TUBA
#  BAR_flag="""+str(self.BAR_flag)+"""
#  TUBE_flag="""+str(self.TUBE_flag)+"""
#  TUYAU_flag="""+str(self.TUYAU_flag)+"""
#  VOLUME_flag="""+str(self.VOLUME_flag)+"""
#  SPRING_flag="""+str(self.SPRING_flag)+"""
#  FRICTION_flag="""+str(self.FRICTION_flag)+"""
""").split("\n") 

        logging.info(flags)
        self.lines=self.lines+flags

        timestep=1
        if self.TUBE_flag and not self.VOLUME_flag and not self.TUYAU_flag:
            if self.SPRING_flag and not self.FRICTION_flag :
                self._base("TUBE","\'ComSup1\'",timestep)
                self._base("DEPL_FORCE_REACTION","\'ComSup3\'",timestep)
                self._ELNO_Mesh("Stress","TUBE",'FlexibilityStress')
                self._deformation_Warp("Deformation_Warp","DEPL_FORCE_REACTION")
                self._deformation_Vector("Deformation_Vectors","DEPL_FORCE_REACTION")
                self._force_Vector("Force_Vectors","DEPL_FORCE_REACTION",'RESU____FORC_NODA_Vector')
            elif self.FRICTION_flag:    
                self._base("TUBE","\'ComSup0\'",timestep)
                self._base("DEPL_FORCE_REACTION","\'ComSup2\'",timestep)
                self._ELNO_Mesh("Stress","TUBE",'FlexibilityStress')
                self._deformation_Warp("Deformation_Warp","DEPL_FORCE_REACTION")
                self._deformation_Vector("Deformation_Vectors","DEPL_FORCE_REACTION")
                self._force_Vector("Force_Vectors","DEPL_FORCE_REACTION",'RESU____FORC_NODA_Vector')
            else:
                self._base("DEPL_FORCE_REACTION","\'ComSup0\'",timestep)
                self._ELNO_Mesh("Stress","DEPL_FORCE_REACTION",'FlexibilityStress')
                self._deformation_Warp("Deformation_Warp","DEPL_FORCE_REACTION")
                self._deformation_Vector("Deformation_Vectors","DEPL_FORCE_REACTION")
                self._force_Vector("Force_Vectors","DEPL_FORCE_REACTION",'RESU____FORC_NODA_Vector')

        if self.TUYAU_flag and not self.VOLUME_flag and not self.TUBE_flag:
            self._base("TUYAU","\'ComSup0\'",timestep)
            self._base("DEPL_FORCE_REACTION","\'ComSup1\'",timestep)
            self._ELNO_Mesh_TUYAU("MaxVonMise","TUYAU",'MAX_VMISUT01_ELNO')  
            self._deformation_Warp("Deformation_Warp","DEPL_FORCE_REACTION")
            self._deformation_Vector("Deformation_Vectors","DEPL_FORCE_REACTION")
            self._force_Vector("Force_Vectors","DEPL_FORCE_REACTION",'RESU____FORC_NODA_Vector')
        elif self.TUYAU_flag and not self.VOLUME_flag and self.TUBE_flag and self.SPRING_flag:
            self._base("TUYAU","\'ComSup0\'",timestep)
            self._base("DEPL_FORCE_REACTION","\'ComSup4\'",timestep)
            self._base("TUBE","\'ComSup3\'",timestep)
            self._ELNO_Mesh("Stress","TUBE",'FlexibilityStress')
            self._ELNO_Mesh_TUYAU("MaxVonMise","TUYAU",'MAX_VMISUT01_ELNO')
            self._deformation_Warp("Deformation_Warp","DEPL_FORCE_REACTION")
            self._deformation_Vector("Deformation_Vectors","DEPL_FORCE_REACTION")
            self._force_Vector("Force_Vectors","DEPL_FORCE_REACTION",'RESU____FORC_NODA_Vector')
#problem  --> ComSups change if springs/masses are either on a TUYAU or TUBE element 
        elif self.TUYAU_flag and not self.VOLUME_flag and self.TUBE_flag and not self.SPRING_flag:
            self._base("TUYAU","\'ComSup0\'",timestep)
            self._base("DEPL_FORCE_REACTION","\'ComSup1\'",timestep)
            self._base("TUBE","\'ComSup2\'",timestep)
            self._ELNO_Mesh("Stress","TUBE",'FlexibilityStress')
            self._ELNO_Mesh_TUYAU("MaxVonMise","TUYAU",'MAX_VMISUT01_ELNO')
            self._deformation_Warp("Deformation_Warp","DEPL_FORCE_REACTION")
            self._deformation_Vector("Deformation_Vectors","DEPL_FORCE_REACTION")
            self._force_Vector("Force_Vectors","DEPL_FORCE_REACTION",'RESU____FORC_NODA_Vector')


        if self.BAR_flag:
            self._base("DEPL_FORCE_REACTION","\'ComSup0\'",timestep)
            self._deformation_Warp("Deformation_Warp","DEPL_FORCE_REACTION")
            self._deformation_Vector("Deformation_Vectors","DEPL_FORCE_REACTION")
            self._force_Vector("Force_Vectors","DEPL_FORCE_REACTION",'RESU____FORC_NODA_Vector')


        if self.VOLUME_flag and self.TUBE_flag:
            if self.CONTINUOUS_VOLUME_flag and self.SPRING_flag:
                coms=["\'ComSup3\'","\'ComSup4\'","\'ComSup5\'"]
            if not self.CONTINUOUS_VOLUME_flag and self.SPRING_flag:
                coms=["\'ComSup2\'","\'ComSup3\'","\'ComSup4\'"]
            if self.CONTINUOUS_VOLUME_flag and not self.SPRING_flag:
                coms=["\'ComSup2\'","\'ComSup3\'","\'ComSup4\'"]
            if not self.CONTINUOUS_VOLUME_flag and not self.SPRING_flag:
                coms=["\'ComSup1\'","\'ComSup2\'","\'ComSup0\'"]

            self._base("VOLUME",coms[0],timestep)
            self._base("TUBE",coms[1],timestep)
            self._base("DEPL_FORCE_REACTION",coms[2],timestep)
            
            self._ELNO_Mesh_3D("VonMise","VOLUME",'R_3D____SIEQ_ELNO')
            self._ELNO_Mesh("Stress","TUBE",'FlexibilityStress')
            self._deformation_Warp("Deformation_Warp","DEPL_FORCE_REACTION")
            self._deformation_Vector("Deformation_Vectors","DEPL_FORCE_REACTION")
            self._force_Vector("Force_Vectors","DEPL_FORCE_REACTION",'RESU____FORC_NODA_Vector')

        elif self.VOLUME_flag and self.TUYAU_flag:
            if self.CONTINUOUS_VOLUME_flag and self.SPRING_flag:
                coms=["\'ComSup0\'","\'ComSup3\'","\'ComSup4\'"]
            if not self.CONTINUOUS_VOLUME_flag and self.SPRING_flag:
                coms=["\'ComSup0\'","\'ComSup2\'","\'ComSup1\'"]
            if self.CONTINUOUS_VOLUME_flag and not self.SPRING_flag:
                coms=["\'ComSup0\'","\'ComSup3\'","\'ComSup4\'"]
            if not self.CONTINUOUS_VOLUME_flag and not self.SPRING_flag:
                coms=["\'ComSup0\'","\'ComSup2\'","\'ComSup1\'"]
                
            self._base("TUYAU",coms[0],timestep)
            self._base("VOLUME",coms[1],timestep)
            self._base("DEPL_FORCE_REACTION",coms[2],timestep)

            self._ELNO_Mesh_TUYAU("MaxVonMise","TUYAU",'MAX_VMISUT01_ELNO')
            self._ELNO_Mesh_3D("VonMise","VOLUME",'R_3D____SIEQ_ELNO')
            self._deformation_Warp("Deformation_Warp","DEPL_FORCE_REACTION")
            self._deformation_Vector("Deformation_Vectors","DEPL_FORCE_REACTION")
            self._force_Vector("Force_Vectors","DEPL_FORCE_REACTION",'RESU____FORC_NODA_Vector')



        timestep=timestep+1 
        self._visualize_local_base("LocalCoordinates",timestep)
        self._finalize()

#==============================================================================
#  Write PostBase
#==============================================================================
    def _initialize(self,resultfile_aster):
        self.lines=self.lines+("""
        
# ======== Select a file for opening:
import Tkinter,tkFileDialog

#root = Tkinter.Tk()
#file = tkFileDialog.askopenfilename(parent=root,
#                                    initialdir='"""+self.my_directory+ """',
#                                    filetypes=[("Result Files","*.rmed")])
#root.destroy()

import pvsimple
pvsimple.ShowParaviewView()
#### import the simple module from the paraview
from pvsimple import *

#Modules to create ParaVis-representation
#from smeca_utils import macro_post
#import presentations

#### disable automatic camera reset on 'Show'
pvsimple._DisableFirstRenderCameraReset()

file=\""""+resultfile_aster+"""\"

       """).split("\n")
        
    def _base(self,file_rmed,comsup,timestep):
        self.lines=self.lines+("""

#------------------------------------------------------------------------------       
# create a new 'MED Reader'
#------------------------------------------------------------------------------

"""+file_rmed+""" = MEDReader(FileName=file)

RenameSource('"""+file_rmed+"""',"""+file_rmed+""")
keys="""+file_rmed+""".GetProperty("FieldsTreeInfo")[::2]
#Get all the fields contained in the ResultFile
arr_name_with_dis=[elt.split("/") for elt in keys]

print (arr_name_with_dis)
#        sep = str(self.MEDfile.GetProperty("Separator")[0])
#        self.fieldList = [elt.split(sep)[0] for elt in arrs_with_dis]

newlist=[]

comfield="""+comsup+"""
        
for arr in arr_name_with_dis:	
	if arr[0]=="TS"""+str(timestep)+"""\" and arr[2]==comfield :
		newlist.append("/".join(arr)) 
	
"""+file_rmed+""".AllArrays = newlist
"""+file_rmed+""".GenerateVectors = 1

renderView1 = GetActiveViewOrCreate('RenderView')

# Guess an absolute scale factor form the bounding box dimensions
 
       """).split("\n")

       
    def _deformation_Warp(self,name_warp,file_rmed): 
        self.lines=self.lines+("""
#------------------------------------------------------------------------------
# create a new 'Warp By Vector'  (Deformation)
#------------------------------------------------------------------------------

# set active source
SetActiveSource("""+file_rmed+""")

"""+name_warp+"""= WarpByVector(Input="""+file_rmed+""")
"""+name_warp+""".Vectors = ['POINTS', 'RESU____DEPL_Vector']
"""+name_warp+""".ScaleFactor = 1


"""+name_warp+"""_Display = Show("""+name_warp+""", renderView1)
"""+name_warp+"""_Display.LineWidth = 4.0
"""+name_warp+"""_Display.RescaleTransferFunctionToDataRange(True)
"""+name_warp+"""_Display.SetScalarBarVisibility(renderView1, True)

ColorBy("""+name_warp+"""_Display, ('POINTS', 'RESU____DEPL_Vector'))

RenameSource('DeformedShape', """+name_warp+""")

RESUDEPLVector_LUT = GetColorTransferFunction('RESUDEPLVector')
RESUDEPLVector_LUT.VectorMode = 'Magnitude'
RESUDEPLVector_LUT_ColorBar = GetScalarBar(RESUDEPLVector_LUT, renderView1)
RESUDEPLVector_LUT_ColorBar.Title = 'Deformation'
RESUDEPLVector_LUT_ColorBar.ComponentTitle = 'Magnitude (mm)'

RESUDEPLVector_PWF = GetOpacityTransferFunction('RESUDEPLVector')                                                        
      """).split("\n")
       
    def _deformation_Vector(self,name_glyph,file_rmed): 
        self.lines=self.lines+("""
#------------------------------------------------------------------------------
#deformation_Vector
#------------------------------------------------------------------------------
# set active source
SetActiveSource("""+file_rmed+""")

"""+name_glyph+"""= Glyph(Input="""+file_rmed+""",GlyphType='Arrow')
SetActiveSource("""+name_glyph+""")     
# Properties modified on glyph1
"""+name_glyph+""".Scalars = ['POINTS', 'None']
"""+name_glyph+""".Vectors = ['POINTS', 'RESU____DEPL_Vector']
"""+name_glyph+""".GlyphMode = 'All Points'
"""+name_glyph+""".ScaleMode = 'vector'
"""+name_glyph+""".ScaleFactor = 1


# show data in view
"""+name_glyph+"""_Display = Show("""+name_glyph+""", renderView1)
"""+name_glyph+"""_Display.SetScalarBarVisibility(renderView1, True)

# set scalar coloring
ColorBy("""+name_glyph+"""_Display, ('POINTS', 'RESU____DEPL_Vector'))

# rename source object
RenameSource('Deformation_Arrows', """+name_glyph+""")

      """).split("\n")


    def _force_Vector(self,name_glyph,file_rmed,fieldName): 
        self.lines=self.lines+("""

#------------------------------------------------------------------------------
# create force_Vectors
#------------------------------------------------------------------------------
SetActiveSource("""+file_rmed+""")
"""+name_glyph+""" = Glyph(Input="""+file_rmed+""",GlyphType='Arrow')
SetActiveSource("""+name_glyph+""")   
# Properties modified on """+name_glyph+"""
"""+name_glyph+""".Scalars = ['POINTS', 'None']
"""+name_glyph+""".Vectors = ['POINTS','"""+fieldName+"""']
"""+name_glyph+""".ScaleMode = 'vector'
"""+name_glyph+""".ScaleFactor = 1
"""+name_glyph+""".GlyphMode = 'All Points'

# show data in view
SetActiveSource("""+name_glyph+""")
"""+name_glyph+"""_Display = Show("""+name_glyph+""", renderView1)
"""+name_glyph+"""_Display.SetScalarBarVisibility(renderView1, True)
"""+name_glyph+"""_Display.SelectInputVectors = ['POINTS', 'GlyphVector']
"""+name_glyph+"""_Display.RescaleTransferFunctionToDataRange(True)

ColorBy("""+name_glyph+"""_Display, ('POINTS', '"""+fieldName+"""'))

# rename source object
RenameSource('Reaction_Forces', """+name_glyph+""")


Force_LUT = GetColorTransferFunction('"""+fieldName.replace('_','')+"""')
Force_LUT.VectorMode = 'Magnitude'
Force_LUT_ColorBar = GetScalarBar(Force_LUT, renderView1)
Force_LUT_ColorBar.Title = 'Forces'
Force_LUT_ColorBar.ComponentTitle ='Magnitude (N)'

Force_PWF = GetOpacityTransferFunction('"""+fieldName.replace('_','')+"""')
     """).split("\n")




    def _ELNO_Mesh(self,name_elno,file_rmed,field):
        self.lines=self.lines+(""" 
#------------------------------------------------------------------------------
# create a new 'ELNO Mesh'       
#------------------------------------------------------------------------------ 
SetActiveSource("""+file_rmed+""")
"""+name_elno+""" = ELNOfieldToSurface(Input="""+file_rmed+""")        


"""+name_elno+"""_Display = Show("""+name_elno+""", renderView1)

"""+name_elno+"""_Display.RescaleTransferFunctionToDataRange(True)
"""+name_elno+"""_Display.SetScalarBarVisibility(renderView1, True)
"""+name_elno+"""_Display.LineWidth = 4.0

ColorBy("""+name_elno+"""_Display, ('POINTS', '"""+field+"""'))

RenameSource('Stress (ELNO-Field)', """+name_elno+""")  

"""+field+"""_LUT = GetColorTransferFunction('"""+field+"""')

"""+field+"""_LUT_ColorBar = GetScalarBar("""+field+"""_LUT, renderView1)
"""+field+"""_LUT_ColorBar.Title = 'Stress'
"""+field+"""_LUT_ColorBar.ComponentTitle = 'Stress(MPa // N/mm**2)'

                                                 
"""+name_elno+"""_Display.RescaleTransferFunctionToDataRange(False)                                                     
"""+field+"""_PWF = GetOpacityTransferFunction('"""+field+"""')
        
       """).split("\n")
        
        
        
    def _ELNO_Mesh_TUYAU(self,name_elno,file_rmed,field): 
            
        self.lines=self.lines+("""    
#------------------------------------------------------------------------------
# create a new 'ELNO Mesh'       
#------------------------------------------------------------------------------ 
SetActiveSource("""+file_rmed+""")
"""+name_elno+""" = ELNOfieldToSurface(Input="""+file_rmed+""")        


"""+name_elno+"""_Display = Show("""+name_elno+""", renderView1)

"""+name_elno+"""_Display.RescaleTransferFunctionToDataRange(True)
"""+name_elno+"""_Display.SetScalarBarVisibility(renderView1, True)
"""+name_elno+"""_Display.LineWidth = 4.0

ColorBy("""+name_elno+"""_Display, ('POINTS', '"""+field+"""'))

RenameSource('MaxVonMise (ELNO-Field)', """+name_elno+""")  

"""+field+"""_LUT = GetColorTransferFunction('"""+field+"""')
"""+field+"""_LUT.VectorMode = 'Component'
"""+field+"""_LUT_ColorBar = GetScalarBar("""+field+"""_LUT, renderView1)
"""+field+"""_LUT_ColorBar.Title = 'VonMise Stress Max over Crosssection'
"""+field+"""_LUT_ColorBar.ComponentTitle = 'Magnitude (MPa // N/mm**2)'

                                                 
"""+name_elno+"""_Display.RescaleTransferFunctionToDataRange(False)                                                     
"""+field+"""_PWF = GetOpacityTransferFunction('"""+field+"""')
        
     """).split("\n")



    def _ELNO_Mesh_3D(self,name_elno,file_rmed,field):

        self.lines=self.lines+("""    
#------------------------------------------------------------------------------
# create a new 'ELNO Mesh' for 3D-elements
#------------------------------------------------------------------------------ 
SetActiveSource("""+file_rmed+""")
"""+name_elno+""" = ELNOfieldToSurface(Input="""+file_rmed+""")        


"""+name_elno+"""_Display = Show("""+name_elno+""", renderView1)

"""+name_elno+"""_Display.RescaleTransferFunctionToDataRange(True)
"""+name_elno+"""_Display.SetScalarBarVisibility(renderView1, True)
"""+name_elno+"""_Display.LineWidth = 4.0

ColorBy("""+name_elno+"""_Display, ('POINTS', '"""+field+"""'))

RenameSource('VonMise (ELNO-Field)', """+name_elno+""")  

"""+field+"""_LUT = GetColorTransferFunction('"""+field+"""')
"""+field+"""_LUT.VectorMode = 'Component'
"""+field+"""_LUT_ColorBar = GetScalarBar("""+field+"""_LUT, renderView1)
"""+field+"""_LUT_ColorBar.Title = 'VonMise Stress'
"""+field+"""_LUT_ColorBar.ComponentTitle = 'Magnitude (MPa // N/mm**2)'

                                                 
"""+name_elno+"""_Display.RescaleTransferFunctionToDataRange(False)                                                     
"""+field+"""_PWF = GetOpacityTransferFunction('"""+field+"""')
        
     """).split("\n")        
        

    def _visualize_local_base(self,file_rmed,timestep): 
        self.lines=self.lines+("""
#------------------------------------------------------------------------------       
# Visualize Local Base   X,Y,Z  (red, yellow, green)
#------------------------------------------------------------------------------
print("Create Visualization of local coordinates: X,Y,Z  (red, yellow, green) ")

"""+file_rmed+""" = MEDReader(FileName=file)

RenameSource('Local Base', """+file_rmed+""")
keys="""+file_rmed+""".GetProperty("FieldsTreeInfo")[::2]
#Get all the fields contained in the ResultFile
arr_name_with_dis=[elt.split("/") for elt in keys]
newlist=[]

comfield='ComSup0'
        
for arr in arr_name_with_dis:	
    if arr[0]=="TS"""+str(timestep)+"""\" and arr[2]==comfield :
        newlist.append("/".join(arr)) 
        
"""+file_rmed+""".AllArrays = newlist       
"""+file_rmed+""".GenerateVectors = 1   

renderView1 = GetActiveViewOrCreate('RenderView')
 
#Script by cbourcier
# Scale factor for glyphs, factor of the bounding box dimensions
scale_factor = 1./10

source = GetActiveSource()

# Pass cell data to cell centers, since glyphs can only be applyed on points

ELNOMesh1 = ELNOfieldToSurface(Input=LocalCoordinates)

# Guess an absolute scale factor form the bounding box dimensions
bounds = source.GetDataInformation().DataInformation.GetBounds()
side = [bounds[1] - bounds[0], bounds[3] - bounds[2], bounds[5] - bounds[4]]
length = min(side) 
scale = length*scale_factor


# Colors of each glyph, same colors as the global base in Paraview 3D viewer
d_colors = {1: [1.0, 0.0, 0.0], # X: red
            2: [1.0, 1.0, 0.0], # Y: yellow
            3: [0.0, 1.0, 0.0]} # Z: green


# For each 3 directions
direction=["X","Y","Z"]
for i in xrange(1, 4):
    # Find the field for the i-th direction
    for name, array in ELNOMesh1.PointData.items():
        if name.endswith("RepLocal_"+direction[i-1]):
            # Create glyphs (that are vectors) and set their scale factor
            Glyph1 = Glyph(Input=ELNOMesh1, Vectors = ['POINTS', name], ScaleMode = 'off')    
            SetActiveSource(Glyph1)   
            Glyph1.Scalars = ['POINTS', 'None']
            Glyph1.GlyphMode = 'All Points'
            # Show the glyphs with the right colors
            color = d_colors[i]
            GlyphRepresentation = Show(DiffuseColor = color)
            RenameSource("LocalAxis_"+direction[i-1], Glyph1)

            Render()

      """).split("\n")


      
    def _finalize(self): 
        self.lines=self.lines+(""" 

try:
    # create a new 'Legacy VTK Reader'
    Visualization_Geom = LegacyVTKReader(FileNames=['/"""+self.my_directory+"""/compound_paravis.vtk'])

    # set active source
    SetActiveSource(Visualization_Geom)

    RenameSource("Visu_Geometry", Visualization_Geom)

    # show data in view
    Visualization_Geom_Display = Show(Visualization_Geom, renderView1)

    # Properties modified on legacyVTKReader1Display
    Visualization_Geom_Display.Opacity = 0.2       
except:
    print("GEOM compound couldn't be loaded")

        
import SalomePyQt
sg = SalomePyQt.SalomePyQt()
sg.activateModule("ParaViS")  

      """).split("\n")      
      
   

            
            
    


            
            
    
