##Winkler Index=name
##maxtemperature=raster
##mintemperature=raster
##winklervalues=output raster
outputs_GDALOGRRASTERCALCULATOR_1=processing.runalg('gdalogr:rastercalculator', maxtemperature,'4',mintemperature,'4',maxtemperature,'5',mintemperature,'5',maxtemperature,'6',mintemperature,'6','((((A+B)/2-10)*30)>0)*(((A+B)/2-10)*30)+((((C+D)/2-10)*30)>0)*(((C+D)/2-10)*30)+((((E+F)/2-10)*30)>0)*(((E+F)/2-10)*30)','-9999',5,None,None)
outputs_GDALOGRRASTERCALCULATOR_2=processing.runalg('gdalogr:rastercalculator', maxtemperature,'7',mintemperature,'7',maxtemperature,'8',mintemperature,'8',maxtemperature,'9',mintemperature,'9','((((A+B)/2-10)*30)>0)*(((A+B)/2-10)*30)+((((C+D)/2-10)*30)>0)*(((C+D)/2-10)*30)+((((E+F)/2-10)*30)>0)*(((E+F)/2-10)*30)','-9999',5,None,None)
outputs_GDALOGRRASTERCALCULATOR_3=processing.runalg('gdalogr:rastercalculator', outputs_GDALOGRRASTERCALCULATOR_1['OUTPUT'],'1',outputs_GDALOGRRASTERCALCULATOR_2['OUTPUT'],'1',maxtemperature,'10',mintemperature,'10',None,'1',None,'1','A+B+((((C+D)/2-10)*30)>0)*(((C+D)/2-10)*30)','-9999',5,None,None)
outputs_SAGARASTERCALCULATOR_1=processing.runalg('saga:rastercalculator', outputs_GDALOGRRASTERCALCULATOR_3['OUTPUT'],[],'g1*(g1>0)',True,7,winklervalues)