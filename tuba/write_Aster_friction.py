# -*- coding: utf-8 -*-
import os

max_friction_loops=5




                                                   
def set_Spring_elements(CodeAster,dict_tubapoints):
    
        text=""
        
        
        for tubapoint in dict_tubapoints:      
            if not tubapoint.friction_coefficient == 0.0:  
                text += "'Friction"+tubapoint.name+"', "

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
        

            insert_lines_at_string(CodeAster.lines,"##MODELISATION",newlines)
            newlines=[]
     
#------------------------------------------------------------------------------
            newlines=[
            "    _F( NOM='GFRICTION',",
            "        UNION=(",
            ]
        
            text="         "
            character_count=0
            for tubapoint in dict_tubapoints:
                if not tubapoint.friction_coefficient == 0:  
                    character_count+=len(tubapoint.name)+4
                    text += "'"+tubapoint.name+"', "
        
                    if character_count > 50:
                        newlines.append(text)
                        text="      "
                        character_count=0
            newlines.append(text)
    
            newlines.extend([
            "        ),",
            "    ),",
            ])
            insert_lines_at_string(CodeAster.lines,"##CREA_GROUPE_NOEUD",newlines)
#------------------------------------------------------------------------------            
            newlines=[
            "    _F( NOM='GFRICTION_f',",
            "        UNION=(",
            ]
        
            text="         "
            character_count=0
            for tubapoint in dict_tubapoints:
                if not tubapoint.friction_coefficient == 0:  
                    character_count+=len(tubapoint.name)+4
                    text += "'"+tubapoint.name+"_f', "
        
                    if character_count > 50:
                        newlines.append(text)
                        text="      "
                        character_count=0
            newlines.append(text)
    
            newlines.extend([
            "        ),",
            "    ),",
            ])
            insert_lines_at_string(CodeAster.lines,"##CREA_GROUPE_NOEUD",newlines)
       
