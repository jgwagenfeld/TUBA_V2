#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
"""
Orginal Code by Pascal KREZEL (pascal.krezel@gmail.com) Janvier 2012
Modified by Jan-Georg WAGENFELD (jangeorgwagenfeld@gmail.com) 2016

This programm is used to prepare a FEM piping network simulation in Code Aster
and Salome. The User defines this piping network in a script with a list
of functions. 

1.The main function processes the script(argument when calling TUBAV3.py)

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

#---UnitCalculator to use different input units---
from external.UnitCalculator import *
auto_converter(mmNS)


logging.basicConfig(level=logging.INFO)
# Track duration of the script
time_start = time.time()
# ------------------------------------------------------------------------------
# Definition where to read and write the input/output-files
# --------------------------------------------------------------------------
my_directory = os.getcwd()
tuba_directory = os.environ["TUBA"]
cmd_script = sys.argv[1].replace(".py", "")   # sys.argv[1]"TUBTUB2.py"

inputFileTuba = my_directory + "/" + cmd_script + ".py"

# File used in Salome to generate the Geometry and Meshing
outputFile_Salome = my_directory + "/" + cmd_script + "_salome" + ".py"

# File used in Code Aster to define Simulation parameters
outputFile_Comm = my_directory + "/" + cmd_script + "_aster" + ".comm"


# File used in Code Aster to define Simulation parameters
outputFile_ParaPost = my_directory + "/" + cmd_script + "_post" + ".py"


def Main():

    
#    simulation=tuba.define_simulation.Simulation() 

    print("\n------------------------")
    print("  reading and processing the User-Input")
    print("------------------------\n")
    
    
    
    exec(open(inputFileTuba).read())

    completed_dict_tubavectors = tub.dict_tubavectors
    completed_dict_tubapoints = tub.dict_tubapoints
    
    print("\n------------------------")
    print("  print point and vector lists with piping properties")
    print("------------------------\n")

   # printall_tuba_points_vectors(completed_dict_tubapoints, completed_dict_tubavectors)

#==============================================================================
# Create Code Salome Object and translate dict_tubavectors,dict_tubapoints-
# Code Salome File --> Python Script to build Geometry/Mesh
# ==============================================================================
    code_salome=tuba.write_Salome_file.Salome(my_directory)
    code_salome.write(completed_dict_tubavectors, completed_dict_tubapoints)
    try:
        f = open(outputFile_Salome, 'w')
        f.write('\n'.join(code_salome.lines))
        f.close()
    except:
        print("Error")

# ==============================================================================
# Create Code Aster Object and translate dict_tubavectors,dict_tubapoints-
# Code Aster File --> .Comm script to load into Aster Module and run Simulation
# ==============================================================================
    code_aster=tuba.write_Aster_file.CodeAster(tuba_directory)
    code_aster.write(completed_dict_tubavectors, completed_dict_tubapoints)
    
    try:
       f = open(outputFile_Comm, 'w')
       f.write('\n'.join(code_aster.lines))
       f.close()
    except:
        print("Error")

# ==============================================================================
# Create Code Aster Object and translate dict_tubavectors,dict_tubapoints-
# Code Aster File --> .Comm script to load into Aster Module and run Simulation
# ==============================================================================
    paraview=tuba.write_ParaPost_file.ParaPost(my_directory)
    
    paraview.write(completed_dict_tubavectors, completed_dict_tubapoints)
    
    try:
       f = open(outputFile_ParaPost, 'w')
       f.write('\n'.join(paraview.lines))
       f.close()
    except:
        print("Error")        
        
        
        
        
#==============================================================================

    print
    print("------------------------")
    print("         OK")
    print("------------------------")
    print

#==============================================================================
#Plots the constructed Points and Vectors to control the constructed network before loading into Salome
    import plot_points_and_vectors
#==============================================================================


    time_end = time.time()
    dtime = time_end - time_start
    print("------------------------")
    print("Execution time :"+str(round(dtime,2)) + "s")

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


Main()





