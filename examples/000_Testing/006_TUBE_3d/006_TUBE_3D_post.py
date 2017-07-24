
        
# ======== Select a file for opening:
import Tkinter,tkFileDialog

root = Tkinter.Tk()
file = tkFileDialog.askopenfilename(parent=root,
                                    initialdir='/home/jangeorg/TUBA/examples/000_Testing/006_TUBE_3d',
                                    filetypes=[("Result Files","*.rmed")])                     
root.destroy()
        
import pvsimple
pvsimple.ShowParaviewView()
#### import the simple module from the paraview
from pvsimple import *
#### disable automatic camera reset on 'Show'
pvsimple._DisableFirstRenderCameraReset()

       
 

try:
    # create a new 'Legacy VTK Reader'
    Visualization_Geom = LegacyVTKReader(FileNames=['//home/jangeorg/TUBA/examples/000_Testing/006_TUBE_3d/compound_paravis.vtk'])

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
      