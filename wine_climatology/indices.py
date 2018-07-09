from osgeo import gdal
import numpy as np
import pandas as pd
import pyproj

gdal.UseExceptions()


def calc_index(grid, index='winkler', base=10, crs=pyproj.Proj('+init=epsg:4326')):
    """
    A function for calculating the BEDD index for a set from a GeoTIFF of raster bands
    
    Parameters
    ----------
    grid : str
           File name or path of multi-band GeoTIFF
    index : 'winkler' or 'bedd' or 'gst' or 'huglin' or 'lti' (str)
            Agroclimatic index being used for evaluation
    base : float or int
           
    """

    try:
        src_ds = gdal.Open(grid)
    except RuntimeError as e:
        print('Unable to open GeoTIFF')
        print(e)
        sys.exit(1)


if __name__ == "__main__":
    pass
