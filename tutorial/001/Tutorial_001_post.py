
        
# ======== Select a file for opening:
import Tkinter,tkFileDialog

root = Tkinter.Tk()
file = tkFileDialog.askopenfilename(parent=root,
                                    initialdir='/home/jangeorg/TUBA/tutorial/001',
                                    filetypes=[("Result Files","*.rmed")])        
              
root.destroy()
        
import pvsimple
pvsimple.ShowParaviewView()
#### import the simple module from the paraview
from pvsimple import *
#### disable automatic camera reset on 'Show'
pvsimple._DisableFirstRenderCameraReset()

        
# create a new 'MED Reader'
new_casermed = MEDReader(FileName=file)

# Properties modified on new_casermed
new_casermed.AllArrays = ['TS1/MAIL/ComSup0/MAX_VMISUT01_ELNO@@][@@GSSNE', 
                          'TS1/MAIL/ComSup0/RESU____DEPL@@][@@P1', 
                          'TS1/MAIL/ComSup0/RESU____FORC_NODA@@][@@P1', 
                          'TS1/MAIL/ComSup0/RESU____REAC_NODA@@][@@P1', 
                          'TS1/MAIL/ComSup0/RESU____SIEF_ELGA@@][@@GAUSS', 
                          'TS1/MAIL/ComSup0/RESU____SIEQ_ELNO@@][@@GSSNE']        

renderView1 = GetActiveViewOrCreate('RenderView')
        
# Properties modified on new_casermed
new_casermed.GenerateVectors = 1        
       

# set active source
SetActiveSource(new_casermed)

# create a new 'Warp By Vector'
warpByVector1 = WarpByVector(Input=new_casermed)

# show data in view
warpByVector1Display = Show(warpByVector1, renderView1)

# Properties modified on warpByVector1Display
warpByVector1Display.LineWidth = 4.0

# set scalar coloring
ColorBy(warpByVector1Display, ('POINTS', 'RESU____DEPL'))

# rescale color and/or opacity maps used to include current data range
warpByVector1Display.RescaleTransferFunctionToDataRange(True)

# show color bar/color legend
warpByVector1Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'RESUDEPL'
rESUDEPLLUT = GetColorTransferFunction('RESUDEPL')

# get opacity transfer function/opacity map for 'RESUDEPL'
rESUDEPLPWF = GetOpacityTransferFunction('RESUDEPL')

RenameSource('DeformedShape', warpByVector1)
# get color legend/bar for rESUDEPLPWF in view renderView1
rESUDEPLPWFColorBar = GetScalarBar(rESUDEPLPWF, renderView1)
# Properties modified on rESUDEPLPWFColorBar
rESUDEPLPWFColorBar.Title = 'Deformation'
# Properties modified on rESUDEPLPWFColorBar
rESUDEPLPWFColorBar.ComponentTitle = 'Magnitude (mm)'

      

       
# create a new 'ELNO Mesh'
eLNOMesh1 = ELNOMesh(Input=new_casermed)
# show data in view
eLNOMesh1Display = Show(eLNOMesh1, renderView1)

# set scalar coloring
ColorBy(eLNOMesh1Display, ('POINTS', 'MAX_VMISUT01_ELNO'))
# rescale color and/or opacity maps used to include current data range
eLNOMesh1Display.RescaleTransferFunctionToDataRange(True)
# show color bar/color legend
eLNOMesh1Display.SetScalarBarVisibility(renderView1, True)
# Properties modified on warpByVector1Display
eLNOMesh1Display.LineWidth = 4.0


# get color transfer function/color map for 'MAXVMISUT01ELNO'
mAXVMISUT01ELNOLUT = GetColorTransferFunction('MAXVMISUT01ELNO')
# get opacity transfer function/opacity map for 'MAXVMISUT01ELNO'
mAXVMISUT01ELNOPWF = GetOpacityTransferFunction('MAXVMISUT01ELNO')


mAXVMISUT01ELNOLUT.VectorMode = 'Component'
# rescale color and/or opacity maps used to exactly fit the current data range
eLNOMesh1Display.RescaleTransferFunctionToDataRange(False)

RenameSource('VMIS_Stress', eLNOMesh1)  

