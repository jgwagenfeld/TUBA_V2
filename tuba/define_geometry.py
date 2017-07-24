#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 22:05:19 2016
"""
#import global_vars as glob
#from global_functions import *
import external.euclid as eu
import logging
import math

import tuba_vars_and_funcs as tub

#==============================================================================
#==============================================================================
class TubaPoint:
    """Containes all information present at a POINT in the piping/rod network

    It is important to  note that each tubapoint inside a piping is always an
    attribute of two vectors, one time as start_tubapoint, one time as end_tubapoint.

    The only exception are start and endpoints of a piping system. For each point it is possibe 
    to check wether it is a element start or an end at the current time.
    """

    def __init__(self, x, y, z, name="", nocount=False):
        self.name = name
        self.pos = eu.Point3(x, y, z)              # Position of the Point
        self.ddl = ['x', 'x', 'x', 'x', 'x', 'x']  # Degree of Freedom/Deflection
        self.ddl_reference = "global"      
        self.friction_coefficient=0.0        
        self.stiffness = [0.0, 0.0, 0.0, 0.0,0.0, 0.0]  # Stiffness-Matrix of the Point
        self.stiffness_reference = "global"   
        self.mass = 0.0                        # Discret Mass at the Point
        self.moment = []           # Sum of Moments applied at the Point
        self.force = []                      # List of Forces applied at the Point
        self.vd1x=tub.vd1x0          # Last noncolinear vector in the piping                
        
        if self.is_element_start():        
            self.vd2x=tub.vd2x0           # Direction of the following vector

        self.vd1x.normalized()
        self.vd2x.normalized()

        if nocount:
            pass
        else:
            tub.tubapoint_counter+=1
            tub.current_tubapoint=self
        logging.debug("Created Tubapoint: "+self.name)
        tub.dict_tubapoints.append(self)  #Write the object instance into the global point list
#------------------------------------------------------------------------------
    def is_element_start(self):
        '''checks if the given tubapoint is a start_tubapoint and as well end_tubapoint of a vector.
        If false, this means that it's the beginning of the piping'''

        same_names=[tubavectors for tubavectors in tub.dict_tubavectors
                    if tubavectors.end_tubapoint.name == self.name]  #Points with the same name
        print ("is element start",self.name, same_names)            
        if same_names==[]:
            return True
            logging.debug(str(self.name)+" is a start point as there is no Vector-end_tubapoint with the same name")
        else:
            return False
            logging.debug(str(self.name)+" is not a Pipingstart as it's as well end_tubapoint of "+str(same_names[0].name))
#------------------------------------------------------------------------------
    def is_element_end(self):
        '''checks if the given tubapoint is a end_tubapoint and as well start_tubapoint of a vector.
        If false, this means that it's the end of the piping'''

        same_names=[tubavectors for tubavectors in tub.dict_tubavectors
                    if tubavectors.start_tubapoint.name == self.name]  #Points with the same name
        print ("is element end",self.name, same_names)             
        if same_names==[]:
            return True
            logging.debug(str(self.name)+" is a start point as there is no Vector-end_tubapoint with the same name")
        else:
            return False
            logging.debug(str(self.name)+" is not a Pipingstart as it's as well end_tubapoint of "+str(same_names[0].name))
#------------------------------------------------------------------------------
    def is_incident_end(self):
        '''checks if the given tubapoint is a icident_end_tubapoint and as well start_tubapoint of a vector.
        '''

        for tubavectors  in tub.dict_tubavectors:
            if tubavectors.__class__.__name__ == "TubaTShape3D":
                if tubavectors.incident_end_tubapoint.name == self.name:
                    return True

#------------------------------------------------------------------------------           
    def get_last_vector(self):
        '''Finds the vector, where this tubapoint acts as an endpoint'''

        for tubavector in tub.dict_tubavectors:
             if tubavector.end_tubapoint.name == self.name:
                 return tubavector
             if tubavector.__class__.__name__ == "TubaTShape3D":
                 if tubavector.incident_end_tubapoint.name == self.name:
                     return tubavector

#------------------------------------------------------------------------------
    def get_next_vector(self):
        '''Finds the vector, where this tubapoint acts as an endpoint'''

        for tubavector in tub.dict_tubavectors:
             if tubavector.start_tubapoint.name == self.name:
                 return tubavector
 
          
            
#==============================================================================
#==============================================================================
class TubaVector:
    """TubVector is the Class to contain all information present on a LINE ELEMENT in the piping/rod network """

    def __init__(self,start_tubapoint,end_tubapoint,vector,name_vector):
        self.name = name_vector
        self.start_tubapoint = start_tubapoint
        self.end_tubapoint = end_tubapoint
        self.vector = vector
        self.vd1x=start_tubapoint.vd1x
        self.section = tub.current_section
        self.material = tub.current_material
        self.temperature = tub.current_temperature
        self.pressure = tub.current_pressure
        self.linear_force = []
        self.model = tub.current_model
        self.sif = 1
        self.cflex = 1

        tub.tubavector_counter += 1
        tub.dict_tubavectors.append(self)
        self._update_attached_tubapoints()
        self._update_global_forces()
    
    def _update_attached_tubapoints(self):
        
#if the new vector is not colinear with the last one, both span a new reference plane and Vd1x can be changed
#   new_vect.start_tubapoint.Vd1x=
        if len(tub.dict_tubavectors)>1:
            if is_colinear(self.vector,tub.dict_tubavectors[-2].vector)==False:
                print("isColinear",self.name)
                self.start_tubapoint.vd1x=tub.dict_tubavectors[-2].vector.normalized()
                self.vd1x=tub.dict_tubavectors[-2].vector.normalized()
            else:
                self.vd1x=tub.dict_tubavectors[-2].vd1x
# As start_tubapoint.Vd2x will always be overriden with the new vector, the case 
# where vd1x and the new vector vd2x are colinear ust be take care of. If not,
# m no referance plane would be spanned by vd1x and vd2x anymore
        else:
            if is_colinear(self.vector, self.start_tubapoint.vd1x):
                self.start_tubapoint.vd1x=self.start_tubapoint.vd2x.normalized()
                self.vd1x=self.start_tubapoint.vd1x

        self.start_tubapoint.vd2x=self.vector.normalized()
        self.end_tubapoint.vd2x=self.vector.normalized()
        
    def _update_global_forces(self):        

# Fluid Weight in Pipe
#--------------------------------------------
        if self.model in ["TUBE","TUYAU"]:
            if tub.current_rho_fluid:
                density_fluid=tub.current_rho_fluid
                outer_radius=self.section[0]
                wall_thickness=self.section[1]
                force_grav_fluid= math.pi*(outer_radius-wall_thickness)**2*density_fluid*tub.G
                print("Fluid_Weight N/mm", force_grav_fluid)
                self.linear_force.append(eu.Vector3(0,0,-force_grav_fluid))
                print("Fluid_Weight N/mm", eu.Vector3(0,0,-force_grav_fluid))

# Insulation of the Pipe
#--------------------------------------------
        if self.model in ["TUBE","TUYAU"]:
            if tub.current_insulation:            
                [insulation_thickness, insulation_density]=tub.current_insulation
                outer_radius=self.section[0]
    
    
                force_grav_insulation= math.pi*((outer_radius+insulation_thickness)**2-outer_radius**2)*insulation_density*9.81
                print("Insulation_Weight N/mm", force_grav_insulation)
                self.linear_force.append(eu.Vector3(0,0,-force_grav_insulation))
 
# Wind Load
#--------------------------------------------        
        
# ==============================================================================
# ==============================================================================
class TubaBent(TubaVector):
    def __init__(self,start_tubapoint,end_tubapoint,center_tubapoint,
                 bending_radius,rotation_axis,angle_bent,name_vect):
        self.bending_radius=bending_radius
        self.center_tubapoint=center_tubapoint
        self.rotation_axis=rotation_axis    #Normal vector on plane containing CenterPoint, Start and end_tubapoint
        self.angle_bent=angle_bent
        TubaVector.__init__(self,start_tubapoint,end_tubapoint,
                                start_tubapoint.vd2x, name_vect)


        print("TUBABENT",self.model)
#        if self.model=='TUBE':
#            self.model="TUBE_BENT"
    #Overrides the function of TubaVector

        self._update_attached_tubapoints()
        self._calculate_SIF_and_Cflex()
        
    
    def _calculate_SIF_and_Cflex(self):
        """calculate Stress intensification and flexibility factor"""
        thickness=self.section[1]
        outerRadius=self.section[0]        

        print(thickness)
        print(outerRadius)
        print(self.bending_radius)        
        h=(thickness*self.bending_radius)/math.pow((outerRadius-thickness/2),2)
        sif=0.9/(h**0.666666)
        cflex=1.65/h
        if sif < 1:   
            sif = 1           
        if cflex < 1:  
            cflex = 1
                    
        self.sif=sif
        self.cflex=cflex
            
        pass

    def _update_attached_tubapoints(self):
        logging.debug("Update attached tubapoints"+ str(self.rotation_axis)
                            +",  "+str(self.angle_bent/math.pi*180))
        
        self.end_tubapoint.vd2x=self.start_tubapoint.vd2x.rotate_around(
                                        self.rotation_axis, self.angle_bent)
                                                       
        self.end_tubapoint.vd1x=self.start_tubapoint.vd2x
                                                                    

#==============================================================================
#==============================================================================
class TubaTShape3D(TubaVector):
    def __init__(self,start_tubapoint,end_tubapoint,incident_tubapoint,
                 incident_vector,incident_section,name_vect):
        self.incident_end_tubapoint=incident_tubapoint
        self.incident_vector=incident_vector
        self.incident_section=incident_section
        TubaVector.__init__(self,start_tubapoint,end_tubapoint,
                                end_tubapoint.pos-start_tubapoint.pos, name_vect)
        self.model="VOLUME"               
                      
        self._update_attached_tubapoints()
        
        print("TubaTshap-Points- Start: ",start_tubapoint.pos)
        print("End",end_tubapoint.pos)
        print("Incident",self.incident_end_tubapoint.pos)
    def _update_attached_tubapoints(self):
        logging.debug("Update attached tubapoints")
                
        self.incident_end_tubapoint.vd2x=self.incident_vector.normalized() 
        self.incident_end_tubapoint.vd1x=self.start_tubapoint.vd2x        
        self.end_tubapoint.vd2x=self.start_tubapoint.vd2x
        self.end_tubapoint.vd1x=self.start_tubapoint.vd1x                            

#==============================================================================
#==============================================================================
def P(x,y="",z="",name_point=""):
    '''Creates a tubapoint with the coordinates P(x,y,z,name)'''

    if not name_point:
        name_point="P"+str(tub.tubapoint_counter)

    if isinstance(x,eu.Point3):
        point=x
        x=point.x
        y=point.y
        z=point.z
#------------------------------------------------------------------------------
    name_point=TubaPoint(x,y,z,name=name_point)
#------------------------------------------------------------------------------

#==============================================================================
#==============================================================================
def Prel(ref_point,x,y,z,name_point=""):
    '''Creates a relative tubapoint using a reference + displacement vector. No connecting Tubavector is created.'''

    if not name_point:
        name_point="P"+str(tub.point_counter)
    #Finds the tubapoint with the attribute  .Name== ref_point and returns it
    ref_point=([point for point in tub.dict_tubapoints if point.name == "a"][0])

    x=ref_point.pos.x+x
    y=ref_point.pos.y+y
    z=ref_point.pos.z+z
#------------------------------------------------------------------------------
    name_point=TubaPoint(x,y,z,name_point) #Create a Point object
#------------------------------------------------------------------------------
    logging.info("Create Prel: " + name_point)
#==============================================================================
#==============================================================================
def gotoP(name_point):
    """The function allowes to changes the current Tubapoint used for the next vector creation"""

    logging.debug("GotoP")
    tub.current_tubapoint=([tubapoint for tubapoint in tub.dict_tubapoints
                                        if tubapoint.name == name_point][0])
                                            
    if tub.current_tubapoint.is_incident_end():
       
        last_vector=tub.current_tubapoint.get_last_vector()
        tub.current_section=last_vector.incident_section                                        
                                            
    logging.info("gotoP: " + name_point)
#==============================================================================
#==============================================================================
def V(x,y,z,name_point=""):
    """Creates a vector and an end point starting from the specified tubapoint. If no tubapoint-name is specified, the vector will be created starting from the last created point. The direction is defined by the
    user input x,y,z.
    """

    logging.debug("Processing V: "+name_point)
    print(name_point)
    if not name_point:
        name_point="P"+str(tub.tubapoint_counter)
    print("name", name_point)
    
    #Get start point of vector
    vector=eu.Vector3(x,y,z)    
    start_tubapoint=tub.current_tubapoint
    end_pos=start_tubapoint.pos+vector
    
    #Create the new tubapoint-Object "end_tubapoint" for the Vector
#------------------------------------------------------------------------------
    name_point=TubaPoint(end_pos.x,end_pos.y,end_pos.z,name_point)
#------------------------------------------------------------------------------ 
    end_tubapoint=tub.current_tubapoint
                  
    name_vector="V"+str(tub.tubavector_counter)
    #Create the TubaVector object containing all the informations of the line element (Material, Temperature, Pressure etc)
#------------------------------------------------------------------------------
    name_vector=TubaVector(start_tubapoint, end_tubapoint, vector, name_vector)
#------------------------------------------------------------------------------ 
    logging.debug("start_point connected?: "+str(start_tubapoint.vd2x))
    
#==============================================================================
#==============================================================================
def Vc(length,name_point=""):
    """Creates a colinear vector in direction of the last vector.
    (The information for the colinear vector is contained in current_tubapoint.Vd2x)"""

    x=length*tub.current_tubapoint.vd2x.x
    y=length*tub.current_tubapoint.vd2x.y
    z=length*tub.current_tubapoint.vd2x.z
    V(x,y,z,name_point)
    
#==============================================================================
def Vp(endpoint_name, startpoint_name=""):
    """Creates a vector from start_tubapoint to end_tubapoint. If no start_tubapoint is specified, the 
    current_tubapoint is used as startpoint
    """
    if not startpoint_name:
        start_tubapoint=tub.current_tubapoint
    else:   
        start_tubapoint=([tubapoint for tubapoint in tub.dict_tubapoints
                                            if tubapoint.name == startpoint_name][0])
    
    end_tubapoint=([tubapoint for tubapoint in tub.dict_tubapoints
                                            if tubapoint.name == endpoint_name][0])


    vector=end_tubapoint.pos-start_tubapoint.pos
    name_vector="V"+str(tub.tubavector_counter)

    name_vector=TubaVector(start_tubapoint, end_tubapoint, vector, name_vector)    
    

#==============================================================================
#==============================================================================
def Bent(bending_radius,arg1="",arg2="",arg3="intersect",name=""):
    """There are 3 general ways to create a pipe bent:
    

