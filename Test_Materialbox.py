#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 14:54:14 2017

@author: jangeorg
"""

#   ca_wizard_mechanical, version 0.2
#   Allows the generation of comm-files for simple 3D structural analyses in code_aster with an interactive GUI
#
#   This work is licensed under the terms and conditions of the GNU General Public License version 3
#   Copyright (C) 2017 Dominik Lechleitner
#   Contact: kaktus018(at)gmail.com
#   GitHub repository: https://github.com/kaktus018/ca_wizard_mechanical
#
#   This file is part of ca_wizard_mechanical.
# 
#   ca_wizard_mechanical is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
# 
#   ca_wizard_mechanical is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
# 
#   You should have received a copy of the GNU General Public License
#   along with ca_wizard_mechanical.  If not, see <http://www.gnu.org/licenses/>.


import os
import pickle
import shutil
import webbrowser
import time
import re
import codecs
import xml.etree.ElementTree as ET
import urllib.parse

from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from tkinter import filedialog

#from cawm_classes import *

os.chdir(os.path.dirname(os.path.abspath(__file__)))

names = []
functions = []
materialSets = []
nodeJointSets = []
restraintSets = []
loadSets = []
contactSets = []
thermalSets = []
geomEntities = ("Volume","Surface","Edge","Vertex/Node","Node joint group")

matLibPath = "matLib.xml"
cawmVersion = "0.2"
mainFormSize = "730x600"

setMatLibPath(matLibPath)
setVersion(cawmVersion)


def matSelMatCBChangedEvent(evt):
    matName = matSelMatCB.get()
    matObj = Material(matName)
    lblMatNum['text'] = "Material number:   "+matObj.matNum
    lblMatCat['text'] = "Material category:   "+matObj.matCat
    lblYoungsModulus['text'] = "Young's modulus:   "+matObj.youngsModulus
    lblPoissonsRatio['text'] = "Poisson's ratio:   "+matObj.poissonRatio
    lblAlpha['text'] = "Coefficient of thermal expansion:   "+matObj.alpha
    lblDensity['text'] = "Density:   "+matObj.density
              
              
              



### Build the GUI

# Main Window
mainForm = Tk()
mainForm.title("ca_wizard_mechanical v" + cawmVersion)
mainForm.geometry(mainFormSize)
mainForm.resizable(width=False, height=False)
# mainForm.style = Style()          

ntbook = Notebook(mainForm)
materialsTab = Frame(ntbook)
ntbook.add(materialsTab, text='Materials')



# Materials Tab
group = LabelFrame(materialsTab, text="List of material assignments")
group.pack(side=LEFT, fill=Y, padx=10, pady=10, ipadx=5, ipady=5)
box = Frame(group, height=500, width=180)
box.pack_propagate(0)
box.pack(side=LEFT)
matAssiListbox = Listbox(box)
matAssiListbox.pack(side=LEFT,padx=5,fill=BOTH,expand=TRUE)
matAssiListbox.bind('<<ListboxSelect>>', matAssiListboxSelectionChanged)
box = Frame(group)
box.pack(pady=20)
Button(box, text="Add", command=addMaterialSet).pack(pady=5)
Button(box, text="Delete", command=deleteMatAssi).pack()
boxR = Frame(materialsTab)
boxR.pack(side=LEFT,fill=Y)
matAssiGroup = LabelFrame(boxR, text="Create/Modify material assignment")
matAssiGroup.pack(padx=10, pady=10, ipadx=5, ipady=5)
box = Frame(matAssiGroup)
box.pack(fill=BOTH)
Label(box, text="  Name of assignment: ").pack(side=LEFT)
matAssiNameLbl = Label(box, text="")
matAssiNameLbl.pack(side=RIGHT)
box = Frame(matAssiGroup)
box.pack(fill=BOTH)
Label(box, text="  Assign to: ").pack(side=LEFT)
matAssiMatCB = Combobox(box, values=getNames([0]), state='readonly')
matAssiMatCB.current(0)
matAssiMatCB.pack(side=RIGHT, pady=5, padx=10)
box = Frame(matAssiGroup)
box.pack(fill=BOTH)
Label(box, text="  Select material: ").pack(side=LEFT)
matSelMatCB = Combobox(box, values=getMatLibNamesFromXML(), state='readonly')
matSelMatCB.current(0)
matSelMatCB.pack(side=RIGHT, pady=5, padx=10)
matSelMatCB.bind("<<ComboboxSelected>>", matSelMatCBChangedEvent)
box = Frame(matAssiGroup)
box.pack(fill=BOTH, padx=5, pady=5)
Button(box, text="Done", command=changeMatAssi).pack(side=RIGHT,padx=10)
Button(box, text="Refresh material list", command=refreshMatCB).pack(side=RIGHT)
group = LabelFrame(boxR, text="Material info")
group.pack(fill=X, padx=10, pady=10)
lblMatNum = Label(group, text="Material number: -")
lblMatNum.pack(fill=BOTH, padx=5, pady=5)
lblMatCat = Label(group, text="Material category: -")
lblMatCat.pack(fill=BOTH, padx=5, pady=5)
lblYoungsModulus = Label(group, text="Young's modulus: -")
lblYoungsModulus.pack(fill=BOTH, padx=5, pady=5)
lblPoissonsRatio = Label(group, text="Poisson's ratio: -")
lblPoissonsRatio.pack(fill=BOTH, padx=5, pady=5)
lblAlpha = Label(group, text="Coefficient of thermal expansion: -")
lblAlpha.pack(fill=BOTH, padx=5, pady=5)
lblDensity = Label(group, text="Density: -")
lblDensity.pack(fill=BOTH, padx=5, pady=5)
disableWidgets(matAssiGroup)    
