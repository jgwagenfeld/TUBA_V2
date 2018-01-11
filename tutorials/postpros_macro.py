# Copyright (C) 2014-2016  CEA/DEN, EDF R&D
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307 USA
#
# See http://www.salome-platform.org/ or email : webmaster.salome@opencascade.com
#

###
# Macro to show SALOME object in ParaView viewer.
# 
# The macro inspects current selection obtained from SALOME GUI
# and displays supported objects in the viewer:
# - GEOM object
# - SMESH mesh object
###

import tempfile, os

import SALOME

import salome
salome.salome_init()

session = salome.naming_service.Resolve('/Kernel/Session')

from pvsimple import *

selection = session.getSelection()

for entry in selection:
    sobj = salome.myStudy.FindObjectID(entry)
    try:
        import GEOM
        from salome.geom import geomBuilder
        geompy = geomBuilder.New(salome.myStudy)
        go = sobj.GetObject()._narrow(GEOM.GEOM_Object)
        if go:
            tmpf = tempfile.NamedTemporaryFile(suffix='.vtk')
            fname = tmpf.name
            tmpf.close()
            geompy.ExportVTK(go, fname)
            ShowParaviewView()
            p = LegacyVTKReader(FileNames=[fname])
            renderView = GetActiveViewOrCreate('RenderView')
            pd = Show(p, renderView)
            renderView.ResetCamera()
            os.remove(fname)
            pass
    except:
        # not geom object
        pass
    try: 
        import SMESH
        from salome.smesh import smeshBuilder
        mesh = smeshBuilder.New(salome.myStudy)
        mo = sobj.GetObject()._narrow(SMESH.SMESH_Mesh)
        if mo:
            tmpf = tempfile.NamedTemporaryFile(suffix='.med')
            fname = tmpf.name
            tmpf.close()
            mo.ExportToMEDX(fname, True, SMESH.MED_V2_2, True, True)
            ShowParaviewView()
            p = MEDReader(FileName=fname)
            renderView = GetActiveViewOrCreate('RenderView')
            pd = Show(p, renderView)
            renderView.ResetCamera()
            os.remove(fname)
            pass
    except:
        # not mesh object
        pass
    pass
