#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 02:34:03 2016

@author: frenell
"""
import collections
import numpy as np
import external.euclid as eu
import logging

import tuba_vars_and_funcs as tub
import tuba.define_geometry as tuba_geom


class ParaPost:
    def __init__(self,tuba_directory):
        self.lines=[]


    def write(self,dict_tubavectors,dict_tubapoints):

        #Point Functions
        self._base(dict_tubapoints)

               
#==============================================================================
#  Write PostBase
#==============================================================================
    def _base(self,dict_tubapoints):
        self.lines=self.lines+("""
        ])
        
        
        
        
        
        
        """).split("\n")