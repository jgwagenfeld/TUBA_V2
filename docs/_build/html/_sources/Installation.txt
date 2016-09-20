
Installation
=================


Prerequistance
---------------


Anaconda
---------------
Propably the easiest way to set up your python environment is by installing `Anaconda <https://www.continuum.io/downloads>`_ (Python 2.7).
Anaconda is a Python distribution including the most popular packages.

Salome-Meca
---------------

Salome-Meca is the platform on which geometry and mesh generation is effected. The FEM simulation is run with the  included Code Aster Module. Furthermore, the ParaVis Module will be used for postprocessing.

To download here: 
`Salome-Meca <http://code-aster.org/V2/spip.php?article303>`_

Tested Versions:

#. Salome-Meca 2015.2
#. Salome-Meca 2016


Older Versions before 2014 probably won't work as the synthax for the salome-script has changed.


Download TUBA from Github
---------------------------
Download `Tuba <https://github.com/jgwagenfeld/TUBA_V2>`_ from the Github-page and unpack in your desired location.
An other option is to go to your desired directory (e.g. your home directory) and execute

::

    git clone https://github.com/jgwagenfeld/TUBA_V2.git

Set Bash command
---------------------------
Make ``TUBA.py`` (located in the main tuba-folder) executable.

::

    chmod a+x TUBA.py



To run Tuba in your terminal via bash-command add the following lines to your  ``.bashrc`` located in your home-directory (show hidden files).

::

    TUBA=local tuba directory path
    export PATH=$TUBA:$PATH
    export TUBA

Last step, source ``.bashrc``  in your terminal.

::

    source ~/.bashrc


Your workspace is now prepared. Go to the next chapter to get a step by step introduction in TUBA functionality.





:ref:`my-reference-label`
