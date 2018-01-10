#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 02:34:03 2016

"""
import os
import collections
import numpy as np
import external.euclid as eu
import logging

import tuba_vars_and_funcs as tub
import tuba.define_geometry as tuba_geom
import library_material


import write_Aster_friction

class CodeAster:

    def __init__(self,tuba_directory):
        self.lines=[]
        self.TUYAU_flag=False
        self.BAR_flag=False
        self.TUBE_flag=False
        self.VOLUME_flag=False
        self.SHELL_flag=False
        self.CABLE_flag=False
        self.FRICTION_flag=False
        self.tuba_directory=tuba_directory


    def write(self,dict_tubavectors,dict_tubapoints,cmd_script):

        self._set_flags_read_comm_base(dict_tubapoints,dict_tubavectors)        
          
       
        #Point Functions
        self._ddl_create_node_group(dict_tubapoints)
        self._ddl(dict_tubapoints)
        
        self._stiffness(dict_tubapoints)
        self._mass(dict_tubapoints)        
        self._force(dict_tubapoints)
        if self.FRICTION_flag:
            write_Aster_friction.set_Spring_elements(self,dict_tubapoints)  
                
        #Vector Functions
        self._linear_forces(dict_tubavectors)                     
        self._model(dict_tubavectors)                    
        self._pressure(dict_tubavectors)
        self._material(dict_tubavectors)
        self._temperature(dict_tubavectors)

        self._section(dict_tubavectors)
        self._section_orientation(dict_tubavectors)
        self._elbow_sif_flexibility(dict_tubavectors)
 
        self._Pipe3D(dict_tubavectors)
        self._TShape3D(dict_tubavectors)
        
        #Simulation
        if not self.FRICTION_flag:
            self._simulation()

        elif self.FRICTION_flag:
            write_Aster_friction._Simulation_loop(self,dict_tubapoints,cmd_script)  


        self._calculate_fields()            
        self._write_results_to_salome()     
        self._write_tables(cmd_script) 
        #Output
        self._clean_for_EFICAS()

#==============================================================================
#  Write Point Properties
#==============================================================================
    
    def _set_flags_read_comm_base(self,dict_tubapoints,dict_tubavectors): 
 
        
        for tubavector in dict_tubavectors:
            if tubavector.model in ["TUYAU"]:
                 self.TUYAU_flag=True
            if tubavector.model in ["BAR"]:
                 self.BAR_flag=True                   
            if tubavector.model in ["TUBE","RECTANGULAR"]:
                 self.TUBE_flag=True       
            if tubavector.model in ["VOLUME"]:
                 self.VOLUME_flag=True 
            if tubavector.model in ["SHELL"]:   #still not implemented
                 self.SHELL_flag=True 
            if tubavector.model in ["CABLE"]:   #still not implemented
                 self.CABLE_flag=True 
                
        for tubapoint in dict_tubapoints:      
            if not tubapoint.friction_coefficient == 0.0:  
                self.FRICTION_flag=True 
                print ("Firction flag =", self.FRICTION_flag)
          
          
        if self.FRICTION_flag:  
            base_text= open(self.tuba_directory+"/tuba/TUBA_COMM_BASE_FRICTION.txt", "r")
        else:
            base_text= open(self.tuba_directory+"/tuba/TUBA_COMM_BASE.txt", "r")
            
        code = base_text.readlines()
        base_text.close()              
 
        print
        print("------------------------")
        print("  Read TUBA_BASE.txt into the Code_Comm-file to process the Aster-Code")
        print("------------------------")

        for line in code :
            line = line[:-1]
            self.lines.append(line)    




    
    def _ddl(self,dict_tubapoints):
        """writes support-information
        """
        for tubapoint in dict_tubapoints:  
            newlines=[]
#            character_count=0
    
            newlines=[str("_F(GROUP_NO='" +tubapoint.name +"',")]
            prefix_ddl=["DX","DY","DZ","DRX","DRY","DRZ"]
            for i,x in enumerate(tubapoint.ddl):
                if str(x) != 'x':
                    newlines.append(7*" "+prefix_ddl[i]+"="+str(x)+",")
           
            if tubapoint.ddl_reference=="global":
                newlines.append(7*" "+"ANGL_NAUT=(0.0,0.0,0),")
                newlines.append("),")  


            elif tubapoint.ddl_reference=="local": 
                #still has to be implemented              
                newlines.append("),")                
                
            if len(newlines)>3:   #just checks if there where actually ddls defined                
                  insert_lines_at_string(self.lines,"##LIAISON_OBLIQUE",newlines)


#==============================================================================            
    def _ddl_create_node_group(self,dict_tubapoints):
                
        newlines=[] 
        newlines.extend([
        "    _F(  NOM='GPOINTS',",
        "         UNION=(",
        ])
        
        text="         "
        character_count=0
        for tubapoint in dict_tubapoints:
            #if not tubapoint.ddl == ['x','x','x','x','x','x']:
            if not "center" in tubapoint.name:    
                character_count+=len(tubapoint.name)+4
                text += "'"+tubapoint.name+"', "
            if not tubapoint.stiffness == [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]:   
                character_count+=len(tubapoint.name)+4
                text += "'"+tubapoint.name+"K', "

            if not tubapoint.friction_coefficient == 0.0:   
                character_count+=len(tubapoint.name)+4
                text += "'"+tubapoint.name+"_f', "

                
            if character_count > 50:
                newlines.append(text)
                text="    "
                character_count=0
        newlines.append(text)

        newlines.extend([
        "        ),",
        "    ),",
        ])
        
        if len(newlines)>4:
            insert_lines_at_string(self.lines,"##CREA_GROUPE_NOEUD",newlines)

       
#==============================================================================
    def _stiffness(self,dict_tubapoints):
        '''writes the defined spring properties at all tubapoints to the aster.comm-file'''
       
                                                    

        text=""
        for tubapoint in dict_tubapoints:      
            if not tubapoint.stiffness == [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]:        
                text += "'Spring"+tubapoint.name+"', "

        if text!="":
            newlines=[
            "    _F(",
            "       GROUP_MA=(",
            ]               
            
            newlines.append("       "+text)
            newlines.extend([
            "       ),",
            "       PHENOMENE='MECANIQUE',",
            "       MODELISATION='DIS_TR',",
            "    ),"
            ])         
        

            insert_lines_at_string(self.lines,"##MODELISATION",newlines)
            newlines=[]
           
      
        for tubapoint in dict_tubapoints: 
  
            if not tubapoint.stiffness == [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]:
                [x,y,z,rx,ry,rz]=tubapoint.stiffness
        
                newlines=[
                "_F(",
                "GROUP_MA = 'Spring" + tubapoint.name + "',",
                "REPERE = 'GLOBAL',",
                "CARA = 'K_TR_D_L',",
                "VALE = (",
                "         " + str(x) + ",",
                "         " + str(y) + ",",
                "         " + str(z) + ",",
                "         " + str(rx) + ",",
                "         " + str(ry) + "," ,
                "         " + str(rz) + ",),",
                "),",
                ]
        
                insert_lines_at_string(self.lines,"##STIFFNESS_DISCRET",newlines)


                newlines=[]
                newlines=[
                "_F(GROUP_NO='"+ tubapoint.name + "K',",
                "       DX=0,",
                "       DY=0,",
                "       DZ=0,",
                "       DRX=0,",
                "       DRY=0,",
                "       DRZ=0,",
                "       ANGL_NAUT=(0.0,0.0,0),",
                "),",                                             
                ]

                if len(newlines)>3:   #just checks if there where actually ddls defined                
                      insert_lines_at_string(self.lines,"##LIAISON_OBLIQUE",newlines)




#==============================================================================
    def _mass(self,dict_tubapoints):
        '''writes the defined mass properties at all tubapoints to the aster.comm-file'''

        text=""
        for tubapoint in dict_tubapoints:      
            if not tubapoint.mass == 0:        
                text += "'"+tubapoint.name+"M', "

        if text!="":
            newlines=[
            "    _F(",
            "       GROUP_MA=(",
            ]               
            
            newlines.append("       "+text)
            newlines.extend([
            "       ),",
            "       PHENOMENE='MECANIQUE',",
            "       MODELISATION='DIS_T',",
            "    ),"
            ])         
        

            insert_lines_at_string(self.lines,"##MODELISATION",newlines)
            newlines=[]
           
      
        for tubapoint in dict_tubapoints: 
  
            if not tubapoint.mass == 0:
                newlines=[
                "_F(",
                "   NOM_GROUP_MA='"+tubapoint.name+"M',",
                "   GROUP_NO='"+tubapoint.name+"',",
                "),",
                ]
      
                insert_lines_at_string(self.lines,"##CREA_POI1",newlines)
                newlines=[]    
    
                print (tubapoint.mass)

        
                newlines=[
                "_F(",
                "GROUP_MA = '" + tubapoint.name + "M',",
                "REPERE = 'GLOBAL',",
                "CARA='M_T_D_N',",
                "VALE = ("+str(tubapoint.mass)+" ) ,",
                "),",
                ]
        
                insert_lines_at_string(self.lines,"##MASS_DISCRET",newlines)


#==============================================================================
    def _moment(self,dict_tubapoints):
        for tubapoint in dict_tubapoints: 
            newlines=[]  
 
            for i,moment in enumerate(tubapoint.moment):
                if moment != (0,0,0):
                    newlines=[
                        "_F(",
                        "GROUP_NO='" + tubapoint.name + "',",
                        "MX="+str(moment.x)+", MY="+str(moment.y)+", MZ="+str(moment.z),
                        "),"
                        ]                           
                    
                    insert_lines_at_string(self.lines,"##FORCE_NODALE",newlines)
#==============================================================================
    def _force(self,dict_tubapoints):
                
        for tubapoint in dict_tubapoints: 
            newlines=[]  

            for i,force in enumerate(tubapoint.force):
                if force != (0,0,0):
                    newlines=[
                        "_F(",
                        "GROUP_NO='" + tubapoint.name + "',",
                        "FX="+str(force.x)+", FY="+str(force.y)+", FZ="+str(force.z),
                        "),"
                        ]                           
                    
                    insert_lines_at_string(self.lines,"##FORCE_NODALE",newlines)
                                   
#==============================================================================
#  Write Vector Properties
#==============================================================================
    def _temperature(self,dict_tubavectors):
        newlines=[]
        grouped_attributes=extract_group_attributes_from_list("temperature","name",dict_tubavectors)

        for item in grouped_attributes:
            newlines=[]
            newlines.extend([
            "_F(",
            "   GROUP_MA=(",
            ])

            character_count=0
            text="    "
            for name in item[1] :
                character_count+=len(name)+4
                text += "'"+name+"', "

                if character_count > 50:
                    newlines.append(text)
                    text="    "
                    character_count=0
            newlines.append(text)

            newlines.extend([
            "   ),",
            "   NOM_CMP='TEMP',",
            "   VALE="+str(item[0])+",",
            "),",
            ])
            insert_lines_at_string(self.lines,"##TEMPERATURE",newlines)

#==============================================================================
    def _material(self,dict_tubavectors):
        newlines=[]
        grouped_attributes=extract_group_attributes_from_list("material","name",dict_tubavectors)

        #======================================================================
        #  Assigne the material to the elements(vectors)
        #======================================================================

        for item in grouped_attributes:
            newlines=[]
            newlines.extend([
            "    _F(",
            "        GROUP_MA=(",
            ])

            character_count=0
            text="            "
            for name in item[1] :
                character_count+=len(name)+4
                text += "'"+name+"', "

                if character_count > 50:
                    newlines.append(text)
                    text="            "
                    character_count=0
            newlines.append(text)

            newlines.extend([
            "        ),",
            "        MATER="+str(item[0])+",",
            "    ),",
            ])

            insert_lines_at_string(self.lines,"##ASSIGN_MATERIAL",newlines)
        #======================================================================
        #   Define the used material
        #======================================================================
            for material in library_material.dict_mat:
                if material == item[0]:
                    [E,nu,rho,alpha,lamba,rhoCp, sh] = material
                    newlines=[
                    material + "=DEFI_MATERIAU(    ",
                    "     ELAS=_F(  E=" + str(E*1e3)+",",
                    "               NU=" + str(nu)+",",
                    "               RHO=" + str(rho*1e-9)+",",
                    "               ALPHA=" + str(alpha*1e-6)+",",
                    "           ),",
                    "     );",
                    ]
                    insert_lines_at_string(self.lines,"##DEF_MATERIAU",newlines)

            for material in library_material.dict_mat_F:
                if material == item[0]:
                    F_Mat_Prop= library_material.dict_mat_F[material]

                    newlines=[
                    "E_"+material+"=DEFI_FONCTION(NOM_PARA='TEMP',",
                    "              VALE=",
                    "              "+str(F_Mat_Prop[0])+",",
                    "              PROL_DROITE='CONSTANT',   ",
                    "              PROL_GAUCHE='CONSTANT',); ",
                    "",]
                    insert_lines_at_string(self.lines,"##DEF_MATERIAU",newlines)


                    newlines=[
                    "NU_"+material+"=DEFI_FONCTION(NOM_PARA='TEMP',",
                    "              VALE=",
                    "              "+str(F_Mat_Prop[1])+",",
                    "              PROL_DROITE='CONSTANT',   ",
                    "              PROL_GAUCHE='CONSTANT',); ",
                    "",]
                    insert_lines_at_string(self.lines,"##DEF_MATERIAU",newlines)

                    newlines=[
                    "A_"+material+"=DEFI_FONCTION(NOM_PARA='TEMP',",
                    "              VALE=",
                    "              "+str(F_Mat_Prop[3])+",",
                    "              PROL_DROITE='CONSTANT',   ",
                    "              PROL_GAUCHE='CONSTANT',); ",
                    "",]
                    insert_lines_at_string(self.lines,"##DEF_MATERIAU",newlines)


                    newlines=[
                    "R_"+material+"=DEFI_CONSTANTE(VALE="+str(F_Mat_Prop[2])+")",
                    "",]

                    
                    insert_lines_at_string(self.lines,"##DEF_MATERIAU",newlines)


                    newlines=[
                    material + "=DEFI_MATERIAU(    ",
                    "     ELAS_FO=_F(  E= E_"+material+",",              
                    "               NU=   NU_"+material+",",  
#                    "               RHO="   + str(F_Mat_Prop[2])+",",    
                    "               RHO=  R_"+material+",",      
                    "               ALPHA=   A_"+material+",",    
                    "               TEMP_DEF_ALPHA= 20 ,     ",
                    "           ),",
                    ");",
                    ]
                    insert_lines_at_string(self.lines,"##DEF_MATERIAU",newlines)


#==============================================================================

    def _pressure(self,dict_tubavectors):
        newlines=[]
        grouped_attributes=extract_group_attributes_from_list("pressure","name",dict_tubavectors)
        
        for item in grouped_attributes :
            #Delete all elements from the List which dont have TUYAU as model
            new_item=[]
            for name in item[1]:
                item_tubavector=([tubavector for tubavector in dict_tubavectors
                                            if tubavector.name == name][0])                                
                if item_tubavector.model in ["TUYAU","VOLUME"] :
                    new_item.append(name)
  
            if  new_item:            
                newlines=[]
                newlines.extend([
                "    _F(",
                "        GROUP_MA=(",
                ])
    
                character_count=0
                text="            "
                for name in new_item :
                    character_count+=len(name)+4
                    text += "'"+name+"', "
    
                    if character_count > 50:
                        newlines.append(text)
                        text="            "
                        character_count=0
                newlines.append(text)

                newlines.extend([
                "        ),",
                "        PRES="+str(item[0])+",",
                "    ),",
                ])
                if item[0]:
                    insert_lines_at_string(self.lines,"##FORCE_TUYAU",newlines)


            for name in item[1]:
                item_tubavector=([tubavector for tubavector in dict_tubavectors
                                            if tubavector.name == name][0])                                
                if item_tubavector.model == "TUBE":
                    new_item.append(name)
  


#==============================================================================
    def _linear_forces(self,dict_tubavectors):
        for tubavector in dict_tubavectors: 
            newlines=[]  
            force_sum = (0,0,0)
            for i,force in enumerate(tubavector.linear_force):
                force_sum=force_sum+force
             
            print("force_sum", force_sum) 
            if force_sum != (0,0,0):
                newlines=[
                    "_F(",
                    "GROUP_MA='" + tubavector.name + "',",
                    "FX="+str(force_sum.x)+", FY="+str(force_sum.y)+", FZ="+str(force_sum.z),
                    "),"
                    ]                           
                
                insert_lines_at_string(self.lines,"##LINEAR_FORCE",newlines)

#==============================================================================
    def _section(self,dict_tubavectors):
        newlines=[]
        grouped_attributes=extract_group_attributes_from_list("section","name",dict_tubavectors)

        for item in grouped_attributes:
            new_item=[]
#------------------------------------------------------------------------------            
            for name in item[1]:
                item_tubavector=([tubavector for tubavector in dict_tubavectors
                                            if tubavector.name == name][0])                                
                if item_tubavector.model in ["TUBE" ,"TUYAU"]: 
                    new_item.append(name)                           
             
            if new_item:        
                newlines=[]
                newlines.extend([
                "    _F(",
                "        GROUP_MA=(",
                ])
    
                character_count=0
                text="           "
                for name in new_item :
                    character_count+=len(name)+4
                    text += "'"+name+"', "
    
                    if character_count > 50:
                        newlines.append(text)
                        text="           "
                        character_count=0
                newlines.append(text)
                newlines.append("        ),")
                
                newlines.extend([
                "        SECTION ='CERCLE',",
                "        CARA=('R','EP',),",
                "        VALE=("+ str(item[0].strip("[],")) +"),",
                "    ),",
                ])
                insert_lines_at_string(self.lines,"##SECTION_TUBE",newlines)    
#------------------------------------------------------------------------------
            new_item=[]
            for name in item[1]:
                item_tubavector=([tubavector for tubavector in dict_tubavectors
                                            if tubavector.name == name][0])                                
                if item_tubavector.model == "RECTANGULAR": 
                    new_item.append(name)                           
            
            if new_item:                    
                newlines=[]
                newlines.extend([
                "_F(",
                "   GROUP_MA=(",
                ])
    
                character_count=0
                text="    "
                for name in new_item :
                    character_count+=len(name)+4
                    text += "'"+name+"', "
    
                    if character_count > 50:
                        newlines.append(text)
                        text="    "
                        character_count=0
                newlines.append(text)
                newlines.append("),")
                item=eval(item[0])
                [height_y,height_z,thickness_y,thickness_z]=item
                solid_crosssection=False
                if thickness_y==0 and thickness_z==0 : solid_crosssection=True
                
                if solid_crosssection:
                    newlines.extend([
                    "   SECTION='RECTANGLE',",
                    "   CARA=('HY','HZ'),",
                    "   VALE=("+str(height_y)+", "+str(height_z)+"),",
                    "),",
                    ])
                else:
                    newlines.extend([
                    "   SECTION='RECTANGLE',",
                    "   CARA=('HY','HZ','EPY','EPZ'),",
                    "   VALE=("+str(height_y)+", "+str(height_z)+", "+
                                str(thickness_y)+", "+str(thickness_z)+"),",
                    "),",
                    ])
                insert_lines_at_string(self.lines,"##SECTION_RECTANGULARBEAM",newlines)            


            for name in item[1]:
                item_tubavector=([tubavector for tubavector in dict_tubavectors
                                            if tubavector.name == name][0])                                
                if item_tubavector.model == "BAR": 
                    new_item.append(name)                           
            
            if new_item:        
                newlines=[]
                newlines.extend([
                "    _F(",
                "        GROUP_MA=(",
                ])
    
                character_count=0
                text="           "
                for name in new_item :
                    character_count+=len(name)+4
                    text += "'"+name+"', "
    
                    if character_count > 50:
                        newlines.append(text)
                        text="           "
                        character_count=0
                newlines.append(text)
                newlines.append("        ),")
                
                newlines.extend([
                "        SECTION ='CERCLE',",
                "        CARA=('R','EP',),",
                "        VALE=("+ str(item[0].strip("[],")) +"),",
                "    ),",
                ])
                insert_lines_at_string(self.lines,"##SECTION_BAR",newlines)                



          
#------------------------------------------------------------------------------            
    def _section_orientation(self,dict_tubavectors):
        newlines=[]
        grouped_attributes=extract_group_attributes_from_list("section_orientation","name",dict_tubavectors)

        print("orientation",grouped_attributes)
        for item in grouped_attributes:
            print(item[0],item[1])
    
            if not item[0]=="0":                    
                newlines.extend([
                "_F(",
                "    GROUP_MA=(",
                ])
    
                character_count=0
                text="    "
                for name in item[1] :
                    character_count+=len(name)+4
                    text += "'"+name+"', "
    
                    if character_count > 50:
                        newlines.append(text)
                        text="    "
                        character_count=0
                newlines.append(text)
                newlines.append("    ),")


            
                newlines.extend([
                "    CARA='ANGL_VRIL',",
                "    VALE="+item[0]+",),",
                ])


        insert_lines_at_string(self.lines,"##SECTION_ORIENTATION",newlines)           
#==============================================================================      
         
    def _model(self,dict_tubavectors):      
        newlines=[]
        grouped_attributes=extract_group_attributes_from_list("model","name",dict_tubavectors) 
        print("grouped_attributes",grouped_attributes)
        for item in grouped_attributes:
            if item[0] == "TUBE" or item[0]=="RECTANGULAR":
                newlines=[]
                newlines.extend([
                "    _F( NOM='GTUBE_D',",       
                "        TYPE_MAILLE = '1D',",
                "        UNION=(",
                ]) 
 
                character_count=0
                text="          "
                for name in item[1] :

                    character_count+=len(name)+4
                    text += "'"+name+"', "
    
                    if character_count > 50:
                        newlines.append(text)
                        text="        "
                        character_count=0
                newlines.append(text)


                newlines.append("        ),")
                newlines.append("    ),")
                insert_lines_at_string(self.lines,"##CREA_GROUPE_MAILLE ",newlines)
                
                newlines=[
                "    _F(",
                "        GROUP_MA='GTUBE_D',",
                "        PHENOMENE='MECANIQUE',",
                "        MODELISATION='POU_D_T',",
                "    ),",
                ]
                
                insert_lines_at_string(self.lines,"##MODELISATION" ,newlines)
              
            if item[0] == "TUYAU":
                newlines=[]
                newlines.extend([
                "    _F(",
                "        NOM='GTUYAU3M',",
                "        TYPE_MAILLE = '1D',",
                "        UNION=(",
                ])
 
                character_count=0
                text="            "
                for name in item[1] :
                    character_count+=len(name)+4
                    text += "'"+name+"', "
    
                    if character_count > 50:
                        newlines.append(text)
                        text="            "
                        character_count=0
                newlines.append(text)


                newlines.append("        ),")
                newlines.append("    ),")
                insert_lines_at_string(self.lines,"##CREA_GROUPE_MAILLE ",newlines)
                
                newlines=[
                "    _F(",
                "        GROUP_MA='GTUYAU3M',",
                "        PHENOMENE='MECANIQUE',",
                "        MODELISATION='TUYAU_3M',",
                "    ),",
                ]                
                insert_lines_at_string(self.lines,"##MODELISATION" ,newlines)                

             
             
            if item[0] == "BAR":

                newlines=[]
                newlines.extend([
                "    _F(",
                "        NOM='GBAR',",
                "        TYPE_MAILLE = '1D',",
                "        UNION=(",
                ])                
                character_count=0
                text="            "
                for name in item[1] :
                    character_count+=len(name)+4
                    text += "'"+name+"', "
    
                    if character_count > 50:
                        newlines.append(text)
                        text="            "
                        character_count=0
                newlines.append(text)


                newlines.append("        ),")
                newlines.append("    ),")
                insert_lines_at_string(self.lines,"##CREA_GROUPE_MAILLE ",newlines)                
                
                newlines=[]
                newlines.extend([                
                "    _F(",
                "        GROUP_MA='GBAR',",                        
                "        PHENOMENE = 'MECANIQUE',",
                "        MODELISATION = 'BARRE',",             
                "    ),",
                ])            
                
                insert_lines_at_string(self.lines,"##MODELISATION" ,newlines)
             
        for tubavector in dict_tubavectors:
            if tubavector.model == "TUYAU" and tubavector.start_tubapoint.is_element_start():
                print("GENE_INTRODUCTION:", tubavector.vd1x, tubavector.start_tubapoint.is_element_start())

                newlines=[                           
                "_F(	GROUP_NO='"+tubavector.start_tubapoint.name+"',",
                "		CARA='GENE_TUYAU',",
                "    VALE=("+str(tubavector.vd1x.x)+","+str(tubavector.vd1x.y)+","+str(tubavector.vd1x.z)+",),",
                "),",]

                insert_lines_at_string(self.lines,"##SECTION_ORIENTATION" ,newlines)
                
#==============================================================================             
    def _Pipe3D(self,dict_tubavectors):                                   

        for tubavector in dict_tubavectors:
            if tubavector.model=="VOLUME" and not isinstance(tubavector,tuba_geom.TubaTShape3D):
                    
                newlines=[
                "_F(",
                "   GROUP_MA=(",
                "  '" +  tubavector.name +"', '"+tubavector.name+"_StartFace','"+tubavector.name+"_EndFace'),",
                "   PHENOMENE='MECANIQUE',",
                "   MODELISATION='3D',",
                "),",
                ]
                
                insert_lines_at_string(self.lines,"##MODELISATION" ,newlines)        
                              
                # Définition des liaisons 3D-TUBE",
                newlines=("""_F(               
    OPTION='3D_POU',
    GROUP_MA_1 ='"""+str(tubavector.name)+"""_StartFace',
    GROUP_NO_2 ='"""+str(tubavector.start_tubapoint.name)+"""',
    ),""").split("\n")
                                    
                newlines=newlines+("""_F(
    OPTION='3D_POU',
    GROUP_MA_1 ='"""+tubavector.name+"""_EndFace',
    GROUP_NO_2 ='"""+tubavector.end_tubapoint.name+"""',
    ),""").split("\n")                  
                                             
                insert_lines_at_string(self.lines,"##LIAISON_3D_TUBE" ,newlines)
#==============================================================================                                        
    def _TShape3D(self,dict_tubavectors):

        for tubavector in dict_tubavectors:
            if isinstance(tubavector,tuba_geom.TubaTShape3D):
                newlines=[
                "_F(",
                "   GROUP_MA=(",
                "  '" + tubavector.name +"', '"+tubavector.name+"_StartFace', '"+
                tubavector.name+"_IncidentFace', '"+tubavector.name+"_EndFace'),",
                "   PHENOMENE='MECANIQUE',",
                "   MODELISATION='3D',",
                "),",
                ]
                
                insert_lines_at_string(self.lines,"##MODELISATION" ,newlines)        
                              
                # Définition des liaisons 3D-TUBE",
                newlines=("""_F(               
    OPTION='3D_POU',
    GROUP_MA_1 ='"""+str(tubavector.name)+"""_StartFace',
    GROUP_NO_2 ='"""+str(tubavector.start_tubapoint.name)+"""',
    ),""").split("\n")
                
                newlines=newlines+("""_F(          
    OPTION='3D_POU',
    GROUP_MA_1 ='"""+str(tubavector.name)+"""_IncidentFace',
    GROUP_NO_2 ='"""+str(tubavector.incident_end_tubapoint.name)+"""',
    ),""").split("\n")      
                
                newlines=newlines+("""_F(
    OPTION='3D_POU',
    GROUP_MA_1 ='"""+tubavector.name+"""_EndFace',
    GROUP_NO_2 ='"""+tubavector.end_tubapoint.name+"""',
    ),""").split("\n")                  
                
                             
                insert_lines_at_string(self.lines,"##LIAISON_3D_TUBE" ,newlines)


#==============================================================================

    def _elbow_sif_flexibility(self,dict_tubavectors):
        
        for tubavector in dict_tubavectors:
            newlines=[]
            if tubavector.model=="TUBE" and isinstance(tubavector,tuba_geom.TubaBent):
                newlines.extend([
                "    _F(",
                "        GROUP_MA=('"+tubavector.name+"'),",
                ])                
                newlines.extend([
                "        SECTION = 'COUDE',",
                "        COEF_FLEX_XY = "+str(tubavector.cflex)+",",
                "        COEF_FLEX_XZ = "+str(tubavector.cflex)+",",
                "        INDI_SIGM_XY = "+str(tubavector.sif)+", ",
                "        INDI_SIGM_XZ = "+str(tubavector.sif)+",", 
                "    ),",
                    ])
            insert_lines_at_string(self.lines,"##SECTION_ELBOW",newlines)  


#==============================================================================
    def _simulation(self):

        newlines=("""

