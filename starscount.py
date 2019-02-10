#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 17:56:50 2019

@author: jeetu
"""


from skimage.feature import blob_log

import glob

from skimage.io import imread

example_file = glob.glob("star.jpg")[0]
im= imread(example_file, as_grey=True)

blob_log = blob_log(im, max_sigma=30,num_sigma=10, threshold=.1)

numrows=len(blob_log)

print("NUmbers of star counted:  ", numrows)
