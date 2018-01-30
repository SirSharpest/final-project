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
from skimage.feature import canny
from skimage.color import rgb2gray
from skimage.morphology import square, erosion
from matplotlib.pyplot import imshow
from matplotlib import pyplot as plt


def cropPercentile(nparr, percent):
    nparr[nparr < np.percentile(nparr, percent).min()] = 0
    return nparr

img = imread('example_barley_grain.png')
gray = rgb2gray(img)
sob = sobel(gray)
edges = canny(gray, low_threshold=0.01 )


plt.figure()
plt.imshow(gray, cmap='gray')

plt.figure()
imshow(edges)

er = erosion(gray, square(10))

plt.figure()
imshow(er)

plt.figure()


imshow(cropPercentile(gray, 90))