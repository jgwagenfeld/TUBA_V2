# -*- coding: utf-8 -*-

###
### This file is generated automatically by SALOME v7.8.0 with dump python functionality
###

import sys
import salome

try:
  Completed_Mesh.ExportMED( r'/home/jangeorg/TUBA/tutorial/001/new_case.mmed', 0, SMESH.MED_V2_2, 1, None ,1)
except:
  print 'ExportToMEDX() failed. Invalid file name?'


import pvsimple
pvsimple.ShowParaviewView()
#### import the simple module from the paraview
from pvsimple import *
#### disable automatic camera reset on 'Show'
pvsimple._DisableFirstRenderCameraReset()

# create a new 'MED Reader'
new_casermed = MEDReader(FileName='/home/jangeorg/TUBA/tutorial/001/new_case.rmed')

# Properties modified on new_casermed
new_casermed.AllArrays = ['TS1/MAIL/ComSup0/MAX_VMISUT01_ELNO@@][@@GSSNE', 'TS1/MAIL/ComSup0/RESU____DEPL@@][@@P1', 'TS1/MAIL/ComSup0/RESU____FORC_NODA@@][@@P1', 'TS1/MAIL/ComSup0/RESU____REAC_NODA@@][@@P1', 'TS1/MAIL/ComSup0/RESU____SIEF_ELGA@@][@@GAUSS', 'TS1/MAIL/ComSup0/RESU____SIEQ_ELNO@@][@@GSSNE']

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [918, 410]

# show data in view
new_casermedDisplay = Show(new_casermed, renderView1)

# reset view to fit data
renderView1.ResetCamera()

#changing interaction mode based on data extents
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [1500.0, 575.0, 10000.0]
renderView1.CameraFocalPoint = [1500.0, 575.0, 0.0]

# Properties modified on new_casermed
new_casermed.GenerateVectors = 1

# Properties modified on new_casermedDisplay
new_casermedDisplay.SelectInputVectors = ['POINTS', 'RESU____DEPL_Vector']

# create a new 'Warp By Vector'
warpByVector1 = WarpByVector(Input=new_casermed)

# show data in view
warpByVector1Display = Show(warpByVector1, renderView1)

# hide data in view
Hide(new_casermed, renderView1)

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

# set active source
SetActiveSource(new_casermed)

# create a new 'ELNO Mesh'
eLNOMesh1 = ELNOMesh(Input=new_casermed)

# show data in view
eLNOMesh1Display = Show(eLNOMesh1, renderView1)

# hide data in view
Hide(new_casermed, renderView1)

# set scalar coloring
ColorBy(eLNOMesh1Display, ('POINTS', 'MAX_VMISUT01_ELNO'))

# rescale color and/or opacity maps used to include current data range
eLNOMesh1Display.RescaleTransferFunctionToDataRange(True)

# show color bar/color legend
eLNOMesh1Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'MAXVMISUT01ELNO'
mAXVMISUT01ELNOLUT = GetColorTransferFunction('MAXVMISUT01ELNO')

# get opacity transfer function/opacity map for 'MAXVMISUT01ELNO'
mAXVMISUT01ELNOPWF = GetOpacityTransferFunction('MAXVMISUT01ELNO')

#change array component used for coloring
mAXVMISUT01ELNOLUT.RGBPoints = [102.55225199846132, 0.231373, 0.298039, 0.752941, 3135.7733391499924, 0.865003, 0.865003, 0.865003, 6168.994426301523, 0.705882, 0.0156863, 0.14902]
mAXVMISUT01ELNOLUT.VectorMode = 'Component'

# Properties modified on mAXVMISUT01ELNOPWF
mAXVMISUT01ELNOPWF.Points = [102.55225199846132, 0.0, 0.5, 0.0, 6168.994426301523, 1.0, 0.5, 0.0]

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

# get color transfer function/color map for 'FamilyIdNode'
familyIdNodeLUT = GetColorTransferFunction('FamilyIdNode')

# get opacity transfer function/opacity map for 'FamilyIdNode'
familyIdNodePWF = GetOpacityTransferFunction('FamilyIdNode')

# Properties modified on glyph1
glyph1.ScaleMode = 'vector'

# Properties modified on glyph1
glyph1.ScaleFactor = 1.0

# set scalar coloring
ColorBy(glyph1Display, ('POINTS', 'RESU____DEPL'))

# rescale color and/or opacity maps used to include current data range
glyph1Display.RescaleTransferFunctionToDataRange(True)

# show color bar/color legend
glyph1Display.SetScalarBarVisibility(renderView1, True)

# reset view to fit data
renderView1.ResetCamera()

# set active source
SetActiveSource(new_casermed)

# set active source
SetActiveSource(glyph1)

# rename source object
RenameSource('Deformation_Arrows', glyph1)

# set active source
SetActiveSource(eLNOMesh1)

