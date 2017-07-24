#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
"""
Based on Code by Pascal KREZEL (pascal.krezel@gmail.com) Janvier 2012
Further developpment by Jan-Georg WAGENFELD (jangeorgwagenfeld@gmail.com) 2016

This programm is used to prepare a FEM piping network simulation in Code Aster
and Salome. The User defines this piping network in a script with a list
of functions. 

1.The main function processes the script(argument when calling TUBA.py)

2.These functions are defined in the tuba-Module - they produce a list of
TubaPoint and TubaVector-Objects. These classes are a container for
the geometry(points,tubes,bents,tshapes) and properties(supports, springs,
temperature, forces, material etc) of the piping.

3.These object lists (dic_TubaPoints, dic_TubaVectors  - defined in
global_vars.py) hold all the information necessary for the piping

4.Within the write_Aster_file and write_Salome_file, these lists are
processed and the Outputfiles for Salome and Aster are generated.

The Salome-Script can be importated directly in Salome by "Load Script".
The Comm-File is used when defining a Study in the Code Aster module
"""

import sys
import os
import math

import logging
import unittest
import time

from subprocess import Popen

# importes the namesspace of the TUBA-Module
import tuba

from tuba.define_geometry import *
from tuba.define_properties import *
from tuba.define_simulation import *
from tuba.define_macros import *

import tuba.write_Aster_file 
import tuba.write_Salome_file 
import tuba.write_ParaPost_file
import tuba.tuba_vars_and_funcs as tub

##---UnitCalculator to use different input units---
#from external.UnitCalculator import *
#
#auto_converter(mmNS)


#logging.basicConfig(level=logging.INFO)
logging.basicConfig(level=logging.DEBUG)
# Track duration of the script
time_start = time.time()
# ------------------------------------------------------------------------------
# Definition where to read and write the input/output-files
# --------------------------------------------------------------------------



salome_root=os.getenv('HOME')+'/salome_meca/appli_V2016/salome' # Salome directory
aster_root=os.getenv('HOME')+'/salome_meca/V2016/tools/Code_aster_frontend-20160/bin/' # Aster directory
                                     
current_directory = os.getcwd()
tuba_directory = os.environ["TUBA"]
cmd_script = sys.argv[1].replace(".py", "")   # sys.argv[1]"TUBTUB2.py"

#try:
#    os.stat(current_directory + "/" + cmd_script)
#except:
#    os.mkdir(current_directory + "/" + cmd_script)                     
                                                             
inputFileTuba = current_directory + '/'+cmd_script+".py"

# File used in Salome to generate the Geometry and Meshing
outputFile_Salome = current_directory + "/"+ cmd_script + "_salome" + ".py"

# File used in Code Aster to define Simulation parameters
outputFile_Comm = current_directory +"/"  + cmd_script + "_aster" + ".comm"

# File used in Code Aster to define Simulation parameters
outputFile_ParaPost = current_directory +"/" + cmd_script + "_post" + ".py"



def Main(argv):
  
#    simulation=tuba.define_simulation.Simulation() 

    print("\n------------------------")
    print("  reading and processing the User-Input")
    print("------------------------\n")
          
    exec(open(inputFileTuba).read())

    completed_dict_tubavectors = tub.dict_tubavectors
    completed_dict_tubapoints = tub.dict_tubapoints
    
#    print("\n------------------------")
#    print("  print point and vector lists with piping properties")
#    print("------------------------\n")
#
#    printall_tuba_points_vectors(completed_dict_tubapoints, completed_dict_tubavectors)

#==============================================================================
# Create Code Salome Object and translate dict_tubavectors,dict_tubapoints-
# Code Salome File --> Python Script to build Geometry/Mesh
# ==============================================================================
    code_salome=tuba.write_Salome_file.Salome(current_directory)
    code_salome.write(completed_dict_tubavectors, completed_dict_tubapoints)
    try:
        f = open(outputFile_Salome, 'w')
        f.write('\n'.join(code_salome.lines))
        f.close()
    except:
        print("Error while writing the Saolme Script")

# ==============================================================================
# Create Code Aster Object and translate dict_tubavectors,dict_tubapoints-
# Code Aster File --> .Comm script to load into Aster Module and run Simulation
# ==============================================================================
    code_aster=tuba.write_Aster_file.CodeAster(tuba_directory)
    code_aster.write(completed_dict_tubavectors, completed_dict_tubapoints,cmd_script)
    
    try:
       f = open(outputFile_Comm, 'w')
       f.write('\n'.join(code_aster.lines))
       f.close()
    except:
        print("Error while writing the Aster Comm-File")

# ==============================================================================
# Create Code Aster Object and translate dict_tubavectors,dict_tubapoints-
# Code Aster File --> .Comm script to load into Aster Module and run Simulation
# ==============================================================================
    paraview=tuba.write_ParaPost_file.ParaPost(current_directory)
    
    paraview.write(completed_dict_tubavectors, completed_dict_tubapoints)
    
    try:
       f = open(outputFile_ParaPost, 'w')
       f.write('\n'.join(paraview.lines))
       f.close()
    except:
        print("Error while writing the PostProssesing Script")        
        
        
#==============================================================================
    for tubavector in completed_dict_tubavectors:
            print(tubavector.name)
            print(tubavector.linear_force)
    print
    print("------------------------")
    print("         OK")
    print("------------------------")
    print

    
    time_end = time.time()
    dtime = time_end - time_start
    print("------------------------")
    print("Execution time :"+str(round(dtime,2)) + "s")

    
    
#==============================================================================
# Check for additional arguments
# -plot  --> launches the matplotlib visualization of the created geometry
# -salome --> launches Salome, using the jut created salome script.
#==============================================================================
       
    
    try:
        if sys.argv[2] =='-plot':
            import plot_points_and_vectors
        if sys.argv[2] =='-salome':
        #Launch Salome    
            salome_stop = Popen(salome_root + ' killall',shell='True')
            salome_stop.wait()
            salome_run = Popen(salome_root + ' ' + outputFile_Salome, shell='True')
            salome_run.wait()
        if sys.argv[2] =='-aster':  # still not working properly
            EXPORT_FILE='Test2.export' # Filename of aster settings
            salome_stop = Popen(salome_root + ' killall',shell='True')
            salome_stop.wait()
            salome_run = Popen(salome_root + ' -t ' + outputFile_Salome, shell='True')
            salome_run.wait()
            
            aster_run = Popen(aster_root + 'as_run ' + EXPORT_FILE, shell='True')
            aster_run.wait()# -*- coding: utf-8 -*-         
            
    except:
        pass
  
#==============================================================================
#==============================================================================
def printall_tuba_points_vectors(dict_tubapoints,dict_tubavectors):

    for tubavector in dict_tubavectors:
        logging.info("==============================")
        logging.info(tubavector.start_tubapoint.name.__str__() +
                     tubavector.start_tubapoint.pos.__str__())
        logging.info(tubavector.name.__str__() + tubavector.vector.__str__())
    if tubavector == dict_tubavectors[-1]:
        logging.info(tubavector.end_tubapoint.name.__str__() +
                     tubavector.end_tubapoint.pos.__str__())
    logging.info("==============================")

    for tubavector in dict_tubavectors:
        logging.info(str(tubavector.__dict__))
    logging.info("==============================")

    for tubapoint in dict_tubapoints:
        logging.info(str(tubapoint.__dict__))
    logging.info("==============================")

#==============================================================================
#==============================================================================    
if __name__ == "__main__":
   Main(sys.argv[1:])






