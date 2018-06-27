# aster-calc-section

## Description
This collection of scripts enables the calculation of section properties with [aster](https://www.code-aster.org/) code with the help of [salome meca](https://www.code-aster.org/). Now, it works with I beam geometry.
- File Manager.py : the main python script reads input file and create communication temporary file. Then, geometry generation and mesh generation are called with salome meca. Finally, code aster is launched with the command MACR_CARA_POUTRE.
- GenPro.py : salome python script for the geometry and the mesh
- SectionAuto.comm : command file for code aster
- SectionAuto.export : settings for code aster calculation
- SectionAuto.input : I beam and H beam geometry
- SectionAuto.output : section properties results

## Use
- User needs to adapt in every each scripts all file paths.
- User needs to take care of python configuration in shell, salome and aster especially to launch pandas module within salome environment.

## Next steps
- Try to be less platform and user dependent ...
- Try to use this database directly in code aster with AFFE_CARA_ELEM.

## References
- [U4.42.02](https://www.code-aster.org/doc/v12/fr/man_u/u4/u4.42.02.pdf)
- [R3.08.03](https://www.code-aster.org/doc/v12/fr/man_r/r3/r3.08.03.pdf)

## Philosophy
I would like to create some tools to facilitate the use of aster code with beam elements.
