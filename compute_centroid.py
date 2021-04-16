# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 12:46:22 2021

@author: jrbrad
"""

import numpy as np
import multiprocessing as mp
from numba import njit




if __name__ == '__main__':
    ''' Input data '''
    '''    - points contains the x and y coordinates of 1000 Cartesian points'''
    '''      This data is 1000 rows long with 2 columns '''
    '''    - assign contains 1s and 0s indicating to which of the five centrois each point is assigned '''
    '''      This data is 1000 rows long, one row for each point, and 5 columns wide.
             A 1 in a particular column indicates assignmentf of a point to the centroid associated with that column '''
    points = np.loadtxt('points.csv').astype(np.float32)
    assign = np.loadtxt('assign.csv').astype(np.int8)
    
    ''' Create code below to compute the 5 centroids based on the given assignments using numpy and multiprocessing '''
    
    
    