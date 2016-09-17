
.. _my-reference-label:

##############################################
How to start
##############################################

Assuming you followed the installation steps in the last chapter (`Installation`_), you can now run TUBA in your terminal with
the Bash command::

$ TUBAV3.py  command_script.py

The command_script as argument is your list of commands defining your geometry, your simulation and output. Executing TUBA will trigger the following actions:

#. generating a 3D-Plot of your defined geometry. The purpose of this plot is to get an immediate visualization of your geometry. 
   If needed, then your command list can be adapted before you start the time consuming import into Salome-Meca.

#. generating ``command_script_salome.py`` which then has to be loaded into Salome (in the Menu bar: ``File`` - ``Load Script...``)

#. generating ``command_script_aster.comm`` which then has to be loaded into the Code Aster Module. The file defines the simulation in Code Aster. Find more informations concerning the structure of comm-files under :ref:code_aster

#. generating ``command_script_post.py`` which then has to be loaded after a successful simulation. This file will start the post processing tool ParaVis and effect some standard plots. It is possible to adapt these plots or add new ones later on.
	

Writing the command script
============================

As mentioned above, the command-script consists of a list of commands defining your piping-geometry (or other rod-structure), it's properties(cross section, material, external and internal loads, etc) and finally also the simulation and post-processing.
It can be edited with any kind of text editor. An IDE with auto completion and auto help like Spyder( include hyper link) can be very helpful in the beginning, especially if you're not so familiar with the available commands.

The following code is a basic command script showing the most important commands - for a complete list of available commands, check - include hyper link. 




::

    #---UnitCalculator to use different input units---
    from external.UnitCalculator import *
    auto_converter(mmNS)

    outerRadius=35
    WallThickness=4
    
    Model("TUYAU")
    SectionTube(outerRadius,WallThickness)
    Temperature(550,T_ref=20)
    Pressure(2*bar())

    P(0,0,0) 
    FixPoint()  

    V(1000,0,0)

    for i in range(0,4):	
    	Vc(1000)
    	Block(z=0)

    Vc(1000)
    Bent(150,90,0)
    
    Vc(1000)
    Block(y=-1000)


    Calculate("Statique_Linear")


Decomposing step by step:
--------------------------
To better understand, how TUBA works, we will decompose the upper script step by step and explaining the functionality.
::

    #---UnitCalculator to use different input units---
    from external.UnitCalculator import *
    auto_converter(mmNS)

`UnitCalculator <https://github.com/maldun/UnitCalculator>`_ is an external python module written by Stefan Reiterer to translate different units.

SalomeMeca does not have a fixed default unit system. The user can choose whatever system is preferred - as long as it is consistent. In the `Unit Table <http://caelinux.org/wiki/downloads/docs/PCarrico/CAELINUX_plasticite/CAELINUX_plasticite.html#SECTION000180000000000000000>`_ you can see different consistent unit systems.

Unit Calculator facilitate the use of different, sometimes more intuitive units like bar. The TUBA script was only tested with the mmNS metric system as base (``auto_converter(mmNS)``), therefore it is advisable to stay in this system. 
The base defines the internal unit system and therefore as well the units of the result. See the documentation of `UnitCalculator <https://github.com/maldun/UnitCalculator>`_ for more informations how to use the calculator and what conversions are available.



::

    outerRadius=35
    WallThickness=4

The command script is pure python code. Therefore variable declaration,loops, if-statements etc. can be used as usual.

::

    Model("TUYAU")
    SectionTube(outerRadius,WallThickness)
    Temperature(550,T_ref=20)
    Pressure(2*bar())

This section defines the global properties of the following piping system. Model defines the finite element used to model the piping - see  :func:`tuba.define_properties.Model`. for a full list of available models.


::

    P(0,0,0) 
    FixPoint()  

    V(1000,0,0)

    for i in range(0,4):	
    	Vc(1000)
    	Block(z=0)

    Vc(1000)
    Bent(150,90,0)
    
    Vc(1000)
    Block(y=-1000)

::

    Calculate("Statique_Linear")


.. sidebar:: Sidebar Title
        :subtitle: Optional Sidebar Subtitle

   Subsequent indented lines comprise
   the body of the sidebar, and are
   interpreted as body elements.

Run the simulation in Salome:
==============================



Analyis the results in ParaVis:
================================
