Developper Section
======================

Create a Macro Command
-----------------------
An easy way to start with the underlying Python code is to create a Macro command for TUBA. A macro is just a sequence of already existing TUBA commands. The best example is the macro ``FixPoint()`` which calls ``Block(x=0,y=0,z=0,rx=0,ry=0,rz=0)``.
For repetitve use of certain structures we could imagine to create a parametric version.
In the following, we walk through the creation of the macro command ``Lyre()``


Naming Convention
-------------------

a TubaPoint object has to be adressed always by a _tubapoint ending:
 f.ex  --> Startpoint  =>   start_tubapoint

In contrast, a real point(euclid.Point3-Object) as a reprensentation of a position in a 3D-Space
can be named _point or _position

This convention is introduced to distiguish between a tubapoint as an information vessel and the
geometrical representation of a point

The same applies for TubaVector-Objects.

TubaPoint
-------------------
.. autoclass:: tuba.define_geometry.TubaPoint
    :members:
    :undoc-members:

TubaVector
-------------------
.. autoclass:: tuba.define_geometry.TubaVector
    :members:
    :undoc-members:
