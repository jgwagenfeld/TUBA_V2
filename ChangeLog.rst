
ChangeLog-done:
TUBA 0.1


2017/5/05:added TUBA.py tubacode.py -salome and -plot to quicklaunch salome or the matplotlib-graph

2017/6/24:  added specialized visualization for Deflection (BlockFunction)

2017/6/28:  added Friction-Simulation Mode  (iterative calculation of an equivalent stiffness at the fricton contact  -   command:   Friction(mu=0.3)

2017/6/28:  added table output of species (at the moment, just generic - plan is to print a complete simulation report with all important informations)

2017/7/08:  added Command Mass(mass=2) to add a discret element

2018/1/01:  new TUBA-arguments  -all,-aster

2018/1/01:  3D Pipe and 3D Bent elements
-----------------------------------------------

2018/1/12:  Removal of Model (is now handled with section commands)

2018/4/29:  Bugfixing, Rework of Bent-Function

2018/4/29:  Restructering TUBA-Mainfunction, cleaning of scripts
-----------------------------------------------

2018/4/29:  Replace  vd2x, vd1x vd3x  with   local_x,local_y and local_z

2018/5/18:  Included contious 3D-elements with possible 1D-supports

2018/6/4:  added Python-functions for temperature f(x,y,z,t)

2018/6/5:  added CABLE section (nonlinear simulation - still not giving prope results)

-----------------------------------------------

2018/6/24:  added structure for custom profile calculation/usage (based on Core Engineering)

2018/6/25:  added NPS/DN tables to the Section 1function (now possible to use strings "DN15" for outer_radius and "SCH-STD" for thickness)

-----------------------------------------------

2020/1/3:  Updated to SalomeMeca2019
2020/1/3:  Added WindFunction(preliminary)
2020/1/3:  Added V_Reducer (VARI_SECT-element)
