
        
# ======== Select a file for opening:
import tkinter
from tkinter import filedialog

root = tkinter.Tk()
file = filedialog.askopenfilename(parent=root,
                                    initialdir='/home/max/salome_meca/TUBA_2019/tutorials/000_Testing/x_008_TUYAU_3d',
                                    filetypes=[("Result Files","*.rmed")])
root.destroy()

import pvsimple
pvsimple.ShowParaviewView()
#### import the simple module from the paraview
from pvsimple import *

#Modules to create ParaVis-representation
#from smeca_utils import macro_post
#import presentations

#### disable automatic camera reset on 'Show'
pvsimple._DisableFirstRenderCameraReset()

file="/home/max/salome_meca/TUBA_2019/tutorials/000_Testing/x_008_TUYAU_3d/008_TUYAU_3D_K_M_F-RESULTS_salome.rmed"

       


#------------------------------------------------------------------------------       
# create a new 'MED Reader'
#------------------------------------------------------------------------------

DEFORMATION_FORCE_REACTION = MEDReader(FileName=file)
RenameSource('DEFORMATION_FORCE_REACTION',DEFORMATION_FORCE_REACTION)

keys=DEFORMATION_FORCE_REACTION.GetProperty("FieldsTreeInfo")[::2]
#Get all the fields contained in the ResultFile
arr_name_with_dis=[elt.split("/") for elt in keys]

for arr in arr_name_with_dis:
    if 'DEPL' in arr[3]:
        comfield=arr[2]
        timestep=arr[0]

print(timestep,comfield)
newlist=[]
for arr in arr_name_with_dis:
	if arr[0]==timestep and arr[2]==comfield :
		newlist.append("/".join(arr)) 

print(newlist)
DEFORMATION_FORCE_REACTION.AllArrays = newlist
DEFORMATION_FORCE_REACTION.GenerateVectors = 1

renderView1 = GetActiveViewOrCreate('RenderView')
# Guess an absolute scale factor form the bounding box dimensions
 
       

#------------------------------------------------------------------------------
# create a new 'Warp By Vector'  (Deformation)
#------------------------------------------------------------------------------

# set active source
SetActiveSource(DEFORMATION_FORCE_REACTION)

Deformation_Warp= WarpByVector(Input=DEFORMATION_FORCE_REACTION)
Deformation_Warp.Vectors = ['POINTS', 'RESU____DEPL_Vector']
Deformation_Warp.ScaleFactor = 1

Deformation_Warp_Display = Show(Deformation_Warp, renderView1)
Deformation_Warp_Display.LineWidth = 4.0
Deformation_Warp_Display.RescaleTransferFunctionToDataRange(True)
Deformation_Warp_Display.SetScalarBarVisibility(renderView1, True)

ColorBy(Deformation_Warp_Display, ('POINTS', 'RESU____DEPL_Vector'))

RenameSource('DeformedShape', Deformation_Warp)

RESUDEPLVector_LUT = GetColorTransferFunction('RESUDEPLVector')
RESUDEPLVector_LUT.VectorMode = 'Magnitude'
RESUDEPLVector_LUT_ColorBar = GetScalarBar(RESUDEPLVector_LUT, renderView1)
RESUDEPLVector_LUT_ColorBar.Title = 'Deformation'
RESUDEPLVector_LUT_ColorBar.ComponentTitle = 'Magnitude (mm)'

RESUDEPLVector_PWF = GetOpacityTransferFunction('RESUDEPLVector')                                                        
      

#------------------------------------------------------------------------------
#deformation_Vector
#------------------------------------------------------------------------------
# set active source
SetActiveSource(DEFORMATION_FORCE_REACTION)

Deformation_Vectors= Glyph(Input=DEFORMATION_FORCE_REACTION,GlyphType='Arrow')
SetActiveSource(Deformation_Vectors)     
# Properties modified on glyph1
Deformation_Vectors.Scalars = ['POINTS', 'None']
Deformation_Vectors.Vectors = ['POINTS', 'RESU____DEPL_Vector']
Deformation_Vectors.GlyphMode = 'All Points'
Deformation_Vectors.ScaleMode = 'vector'
Deformation_Vectors.ScaleFactor = 1

