##ClimateNA Processing=name
##boundaries=vector
##climatena=raster
##regionboundaries=vector
##quebecclip=output raster
##regionclip=output raster
outputs_SAGACLIPGRIDWITHPOLYGON_1=processing.runalg('saga:clipgridwithpolygon', climatena,boundaries,None)
outputs_MODELERCLIPGRIDMODEL_1=processing.runalg('modeler:clipgridmodel', outputs_SAGACLIPGRIDWITHPOLYGON_1['OUTPUT'],regionboundaries,regionclip)
outputs_GDALOGRWARPREPROJECT_1=processing.runalg('gdalogr:warpreproject', outputs_SAGACLIPGRIDWITHPOLYGON_1['OUTPUT'],'+proj=lcc +lat_1=49 +lat_2=77 +lat_0=0 +lon_0=-95 +x_0=0 +y_0=0 +datum=WGS84 +units=m +no_defs','EPSG:4326','-9999',0.0,0,5,4,75.0,6.0,1.0,True,0,True,None,quebecclip)
outputs_SCRIPTCLEARTMPFOLDER_1=processing.runalg('script:cleartmpfolder', )