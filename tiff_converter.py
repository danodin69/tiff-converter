# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 14:01:18 2022
Modified on thur Jun 30 23:11:12 2022
author : @dpoxo
using python 3.6

"""

from osgeo import gdal
import os
import matplotlib.pyplot as plt
import numpy as np
os.getcwd()

dataset = gdal.Open(r'lesser_tiff.tiff')
dataset2 = gdal.Open(r'lesser_tiff2.tiff')

print('Dataset1 numbers are: ', dataset.RasterCount)

band1 = dataset.GetRasterBand(1)
band2 = dataset.GetRasterBand(2)
band3 = dataset.GetRasterBand(3)
b1 = band1.ReadAsArray()
b2 = band2.ReadAsArray()
b3 = band3.ReadAsArray()

print('Working on conversion...')
img = np.dstack((b1, b2, b3))
print('Processing...')
figure = plt.figure(figsize=(10,5))
print('Figure size set...')
plt.imshow(img)
print('...')
plt.savefig('converted_tiff.pdf', dpi =300)
print('File saved to current directory!')
plt.show()