# Run the simulation
#---------------------------------------------------                       
RESU=MECA_STATIQUE(
     MODELE=MODMECA,
     CHAM_MATER=CH_MAT,
     CARA_ELEM=CARAELEM,
     INST=1,
     EXCIT=(
         _F(   CHARGE=BLOCAGE
          ),
         _F(   CHARGE=LOAD,
          ),

         ##CHARGEMENT
     ),
);""").split("\n")   
        insert_lines_at_string(self.lines, "##SIMULATION", newlines)



#==============================================================================
    def _calculate_fields(self):
        list_criteres=[]
        list_contraintes = []
        
        if self.TUBE_flag:
            list_contraintes.extend(('\'SIPO_ELNO\'','\'SIPO_NOEU\'','\'SIPM_ELNO\''))         
        if self.TUYAU_flag:                                 
            pass
        if self.VOLUME_flag:                                    
            list_contraintes.extend(('\'SIGM_ELNO\'','\'SIGM_ELGA\''))
            list_criteres.append('\'SIEQ_ELNO\'')

        list_contraintes=list(set(list_contraintes))   #removes dublicates
        list_contraintes = ",".join(list_contraintes )       
        list_criteres = ",".join(list_criteres ) 

        print("STATIQUE_LINEAIRE")  
        print("TUBE_flag:",self.TUBE_flag)
        print("TUYAU_flag:",self.TUYAU_flag)
        print("VOLUME_flag:",self.VOLUME_flag)
        print("list_contraintes:",list_contraintes)        
        print("list_criteres:",list_criteres) 

        newlines=("""