#------------------------------------------------------------------------------
        for tubapoint in dict_tubapoints: 
  
            if not tubapoint.friction_coefficient == 0: 

                newlines=[
                "_F(",
                "GROUP_MA = 'Friction" + tubapoint.name + "',",
                "REPERE = 'GLOBAL',",
                "CARA = 'K_TR_D_L',",
                "VALE = (",
                "         "+tubapoint.name+"_KX[i-1],",
                "         "+tubapoint.name+"_KY[i-1],",
                "         "+tubapoint.name+"_KZ[i-1],",
                "         0,",
                "         0,",
                "         0,),",
                "),"]
                
        
                insert_lines_at_string(CodeAster.lines,"##STIFFNESS_DISCRET",newlines)
                newlines=[]                
                
                newlines=[
                "_F(GROUP_NO='"+ tubapoint.name + "_f',",
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
                      insert_lines_at_string(CodeAster.lines,"##LIAISON_OBLIQUE",newlines)


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

                newlines=[
                tubapoint.name+"_KX=[0]*"+str(max_friction_loops),
                tubapoint.name+"_KY=[0]*"+str(max_friction_loops),
                tubapoint.name+"_KZ=[0]*"+str(max_friction_loops),
]
                insert_lines_at_string(CodeAster.lines,"##VARIABLES",newlines)
                newlines=[] 


                    
#                newlines=['friction_points.append(\''+tubapoint.name+'\')']
#                insert_lines_at_string(CodeAster.lines,"##PYTHON",newlines)
                newlines=[] 
#------------------------------------------------------------------------------
def _Simulation_loop(CodeAster,dict_tubapoints,cmd_script):
        print("FileSystem",os.getcwd())
        newlines=("""
import numpy as np
import os
import math 

                 
my_directory = os.getenv('HOME')   #os.getcwd()
current_directory ='"""+ os.getcwd()+"""'


OUTPUT_FILE='/"""+cmd_script+"""_FrictionResults.output' # Filename of the output file
fileOutput = current_directory + OUTPUT_FILE # Define output file

result_lines=[]
 
""").split("\n")                 
                  


        insert_lines_at_string(CodeAster.lines,"##PYTHON",newlines) 
        newlines=[]
#------------------------------------------------------------------------------
        newlines=[  
                
        "RES=[None]*"+str(max_friction_loops),
        "CAP=[None]*"+str(max_friction_loops),
        "TDEPL=[None]*"+str(max_friction_loops),
        "T_F=[None]*"+str(max_friction_loops),              
        "T_F_f=[None]*"+str(max_friction_loops),  
        "Deform=[None]*"+str(max_friction_loops),
        "Reaction =[None]*"+str(max_friction_loops),
        "Force =[None]*"+str(max_friction_loops),
        "", 
        "result_lines=[]",                        
        "",
        "",
        "for i in range(1,"+str(max_friction_loops)+"):",
        ]
        insert_lines_at_string(CodeAster.lines,"##VARIABLES",newlines)
        newlines=[] 
    
        print("STATIQUE_LINEAIRE")
        newlines=("""
        
              
RES[i]=MECA_STATIQUE(
         MODELE=MODMECA,
         CHAM_MATER=CH_MAT,
         CARA_ELEM=CAP[i],
         INST=1,
         EXCIT=(
                 _F(   CHARGE=BLOCAGE
                 ),
                 _F(   CHARGE=LOAD,
                 ),

         ##CHARGEMENT
     ),
);

RES[i]=CALC_CHAMP(reuse =RES[i],
         RESULTAT=RES[i],
         FORCE=('REAC_NODA','FORC_NODA'),
         );

TDEPL[i]=POST_RELEVE_T(ACTION=(_F(OPERATION='EXTRACTION',
                          INTITULE='ReacXYZ',
                          RESULTAT=RES[i],
                          NOM_CHAM='DEPL',
                          PRECISION=0.0001,
                          GROUP_NO='GFRICTION',
                          TOUT_CMP='OUI',),),
               TITRE='Deformation',);
Deform[i]=TDEPL[i].EXTR_TABLE(); 
    	
#Reaction forces in the helpernode --> is the resulting friction force
T_F_f[i]=POST_RELEVE_T(ACTION=(_F(OPERATION='EXTRACTION',
                          INTITULE='ReacXYZ',
                          RESULTAT=RES[i],
                          NOM_CHAM='FORC_NODA',
                          PRECISION=0.0001,
                          GROUP_NO='GFRICTION_f',
                          TOUT_CMP='OUI',),),
               TITRE='Forces',);      
Reaction[i]=T_F_f[i].EXTR_TABLE();


        
T_F[i]=POST_RELEVE_T(ACTION=(_F(OPERATION='EXTRACTION',
                          INTITULE='ReacXYZ',
                          RESULTAT=RES[i],
                          NOM_CHAM='REAC_NODA',
                          PRECISION=0.0001,
                          GROUP_NO='GFRICTION',
                          TOUT_CMP='OUI',),),
               TITRE='Forces',);      
Force[i]=T_F[i].EXTR_TABLE();
        

#get deformation
#get delta_deformation last iteration
#if changed less than 1%  -- stop iteration

#update new stiffness  --  kx=friction_coefficient*reactionforce/deformation
#--------------------------------------------------------------------------------------
""").split("\n")  
    
    
        newlines=newlines+("""
result_lines.append("--------------Iteration "+str(i)+"--------------")
result_lines.append("---------------------------------------")
""").split("\n")  
        
        g=0
        for tubapoint in dict_tubapoints:
             if not tubapoint.friction_coefficient == 0: 
 
                 newlines=newlines+("""           
"""+tubapoint.name+"""sum_deform=math.sqrt(
Deform[i].values()['DX']["""+str(g)+"""]**2+
Deform[i].values()['DY']["""+str(g)+"""]**2+
Deform[i].values()['DZ']["""+str(g)+"""]**2)

"""+tubapoint.name+"""sum_reaction=math.sqrt(
Force[i].values()['DX']["""+str(g)+"""]**2+
Force[i].values()['DY']["""+str(g)+"""]**2+                                           
Force[i].values()['DZ']["""+str(g)+"""]**2)

"""+tubapoint.name+"""K_FRICTION_force="""+str(tubapoint.friction_coefficient)+"*"+tubapoint.name+"""sum_reaction

"""+tubapoint.name+"""_KX[i]="""+tubapoint.name+"""K_FRICTION_force/"""+tubapoint.name+"""sum_deform                           
"""+tubapoint.name+"""_KY[i]="""+tubapoint.name+"""K_FRICTION_force/"""+tubapoint.name+"""sum_deform
"""+tubapoint.name+"""_KZ[i]="""+tubapoint.name+"""K_FRICTION_force/"""+tubapoint.name+"""sum_deform
#if not Deform[i].values()['DZ']["""+str(g)+"""]==0:
#    """+tubapoint.name+"""_KZ[i]="""+tubapoint.name+"""K_FRICTION_force*math.sqrt("""+tubapoint.name+"""sum_deform**2-Deform[i].values()['DX']["""+str(g)+"""]**2)

                                                          
""").split("\n")  
                 

                 newlines=newlines+(""" 
result_lines.append("             TUBAPOINT """+tubapoint.name+"""\")
result_lines.append("  ")  
result_lines.append("Friction Force at Point:"+ str("""+tubapoint.name+"""K_FRICTION_force))               
result_lines.append("Total Deformation at Point:"+ str("""+tubapoint.name+"""sum_deform))
result_lines.append("DX: "+str(round(Deform[i].values()['DX']["""+str(g)+"""],4))+", "+
                            "DY: "+str(round(Deform[i].values()['DY']["""+str(g)+"""],4))+", "+
                            "DZ: "+str(round(Deform[i].values()['DZ']["""+str(g)+"""],4)))                                  
result_lines.append("  ")
result_lines.append("Total ReactionForce at Point:"+ str("""+tubapoint.name+"""sum_reaction))
result_lines.append("DX: "+str(round(Reaction[i].values()['DX']["""+str(g)+"""],4))+", "+
                            "DY: "+str(round(Reaction[i].values()['DY']["""+str(g)+"""],4))+", "+
                            "DZ: "+str(round(Reaction[i].values()['DZ']["""+str(g)+"""],4)))   
result_lines.append("  ")
result_lines.append("Force at Point:")
result_lines.append("DX: "+str(round(Force[i].values()['DX']["""+str(g)+"""],4))+", "+
                            "DY: "+str(round(Force[i].values()['DY']["""+str(g)+"""],4))+", "+
                            "DZ: "+str(round(Force[i].values()['DZ']["""+str(g)+"""],4)))   
result_lines.append("  ")

result_lines.append("New Friction Stiffness") 
result_lines.append("X: "+str(round("""+tubapoint.name+"""_KX[i],4))+", "+
                    "Y: "+str(round("""+tubapoint.name+"""_KY[i],4))+", "+
                    "Z: "+str(round("""+tubapoint.name+"""_KZ[i],4))                  
                    )
result_lines.append("---------------------------------------")
last=i
                   """).split("\n")  
                 g=g+1 
        insert_lines_at_string(CodeAster.lines, "##FRICTION_LOOP", newlines)
        newlines=[]    
        
        
        
        

        newlines=newlines+(""" 
try:
   f = open(fileOutput, 'w')    #'a' opens the file for appending , 'w' opens file and erases
   f.write("""+'\'\\n\''+""".join(result_lines))
   f.close()
except:
   print("Error")


RESU=MECA_STATIQUE(
         MODELE=MODMECA,
         CHAM_MATER=CH_MAT,
         CARA_ELEM=CAP[last],
         INST=1,
         EXCIT=(
                 _F(   CHARGE=BLOCAGE
                 ),
                 _F(   CHARGE=LOAD,
                 ),

         ##CHARGEMENT
     ),
);


""").split("\n")                     

        insert_lines_at_string(CodeAster.lines, "##LOOP_OUTPUT", newlines)
        newlines=[]    
             
             

    
    


def insert_lines_at_string(lines,substring,newlines):
    """In a list of strings, find the substring, and append the newlines before
    that string taking into account the whitespaces before it"""
    for line in lines:
        if substring in line:
            index=lines.index(line)
            whitespace_count=len(line) - len(line.lstrip())


    for line in reversed(newlines):
        lines.insert(index,whitespace_count*" "+line)