# show data in view
Deformation_Vectors_Display = Show(Deformation_Vectors, renderView1)
Deformation_Vectors_Display.SetScalarBarVisibility(renderView1, True)

# set scalar coloring
ColorBy(Deformation_Vectors_Display, ('POINTS', 'RESU____DEPL_Vector'))

# rename source object
RenameSource('Deformation_Arrows', Deformation_Vectors)

      


#------------------------------------------------------------------------------
# create force_Vectors
#------------------------------------------------------------------------------
SetActiveSource(DEFORMATION_FORCE_REACTION)
Force_Vectors = Glyph(Input=DEFORMATION_FORCE_REACTION,GlyphType='Arrow')
SetActiveSource(Force_Vectors)   
# Properties modified on Force_Vectors
Force_Vectors.Scalars = ['POINTS', 'None']
Force_Vectors.Vectors = ['POINTS','RESU____FORC_NODA_Vector']
Force_Vectors.ScaleMode = 'vector'
Force_Vectors.ScaleFactor = 1
Force_Vectors.GlyphMode = 'All Points'

# show data in view
SetActiveSource(Force_Vectors)
Force_Vectors_Display = Show(Force_Vectors, renderView1)
Force_Vectors_Display.SetScalarBarVisibility(renderView1, True)
Force_Vectors_Display.SelectInputVectors = ['POINTS', 'GlyphVector']
Force_Vectors_Display.RescaleTransferFunctionToDataRange(True)

ColorBy(Force_Vectors_Display, ('POINTS', 'RESU____FORC_NODA_Vector'))

# rename source object
RenameSource('Reaction_Forces', Force_Vectors)

Force_LUT = GetColorTransferFunction('RESUFORCNODAVector')
Force_LUT.VectorMode = 'Magnitude'
Force_LUT_ColorBar = GetScalarBar(Force_LUT, renderView1)
Force_LUT_ColorBar.Title = 'Forces'
Force_LUT_ColorBar.ComponentTitle ='Magnitude (N)'

Force_PWF = GetOpacityTransferFunction('RESUFORCNODAVector')
     


#------------------------------------------------------------------------------       
# create a new 'MED Reader'
#------------------------------------------------------------------------------

TEMPERATURE = MEDReader(FileName=file)
RenameSource('TEMPERATURE',TEMPERATURE)

keys=TEMPERATURE.GetProperty("FieldsTreeInfo")[::2]
#Get all the fields contained in the ResultFile
arr_name_with_dis=[elt.split("/") for elt in keys]

for arr in arr_name_with_dis:
    if '_T_' in arr[3]:
        comfield=arr[2]
        timestep=arr[0]

print(timestep,comfield)
newlist=[]
for arr in arr_name_with_dis:
	if arr[0]==timestep and arr[2]==comfield :
		newlist.append("/".join(arr)) 

print(newlist)
TEMPERATURE.AllArrays = newlist
TEMPERATURE.GenerateVectors = 1

renderView1 = GetActiveViewOrCreate('RenderView')
# Guess an absolute scale factor form the bounding box dimensions
 
       
    
#------------------------------------------------------------------------------
# create a new 'ELNO Mesh' for 3D-elements
#------------------------------------------------------------------------------ 
SetActiveSource(TEMPERATURE)
Temperature_function = ELNOfieldToSurface(Input=TEMPERATURE)        
Temperature_function_Display = Show(Temperature_function, renderView1)

Temperature_function_Display.RescaleTransferFunctionToDataRange(True)
Temperature_function_Display.SetScalarBarVisibility(renderView1, True)
Temperature_function_Display.LineWidth = 4.0

ColorBy(Temperature_function_Display, ('POINTS', 'RES_T_F_TEMP'))

RenameSource('Temperature_function', Temperature_function)  

