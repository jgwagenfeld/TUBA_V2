##############################################
Installation
##############################################


Prerequistance
=================


Anaconda
=================
Propably the easiest way to set up your python environment is to install the Anaconda distribution.
`Anaconda <https://www.continuum.io/downloads>`_   is a Python

Salome-Meca
====================

`Salome-Meca <http://code-aster.org/V2/spip.php?article303>`_

Tested Versions:

#. Salome-Meca 2015.2
#. Salome-Meca 2016


Older Versions before 2014 probably won't work as the synthax for the salome-script has changed.


Download TUBA from Github
============================
Download `Tuba <https://github.com/jgwagenfeld/TUBA_reloaded>`_ from the Github-page and unpack in your desired location.


Set Bash command
=================
Make ``TUBA.py``  executable

::

    chmod a+x TUBA.py



To run Tuba in your terminal via bash-command add the following lines to your  ``.bashrc`` located in your home-directory (show hidden files).

::

    TUBA=adresse du répertoire où TUBA est installé.
    export PATH=$TUBA:$PATH
    export TUBA

Last step, source ``.bashrc``  in your terminal.

::

    source ~/.bashrc


Your workspace is now prepared. Go to the next chapter to get a step by step introduction in TUBA functionality.





:ref:`my-reference-label`
