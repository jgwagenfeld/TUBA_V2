# -*- coding: utf-8 -*-

###
### This file is generated automatically by SALOME v7.8.0 with dump python functionality
###

import sys
import salome

salome.salome_init()
theStudy = salome.myStudy

import salome_notebook
notebook = salome_notebook.NoteBook(theStudy)
sys.path.insert( 0, r'/home/jangeorg/TUBA/tutorial/001')

###
### PARAVIS component
###

import pvsimple
pvsimple.ShowParaviewView()
#### import the simple module from the paraview
from pvsimple import *
#### disable automatic camera reset on 'Show'
pvsimple._DisableFirstRenderCameraReset()

# get active source.
warpByVector1 = GetActiveSource()

# set active source
SetActiveSource(warpByVector1)

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [918, 395]

# show data in view
warpByVector1Display = Show(warpByVector1, renderView1)

# reset view to fit data
renderView1.ResetCamera()

# find source
mEDReader1 = FindSource('MEDReader1')

# set active source
SetActiveSource(mEDReader1)

# show data in view
mEDReader1Display = Show(mEDReader1, renderView1)

# set active source
SetActiveSource(mEDReader1)

# set active source
SetActiveSource(warpByVector1)

# set active source
SetActiveSource(mEDReader1)

# set active source
SetActiveSource(warpByVector1)

# change representation type
warpByVector1Display.SetRepresentationType('Streaming Particles')

# Properties modified on mEDReader1
mEDReader1.AllArrays = ['TS1/MAIL/ComSup0/MAX_VMISUT01_ELNO@@][@@GSSNE', 'TS1/MAIL/ComSup0/RESU____DEPL@@][@@P1', 'TS1/MAIL/ComSup0/RESU____FORC_NODA@@][@@P1', 'TS1/MAIL/ComSup0/RESU____REAC_NODA@@][@@P1', 'TS1/MAIL/ComSup0/RESU____SIEF_ELGA@@][@@GAUSS', 'TS1/MAIL/ComSup0/RESU____SIEQ_ELNO@@][@@GSSNE']

# Properties modified on warpByVector1
warpByVector1.Vectors = [None, 'RESU____DEPL_Vector']

# Properties modified on warpByVector1Display
warpByVector1Display.SelectUncertaintyArray = [None, 'FamilyIdNode']

# Properties modified on warpByVector1Display
warpByVector1Display.SelectInputVectors = ['POINTS', 'RESU____DEPL_Vector']

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.CameraPosition = [1500.0, 575.0, 6206.778106322937]
renderView1.CameraFocalPoint = [1500.0, 575.0, 0.0]
renderView1.CameraParallelScale = 1606.4323826417344


if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser(1)