RES_T_F_TEMP_LUT = GetColorTransferFunction('RES_T_F_TEMP')
RES_T_F_TEMP_LUT.VectorMode = 'Component'
RES_T_F_TEMP_LUT_ColorBar = GetScalarBar(RES_T_F_TEMP_LUT, renderView1)
RES_T_F_TEMP_LUT_ColorBar.Title = 'Temperature_function'
RES_T_F_TEMP_LUT_ColorBar.ComponentTitle = 'Temperature [Celsius]'

Temperature_function_Display.RescaleTransferFunctionToDataRange(False)                                                     
RES_T_F_TEMP_PWF = GetOpacityTransferFunction('RES_T_F_TEMP')
        
     
    
#------------------------------------------------------------------------------
# create a new 'ELNO Mesh' for 3D-elements
#------------------------------------------------------------------------------ 
SetActiveSource(TEMPERATURE)
Temperature_real = ELNOfieldToSurface(Input=TEMPERATURE)        
Temperature_real_Display = Show(Temperature_real, renderView1)

Temperature_real_Display.RescaleTransferFunctionToDataRange(True)
Temperature_real_Display.SetScalarBarVisibility(renderView1, True)
Temperature_real_Display.LineWidth = 4.0

ColorBy(Temperature_real_Display, ('POINTS', 'CHA_T_R'))

RenameSource('Temperature_real', Temperature_real)  

CHA_T_R_LUT = GetColorTransferFunction('CHA_T_R')
CHA_T_R_LUT.VectorMode = 'Component'
CHA_T_R_LUT_ColorBar = GetScalarBar(CHA_T_R_LUT, renderView1)
CHA_T_R_LUT_ColorBar.Title = 'Temperature_real'
CHA_T_R_LUT_ColorBar.ComponentTitle = 'Temperature [Celsius]'

Temperature_real_Display.RescaleTransferFunctionToDataRange(False)                                                     
CHA_T_R_PWF = GetOpacityTransferFunction('CHA_T_R')
        
     


#------------------------------------------------------------------------------       
# create a new 'MED Reader'
#------------------------------------------------------------------------------

VOLUME = MEDReader(FileName=file)
RenameSource('VOLUME',VOLUME)

keys=VOLUME.GetProperty("FieldsTreeInfo")[::2]
#Get all the fields contained in the ResultFile
arr_name_with_dis=[elt.split("/") for elt in keys]

for arr in arr_name_with_dis:
    if 'R_3D____SIEQ' in arr[3]:
        comfield=arr[2]
        timestep=arr[0]

print(timestep,comfield)
newlist=[]
for arr in arr_name_with_dis:
	if arr[0]==timestep and arr[2]==comfield :
		newlist.append("/".join(arr)) 

print(newlist)
VOLUME.AllArrays = newlist
VOLUME.GenerateVectors = 1

renderView1 = GetActiveViewOrCreate('RenderView')
# Guess an absolute scale factor form the bounding box dimensions
 
       
    
#------------------------------------------------------------------------------
# create a new 'ELNO Mesh' for 3D-elements
#------------------------------------------------------------------------------ 
SetActiveSource(VOLUME)
VonMise = ELNOfieldToSurface(Input=VOLUME)        
VonMise_Display = Show(VonMise, renderView1)

VonMise_Display.RescaleTransferFunctionToDataRange(True)
VonMise_Display.SetScalarBarVisibility(renderView1, True)
VonMise_Display.LineWidth = 4.0

ColorBy(VonMise_Display, ('POINTS', 'R_3D____SIEQ_ELNO'))

RenameSource('VonMise', VonMise)  

R_3D____SIEQ_ELNO_LUT = GetColorTransferFunction('R_3D____SIEQ_ELNO')
R_3D____SIEQ_ELNO_LUT.VectorMode = 'Component'
R_3D____SIEQ_ELNO_LUT_ColorBar = GetScalarBar(R_3D____SIEQ_ELNO_LUT, renderView1)
R_3D____SIEQ_ELNO_LUT_ColorBar.Title = 'VonMise'
R_3D____SIEQ_ELNO_LUT_ColorBar.ComponentTitle = 'Magnitude (MPa // N/mm**2)'

