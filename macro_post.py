# -*- coding: utf-8 -*-
#
# Use : from smeca_utils import macro_post
# Fields must be defined on nodes.

    
import os
from math import sqrt

try : import pvsimple as PV
except : import paravis.simple as PV

class DefaultParameters(object):
    """Parameters"""
    __slots__ = ('nbColor', 'scalarType', 'labelFormat', 'labelSize', 'titleSize')
    nbColor = 8
    scalarType = 'HSV'
    labelFormat = '%.1f'
    labelSize = 12 
    titleSize = 12

class Parameters(DefaultParameters):
    """ Modification des parametres defaut """
    pass

class ParavisSalomeMeca:
    """
    Load and filter MED data.
    """
    def __init__(self, MEDfileName="",nomcomplet="",dim1=0,dim2=0):
        """
        """
        for _view_repr in PV.GetRenderView().Representations:
            _view_repr.Visibility = 0

        self.MEDfile = PV.MEDReader(FileName=MEDfileName)
        self._setMEDfileProperties(nomcomplet)
        self.Source = self.MEDfile
        self.OldSource = None
        self.OldText = None
        self.lineChartView = None
        self.param = Parameters()
        
        # renderView1 = PV.GetActiveViewOrCreate('RenderView')
        # uncomment following to set a specific view size
        # renderView1.ViewSize = [1432, 671]
        tt=[dim1,dim2];
        if dim1*dim2>0 :
            try :
                PV.ViewSize = tt
            except :
                print("var_dim mal para")

    def _check_field_name(self, field_name):
        """Check existence of field_name in list of known fields."""
        

        if field_name not in self.fieldList:
            raise IOError(
                "%s : Nom de champ inexistant dans la liste des champs %s" %
                (field_name, self.fieldList))

    def _setMEDfileProperties(self,nomcomplet=None):
        """
        Update a self.MEDfile object.
        """

        #self.MEDfile.AllArrays = ['TS0/MAIL/ComSup0/URESI___EPSG_NOEU@@][@@P1', 'TS0/MAIL/ComSup0/URESI___SIEF_NOEU@@][@@P1']
        if nomcomplet : 
            self.MEDfile.AllArrays =nomcomplet
    
        self.listeTime = self.MEDfile.TimestepValues

        keys = self.MEDfile.GetProperty("FieldsTreeInfo")[::2]
        arrs_with_dis = [elt.split("/")[-1] for elt in keys]
        sep = str(self.MEDfile.GetProperty("Separator")[0])
        self.fieldList = [elt.split(sep)[0] for elt in arrs_with_dis]

    def getFieldName(self, name=""):
        """
        Recupere le nom complet d'un field contenant name
        """
        _field_name = None
        for _fullname in self.fieldList:
            if name in _fullname:
                _field_name = _fullname
        return _field_name

    def _getFieldInfo(self, fieldName="", cp=""):
        """
        Recupere l'info des composantes du champ aux noeuds.
        NB : à l'instant courant.

        @return nb_cp, num_cp, range_cp
        """
        self._check_field_name(fieldName)
