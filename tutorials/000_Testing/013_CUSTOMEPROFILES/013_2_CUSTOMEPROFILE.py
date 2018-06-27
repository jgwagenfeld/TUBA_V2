#---UnitCalculator to use different input units---
from external.UnitCalculator import *
auto_converter(mmNS)

with open(os.environ["TUBA"]+'/external/Section/IBeam.input') as csvfile:
    reader = csv.DictReader(csvfile)
    distance=0    
    for row in reader:
		P(0,distance,0)  
		distance=distance+3*float(row["H"])		
		FixPoint()
		SectionIBeam(row["NAME"])		
		SectionOrientation(0)
		V(50*float(row["H"]),0,0)
		Force(z=10000)        



