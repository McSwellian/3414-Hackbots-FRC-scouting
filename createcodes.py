# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 19:12:01 2018

@author: Maxwell Ledermann
"""

import os
from itertools import combinations,product
import numpy as np
import cv2

def createCodes():
    #The value of size-(2*border) must be divisible by three
    #Smaller resolutions save time, but are less accurate for detection
    size=400
    border=29
    squareSide=int((size-(2*border))/3)
    
    if not os.path.exists('Nonacodes'):
        os.mkdir('Nonacodes')
    
    combos = list(combinations(list(product([0,1,2],repeat=2)),3))
    for codeNumber,item in enumerate(combos):
        code = np.zeros((size,size), np.uint8)
        code[border:size-border,border:size-border] = 255
        for coords in item:
            code[int(border+squareSide*coords[0]):int(border+squareSide*(coords[0]+1)),int(border+squareSide*coords[1]):int(border+squareSide*(coords[1]+1))] = [0]
        cv2.imwrite("Nonacodes/code"+str(codeNumber+1)+".png",code)
        
createCodes()