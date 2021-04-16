# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 11:07:27 2021

@author: jrbrad
"""

import numpy as np
import multiprocessing as mp


if __name__ == '__main__':
    n = 10

    p = np.random.random((n,n))
    q = np.random.random((n,n))
    
    print(p.dot(q))
    
''' create code below using numpy and multiprocessing to replicate dot product above '''

