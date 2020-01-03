#! /home/cae/anaconda3/bin/python
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 22:06:23 2016

"""
import external.euclid as eu
import logging
import math
import tuba.tuba_vars_and_funcs as tub

class TubaBuilder:

    def __init__(self):
        self.current_temperature = 20
        self.current_ref_temperature = 20
        self.current_pressure = ""
        self.current_model = "TUBE"
        self.current_section = []
        self.current_section_orientation = 0
        self.current_material = "SS316"
        
        self.current_rho_fluid=0
        self.current_insulation=[]
        
        self.tubapoint_counter = 0
        self.dict_tubapoints = []
        self.current_tubapoint = []
        
        self.tubavector_counter = 0
        self.dict_tubavectors = []
        self.current_tubavector = []


    def getVector(name):
        
        vector=[]
        return vector