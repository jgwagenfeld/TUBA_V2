# The MIT License (MIT)
#
# Copyright (c) 2013 Stefan Reiterer  -  maldun.finsterschreck@gmail.com
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.



from __future__ import print_function

class UnitTester(object):

    def testMassUnits(self):

        from UnitCalculator import kg, g, T
        
        print("Test mass Units: ", 
              T(T) == 1.0,
              kg(kg) == 1.0,
              g(g) == 1.0,
              kg(g) == 1000.0, 
              g(kg) == 0.001, 
              T(kg) == 1000.0, 
              T(g) == 1000000.0, 
              kg(T) == 0.001, 
              g(T) == 0.000001)
    
    def testMetricUnits(self):

        from UnitCalculator import km, m, dm, cm, mm
        
        print("Test metric units: ", 
              km(km) == 1.0,
              km(m) == 1e+3, 
              km(dm) == 1e+4,
              km(cm) == 1e+5, 
              km(mm) == 1e+6, 
              m(km) == 1e-3,
              m(m) == 1.0,
              m(dm) == 1e+1,
              m(cm) == 1e+2,
              m(mm) == 1e+3,
              dm(km) == 1e-4,
              dm(m) == 1e-1,
              dm(dm) == 1.0,
              dm(cm) == 1e+1,
              dm(mm) == 1e+2,
              cm(km) == 1e-5,
              cm(m) == 1e-2,
              cm(dm) == 1e-2/1e-1,
              cm(cm) == 1e+0,
              cm(mm) == 1e+1,
              mm(km) == 1e-6,
              mm(m) == 1e-3,
              mm(dm) == 1e-2,
              mm(cm) == 1e-1,
              mm(mm) == 1e+0
              )

    def testPressureUnits(self):
        
        from UnitCalculator import Pa, MPa, bar, mbar

        print("Test pressure units: ",
              Pa(Pa) == 1.0,
              MPa(MPa) == 1.0,
              MPa(Pa) == 1e+6,
              Pa(MPa) == 1e-6,
              bar(Pa) == 1e+5,
              bar(MPa) == 1e-1,
              bar(bar) == 1.0,
              Pa(bar) == 1e-5,
              MPa(bar) == 1e+1,
              mbar(mbar) == 1.0,
              mbar(bar) == 1e-3,
              mbar(Pa) == 1e+2,
              mbar(MPa) == 1e-4,
              Pa(mbar) == 1e-2,
              )

    def testForceUnits(self):

        from UnitCalculator import kN, N

        print("Test force units: ",
              kN(kN) == 1.0,
              N(N) == 1.0,
              kN(N) == 1e+3,
              N(kN) == 1e-3)

    def testTimeUnits(self):

        from UnitCalculator import sec, minute, hour

        print("Test time units: ", 
              hour(hour) == 1.0,
              minute(hour) == 1/60.0,
              sec(hour) == 1/3600.0,
              hour(minute) == 60.0,
              minute(minute) == 1.0,
              sec(minute) == 1/60.,
              hour(sec) == 3600.0,
              minute(sec) == 60.0,
              sec(sec) == 1.0)

    def testRadiantUnits(self):

        from UnitCalculator import rad, grad

        from math import pi

        print("Test radiant units: ",
              rad(rad) == 1.0,
              rad(grad) == 180.0/pi,
              grad(grad) == 1.0,
              grad(rad) == pi/180.,
              )
              

    def testTemperatureUnits(self):
        
        from UnitCalculator import degK, degC

        print("Test temperature units: ",
              degC(degK) == 1.0,
              degK(degC) == 1.0,
              degC(degC) == 1.0,
              degK(degK) == 1.0,
              degK.convertWithOrigin(0.0,degK) == 0,
              degK.convertWithOrigin(0.0,degC) == -273.15
              )

    def testPowerUnits(self):

        from UnitCalculator import W,mW

        print("Test power Units: ",
              W(W) == 1.0,
              W(mW) == 1000.0,
              mW(W) == 1e-3,
              mW(mW) == 1.0,
              )

    def testEnergyUnits(self):

        from UnitCalculator import J, mJ

        print("Test energy Units: ",
              J(J) == 1.0,
              J(mJ) == 1000.0,
              mJ(J) == 1e-3,
              mJ(mJ) == 1.0,
              )


    def testAutoConversionMKS(self):
        
        from UnitCalculator import kg, km, sec, W, mJ, Pa, rad, degC, auto_converter, MKS

        auto_converter(MKS)

        print("Test autoconversion to MKS: ",
              kg() == 1.0,
              km() == 1000.0,
              sec() == 1.0,
              W() == 1.0,
              mJ() == 1e-3,
              Pa() == 1.0,
              rad() == 1.0,
              degC() == 1.0,
              degC.convertWithOrigin(0.0) == 0.0,
              )

    def testAutoConversionSI(self):
        
        from UnitCalculator import kg, km, sec, W, mJ, Pa, rad, degC,auto_converter, SI 

        auto_converter(SI)

        print("Test autoconversion to SI: ",
              kg() == 1.0,
              km() == 1000.0,
              sec() == 1.0,
              W() == 1.0,
              mJ() == 1e-3,
              Pa() == 1.0,
              rad() == 1.0,
              degC() == 1.0,
              degC.convertWithOrigin(0.0) == 273.15,
              )

    def testAutoConversionmmNS(self):
        
        from UnitCalculator import kg, km, sec, W, mJ, Pa, rad, degC, auto_converter,mmNS

        auto_converter(mmNS)

        print("Test autoconversion to mmNS: ",
              kg() == 1e-3,
              km() == 1000000.0,
              sec() == 1.0,
              W() == 1000.0,
              mJ() == 1.0,
              Pa() == 1e-6,
              rad() == 1.0,
              degC() == 1.0,
              degC.convertWithOrigin(0.0) == 0.0,
              )

    def testAlgebra(self):

        from UnitCalculator import kg, km, sec, W, mJ, Pa, rad, degC, auto_converter,mmNS, m, kN, hour

        auto_converter(mmNS)

        print("Test conversion algebra: ",
              8.000*kg()/(m()**3) == 8.000*kg/m**3,
              5*kN()*m() == 5*kN*m,
              2*km()/hour() == 2*km/hour,
              km()/hour() == km/hour
              )


    def __init__(self):

        print("Test Conversion factors: ")
        self.testMetricUnits()
        self.testMassUnits()
        self.testPressureUnits()
        self.testForceUnits()
        self.testTimeUnits()
        self.testRadiantUnits()
        self.testTemperatureUnits()
        self.testPowerUnits()
        self.testEnergyUnits()
        self.testAutoConversionMKS()
        self.testAutoConversionSI()
        self.testAutoConversionmmNS()
        self.testAlgebra()

UnitTester()