# Calculate Reaction Forces from obtained results
#---------------------------------------------------

RESU=CALC_CHAMP(reuse =RESU,
     RESULTAT=RESU,
     FORCE=('REAC_NODA','FORC_NODA'),""").split("\n")
        if list_contraintes: 
            newlines.append("     CONTRAINTE=("+list_contraintes+"),")
        if list_criteres: 
            newlines.append("     CRITERES=("+list_criteres+"),")  

        newlines.append(");")

#        newlines=newlines+("""
#RESU=CALC_CHAMP(reuse =RESU,
#     RESULTAT=RESU,
#     GROUP_MA='GTUBE_D',     
#     CONTRAINTE=("""+list_contraintes+"""),   
#     );                  
#         """).split("\n")            

        if self.TUBE_flag:
            newlines=newlines+("""
MFlex = FORMULE(
    NOM_PARA=('SMT','SMFY', 'SMFZ', ),
    VALE=\"\"\"sqrt(SMFY**2 + SMFZ**2 +2*SMT**2)\"\"\")  

RES_MPP = CALC_CHAMP(
    RESULTAT=RESU,
    CHAM_UTIL=_F(
        NOM_CHAM='SIPO_ELNO',
        FORMULE=(MFlex),
        NUME_CHAM_RESU=2,
    ),
);  """).split("\n")   


        if self.TUYAU_flag:
            newlines=newlines+("""
RESU=CALC_CHAMP(reuse =RESU,
     RESULTAT=RESU,
     GROUP_MA='GTUYAU3M',
     CRITERES='SIEQ_ELNO',);
        

MAX_VMIS=POST_CHAMP(
    RESULTAT=RESU,
    TOUT_ORDRE='OUI',
    GROUP_MA='GTUYAU3M',
    MIN_MAX_SP=(
    _F( NOM_CHAM='SIEQ_ELNO',
           NOM_CMP='VMIS',
           TYPE_MAXI='MAXI',
           NUME_CHAM_RESU=1,
           ),
    ),
);
        """).split("\n")     
#include Formula ASME 31.3  319.4.4.   
        insert_lines_at_string(self.lines, "##CALCULATE_FIELDS", newlines)

#==============================================================================
    def _write_results_to_salome(self):
        newlines=[]
        newlines=newlines+("""
# PRINT RESULTS  to  .MED  ->  Salome
#---------------------------------------------------    
   
IMPR_RESU(UNITE=80,FORMAT='MED',RESU=(
        _F(RESULTAT=RESU),
        _F(CHAM_GD=CHA_TEMP)

        ,""").split("\n")

        if self.TUBE_flag:
            newlines=newlines+("""    
        _F(RESULTAT=RES_MPP,GROUP_MA=('GTUBE_D'),NOM_CHAM='UT02_ELNO',NOM_CHAM_MED='Flexibiliy Stress',),
""").split("\n") 

        if self.TUYAU_flag:
            newlines=newlines+(""" 
        _F(RESULTAT=MAX_VMIS),
 """).split("\n")        
        newlines.append("));")          

        if self.FRICTION_flag:     
            newlines.append("IMPR_RESU(UNITE=80, FORMAT='MED', CONCEPT=_F(CARA_ELEM=CAP[-1], REPERE_LOCAL='ELNO', MODELE=MODMECA), )")
        else:    
            newlines.append("IMPR_RESU(UNITE=80, FORMAT='MED', CONCEPT=_F(CARA_ELEM=CARAELEM, REPERE_LOCAL='ELNO', MODELE=MODMECA), )")



        insert_lines_at_string(self.lines, "##RESULTS_TO_SALOME", newlines)
        
#==============================================================================
    def _write_tables(self,cmd_script):
        newlines=("""
#Results(Deformation, Reaction Forces and Forces) at specific nodes are saved in a txt-file
#-----------------------------------------------------------------------------------------             
Tab_DEPL=CREA_TABLE(RESU=_F(RESULTAT=RESU,
						 GROUP_NO='GPOINTS', #'ALL'
						 NOM_CHAM='DEPL',
						 NOM_CMP=('DX','DY','DZ'),
						 PRECISION=0.1,   
						 ),
                );
Tab_REAC=CREA_TABLE(RESU=_F(RESULTAT=RESU,
						 GROUP_NO='GPOINTS', #'ALL'
						 NOM_CHAM='REAC_NODA',
						 NOM_CMP=('DX','DY','DZ'),
						 PRECISION=0.1,   
						 ),
                );    
Tab_FORC=CREA_TABLE(RESU=_F(RESULTAT=RESU,
						 GROUP_NO='GPOINTS',    #'ALL'
						 NOM_CHAM='FORC_NODA',
						 NOM_CMP=('DX','DY','DZ'),
						 PRECISION=0.1,                         
						 ),
                );    
    
var_depl=Tab_DEPL.EXTR_TABLE();
var_reac=Tab_REAC.EXTR_TABLE();
var_forc=Tab_FORC.EXTR_TABLE();                            

if var_depl['COOR_Z']:
    var_depl=var_depl['NOM_CHAM','NOEUD','COOR_X','COOR_Y','COOR_Z','DX','DY','DZ']
    var_reac=var_reac['NOM_CHAM','NOEUD','COOR_X','COOR_Y','COOR_Z','DX','DY','DZ']                        
    var_forc=var_forc['NOM_CHAM','NOEUD','COOR_X','COOR_Y','COOR_Z','DX','DY','DZ']
else:
    var_depl=var_depl['NOM_CHAM','NOEUD','COOR_X','COOR_Y','DX','DY','DZ']
    var_reac=var_reac['NOM_CHAM','NOEUD','COOR_X','COOR_Y','DX','DY','DZ']                        
    var_forc=var_forc['NOM_CHAM','NOEUD','COOR_X','COOR_Y','DX','DY','DZ']    
                         
#mass=POST_ELEM(
#    RESULTAT =RESU ,
#    MASS_INER=_F(TOUT='OUI' ),
#    TITRE= 'mass',
#    ) ;
#var_mass=mass.EXTR_TABLE();
#var_mass=var_mass['LIEU','MASSE']        


                                  
import os
current_directory ='"""+ os.getcwd()+"""'

OUTPUT_FILE='/"""+cmd_script+"""_Tables.output' # Filename of the output file
fileOutput = current_directory + OUTPUT_FILE # Define output file                    
                    
try:
   f = open(fileOutput, 'w')    #'a' opens the file for appending , 'w' opens file and erases
   f.write(str(var_depl)+str(var_reac)+str(var_forc))#+'\\n'+'Total Mass in tons \\n'+str(var_mass))
   f.close()
   
except:
   print("Error")

        """).split("\n") 
     
        insert_lines_at_string(self.lines, "##TABLE_OUTPUT", newlines)

    
#    
    def _clean_for_EFICAS(self):  
        """All the markers ## which come from the Base-Comm Textfile used to
        write the Aster Code are removed"""
        cleaned_lines = [line for line in self.lines if not line.lstrip().startswith('##')]
        self.lines=cleaned_lines
#==============================================================================
#==============================================================================

def insert_lines_at_string(lines,substring,newlines):
    """In a list of strings, find the substring, and append the newlines before
    that string taking into account the whitespaces before it (This function is used to 
    insert lines in to the TUBA_COMM_BASE.txt at the right poition"""
    for line in lines:
        if substring in line:
            index=lines.index(line)
            whitespace_count=len(line) - len(line.lstrip())


    for line in reversed(newlines):
        lines.insert(index,whitespace_count*" "+line)

#==============================================================================

def extract_group_attributes_from_list(key_attribute,name_attribute,dict_tubavectors):
    key_attribute="o."+ key_attribute
    name="o."+ name_attribute

    extracted_attributes=[(eval(key_attribute),eval(name)) for o in dict_tubavectors]

    
    grouped_attributes = collections.defaultdict(list)
    for key, name in extracted_attributes:
        grouped_attributes[str(key)].append(name)

    return (grouped_attributes.items())


        
    
