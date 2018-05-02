# -*- coding: iso-8859-1 -*-
#Script by cbourcier
from paraview.simple import *
paraview.simple._DisableFirstRenderCameraReset()

import sys

# Colors of each glyph, same colors as the global base in Paraview 3D viewer
d_colors = {1: [1.0, 0.0, 0.0], # X: red
            2: [1.0, 1.0, 0.0], # Y: yellow
            3: [0.0, 1.0, 0.0]} # Z: green

# Scale factor for glyphs, factor of the bounding box dimensions
scale_factor = 1./10

source = GetActiveSource()

# Pass cell data to cell centers, since glyphs can only be applyed on points
CellCenters1 = CellCenters()

# Guess an absolute scale factor form the bounding box dimensions
bounds = source.GetDataInformation().DataInformation.GetBounds()
side = [bounds[1] - bounds[0], bounds[3] - bounds[2], bounds[5] - bounds[4]]
length = min(side) 
scale = length*scale_factor

# For each 3 directions
for i in xrange(1, 4):
  # Find the field for the i-th direction
  for name, array in CellCenters1.PointData.items():
    if name.endswith("REPLO_%i"%i):
      # Create glyphs (that are vectors) and set their scale factor
      Glyph1 = Glyph(Input=CellCenters1, Vectors = ['POINTS', name], ScaleMode = 'off', SetScaleFactor = scale)

      # Show the glyphs with the right colors
      color = d_colors[i]
      GlyphRepresentation = Show(DiffuseColor = color)
      
      RenameSource("Glyph_%s"%name, Glyph1)

      Render()
  
if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser(1)
