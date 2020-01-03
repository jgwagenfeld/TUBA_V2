"""
Created on Sun Mar 27 22:05:19 2016
"""
#import global_vars as glob
#from global_functions import *
import external.euclid as eu
import logging
import math
import readchar

import tuba.tuba_vars_and_funcs as tub

def create_reducer(dict_tubavectors):
    for i,tubavector in enumerate(dict_tubavectors):    
        if not tubavector.end_tubapoint.is_element_end():
            if tubavector.end_tubapoint.get_next_vector().section!=tubavector.section:
                print("Reducer or Expander")
            
        
    
def create_weld(self,dict_tubavectors):
    pass