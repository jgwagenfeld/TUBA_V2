#!/usr/bin/env python
# -*- coding: utf-8 -*-

 ######  ######## ######## ##     ## ########
##    ## ##          ##    ##     ## ##     ##
##       ##          ##    ##     ## ##     ##
 ######  ######      ##    ##     ## ########
      ## ##          ##    ##     ## ##
##    ## ##          ##    ##     ## ##
 ######  ########    ##     #######  ##
# General modules
import sys
import numpy as np
import csv
import os
# Salome modules
import salome
import salome_notebook
# Geometry modules
import GEOM
from salome.geom import geomBuilder
import math
import SALOMEDS
# Mesh modules
import  SMESH, SALOMEDS
from salome.smesh import smeshBuilder
WORKING_DIR=os.getcwd() # Working directory
TEMP_FILE='Temp.input' # Filename of the temp file (from input to processing)
MESH_FILE='SectionAuto.med'
fileInput = WORKING_DIR + TEMP_FILE


with open(fileInput) as csvfile:
    reader = csv.DictReader(csvfile)
    for data in reader:
		print(data)
		H = float(data['H'])
		B = float(data['B'])
		Tw = float(data['Tw'])
		Tf = float(data['Tf'])
		R = float(data['R'])
		MinSize = Tw/10
		MaxSize = Tw/6

 ######     ###    ##        #######  ##     ## ########
##    ##   ## ##   ##       ##     ## ###   ### ##
##        ##   ##  ##       ##     ## #### #### ##
 ######  ##     ## ##       ##     ## ## ### ## ######
      ## ######### ##       ##     ## ##     ## ##
##    ## ##     ## ##       ##     ## ##     ## ##
 ######  ##     ## ########  #######  ##     ## ########
salome.salome_init()
theStudy = salome.myStudy
sys.path.insert( 0, WORKING_DIR)

 ######   ########  #######  ##     ##
##    ##  ##       ##     ## ###   ###
##        ##       ##     ## #### ####
##   #### ######   ##     ## ## ### ##
##    ##  ##       ##     ## ##     ##
##    ##  ##       ##     ## ##     ##
 ######   ########  #######  ##     ##
geompy = geomBuilder.New(theStudy)
# Vertex definiton
P0 = geompy.MakeVertex(0, 0, 0)
P1 = geompy.MakeVertex(Tw/2, 0, 0)
P2 = geompy.MakeVertex(Tw/2, H/2-Tf-R, 0)
P3 = geompy.MakeVertex(Tw/2+R, H/2-Tf-R, 0)
P4 = geompy.MakeVertex(Tw/2+R, H/2-Tf, 0)
P5 = geompy.MakeVertex(B/2, H/2-Tf, 0)
P6 = geompy.MakeVertex(B/2, H/2, 0)
P7 = geompy.MakeVertex(0, H/2, 0)
# Edge definition
Ox = geompy.MakeLineTwoPnt(P0, P1)
Oy = geompy.MakeLineTwoPnt(P0, P7)
L0 = geompy.MakeLineTwoPnt(P1, P2)
L1 = geompy.MakeArcCenter(P3, P4, P2,False)
L2 = geompy.MakeLineTwoPnt(P4, P5)
L3 = geompy.MakeLineTwoPnt(P5, P6)
L4 = geompy.MakeLineTwoPnt(P6, P7)
L5 = geompy.MakeMirrorByAxis(L0, Oy)
L6 = geompy.MakeMirrorByAxis(L1, Oy)
L7 = geompy.MakeMirrorByAxis(L2, Oy)
L8 = geompy.MakeMirrorByAxis(L3, Oy)
L9 = geompy.MakeMirrorByAxis(L4, Oy)
L10 = geompy.MakeMirrorByAxis(L0, Ox)
L11 = geompy.MakeMirrorByAxis(L1, Ox)
L12 = geompy.MakeMirrorByAxis(L2, Ox)
L13 = geompy.MakeMirrorByAxis(L3, Ox)
L14 = geompy.MakeMirrorByAxis(L4, Ox)
L15 = geompy.MakeMirrorByAxis(L5, Ox)
L16 = geompy.MakeMirrorByAxis(L6, Ox)
L17 = geompy.MakeMirrorByAxis(L7, Ox)
L18 = geompy.MakeMirrorByAxis(L8, Ox)
L19 = geompy.MakeMirrorByAxis(L9, Ox)
# Face definition
Face = geompy.MakeFaceWires([L0, L1, L2, L3, L4, L5, L6, L7, L8, L9, L10, L11, L12, L13, L14, L15, L16, L17, L18, L19], 1)
# Compound and partition definition
Compound = geompy.MakeCompound([P0, Face])
Partition = geompy.MakePartition([Compound], [], [], [], geompy.ShapeType["FACE"], 0, [], 0)
# Group definition
MyPoint = geompy.CreateGroup(Partition, geompy.ShapeType["VERTEX"])
MyBorder = geompy.CreateGroup(Partition, geompy.ShapeType["EDGE"])
MySect = geompy.CreateGroup(Partition, geompy.ShapeType["FACE"])
geompy.UnionIDs(MyPoint, [43])
geompy.UnionIDs(MyBorder, [3, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42])
geompy.UnionIDs(MySect, [1])

##     ## ########  ######  ##     ##
###   ### ##       ##    ## ##     ##
#### #### ##       ##       ##     ##
## ### ## ######    ######  #########
##     ## ##             ## ##     ##
##     ## ##       ##    ## ##     ##
##     ## ########  ######  ##     ##
smesh = smeshBuilder.New(theStudy)
Mesh = smesh.Mesh(Partition)
# NETGEN
NETGEN_2D = Mesh.Triangle(algo=smeshBuilder.NETGEN_1D2D)
NETGEN_2D_Parameters = NETGEN_2D.Parameters()
NETGEN_2D_Parameters.SetSecondOrder( 0 )
NETGEN_2D_Parameters.SetOptimize( 1 )
NETGEN_2D_Parameters.SetFineness( 2 )
NETGEN_2D_Parameters.SetUseSurfaceCurvature( 1 )
NETGEN_2D_Parameters.SetFuseEdges( 1 )
NETGEN_2D_Parameters.SetQuadAllowed( 0 )
NETGEN_2D_Parameters.SetMinSize( MinSize )
NETGEN_2D_Parameters.SetMaxSize( MaxSize )
# Calculation
isDone = Mesh.Compute()
# Group definition
MyPoint_1 = Mesh.GroupOnGeom(MyPoint,'MyPoint',SMESH.NODE)
MyBorder_1 = Mesh.GroupOnGeom(MyBorder,'MyBorder',SMESH.EDGE)
MySect_1 = Mesh.GroupOnGeom(MySect,'MySect',SMESH.FACE)
MyBorder_2 = Mesh.GroupOnGeom(MyBorder,'MyBorder',SMESH.NODE)
MySect_2 = Mesh.GroupOnGeom(MySect,'MySect',SMESH.NODE)
smesh.SetName(Mesh.GetMesh(), 'Mesh')
# Export MESH

Mesh.ExportMED(os.getcwd()+"/SectionAuto.mmed", 0)



