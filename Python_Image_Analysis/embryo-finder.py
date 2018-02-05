#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 17:58:57 2018

@author: nathan
"""

from PIL import Image
import numpy as np
from skimage.io import imread
from skimage.filters import sobel
from skimage.filters import median
from skimage.feature import canny
from skimage.color import rgb2gray
from skimage.morphology import square, erosion
from matplotlib.pyplot import imshow
from matplotlib import pyplot as plt


def cropPercentile(nparr, percent):
    nparr[nparr < np.percentile(nparr, percent).min()] = 0
    return nparr

img = imread('../../Images/Example Grains/example_barley_grain.png')
gray = rgb2gray(img)


# Plot from same origin to top point 
# Do this over lots of points 

plt.figure()
plt.imshow(gray, cmap='gray')
