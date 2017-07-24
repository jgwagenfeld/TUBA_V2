#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 13:23:25 2017

@author: jangeorg
"""

import pandas as pd
from subprocess import Popen

SALOME_ROOT='/home/jangeorg/salome_meca/appli_V2016/salome' # Salome directory
ASTER_ROOT='/home/jangeorg/salome_meca/V2016/tools/Code_aster_frontend-20160/bin/'


WORKING_DIR='/home/jangeorg/TUBA/Popen/' # Working directory



PROC_FILE='Tutorial_001_salome.py' # Filename of the geometry and meshing scripty

salome_stop = Popen(SALOME_ROOT + ' killall',shell='True')
salome_stop.wait()
salome_run = Popen(SALOME_ROOT + ' ' + WORKING_DIR + PROC_FILE, shell='True')
salome_run.wait()





#
#f = open(fileOutput,"a") # Open output file in append mode
#f.write(data['NAME'][i]+',') # Write name of the next section
#f.close() # Close output file


EXPORT_FILE='Test.export' # Filename of aster settings

# Launch aster calculation
aster_run = Popen(ASTER_ROOT + 'as_run ' + EXPORT_FILE, shell='True')
aster_run.wait()