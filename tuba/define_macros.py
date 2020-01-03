# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 21:31:36 2016

"""
from tuba.define_geometry import *
from tuba.define_properties import *
import tuba.tuba_vars_and_funcs as tub

def FixPoint():
    """Creates a fixed Point"""
    Block(0,0,0,0,0,0)
    
def Joint():
    '''Restrains all 3 spatial directions but allows rotation around the axis'''
    Block(0,0,0,'x','x','x')


def Guide():
    """ A guide only allows movement in coaxial direction"""
    Block('x',0,0,'x','x','x')

   