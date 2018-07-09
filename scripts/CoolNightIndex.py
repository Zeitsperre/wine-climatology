##Cool Night Index=name
##minimumtemperature=raster
##coolnightvalues=output raster
outputs_GDALOGRRASTERCALCULATOR_1=processing.runalg('gdalogr:rastercalculator', minimumtemperature,'9',None,'1',None,'1',None,'1',None,'1',None,'1','A','-9999',5,None,coolnightvalues)
