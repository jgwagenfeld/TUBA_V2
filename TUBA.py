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

import logging
import time
import pprint

from subprocess import Popen,PIPE, check_output

# importes the namesspace of the TUBA-Module
import tuba

import argument_plot

#Imports needed to process functions in tubascript used exectuetuba
# -----------------------------------------------------------------------------
from tuba.define_geometry import *
from tuba.define_properties import *
from tuba.define_simulation import *
from tuba.define_macros import *

from external.UnitCalculator import *
# -----------------------------------------------------------------------------

import tuba.write_Aster_file 
import tuba.write_Salome_file 
import tuba.write_ParaPost_file
import tuba.write_ExportAster_file 

import tuba.tuba_vars_and_funcs as tub

#logging.basicConfig(level=logging.INFO)
logging.basicConfig(level=logging.DEBUG)

time_start = time.time() # Track duration of the script
# -----------------------------------------------------------------------------
# Definition where to read and write the input/output-files
# -----------------------------------------------------------------------------
salome_root=os.getenv('HOME')+'/salome_meca/appli_V2017.0.2/salome' # Salome directory
aster_root=os.getenv('HOME')+'/salome_meca/appli_V2017.0.2/salome shell -- as_run' # Aster directory

#salome_root=os.getenv('HOME')+'/salome_meca/appli_V2016/salome' # Salome directory
#aster_root=os.getenv('HOME')+'/salome_meca/V2016/tools/Code_aster_testing-1320/bin/aster' # Aster directory

current_directory = os.getcwd()
tuba_directory = os.environ["TUBA"]
cmd_script = sys.argv[1].replace(".py", "")   # sys.argv[1]"TUBTUB2.py"

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

outputFile_PrintAll=current_directory +"/" + cmd_script+ "_PrintAll.txt"


def main(argv):
    write_AllClean(cmd_script)
    if sys.argv[2] =='-plot':
        completed_dict_tubapoints,completed_dict_tubavectors=executetuba(inputFileTuba)

        argument_plot.plot_points_and_vectors(completed_dict_tubavectors,completed_dict_tubapoints)
    elif sys.argv[2] =='-salome':
        completed_dict_tubapoints,completed_dict_tubavectors=executetuba(inputFileTuba)

        salome_stop = Popen(salome_root + ' killall',shell='True')
        salome_stop.wait()
        salome_run = Popen(salome_root + ' ' + outputFile_Salome, shell='True', executable="/bin/bash")
        salome_run.wait()
    elif sys.argv[2] =='-aster':  # still not working properly

        aster_run = Popen(aster_root+ " " + outputFile_ExportAster, shell='True',executable="/bin/bash")
        aster_run.wait()# -*- coding: utf-8 -*-         
        
#        salome_stop = Popen(salome_root + ' killall',shell='True', executable="/bin/bash")
#        salome_stop.wait()
#        salome_run = Popen(salome_root + ' ' + outputFile_ParaPost, shell='True', executable="/bin/bash")
    elif sys.argv[2] =='-all':  # still not working properly
        completed_dict_tubapoints,completed_dict_tubavectors=executetuba(inputFileTuba)

        salome_stop = Popen(salome_root + ' killall',shell='True', executable="/bin/bash")
        salome_stop.wait()
        salome_run = Popen(salome_root + ' -t ' + outputFile_Salome, shell='True', executable="/bin/bash")
        salome_run.wait()
        
        aster_run = Popen(aster_root+ " " + outputFile_ExportAster, shell='True', executable="/bin/bash")
        aster_run.wait()# -*- coding: utf-8 -*-         

        salome_stop = Popen(salome_root + ' killall',shell='True', executable="/bin/bash")
        salome_stop.wait()
        salome_run = Popen(salome_root + ' ' + outputFile_ParaPost, shell='True', executable="/bin/bash")
    elif sys.argv[2] =='-test':  # still not working properly
        completed_dict_tubapoints,completed_dict_tubavectors=executetuba(inputFileTuba)

        salome_stop = Popen(salome_root + ' killall',shell='True', executable="/bin/bash")
        salome_stop.wait()
        salome_run = Popen(salome_root + ' -t ' + outputFile_Salome, shell='True', executable="/bin/bash")
        salome_run.wait()
        
        aster_run = Popen(aster_root+ " " + outputFile_ExportAster, shell='True', executable="/bin/bash")
        aster_run.wait()# -*- coding: utf-8 -*-         

    elif sys.argv[2] =='-print':
        completed_dict_tubapoints,completed_dict_tubavectors=executetuba(inputFileTuba)
        printall_tuba_points_vectors(completed_dict_tubapoints,completed_dict_tubavectors)

