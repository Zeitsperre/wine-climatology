##Branas Index=name
##precipitation=raster
##meantemperature=raster
##branasvalues=output raster
outputs_GDALOGRRASTERCALCULATOR_1=processing.runalg('gdalogr:rastercalculator', meantemperature,'4',precipitation,'4',meantemperature,'5',precipitation,'5',meantemperature,'6',precipitation,'6','A*(A>0)*B*(B>0)+C*(C>0)*D*(D>0)+E*(E>0)*F*(F>0)','-9999',5,None,None)
outputs_GDALOGRRASTERCALCULATOR_2=processing.runalg('gdalogr:rastercalculator', meantemperature,'7',precipitation,'7',meantemperature,'8',precipitation,'8',meantemperature,'9',precipitation,'9','A*(A>0)*B*(B>0)+C*(C>0)*D*(D>0)+E*(E>0)*F*(F>0)','-9999',5,None,None)
outputs_SAGARASTERCALCULATOR_1=processing.runalg('saga:rastercalculator', outputs_GDALOGRRASTERCALCULATOR_1['OUTPUT'],[outputs_GDALOGRRASTERCALCULATOR_2['OUTPUT']],'g1+h1',True,7,branasvalues)