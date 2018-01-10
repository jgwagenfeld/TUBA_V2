#! /usr/bin/env python2
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

from subprocess import Popen,PIPE

# importes the namesspace of the TUBA-Module
import tuba

import argument_plot

from tuba.define_geometry import *
from tuba.define_properties import *
from tuba.define_simulation import *
from tuba.define_macros import *

import tuba.write_Aster_file 
import tuba.write_Salome_file 
import tuba.write_ParaPost_file
import tuba.write_ExportAster_file 

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
salome_root=os.getenv('HOME')+'/salome_meca/appli_V2017.0.2/salome' # Salome directory
aster_root=os.getenv('HOME')+'/salome_meca/appli_V2017.0.2/salome shell -- as_run' # Aster directory


#salome_root=os.getenv('HOME')+'/salome_meca/appli_V2016/salome' # Salome directory
#aster_root=os.getenv('HOME')+'/salome_meca/V2016/tools/Code_aster_testing-1320/bin/aster' # Aster directory

                                     
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
outputFile_Comm = cmd_script + "_aster" + ".comm"

# File used in Code Aster to define Simulation parameters
outputFile_ParaPost = current_directory +"/" + cmd_script + "_post" + ".py"

# File used in Code Aster to run it from the command-line (-aster argument)
outputFile_ExportAster = current_directory +"/" + cmd_script+ ".export"

resultfile_aster=current_directory+"/"+cmd_script+"-RESULTS_salome.rmed"


def Main(argv):
  
#    simulation=tuba.define_simulation.Simulation() 

    print("\n------------------------")
    print("  reading and processing the User-Input")
    print("------------------------\n")

    exec(open(inputFileTuba).read())

    completed_dict_tubavectors = tub.dict_tubavectors
    completed_dict_tubapoints = tub.dict_tubapoints

    print(completed_dict_tubapoints)
    print(tub.dict_tubapoints)

#    print("\n------------------------")
#    print("  print point and vector lists with piping properties")
#    print("------------------------\n")
#
#    printall_tuba_points_vectors(completed_dict_tubapoints, completed_dict_tubavectors)

#==============================================================================
# Create Code Salome Object and translate dict_tubavectors,dict_tubapoints-
# Code Salome File --> Python Script to build Geometry/Mesh
# ==============================================================================
    print("\n ------------------------")
    print("        GENERATE SALOME-SCRIPT")
    print(" ------------------------ \n")

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
    print("\n ------------------------")
    print("        GENERATE ASTERCOMM-SCRIPT")
    print(" ------------------------ \n")

    code_aster=tuba.write_Aster_file.CodeAster(tuba_directory)
    code_aster.write(completed_dict_tubavectors,completed_dict_tubapoints,cmd_script)

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
    print("\n ------------------------")
    print("        GENERATE PARAVIS-SCRIPT")
    print(" ------------------------ \n")

    paraview=tuba.write_ParaPost_file.ParaPost(current_directory)

    paraview.write(completed_dict_tubavectors, completed_dict_tubapoints,resultfile_aster)

    try:
       f = open(outputFile_ParaPost, 'w')
       f.write('\n'.join(paraview.lines))
       f.close()
    except:
        print("Error while writing the PostProssesing Script")        

# ==============================================================================
# Create the .export-file for an automated run of CodeAster
# ==============================================================================
    print("\n ------------------------")
    print("        GENERATE .EXPORT ASTER FILE")
    print(" ------------------------ \n")

    tuba.write_ExportAster_file.writeExport(
                                cmd_script=cmd_script,
                                outputFile_ExportAster=outputFile_ExportAster,
                                outputFile_Comm=outputFile_Comm,            
                                aster_root=aster_root,
                                resultfile_aster=resultfile_aster,
                                current_directory=current_directory)

#==============================================================================
    for tubavector in completed_dict_tubavectors:
            print(tubavector.name)
            print(tubavector.linear_force)
    print("\n ------------------------")
    print("        TUBA-GENERATION FINISHED")
    print(" ------------------------\n")

    time_end = time.time()
    dtime = time_end - time_start
    print("Execution time :"+str(round(dtime,2)) + "s")
    print("------------------------")

#==============================================================================
# Check for additional arguments
# -plot  --> launches the matplotlib visualization of the created geometry
# -salome --> launches Salome, using the jut created salome script.
#==============================================================================
    writeAllClean(cmd_script)
    
    try:
        if sys.argv[2] =='-plot':
            print(completed_dict_tubapoints)
            argument_plot.plot_points_and_vectors(completed_dict_tubavectors,completed_dict_tubapoints)
        if sys.argv[2] =='-salome':
        #Launch Salome    
            salome_stop = Popen(salome_root + ' killall',shell='True')
            salome_stop.wait()
            salome_run = Popen(salome_root + ' ' + outputFile_Salome, shell='True')
            salome_run.wait()
        if sys.argv[2] =='-aster':  # still not working properly
            aster_run = Popen(aster_root+ " " + outputFile_ExportAster, shell='True')
            aster_run.wait()# -*- coding: utf-8 -*-         
        if sys.argv[2] =='-all':  # still not working properly
            salome_stop = Popen(salome_root + ' killall',shell='True')
            salome_stop.wait()
            salome_run = Popen(salome_root + ' -t ' + outputFile_Salome, shell='True')
            salome_run.wait()
            
            aster_run = Popen(aster_root+ " " + outputFile_ExportAster, shell='True')
            aster_run.wait()# -*- coding: utf-8 -*-         

            salome_stop = Popen(salome_root + ' killall',shell='True')
            salome_stop.wait()
            salome_run = Popen(salome_root + ' ' + outputFile_ParaPost, shell='True')


        if sys.argv[2] =='-print':
            printall_tuba_points_vectors(completed_dict_tubapoints,completed_dict_tubavectors)          
    except:
        pass
#==============================================================================
#==============================================================================
def printall_tuba_points_vectors(dict_tubapoints,dict_tubavectors):
    import pprint
    for tubavector in dict_tubavectors:
        print("==============================")
        print(tubavector.start_tubapoint.name.__str__() +
                     tubavector.start_tubapoint.pos.__str__())
        print(tubavector.name.__str__() + tubavector.vector.__str__())
    if tubavector == dict_tubavectors[-1]:
        print(tubavector.end_tubapoint.name.__str__() +
                     tubavector.end_tubapoint.pos.__str__())
    print("==============================")

    for tubavector in dict_tubavectors:
        print("")
        print('--------------'+tubavector.name+'----------------')
        pprint.pprint(tubavector.__dict__)
    print("==============================")

    for tubapoint in dict_tubapoints:
        print("")
        print('--------------'+tubapoint.name+'---------------')
        pprint.pprint(tubapoint.__dict__)
    print("==============================")
#==============================================================================

def writeAllClean(cmd_script):
    lines=("""
#!/bin/sh
cd ${0%/*} || exit 1    # Run from this directory

echo "--------"
echo "Deleting all files but TUBA-script ..."
find . -not -name \""""+cmd_script+""".py\"  -exec rm -rf {} \;
echo "--------"
#------------------------------------------------------------------------------
""").split("\n")

    try:
       f = open("AllClean", 'w')
       f.write('\n'.join(lines))
       f.close()
    except:
        print("Error while writing the PostProssesing Script")        
        
    bashCommand = "chmod +x AllClean"
    process = Popen(bashCommand.split(), stdout=PIPE)
    output, error = process.communicate()

#==============================================================================    
if __name__ == "__main__":
   Main(sys.argv[1:])