VonMise_Display.RescaleTransferFunctionToDataRange(False)                                                     
R_3D____SIEQ_ELNO_PWF = GetOpacityTransferFunction('R_3D____SIEQ_ELNO')
        
     


#------------------------------------------------------------------------------       
# create a new 'MED Reader'
#------------------------------------------------------------------------------

TUYAU = MEDReader(FileName=file)
RenameSource('TUYAU',TUYAU)

keys=TUYAU.GetProperty("FieldsTreeInfo")[::2]
#Get all the fields contained in the ResultFile
arr_name_with_dis=[elt.split("/") for elt in keys]

for arr in arr_name_with_dis:
    if 'MAX_VMIS' in arr[3]:
        comfield=arr[2]
        timestep=arr[0]

print(timestep,comfield)
newlist=[]
for arr in arr_name_with_dis:
	if arr[0]==timestep and arr[2]==comfield :
		newlist.append("/".join(arr)) 

print(newlist)
TUYAU.AllArrays = newlist
TUYAU.GenerateVectors = 1

renderView1 = GetActiveViewOrCreate('RenderView')
# Guess an absolute scale factor form the bounding box dimensions
 
       
    
#------------------------------------------------------------------------------
# create a new 'ELNO Mesh' for 3D-elements
#------------------------------------------------------------------------------ 
SetActiveSource(TUYAU)
MaxVonMise = ELNOfieldToSurface(Input=TUYAU)        
MaxVonMise_Display = Show(MaxVonMise, renderView1)

MaxVonMise_Display.RescaleTransferFunctionToDataRange(True)
MaxVonMise_Display.SetScalarBarVisibility(renderView1, True)
MaxVonMise_Display.LineWidth = 4.0

ColorBy(MaxVonMise_Display, ('POINTS', 'MAX_VMISUT01_ELNO'))

RenameSource('MaxVonMise', MaxVonMise)  

MAX_VMISUT01_ELNO_LUT = GetColorTransferFunction('MAX_VMISUT01_ELNO')
MAX_VMISUT01_ELNO_LUT.VectorMode = 'Component'
MAX_VMISUT01_ELNO_LUT_ColorBar = GetScalarBar(MAX_VMISUT01_ELNO_LUT, renderView1)
MAX_VMISUT01_ELNO_LUT_ColorBar.Title = 'MaxVonMise'
MAX_VMISUT01_ELNO_LUT_ColorBar.ComponentTitle = 'Magnitude (MPa // N/mm**2)'

MaxVonMise_Display.RescaleTransferFunctionToDataRange(False)                                                     
MAX_VMISUT01_ELNO_PWF = GetOpacityTransferFunction('MAX_VMISUT01_ELNO')
        
     

#------------------------------------------------------------------------------       
# Visualize Local Base   X,Y,Z  (red, yellow, green)
#------------------------------------------------------------------------------
print("Create Visualization of local coordinates: X,Y,Z  (red, yellow, green) ")

LocalCoordinates = MEDReader(FileName=file)
RenameSource('LocalCoordinates',LocalCoordinates)



keys=LocalCoordinates.GetProperty("FieldsTreeInfo")[::2]
#Get all the fields contained in the ResultFile
arr_name_with_dis=[elt.split("/") for elt in keys]


for arr in arr_name_with_dis:
    if 'RepLocal' in arr[3]:
        comfield=arr[2]
        timestep=arr[0]

print(timestep,comfield)
newlist=[]
for arr in arr_name_with_dis:
	if arr[0]==timestep and arr[2]==comfield :
		newlist.append("/".join(arr)) 

print(newlist)
LocalCoordinates.AllArrays = newlist
LocalCoordinates.GenerateVectors = 1


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

            localAxis = FindSource('LocalAxis_"+direction[i-1]+"')
            # hide data in view
            Hide(localAxis, renderView1)

      
 

try:
    # create a new 'Legacy VTK Reader'
    Visualization_Geom = LegacyVTKReader(FileNames=['//home/max/salome_meca/TUBA_2019/tutorials/000_Testing/x_008_TUYAU_3d/compound_paravis.vtk'])

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

      