#.  Bent(bending_radius,arg1=Vector3): \n
    arg1 as a vector defines the new direction after the bent
    With this function, it's not possible to create 180°-bents as the bending plane
    would not be defined. A workaround would be to define 2 consecutive 90°-bents \n
    
#.  Bent(bending_radius,arg1=ang_Bent,arg2=ang_Orient): \n
    With the input arg1=bent angle and arg2=orientation angle (defined as a dihedral angle),
    the new direction after the bent can be calculated. \n

#.  Give 2 absolut vectors and make bent in between -- still not implemented


arg3 defines around which point the bent will be created.
For "add" the start_tubapoint of the Bent will be the end_tubapoint of the last vector.\n
For "intersect" the last vector will be changed. Its end_tubapoint will be defined as
intersection point of the current and new vector of the piping

    """

   #TO DO: when intersection problem arises (no vector before bent to move old end_tubapoint)--> switch automatically to add and bring a warning

    if arg3=="intersect":
        tub.current_tubapoint.pos=tub.current_tubapoint.pos - \
                                     tub.current_tubapoint.vd2x*bending_radius
        start_tubapoint=tub.current_tubapoint
    elif arg3=="add":
# The end_tubapoint of the last vector is as well the start_tubapoint of the bent.
# The intersection point in x=bentradius is created

        start_tubapoint=tub.current_tubapoint
    else:
        logging.ERROR("Only \"intersect\" or \"add\" are allowed as input")

    print(start_tubapoint.__dict__)
    logging.debug("bending_radius ="+str(bending_radius)+ "  Mode: "+str(arg3))
    logging.debug("currentPoint: "+str(tub.current_tubapoint.pos))
    logging.debug("start_tubapoint.Pos: "+str(start_tubapoint.pos))
#    logging.debug("Intersectpoint: "+str(intersectpoint))


    if arg1=="" and arg2=="":  #1. version of the bentfunction Bent(bending_radius)
        pass

    elif  arg1!="" and arg2=="": #2. version of bentfunction Bent(bending_radius,arg1=Vector3)
        new_direction=eu.Vector3(0, 0, 0) + arg1
        bent_dot=start_tubapoint.vd2x.dot(new_direction.normalized())
        logging.debug("bent_dot: "+str(bent_dot))
        angle_bent=math.acos(bent_dot)


    elif arg1!="" and arg2!="":  #3. version of the bentfunction  Bent(bending_radius,arg1=ang_Bent,arg2=ang_Orient)
        angle_bent=arg1*math.pi/180
        angle_orient=arg2*math.pi/180
        new_direction=dihedral_vector(start_tubapoint.vd1x,
                                  start_tubapoint.vd2x,angle_bent,angle_orient)


    logging.debug("Bent-Vector"+str(new_direction))
    
    #In Case of angle_bent=180degree the function would have problems to construct the arc. Therefore, its split in 2x90degree
    if angle_bent==math.pi :
        print("Spezial case angle=180")
        Bent(bending_radius,angle_bent/2*180/math.pi,angle_orient*180/math.pi,arg3,name)
        Bent(bending_radius,angle_bent/2*180/math.pi,angle_orient*180/math.pi,arg3,name)
    else:
           #The second version is the standard version. Version1 and Version3 are porcessed to be  handeled in Version2
        rotation_axis=start_tubapoint.vd2x.cross(new_direction)    #normal vector of bent plane


        logging.debug("new_direction "+str(new_direction))

        vector_start_center=rotation_axis.cross(start_tubapoint.vd2x).normalized()    #from start_tubapoint go to direction centerpoint
        logging.debug("vector_start_center"+str(vector_start_center))
        center_pos=start_tubapoint.pos+vector_start_center*bending_radius
     
        name_center_tubapoint="P"+str(tub.tubapoint_counter-1)+"_"+str(tub.tubapoint_counter)+"_center"

        #------------------------------------------------------------------------------
        name_center_tubapoint=TubaPoint(center_pos.x,center_pos.y,center_pos.z,name=name_center_tubapoint,nocount=True)
        #------------------------------------------------------------------------------

        vector_center_end=-vector_start_center.rotate_around(rotation_axis,angle_bent).normalized()

        end_pos=center_pos+vector_center_end*bending_radius


        
        if name=="":
            name_end_tubapoint="P"+str(tub.tubapoint_counter)

        else:
            name_end_tubapoint = name
     
        print(bending_radius)
        #------------------------------------------------------------------------------
        name_end_tubapoint = TubaPoint(end_pos.x,end_pos.y,end_pos.z,
                                     name=name_end_tubapoint)
        #------------------------------------------------------------------------------

        #Create the BendObject and add it to the tub.dic_Vectors list  with (Tubastart_tubapoint,Tubaend_tubapoint,TubaCenterPoint)
        #TubaBent(TubaVector): __init__(self,start_tubapoint,end_tubapoint,CenterPoint,bending_radius,VdN,name_vect):
        name_vect = "V_Bent"+str(tub.tubavector_counter)
     
        #------------------------------------------------------------------------------
        name_vect = TubaBent(start_tubapoint,name_end_tubapoint,name_center_tubapoint
                           ,bending_radius,rotation_axis,angle_bent, name_vect)
                
        #------------------------------------------------------------------------------

        logging.debug("===================================")
        logging.debug("                                   ")
        logging.debug("           tubabent                ")
        logging.debug("Start_Tubapoint "+str(name_vect.start_tubapoint.name))
        logging.debug("End_Tubapoint "+str(name_vect.end_tubapoint.name))
        logging.debug("bending_radius "+str(name_vect.bending_radius))
        logging.debug("rotation_axis "+str(name_vect.rotation_axis))
        logging.debug("angle_bent "+str(name_vect.angle_bent*180/math.pi))
        logging.debug("                                   ")
        logging.debug("start_tubapoint.Vd2x "+str(name_vect.start_tubapoint.vd2x))
        logging.debug("end_tubapoint.Vd2x "+str(name_vect.end_tubapoint.vd2x))
        logging.debug("                                   ")
        logging.debug("Tubabent:  "+str(name_vect.__dict__))
        logging.debug("===================================")
        
#==============================================================================
#==============================================================================        
def TShape3D(incident_radius,incident_thickness,angle_orient,
             name_incident_end="",name_main_end="",             
             incident_halflength=0,main_halflength=0,
             arg="intersect"):
    """Creates a TShape Object. The Main Section continues with the 
    before defines Cross-Section. The branche is defined by the user-arguments
    """
           
    if arg == "intersect":

        tub.current_tubapoint.pos = tub.current_tubapoint.pos - \
                                     tub.current_tubapoint.vd2x*main_halflength
        start_tubapoint = tub.current_tubapoint
        print("CurrentPoint",tub.current_tubapoint.vd2x*main_halflength)      
    elif arg == "add":
# The end_tubapoint of the last vector is as well the start_tubapoint of the bent.
# The intersection point in x=bentradius is created

        start_tubapoint=tub.current_tubapoint

        
    else:
        logging.ERROR("Only \"intersect\" or \"add\" are allowed as input")           


    if incident_halflength == 0: incident_halflength=4*incident_radius   
    if main_halflength == 0: main_halflength=4*tub.current_section[0]   #current_section[0]=Radius Main

    center_pos = tub.current_tubapoint.pos + \
                                     tub.current_tubapoint.vd2x*main_halflength 
    print("ceter_pos", center_pos)                                 
    main_end_pos = tub.current_tubapoint.pos + \
                                     tub.current_tubapoint.vd2x*2*main_halflength

    print("main_pos", main_end_pos) 

    angle_orient = angle_orient*math.pi/180
    new_direction = dihedral_vector(start_tubapoint.vd1x,
                                start_tubapoint.vd2x,90*math.pi/180,angle_orient)
                                
    vector_center_incidentend = new_direction*incident_halflength 
                              
    incident_end_pos = center_pos+vector_center_incidentend
    print("Incident_end_pos",incident_end_pos)
    
    
     
    if not name_incident_end:                       
        name_incident_end="P"+str(tub.tubapoint_counter)
#------------------------------------------------------------------------------
    name_incident_end = TubaPoint(incident_end_pos.x,incident_end_pos.y,incident_end_pos.z,
                            name=name_incident_end)
    incident_end_tubapoint = name_incident_end                       
#------------------------------------------------------------------------------     

    if not name_main_end:
        name_main_end = "P"+str(tub.tubapoint_counter)  
#------------------------------------------------------------------------------
    name_main_end = TubaPoint(main_end_pos.x,main_end_pos.y,main_end_pos.z,
                            name=name_main_end)
    main_end_tubapoint=name_main_end
#------------------------------------------------------------------------------


    incident_section = [incident_radius,incident_thickness]
    
    name = "TShape"    
#------------------------------------------------------------------------------
    TubaTShape3D(start_tubapoint,main_end_tubapoint,incident_end_tubapoint,
                 vector_center_incidentend,incident_section,name)
#------------------------------------------------------------------------------


#==============================================================================
def dihedral_vector(vd1x,vd2x,thetad3x,thetad2x):
    '''calculates the dihedral vector. For more information check
    https://sites.google.com/site/pasceque/francais/b---logiciels-developpes/tuba/6-theorie/angles-dihedriques'''

    vd1x = vd1x.normalized()
    vd2x = vd2x.normalized()
    vd3x = vd2x.cross(vd1x)
    print(vd1x.magnitude)

    v_firstrotation = vd2x.rotate_around(vd3x,thetad3x)
    v_secondrotation = v_firstrotation.rotate_around(vd2x,thetad2x)

    v_final = v_secondrotation
    return v_final
#==============================================================================
def is_colinear(vector1,vector2):
    '''checks if both vector are colinear (cross-product==0) '''
    if vector1.cross(vector2).__abs__() == 0:
        logging.debug(str(vector1)+" and "+str(vector2)+"are colinear")
        return True
    else:
        logging.debug(str(vector1)+" and "+ str(vector2)+"are not colinear")
        return False
#==============================================================================