# get color legend/bar for mAXVMISUT01ELNOLUT in view renderView1
mAXVMISUT01ELNOLUTColorBar = GetScalarBar(mAXVMISUT01ELNOLUT, renderView1)
# Properties modified on mAXVMISUT01ELNOLUTColorBar
mAXVMISUT01ELNOLUTColorBar.Title = 'VonMise Stress'
# Properties modified on mAXVMISUT01ELNOLUTColorBar
mAXVMISUT01ELNOLUTColorBar.ComponentTitle = 'Magnitude (MPa)'   
     


# set active source
SetActiveSource(new_casermed)

# create a new 'Glyph'
glyph1 = Glyph(Input=new_casermed,
    GlyphType='Arrow')

# Properties modified on glyph1
glyph1.Vectors = ['POINTS', 'RESU____DEPL_Vector']
glyph1.GlyphMode = 'All Points'

# show data in view
glyph1Display = Show(glyph1, renderView1)

# show color bar/color legend
glyph1Display.SetScalarBarVisibility(renderView1, True)

# Properties modified on glyph1
glyph1.ScaleMode = 'vector'

# Properties modified on glyph1
glyph1.ScaleFactor = 1.0

# set scalar coloring
ColorBy(glyph1Display, ('POINTS', 'RESU____DEPL'))

# show color bar/color legend
glyph1Display.SetScalarBarVisibility(renderView1, True)


# rename source object
RenameSource('Deformation_Arrows', glyph1)

# get color legend/bar for rESUDEPLLUT in view renderView1
rESUDEPLLUTColorBar = GetScalarBar(rESUDEPLLUT, renderView1)
# Properties modified on rESUDEPLLUTColorBar
rESUDEPLLUTColorBar.Title = 'Deformation'
# Properties modified on rESUDEPLLUTColorBar
rESUDEPLLUTColorBar.ComponentTitle = 'Magnitude (mm)'

      

SetActiveSource(new_casermed)

# create a new 'Glyph'
glyph1_1 = Glyph(Input=new_casermed,
    GlyphType='Arrow')

# Properties modified on glyph1_1
glyph1_1.Scalars = ['POINTS', 'None']
glyph1_1.Vectors = ['POINTS', 'RESU____FORC_NODA_Vector']
glyph1_1.ScaleMode = 'vector'
glyph1_1.ScaleFactor = 0.0020176490811640107

# show data in view
glyph1_1Display = Show(glyph1_1, renderView1)

# Properties modified on glyph1_1
glyph1_1.GlyphMode = 'All Points'

# Properties modified on glyph1_1Display
glyph1_1Display.SelectInputVectors = ['POINTS', 'GlyphVector']

# set scalar coloring
ColorBy(glyph1_1Display, ('POINTS', 'RESU____FORC_NODA'))

# rescale color and/or opacity maps used to include current data range
glyph1_1Display.RescaleTransferFunctionToDataRange(True)

# show color bar/color legend
glyph1_1Display.SetScalarBarVisibility(renderView1, True)

# set active source
SetActiveSource(glyph1)

# show data in view
glyph1Display = Show(glyph1, renderView1)

# show color bar/color legend
glyph1Display.SetScalarBarVisibility(renderView1, True)

# set active source
SetActiveSource(glyph1)

# rename source object
RenameSource('Reaction_Forces', glyph1_1)

# get color transfer function/color map for 'RESUFORCNODA'
rESUFORCNODALUT = GetColorTransferFunction('RESUFORCNODA')

# get opacity transfer function/opacity map for 'RESUFORCNODA'
rESUFORCNODAPWF = GetOpacityTransferFunction('RESUFORCNODA')


# get color legend/bar for mAXVMISUT01ELNOPWF in view renderView1
rESUFORCNODALUTColorBar = GetScalarBar(rESUFORCNODALUT, renderView1)
# Properties modified on rESUFORCNODALUTColorBar
rESUFORCNODALUTColorBar.Title = 'Forces'
# Properties modified on rESUFORCNODALUTColorBar
rESUFORCNODALUTColorBar.ComponentTitle ='Magnitude (N)'



     
 
        
        
if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser(1)
      