
        
# ======== Select a file for opening:
import Tkinter,tkFileDialog

root = Tkinter.Tk()
file = tkFileDialog.askopenfilename(parent=root,
                                    initialdir='/home/jangeorg/TUBA/examples/000_Testing/008_RECANGULAR',
                                    filetypes=[("Result Files","*.rmed")])                     
root.destroy()
        
import pvsimple
pvsimple.ShowParaviewView()
#### import the simple module from the paraview
from pvsimple import *
#### disable automatic camera reset on 'Show'
pvsimple._DisableFirstRenderCameraReset()

       
      

#------------------------------------------------------------------------------       
# create a new 'MED Reader'
#------------------------------------------------------------------------------

new_casermed_00 = MEDReader(FileName=file)

RenameSource('Results', new_casermed_00)
keys=new_casermed_00.GetProperty("FieldsTreeInfo")[::2]
#Get all the fields contained in the ResultFile
arr_name_with_dis=[elt.split("/") for elt in keys]
newlist=[]

comfield='ComSup0'
for arr in arr_name_with_dis:	
    if arr[2]=='ComSup1':
          comfield='ComSup0'

        
for arr in arr_name_with_dis:	
	if arr[0]=="TS1" and arr[2]==comfield :
		newlist.append("/".join(arr)) 
	

new_casermed_00.AllArrays = newlist       
new_casermed_00.GenerateVectors = 1   

renderView1 = GetActiveViewOrCreate('RenderView')

# Guess an absolute scale factor form the bounding box dimensions
#scale_factor=1/10.

#bounds = new_casermed_00.GetDataInformation().DataInformation.GetBounds()
#side = [bounds[1] - bounds[0], bounds[3] - bounds[2], bounds[5] - bounds[4]]
#length = min(side) 
#adapted_scale = length*scale_factor   
       
 
#------------------------------------------------------------------------------
# create a new 'ELNO Mesh'       
#------------------------------------------------------------------------------ 
SetActiveSource(new_casermed_00)
Stress = ELNOMesh(Input=new_casermed_00)        


Stress_Display = Show(Stress, renderView1)

Stress_Display.RescaleTransferFunctionToDataRange(True)
Stress_Display.SetScalarBarVisibility(renderView1, True)
Stress_Display.LineWidth = 4.0

ColorBy(Stress_Display, ('POINTS', 'RESU____SIPO_ELNO'))

RenameSource('Stress (ELNO-Field)', Stress)  

RESU____SIPO_ELNO_LUT = GetColorTransferFunction('RESU____SIPO_ELNO')

RESU____SIPO_ELNO_LUT_ColorBar = GetScalarBar(RESU____SIPO_ELNO_LUT, renderView1)
RESU____SIPO_ELNO_LUT_ColorBar.Title = 'Stress'
RESU____SIPO_ELNO_LUT_ColorBar.ComponentTitle = 'Stress(MPa // N/mm**2)'

                                                 
Stress_Display.RescaleTransferFunctionToDataRange(False)                                                     
RESU____SIPO_ELNO_PWF = GetOpacityTransferFunction('RESU____SIPO_ELNO')
        
       

#------------------------------------------------------------------------------
# create a new 'Warp By Vector'  (Deformation)
#------------------------------------------------------------------------------

# set active source
SetActiveSource(new_casermed_00)

Deformation_Warp= WarpByVector(Input=new_casermed_00)
Deformation_Warp.Vectors = ['POINTS', 'RESU____DEPL_Vector']

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
SetActiveSource(new_casermed_00)

Deformation_Vectors= Glyph(Input=new_casermed_00,GlyphType='Arrow')
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
SetActiveSource(new_casermed_00)
Force_Vectors = Glyph(Input=new_casermed_00,GlyphType='Arrow')
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
     
 

try:
    # create a new 'Legacy VTK Reader'
    Visualization_Geom = LegacyVTKReader(FileNames=['//home/jangeorg/TUBA/examples/000_Testing/008_RECANGULAR/compound_paravis.vtk'])

    # set active source
    SetActiveSource(Visualization_Geom)

    RenameSource("Visu_Geometry", Visualization_Geom)

    # show data in view
    Visualization_Geom_Display = Show(Visualization_Geom, renderView1)

    # Properties modified on legacyVTKReader1Display
    Visualization_Geom_Display.Opacity = 0.2       
except:
    print("GEOM compound couldn't be loaded")

        
if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser(1)
      