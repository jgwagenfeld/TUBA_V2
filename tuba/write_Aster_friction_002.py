# -*- coding: utf-8 -*-
import os

max_friction_loops=15

def set_Spring_elements(CodeAster,dict_tubapoints):

        print("FileSystem",os.getcwd())
        newlines=("""
import numpy as np
import os
import math 

friction_points=[]                  
my_directory = os.getenv('HOME')   #os.getcwd()
current_directory ='"""+ os.getcwd()+"""'


OUTPUT_FILE='/Friction.output' # Filename of the output file
fileOutput = current_directory + OUTPUT_FILE # Define output file

result_lines=[]

print("Fileoutput",fileOutput)
""").split("\n")                 
                  


        insert_lines_at_string(CodeAster.lines,"##PYTHON",newlines) 
        newlines=[]
                                                   

        text=""
        for tubapoint in dict_tubapoints:      
            if not tubapoint.friction_coefficient == 0:  
                CodeAster.FRICTION_flag=True
                text += "'"+tubapoint.name+"K_FRICTION', "

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
     
        if CodeAster.FRICTION_flag==True:
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
        
        if len(newlines)>4:
            insert_lines_at_string(CodeAster.lines,"##CREA_GROUPE_NOEUD",newlines)
            newlines=[]

        for tubapoint in dict_tubapoints: 
  
            if not tubapoint.friction_coefficient == 0: 
                newlines=[
                "_F(NOM_GROUP_MA='"+tubapoint.name+"K_FRICTION',", 
                "   GROUP_NO='"+tubapoint.name+"',",
                "),",
                ]
      
                insert_lines_at_string(CodeAster.lines,"##CREA_POI1",newlines)
                newlines=[]    
            
                newlines=[
                "_F(",
                "GROUP_MA = '" + tubapoint.name + "K_FRICTION',",
                "REPERE = 'LOCAL',",
                "CARA = 'K_TR_D_N',",
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
                


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

                newlines=[
                tubapoint.name+"_KX=[0]*"+str(max_friction_loops),
                tubapoint.name+"_KY=[0]*"+str(max_friction_loops),
                tubapoint.name+"_KZ=[0]*"+str(max_friction_loops),
]
                insert_lines_at_string(CodeAster.lines,"##VARIABLES",newlines)
                newlines=[] 


                    
                newlines=['friction_points.append(\''+tubapoint.name+'\')']
                insert_lines_at_string(CodeAster.lines,"##PYTHON",newlines)
                newlines=[] 


def _Simulation_loop(CodeAster,dict_tubapoints):
        newlines=[  
                
        "RESU=[None]*"+str(max_friction_loops),
        "CAP=[None]*"+str(max_friction_loops),
        "TAB1=[None]*"+str(max_friction_loops),
        "TAB2=[None]*"+str(max_friction_loops),
        "Deform=[None]*"+str(max_friction_loops),
        "Reaction =[None]*"+str(max_friction_loops),
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
        
              
RESU[i]=MECA_STATIQUE(
         MODELE=MODMECA,
         CHAM_MATER=CHMATH,
         CARA_ELEM=CAP[i],
         INST=1,
         EXCIT=(
                 _F(   CHARGE=BLOCAGE
                 ),
                 _F(   CHARGE=CHARG1,
                 ),

         ##CHARGEMENT
     ),
);

RESU[i]=CALC_CHAMP(reuse =RESU[i],
         RESULTAT=RESU[i],
         FORCE=('REAC_NODA','FORC_NODA'),
         CONTRAINTE=('SIGM_ELGA','SIGM_ELNO'),
         #CONTRAINTE=('SIEF_ELGA','SIPO_NOEU')
         );





TAB1[i]=POST_RELEVE_T(ACTION=(_F(OPERATION='EXTRACTION',
                          INTITULE='ReacXYZ',
                          RESULTAT=RESU[i],
                          NOM_CHAM='DEPL',
                          PRECISION=0.0001,
                          GROUP_NO='GFRICTION',
                          TOUT_CMP='OUI',),),
               TITRE='Deformation',);
Deform[i]=TAB1[i].EXTR_TABLE(); 
    	

TAB2[i]=POST_RELEVE_T(ACTION=(_F(OPERATION='EXTRACTION',
                          INTITULE='ReacXYZ',
                          RESULTAT=RESU[i],
                          NOM_CHAM='REAC_NODA',
                          PRECISION=0.0001,
                          GROUP_NO='GFRICTION',
                          TOUT_CMP='OUI',),),
               TITRE='Forces',);      
Reaction[i]=TAB2[i].EXTR_TABLE();



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
Reaction[i].values()['DX']["""+str(g)+"""]**2+
Reaction[i].values()['DY']["""+str(g)+"""]**2+                                           
Reaction[i].values()['DZ']["""+str(g)+"""]**2)

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
result_lines.append("New Friction Stiffness") 
result_lines.append("X: "+str(round("""+tubapoint.name+"""_KX[i],4))+", "+
                    "Y: "+str(round("""+tubapoint.name+"""_KY[i],4))+", "+
                    "Z: "+str(round("""+tubapoint.name+"""_KZ[i],4))                  
                    )
result_lines.append("---------------------------------------")
last=i
                   """).split("\n")  
                 g=g+1 
        insert_lines_at_string(CodeAster.lines, "##SIMULATION", newlines)
        newlines=[]    
        
        
        
        

        newlines=newlines+(""" 
try:
   f = open(fileOutput, 'w')    #'a' opens the file for appending , 'w' opens file and erases
   f.write("""+'\'\\n\''+""".join(result_lines))
   f.close()
except:
   print("Error")



RES=RESU[last]
IMPR_RESU(FORMAT='MED',RESU=_F(RESULTAT=RES));

""").split("\n")                     

        insert_lines_at_string(CodeAster.lines, "##OUTPUT", newlines)
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