# rename source object
RenameSource('VMIS_Stress', eLNOMesh1)

# set active source
SetActiveSource(warpByVector1)

# rename source object
RenameSource('DeformedShape', warpByVector1)

# reset view to fit data
renderView1.ResetCamera()

# hide data in view
Hide(glyph1, renderView1)

# set active source
SetActiveSource(glyph1)

# show data in view
glyph1Display = Show(glyph1, renderView1)

# show color bar/color legend
glyph1Display.SetScalarBarVisibility(renderView1, True)

# hide data in view
Hide(glyph1, renderView1)

# show data in view
glyph1Display = Show(glyph1, renderView1)

# show color bar/color legend
glyph1Display.SetScalarBarVisibility(renderView1, True)

# set active source
SetActiveSource(glyph1)

# create a new 'Glyph'
glyph1_1 = Glyph(Input=glyph1,
    GlyphType='Arrow')

# Properties modified on glyph1_1
glyph1_1.ScaleMode = 'vector'
glyph1_1.ScaleFactor = 1.0
glyph1_1.GlyphMode = 'All Points'

# show data in view
glyph1_1Display = Show(glyph1_1, renderView1)

# show color bar/color legend
glyph1_1Display.SetScalarBarVisibility(renderView1, True)

# set scalar coloring
ColorBy(glyph1_1Display, ('POINTS', 'RESU____FORC_NODA'))

# rescale color and/or opacity maps used to include current data range
glyph1_1Display.RescaleTransferFunctionToDataRange(True)

# show color bar/color legend
glyph1_1Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'RESUFORCNODA'
rESUFORCNODALUT = GetColorTransferFunction('RESUFORCNODA')

# get opacity transfer function/opacity map for 'RESUFORCNODA'
rESUFORCNODAPWF = GetOpacityTransferFunction('RESUFORCNODA')

# hide data in view
Hide(glyph1, renderView1)

# set active source
SetActiveSource(glyph1)

# show data in view
glyph1Display = Show(glyph1, renderView1)

# show color bar/color legend
glyph1Display.SetScalarBarVisibility(renderView1, True)

# hide data in view
Hide(glyph1_1, renderView1)

# set active source
SetActiveSource(glyph1_1)

# show data in view
glyph1_1Display = Show(glyph1_1, renderView1)

# show color bar/color legend
glyph1_1Display.SetScalarBarVisibility(renderView1, True)

# Properties modified on glyph1_1
glyph1_1.Vectors = ['POINTS', 'RESU____FORC_NODA_Vector']

# Properties modified on glyph1_1
glyph1_1.ScaleFactor = 0.002992658624425616

# Properties modified on glyph1_1
glyph1_1.Scalars = ['POINTS', 'None']

# set active source
SetActiveSource(glyph1)

# set active source
SetActiveSource(glyph1)

# hide data in view
Hide(glyph1, renderView1)

# set active source
SetActiveSource(glyph1_1)

# set active source
SetActiveSource(glyph1)

# set active source
SetActiveSource(glyph1_1)

# set active source
SetActiveSource(glyph1)

# hide data in view
Hide(glyph1_1, renderView1)

# show data in view
glyph1Display = Show(glyph1, renderView1)

# show color bar/color legend
glyph1Display.SetScalarBarVisibility(renderView1, True)

# destroy glyph1_1
Delete(glyph1_1)
del glyph1_1

# set active source
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
glyph1_1Display.SelectUncertaintyArray = [None, 'FamilyIdNode']

# Properties modified on glyph1_1Display
glyph1_1Display.SelectInputVectors = ['POINTS', 'GlyphVector']

# set scalar coloring
ColorBy(glyph1_1Display, ('POINTS', 'RESU____FORC_NODA'))

# rescale color and/or opacity maps used to include current data range
glyph1_1Display.RescaleTransferFunctionToDataRange(True)

# show color bar/color legend
glyph1_1Display.SetScalarBarVisibility(renderView1, True)

# rename source object
RenameSource('Reaction_Forces', glyph1_1)

# hide data in view
Hide(glyph1, renderView1)

# set active source
SetActiveSource(glyph1)

# show data in view
glyph1Display = Show(glyph1, renderView1)

# show color bar/color legend
glyph1Display.SetScalarBarVisibility(renderView1, True)

# hide data in view
Hide(glyph1, renderView1)

# show data in view
glyph1Display = Show(glyph1, renderView1)

# show color bar/color legend
glyph1Display.SetScalarBarVisibility(renderView1, True)

# set active source
SetActiveSource(glyph1)

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [6830.85171298056, 1900.5552973510178, 8160.787534210297]
renderView1.CameraFocalPoint = [2155.3954702509095, -214.88696629271615, 131.34417289542637]
renderView1.CameraViewUp = [-0.07362525783913507, 0.9741061531270979, -0.21376745273321626]
renderView1.CameraParallelScale = 1669.2906491948818


if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser(1)
