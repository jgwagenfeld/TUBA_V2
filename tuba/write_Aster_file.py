#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 02:34:03 2016

"""
import collections
import numpy as np
import external.euclid as eu
import logging

import tuba_vars_and_funcs as tub
import tuba.define_geometry as tuba_geom
import library_material


class CodeAster:
    def __init__(self,tuba_directory):
        self.lines=[]
        self.TUYAU_flag=False

        base_text= open(tuba_directory+"/tuba/TUBA_COMM_BASE.txt", "r")
        code = base_text.readlines()
        base_text.close()

        print
        print("------------------------")
        print("  Read TUBA_BASE.txt into the Code_Comm-file to process the Aster-Code")
        print("------------------------")

        for line in code :
            line = line[:-1]
            self.lines.append(line)

    def write(self,dict_tubavectors,dict_tubapoints):

        #Point Functions
        self._ddl_create_node_group(dict_tubapoints)
        self._ddl(dict_tubapoints)
        
        self._stiffness(dict_tubapoints)
        self._force(dict_tubapoints)
                
        #Vector Functions
        self._linear_forces(dict_tubavectors)                     
        self._model(dict_tubavectors)                    
        self._pressure(dict_tubavectors)
        self._material(dict_tubavectors)
        self._temperature(dict_tubavectors)
        self._section(dict_tubavectors)
        self._TShape3D(dict_tubavectors)
        
        #Simulation
        self._simulation()
        self._write_tables()

#==============================================================================
#  Write Point Properties
#==============================================================================
    def _ddl(self,dict_tubapoints):
        """writes support-information
        """
        for tubapoint in dict_tubapoints:  
            newlines=[]
            character_count=0
    
            newlines=[str("_F(GROUP_NO='" +tubapoint.name +"',")]
            prefix_ddl=["DX","DY","DZ","DRX","DRY","DRZ"]
            for i,x in enumerate(tubapoint.ddl):
                if str(x) != 'x':
                    newlines.append(7*" "+prefix_ddl[i]+"="+str(x)+",")
    
            newlines.append(7*" "+"ANGL_NAUT=(0.0,0.0,0),")
            newlines.append("),")
    
            if len(newlines)>3:   #just checks if there where actually ddls defined
                insert_lines_at_string(self.lines,"#LIAISON_OBLIQUE",newlines)

#==============================================================================            
    def _ddl_create_node_group(self,dict_tubapoints):
                
        newlines=[] 
        newlines.extend([
        "    _F(    NOM='GPOINTS',",
        "         UNION=(",
        ])
        
        text="         "
        character_count=0
        for tubapoint in dict_tubapoints:
            if not tubapoint.ddl == ['x','x','x','x','x','x']:
                character_count+=len(tubapoint.name)+4
                text += "'"+tubapoint.name+"', "
    
                if character_count > 50:
                    newlines.append(text)
                    text="    "
                    character_count=0
        newlines.append(text)

        newlines.extend([
        "    ),",
        "),",
        ])
        
        if newlines>4:
            insert_lines_at_string(self.lines,"#CREA_GROUPE_NOEUD",newlines)

#==============================================================================
    def _stiffness(self,dict_tubapoints):
        '''writes the defined spring properties at all tubapoints to the aster.comm-file'''
       
                                                    

        text=""
        for tubapoint in dict_tubapoints:      
            if not tubapoint.stiffness == [0, 0, 0, 0, 0, 0]:        
                text += "'"+tubapoint.name+"K', "

        if text!="":
            newlines=[
            "_F(",
            "   GROUP_MA=(",
            ]               
            
            newlines.append("       "+text)
            newlines.extend([
            "   ),",
            "   PHENOMENE='MECANIQUE',",
            "   MODELISATION='DIS_TR',",
            "),"
            ])         
        

            insert_lines_at_string(self.lines,"#MODELISATION",newlines)
            newlines=[]
           
      
        for tubapoint in dict_tubapoints: 
  
            if not tubapoint.stiffness == [0, 0, 0, 0, 0, 0]:
                newlines=[
                "_F(",
                "   NOM_GROUP_MA='"+tubapoint.name+"K',",
                "   GROUP_NO='"+tubapoint.name+"',",
                "),",
                ]
      
                insert_lines_at_string(self.lines,"#CREA_POI1",newlines)
                newlines=[]    
    
                print (tubapoint.stiffness)
                [x,y,z,rx,ry,rz]=tubapoint.stiffness
        
                newlines=[
                "_F(",
                "GROUP_MA = '" + tubapoint.name + "K',",
                "REPERE = 'LOCAL',",
                "CARA = 'K_TR_D_N',",
                "VALE = (",
                "         " + str(x) + ",",
                "         " + str(y) + ",",
                "         " + str(z) + ",",
                "         " + str(rx) + ",",
                "         " + str(ry) + "," ,
                "         " + str(rz) + ",),",
                "),",
                ]
        
                insert_lines_at_string(self.lines,"#STIFFNESS_DISCRET",newlines)




#==============================================================================
    def _moment(self,dict_tubapoints):
        for tubapoint in dict_tubapoints: 
            newlines=[]  
 
            for i,moment in enumerate(tubapoint.moment):
                if force != (0,0,0):
                    newlines=[
                        "_F(",
                        "GROUP_NO='" + tubapoint.name + "',",
                        "MX="+str(moment.x)+", MY="+str(moment.y)+", MZ="+str(moment.z),
                        "),"
                        ]                           
                    
                    insert_lines_at_string(self.lines,"#FORCE_NODALE",newlines)
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
                    
                    insert_lines_at_string(self.lines,"#FORCE_NODALE",newlines)
                                   
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
            insert_lines_at_string(self.lines,"#CHAMP_TEMP",newlines)

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

            insert_lines_at_string(self.lines,"#CHMAT_AFFE",newlines)
            insert_lines_at_string(self.lines,"#CHMATH_AFFE",newlines)
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
                    insert_lines_at_string(self.lines,"#DEF_MATERIAU",newlines)

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
                    insert_lines_at_string(self.lines,"#DEF_MATERIAU",newlines)


                    newlines=[
                    "NU_"+material+"=DEFI_FONCTION(NOM_PARA='TEMP',",
                    "              VALE=",
                    "              "+str(F_Mat_Prop[1])+",",
                    "              PROL_DROITE='CONSTANT',   ",
                    "              PROL_GAUCHE='CONSTANT',); ",
                    "",]
                    insert_lines_at_string(self.lines,"#DEF_MATERIAU",newlines)

                    newlines=[
                    "A_"+material+"=DEFI_FONCTION(NOM_PARA='TEMP',",
                    "              VALE=",
                    "              "+str(F_Mat_Prop[3])+",",
                    "              PROL_DROITE='CONSTANT',   ",
                    "              PROL_GAUCHE='CONSTANT',); ",
                    "",]
                    insert_lines_at_string(self.lines,"#DEF_MATERIAU",newlines)


                    newlines=[
                    material + "=DEFI_MATERIAU(    ",
                    "     ELAS_FO=_F(  E= E_"+material+",",              
                    "               NU=   NU_"+material+",",  
                    "               RHO="   + str(F_Mat_Prop[2])+",",      
                    "               ALPHA=   A_"+material+",",    
                    "               TEMP_DEF_ALPHA= 20 ,     ",
                    "           ),",
                    ");",
                    ]
                    insert_lines_at_string(self.lines,"#DEF_MATERIAU",newlines)


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
                if item_tubavector.model == "TUYAU" or item_tubavector.model == "3D" :
                    new_item.append(name)
  
            print("ITem", item)
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
                    insert_lines_at_string(self.lines,"#FORCE_TUYAU",newlines)

#==============================================================================
    def _linear_forces(self,dict_tubavectors):
        for tubavector in dict_tubavectors: 
            newlines=[]  

            for i,force in enumerate(tubavector.linear_force):
                if force != (0,0,0):
                    newlines=[
                        "_F(",
                        "GROUP_MA='" + tubavector.name + "',",
                        "FX="+str(force.x)+", FY="+str(force.y)+", FZ="+str(force.z),
                        "),"
                        ]                           
                    
                    insert_lines_at_string(self.lines,"#FORCE_POUTRE",newlines)

#==============================================================================
    def _section(self,dict_tubavectors):
        newlines=[]
        grouped_attributes=extract_group_attributes_from_list("section","name",dict_tubavectors)

        for item in grouped_attributes:
            #Delete all elements from the List which dont have TUBE as model
            new_item=[]
#------------------------------------------------------------------------------            
            for name in item[1]:
                item_tubavector=([tubavector for tubavector in dict_tubavectors
                                            if tubavector.name == name][0])                                
                if item_tubavector.model == "TUBE" or item_tubavector.model == "TUYAU": 
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
                insert_lines_at_string(self.lines,"#SECTION_TUBE",newlines)    
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
                insert_lines_at_string(self.lines,"#SECTION_POUTRE",newlines)            



            
    
            
            
            
       
#==============================================================================      
         
    def _model(self,dict_tubavectors):      
        newlines=[]
        grouped_attributes=extract_group_attributes_from_list("model","name",dict_tubavectors) 
  
        for item in grouped_attributes:
            if item[0] == "TUBE" or item[0]=="RECTANGULAR":
                newlines=[]
                newlines.extend([
                "    _F(",
                "        NOM='GTUBE_D',",
                "        TYPE_MAILLE = '1D',",
                "        UNION=(",
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


                newlines.append("       ),")
                newlines.append("),")
                insert_lines_at_string(self.lines,"#CREA_GROUPE_MAILLE ",newlines)


                
                newlines=[
                "    _F(",
                "        GROUP_MA='GTUBE_D',",
                "        PHENOMENE='MECANIQUE',",
                "        MODELISATION='POU_D_T',",
                "    ),",
                ]
                
                insert_lines_at_string(self.lines,"#MODELISATION" ,newlines)
                
            if item[0] == "TUYAU":
                self.TUYAU_flag=True
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
                insert_lines_at_string(self.lines,"#CREA_GROUPE_MAILLE ",newlines)


                
                newlines=[
                "    _F(",
                "        GROUP_MA='GTUYAU3M',",
                "        PHENOMENE='MECANIQUE',",
                "        MODELISATION='TUYAU_3M',",
                "    ),",
                ]
                
                insert_lines_at_string(self.lines,"#MODELISATION" ,newlines)                
                
            if item[0] == "3D":  
                pass
                
#==============================================================================             
    def _TShape3D(self,dict_tubavectors):

        for tubavector in dict_tubavectors:
            if tubavector.model=="3D":
                newlines=[
                "_F(",
                "   GROUP_MA=(",
                "  '" + tubavector.name +"', '"+tubavector.name+"StartFace', '"+
                tubavector.name+"IncidentFace', '"+tubavector.name+"EndFace'),",
                "   PHENOMENE='MECANIQUE',",
                "   MODELISATION='3D',",
                "),",
                ]
                
                insert_lines_at_string(self.lines,"#MODELISATION" ,newlines)        
                

                
                # Définition des liaisons 3D-TUBE",
                newlines=("""_F(               
    OPTION='3D_POU',
    GROUP_MA_1 ='"""+str(tubavector.name)+"""StartFace',
    GROUP_NO_2 ='"""+str(tubavector.start_tubapoint.name)+"""',
    ),""").split("\n")
                
                newlines=newlines+("""_F(          
    OPTION='3D_POU',
    GROUP_MA_1 ='"""+str(tubavector.name)+"""IncidentFace',
    GROUP_NO_2 ='"""+str(tubavector.incident_end_tubapoint.name)+"""',
    ),""").split("\n")      
                
                newlines=newlines+("""_F(
    OPTION='3D_POU',
    GROUP_MA_1 ='"""+tubavector.name+"""EndFace',
    GROUP_NO_2 ='"""+tubavector.end_tubapoint.name+"""',
    ),""").split("\n")                  
                
                             
                insert_lines_at_string(self.lines,"#LIAISON_3D_TUBE" ,newlines)

            
#==============================================================================

    def _simulation(self):
        print("STATIQUE_LINEAIRE")
        newlines=("""