#        nb_cp = 0
#        num_cp = 0
#        range_cp=[0.,1.]
        
        for _info_array in self.MEDfile.PointData :
            if _info_array.GetName() == fieldName:
                nb_cp = _info_array.GetNumberOfComponents()
                print(nb_cp)
                print(_info_array.GetNumberOfComponents())
                if cp == "":	# Magnitude
                    num_cp = 0
                    norm_min = 0
                    norm_max = 0
                    for n in range(min(3, nb_cp)):
                        norm_min = (norm_min +
                                    _info_array.GetComponentRange(n)[0] *
                                    _info_array.GetComponentRange(n)[0])
                        norm_max = (norm_max +
                                    _info_array.GetComponentRange(n)[1] *
                                    _info_array.GetComponentRange(n)[1])
                    range_cp = [sqrt(norm_min), sqrt(norm_max)]
                else:
                    for n in range(nb_cp):
                        if _info_array.GetComponentName(n) == cp:
                            num_cp = n
                            range_cp = _info_array.GetComponentRange(n)

        return nb_cp, num_cp, range_cp

    def extractGroup(self, lgroup=None):
        """
        Extrait les groupes de mailles
        """
        if lgroup is None:
            lgroup = []
        lgroup_name = ['GRP_' + _group.upper() for _group in lgroup]
        resu = PV.ExtractGroup()
        resu.AllGroups = lgroup_name
        self.Source = resu

    def _getNormale(self, P1, P2, P3):
        try :
            print('test V2')
            """
            Normale plan passant par trois points
            """
            U = [P2[0] - P1[0], P2[1] - P1[1], P2[2] - P1[2]]
            V = [P3[0] - P1[0], P3[1] - P1[1], P3[2] - P1[2]]
            nx = U[1] * V[2] - U[2] * V[1]
            ny = U[2] * V[0] - U[0] * V[2]
            nz = U[0] * V[1] - U[1] * V[0]
            norm = (nx * nx + ny * ny + nz * nz) ** 0.5
            if norm < 1e-6:
                Normale = [1., 0., 0.]
                print("Les 3 points P1, P2 et P3 ne sont pas correctement définis pour déterminer un plan : changez les coordonnées de ceux ci si nécessaire")
                print("La normale aa plan prise par défaut est de direction : [1., 0., 0.]")
                print("Ce plan passe par le point P1")
            else:
                Normale = [nx / norm, ny / norm, nz / norm]
        except :
            Normale = [1., 0., 0.]
            print("V2 : Les 3 points P1, P2 et P3 ne sont pas correctement définis pour déterminer un plan : changez les coordonnées de ceux ci si nécessaire")
        return Normale

    def applyClip(self, P1, P2, P3, side=0):
        """
        Clip filter defined from 3 points.
        """
        Normale = self._getNormale(P1, P2, P3)
        Origin = P1

        Clip = PV.Clip()
        Clip.ClipType.Origin = Origin
        Clip.ClipType.Normal = Normale
        Clip.InsideOut = side
        PV.Hide3DWidgets(proxy=Clip)

        self.Source = Clip

    def applySlice(self, P1, P2, P3):
        """
        Applique un filtre Slice
        """

        Normale = self._getNormale(P1, P2, P3)
        Origin = P1

        Slice = PV.Slice()
        Slice.SliceType.Origin = Origin
        Slice.SliceType.Normal = Normale
        Slice.SliceOffsetValues = [0.0]
        PV.Hide3DWidgets(proxy=Slice)

        self.Source = Slice

    def applyWarp(self, fieldName="", scale_factor=1.0):
        """
        Applique un filtre WarpByVector
        """
        self._check_field_name(fieldName)
        nb_cp, _, _ = self._getFieldInfo(fieldName=fieldName)

        if nb_cp != 3:
            _tmp = PV.Calculator()
            if nb_cp == 2:
                _tmp.Function = ("{0}_DX*iHat+{0}_DY*jHat+0*kHat".
                                format(fieldName))
            elif nb_cp > 3:
                _tmp.Function = ("{0}_DX*iHat+{0}_DY*jHat+{0}_DZ*kHat".
                                format(fieldName))
            _tmp.ResultArrayName = fieldName + "_Vector"
            fieldName = fieldName + "_Vector"

        Warp = PV.WarpByVector()
        Warp.Vectors = ['POINTS', fieldName]
        Warp.ScaleFactor = scale_factor

        self.Source = Warp

    def applyScalarBar(self, fieldName="", cp="", num_time=0,
                      val_min=None, val_max=None, step=None,show_rep="Surface"):
        """
        Render field
        """
        self._check_field_name(fieldName)
        AnimationScene = PV.GetAnimationScene()
        AnimationScene.AnimationTime = self.listeTime[num_time]

        if self.OldSource : PV.Hide(self.OldSource,PV.GetRenderView())
        _DataRep=PV.Show(self.Source,PV.GetRenderView())
        try : 
            _DataRep.SetRepresentationType(show_rep)
        except :
            _DataRep.SetRepresentationType('Surface')
            print("show_rep var mal param")

        PV.ResetCamera()

        nb_cp, num_cp, range_cp = self._getFieldInfo(fieldName=fieldName,cp=cp)

        if cp == "":
            mode = "Magnitude"
        else:
            mode = "Component"

        if val_min is None:
            val_min = range_cp[0]
        if val_max is None:
            val_max = range_cp[1]
        if step is None:
            nb_color = self.param.nbColor
        else :
            nb_color = int((val_max - val_min) / step) 
            if (nb_color < 2) : nb_color = 2
        _RGBPoints = [val_min, 0.0, 0.0, 1.0, val_max, 1.0, 0.0, 0.0]
        print(fieldName)
        PV.ColorBy(_DataRep,('POINTS',fieldName))
        _DataRep.RescaleTransferFunctionToDataRange(True)
        _DataRep.SetScalarBarVisibility(PV.GetRenderView(),True)


        # LookupTable
        _LookupTable  = PV.GetColorTransferFunction(fieldName.replace('_',''))
        _LookupTable_op = PV.GetOpacityTransferFunction(fieldName.replace('_',''))
        _LookupTable.VectorMode = mode
        if mode == "Component":
          _LookupTable.VectorComponent = num_cp
        _LookupTable.NumberOfTableValues = nb_color
        _LookupTable.ColorSpace = self.param.scalarType
        _LookupTable.ScalarRangeInitialized=1.0
        _LookupTable.LockDataRange=1
        _LookupTable.RGBPoints = _RGBPoints

        
        # Barre d'echelle
        _ScalarBar = PV.GetScalarBar(_LookupTable,PV.GetRenderView())
        _ScalarBar.LabelColor=[0.0, 0.0, 0.0]
        _ScalarBar.DrawTickLabels = 0
        _ScalarBar.DrawSubTickMarks = 0
        _ScalarBar.DrawTickMarks = 0

        _ScalarBar.AutomaticAnnotations = 1
        _ScalarBar.DrawAnnotations = 1
        _ScalarBar.TextPosition = 'Ticks right/top, annotations left/bottom'

        _ScalarBar.TitleColor=[0.0, 0.0, 0.0]
        _ScalarBar.Title= " "
        _ScalarBar.ComponentTitle = " "


        self.OldSource = self.Source

    def showView3D(self, oeil=(1, 0, 0), titre="",font="", fontsize=0, titrepos="", titrealig="", axe_visibility=0, color1=0, color2=0, color3=0):
        
        """Affiche une vue depuis oeil avec titre.

        L'oeil, ou la camera, pointe vers l'origine du repère courant
        """
        self.titre = titre
        view = PV.GetRenderView()
        view.Background = [1.0, 1.0, 1.0]
        view.CameraFocalPoint = [0., 0., 0.]
        view.CameraPosition = [oeil[0] * 1.E+10, oeil[1] * 1.E+10,
                              oeil[2] * 1.E+10]
        try:
            view.CameraViewUp = [0., 0., 1.]
        except:
            view.CameraViewUp = [0., 1., 0.]

            
            
            
        #representation
        # ttDisplay = PV.Show(self.MEDfile, PV.GetRenderView())
        
        # try :
            # ttDisplay.SetRepresentationType(show_rep)
        # except :
            # ttDisplay.SetRepresentationType('Surface')
            # print("valeur de show_rep entrée nok, Surface par de")
            
            
        PV.ResetCamera()
        self._showText(titre=titre,font=font, fontsize=fontsize,  titrepos=titrepos, titrealig=titrealig, color1=color1, color2=color2, color3=color3)
        #self._showText2(titre=titre)
        PV.SetActiveSource(self.Source)
        
        
        if axe_visibility==1 :
            view.OrientationAxesVisibility = 1
        else :
            view.OrientationAxesVisibility = 0
        


    def setActiveMED(self):
        """
        On remet la source sur le MEDfile
        """
        PV.SetActiveSource(self.MEDfile)
        self.Source = self.MEDfile

    def savePicture(self, outputFile = "output.png", magnification = 1):
        """
        Permet d'exporter la visualisation dans un fichier
        magnification permet d'augmenter la resolution (x2, x3...)
        """
        PV.WriteImage(outputFile, Magnification = magnification)
        #logging.info("Picture saved in %s", outputFile)

    def _showText2(self, titre=""):
        """
        Write text in the picture
        """
        Text = PV.Text()
        Text.Text = titre
        if self.OldText : PV.Hide(self.OldText,PV.GetRenderView())
        _DataText=PV.Show(Text,PV.GetRenderView())
        _DataText.FontSize = 10
        _DataText.FontFamily = 'Times'
        _DataText.Color = [0.0, 0.0, 0.0]
        _DataText.Justification = 'Center'
        _DataText.WindowLocation = 'LowerCenter'

        self.OldText=Text

    def _showText(self, titre="",font="", fontsize=0,  titrepos="", titrealig="", color1=0, color2=0, color3=0):
        """
        Write text in the picture
        """
        Text = PV.Text()
        Text.Text = titre
        if self.OldText : PV.Hide(self.OldText,PV.GetRenderView())
        
        _DataText=PV.Show(Text,PV.GetRenderView())
        
        # fontsize
        if fontsize>0 :
            try :
                _DataText.FontSize = fontsize
            except : 
                print("valeur de fontsize entrée nok")
                _DataText.FontSize = 10
        else :
            _DataText.FontSize = 10
            
        # font
        if font=="":
            try : 
                _DataText.FontFamily = font
            except : 
                _DataText.FontFamily = 'Times'
                print("valeur de FontFamily entrée nok")
        else : 
            _DataText.FontFamily = 'Times'
        
                    
        # color
        try : 
            _DataText.Color = [color1, color2, color3]
        except : 
            _DataText.Color = [0.0, 0.0, 0.0]
            print("valeur de text color entrée nok")
        
        
        
                    
        # _DataText.Justification
        try : 
            _DataText.Justification = titrealig
        except : 
            _DataText.Justification = 'Center'
            print("valeur de text Justification entrée nok")
        
        
                    
        # _DataText.WindowLocation
        try : 
            _DataText.Justification = titrepos
        except : 
            _DataText.WindowLocation = 'LowerCenter'
            print("valeur de text Justification entrée nok")
        
        

        self.OldText=Text

    def _showText(self, titre="",font="", fontsize=0,  titrepos="", titrealig="", color1=0, color2=0, color3=0):
        """
        Write text in the picture
        """
        Text = PV.Text()
        Text.Text = titre
        if self.OldText : PV.Hide(self.OldText,PV.GetRenderView())
        
        _DataText=PV.Show(Text,PV.GetRenderView())
        
        # fontsize
        if fontsize>0 :
            try :
                _DataText.FontSize = fontsize
            except : 
                print("valeur de fontsize entrée nok")
                _DataText.FontSize = 10
        else :
            _DataText.FontSize = 10
            
        # font
        if font=="":
            try : 
                _DataText.FontFamily = font
            except : 
                _DataText.FontFamily = 'Times'
                print("valeur de FontFamily entrée nok")
        else : 
            _DataText.FontFamily = 'Times'
        
                    
        # color
        try : 
            _DataText.Color = [color1, color2, color3]
        except : 
            _DataText.Color = [0.0, 0.0, 0.0]
            print("valeur de text color entrée nok")
        
        
        
                    
        # _DataText.Justification
        try : 
            _DataText.Justification = titrealig
        except : 
            _DataText.Justification = 'Center'
            print("valeur de text Justification entrée nok")
        
        
                    
        # _DataText.WindowLocation
        try : 
            _DataText.Justification = titrepos
        except : 
            _DataText.WindowLocation = 'LowerCenter'
            print("valeur de text Justification entrée nok")
        
        

        self.OldText=Text

    def plotLine(self, num_time=0, P1=None, P2=None, liste_curve=None,
                outputFile="output.png"):
        """
        Imprime une liste de courbes definies par le dico liste_curve
            fieldName,cp
        """
        if liste_curve is None:
            liste_curve = [{}]
        AnimationScene = PV.GetAnimationScene()
        AnimationScene.AnimationTime = self.listeTime[num_time]

        renderview = PV.GetRenderView()
        viewLayout = PV.GetLayout()

        Curve = PV.PlotOverLine()
        Curve.Source.Point1 = P1
        Curve.Source.Point2 = P2

        if not self.lineChartView : 
            viewLayout = PV.GetLayout()
            self.lineChartView = PV.CreateView('XYChartView')
            viewLayout.AssignView(2,self.lineChartView)

        PV.SetActiveView(self.lineChartView)

        display = PV.Show(Curve,self.lineChartView)
        display.SeriesVisibility = []
        
        # Selection courbes champs/composantes utilisateur
        name=[]
        for curve in liste_curve :
          fieldName = curve.get('fieldName')
          cp = curve.get('cp')
          if cp =='' : cp='Magnitude'
          name.append(fieldName+"_"+cp)

        display.SeriesVisibility=name

        self.savePicture(outputFile =outputFile)

        PV.Hide(Curve,self.lineChartView)

        PV.SetActiveView(renderview)
        self.Source = self.MEDfile
        PV.SetActiveSource(self.Source)

        
        