#==============================================================================
#==============================================================================
def executetuba(inputFileTuba):
    logging.info("\n-----------------------------------------")
    logging.info("  reading and processing the User-Input")
    logging.info("-----------------------------------------\n")

    logging.info("Input: "+inputFileTuba)
    logging.info("argv1: "+sys.argv[1])
    logging.info("argv2: "+sys.argv[2])
    
    exec(open(inputFileTuba).read())

    completed_dict_tubavectors = tub.dict_tubavectors
    completed_dict_tubapoints = tub.dict_tubapoints
#==============================================================================
# Create Code Salome Object and translate dict_tubavectors,dict_tubapoints-
# Code Salome File --> Python Script to build Geometry/Mesh
# ==============================================================================
    logging.info("\n-----------------------------------------")
    logging.info("        GENERATE SALOME-SCRIPT")
    logging.info("-----------------------------------------\n")

    code_salome=tuba.write_Salome_file.Salome(current_directory)
    code_salome.write(completed_dict_tubavectors, completed_dict_tubapoints,cmd_script)
    try:
        f = open(outputFile_Salome, 'w')
        f.write('\n'.join(code_salome.lines))
        f.close()
    except:
        logging.error("Error while writing the Saolme Script")
# ==============================================================================
# Create Code Aster Object and translate dict_tubavectors,dict_tubapoints-
# Code Aster File --> .Comm script to load into Aster Module and run Simulation
# ==============================================================================
    logging.info("-----------------------------------------")
    logging.info("        GENERATE ASTERCOMM-SCRIPT")
    logging.info("-----------------------------------------\n")

    code_aster=tuba.write_Aster_file.CodeAster(tuba_directory)
    code_aster.write(completed_dict_tubavectors,completed_dict_tubapoints,cmd_script)

    try:
       f = open(outputFile_Comm, 'w')
       f.write('\n'.join(code_aster.lines))
       f.close()
    except:
        logging.error("Error while writing the Aster Comm-File")
# ==============================================================================
# Create Code Aster Object and translate dict_tubavectors,dict_tubapoints-
# Code Aster File --> .Comm script to load into Aster Module and run Simulation
# ==============================================================================
    logging.info("-----------------------------------------")
    logging.info("        GENERATE PARAVIS-SCRIPT")
    logging.info("-----------------------------------------\n")

    paraview=tuba.write_ParaPost_file.ParaPost(current_directory)
    paraview.write(completed_dict_tubavectors, completed_dict_tubapoints,resultfile_aster)

    try:
       f = open(outputFile_ParaPost, 'w')
       f.write('\n'.join(paraview.lines))
       f.close()
    except:
        logging.error("Error while writing the PostProssesing Script")
# ==============================================================================
# Create the .export-file for an automated run of CodeAster
# ==============================================================================
    logging.info("-----------------------------------------")
    logging.info("        GENERATE .EXPORT ASTER FILE")
    logging.info("-----------------------------------------\n")

    tuba.write_ExportAster_file.writeExport(
                                cmd_script=cmd_script,
                                outputFile_ExportAster=outputFile_ExportAster,
                                outputFile_Comm=outputFile_Comm,            
                                aster_root=aster_root,
                                resultfile_aster=resultfile_aster,
                                current_directory=current_directory)
#==============================================================================

    logging.info("-----------------------------------------")
    logging.info("        TUBA-SCRIPT FINISHED")
    logging.info("-----------------------------------------")

    time_end = time.time()
    dtime = time_end - time_start
    logging.info("    Execution time :"+str(round(dtime,2)) + "s")
    logging.info("-----------------------------------------\n")

    return completed_dict_tubapoints,completed_dict_tubavectors

def printall_tuba_points_vectors(dict_tubapoints,dict_tubavectors):
    lines=[]
    lines.extend(["-----------------------------------------"])
    lines.extend(["  print point and vector lists with piping properties"])
    lines.extend(["-----------------------------------------"])

    for tubavector in dict_tubavectors:
        lines.extend(['--------------'+tubavector.name+'----------------'])
        lines.extend([tubavector.__dict__])
        lines.extend([''])
    lines.extend(["=============================="])

    for tubapoint in dict_tubapoints:
        lines.extend(['--------------'+tubapoint.name+'---------------'])
        lines.extend([tubapoint.__dict__])
        lines.extend([''])
    lines.extend(["=============================="])

    pprint.pprint(lines)

    try:
       f = open(outputFile_PrintAll, 'w')
       pprint.pprint(lines, f)
       f.close()
    except:
        logging.error("Error while writing the TubaPrintAll Output")
#==============================================================================

def write_AllClean(cmd_script):
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
        logging.error(("Error while writing the PostProssesing Script"))

    bashCommand = "chmod +x AllClean"
    process = Popen(bashCommand.split(), stdout=PIPE)
    output, error = process.communicate()
#==============================================================================    


if __name__ == "__main__":
   main(sys.argv[1:])