RESU=MECA_STATIQUE(
     MODELE=MODMECA,
     CHAM_MATER=CHMATH,
     CARA_ELEM=CARAELEM,
     INST=1,
     EXCIT=(
         _F(   CHARGE=BLOCAGE
          ),
         _F(   CHARGE=POIDS,
          ),
         _F(   CHARGE=CHARG1,
          ),

         #CHARGEMENT
     ),
);

RESU=CALC_CHAMP(reuse =RESU,
     RESULTAT=RESU,
     FORCE=('REAC_NODA','FORC_NODA'),
     CONTRAINTE=('SIEF_ELGA'),
     #CONTRAINTE=('SIEF_ELGA','SIPO_NOEU')""").split("\n")
            
        if self.TUYAU_flag:
            newlines=newlines+("""     CRITERES=('SIEQ_ELNO'),""").split("\n")          
        
        newlines=newlines+(""");
 
IMPR_RESU(FORMAT='MED',RESU=_F(RESULTAT=RESU));            
        """).split("\n")
           
           
        if self.TUYAU_flag:
            newlines=newlines+("""
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
  
IMPR_RESU(FORMAT='MED',RESU=_F(RESULTAT=MAX_VMIS));
        """).split("\n") 
     





##    Table=POST_RELEVE_T(ACTION=(_F(OPERATION='EXTRACTION',
##                              INTITULE='ReacXYZ',
##                              RESULTAT=RESU,
##                              NOM_CHAM='REAC_NODA',
##                              PRECISION=0.0001,
##                              GROUP_NO='GPOINTS',
##                              TOUT_CMP='OUI',),),
##                   TITRE='Principal stress',);




##    IMPR_TABLE(TABLE=Table,
##          FORMAT='TABLEAU',
##          SEPARATEUR=' ,',
##          TITRE='Reac/Force at nodes',);

#MFlex = FORMULE(
#    NOM_PARA=('SMT','SMFY', 'SMFZ', ),
#    VALE=\"\"\"sqrt(SMFY**2 + SMFZ**2 )+SMT**2\"\"\"
#)
#
#
#RES_MPP = CALC_CHAMP(
#    RESULTAT=RESU,
#    CHAM_UTIL=_F(
#        NOM_CHAM='SIPO_NOEU',
#        FORMULE=(MFlex),
#        NUME_CHAM_RESU=2,
#    ),
#);
#
#IMPR_RESU(FORMAT='MED',RESU=_F(RESULTAT=RES_MPP,LIST_INST=listresu,NOM_CHAM_MED='sigflex',));
#      """).split("\n")

        insert_lines_at_string(self.lines, "#CALCULS", newlines)


    def _write_tables(self):
        pass
#==============================================================================
#==============================================================================

def insert_lines_at_string(lines,substring,newlines):
    """In a list of strings, find the substring, and append the newlines before
    that string taking into account the whitespaces before it"""
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


        
    
    
    