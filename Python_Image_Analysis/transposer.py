#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 20:28:24 2017

@author: nathan
"""


from PIL import Image
import numpy as np
from os.path import basename, exists
from os import makedirs
from skimage.io import imread
from matplotlib.pyplot import imshow
from glob import glob


def findfiles(startdir):
    print(startdir + '/*.tif')
    return glob(startdir + '*/*.tif')


def transposeALL(direct):

    files = findfiles(direct)

    for f in files:
        print('Working on {0}'.format(f))

        tmp = imread(f)

        tmp = tmp.transpose(1, 2, 0)
        tmp = tmp.transpose(2, 1, 0)
        directory = f.rsplit('/', 1)[0] + '/extracted'

        if not exists(directory):
            makedirs(directory)

        for i in range(0, tmp.shape[2]):
            Image.fromarray(tmp[:, :, i]).save(
                '{0}/{1}.png'.format(directory, i))


transposeALL('/home/nathan/Diss/Playground/')

print('Done!')
