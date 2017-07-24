#!#! /usr/bin/env python
# -*- coding: utf-8 -*-
import external.euclid as eu
import logging

from external.UnitCalculator import *
auto_converter(mmNS)

G=9.81*m()/sec()

current_temperature = 20
current_ref_temperature = 20
current_pressure = ""
current_model = "TUBE"
current_section = []
current_material = "SS316"

current_rho_fluid=0
current_insulation=[]

tubapoint_counter = 0
dict_tubapoints = []
current_tubapoint = []

tubavector_counter = 0
dict_tubavectors = []
current_tubavector = []

vd1x0 = eu.Vector3(0, 1, 0)              # default dihedral vector 1
vd2x0 = eu.Vector3(1, 0, 0)

V_gravitation = eu.Vector3(0, 0, -9.8)   # gravitational vector (m/s²)

MeshNbElement = 10

colors = {
    "BLOCK_DEFORMATION":"1,0.5,0",    
    "BLOCK":"1,1,0",                    #yellow
    "POUTRE_RECTANGLE":"0.8,0.8,0.8",       #grey
    "RECTANGULAR":"0.8,0.8,0.8",            #grey
    "TUBE":"0.6,0.6,0.6",                   #grey
    "TUBE_BENT":"0.6,0.6,0.6",                   #grey
    "BAR":"0.4,0.4,0.4",                    #grey
    "CABLE":"0.8,0.8,0.8",                  #grey
    "TUYAU":"0.9,0.9,0.9",                  #grey
    "STIFFNESS":"0,0,1",            #blue
    "VOLUME":"0.5,0.8,0.8",
    "Masse":"0,0,1",
    "FORCE":"1,0,0",

    }
    

