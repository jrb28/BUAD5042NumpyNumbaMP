# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 11:38:04 2021

@author: jrbrad
"""

import numpy as np
import multiprocessing as mp
import requests
from numba import njit

def getData():
    search_url = 'https://jrbrad.people.wm.edu/deleteme/knapsack.json'
    response = requests.get(search_url, headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"})
    x = response.json()
    
    for i in range(len(x)):
        myData = x[i]['data']
        x[i]['data'] = {}
        for j in range(len(myData)):
            x[i]['data'][j] = tuple(myData[j])
    return x

def get_pop():
    search_url = 'https://jrbrad.people.wm.edu/deleteme/pop.json'
    response = requests.get(search_url, headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"})
    return response.json()

def pop_fit():
    return 


if __name__ == '__main__':
    ''' Get cell tower data '''
    probData = getData()
    problems = range(len(probData))
    problem_id = 9
    budget = probData[problem_id]['cap']
    towers = probData[problem_id]['data']
    ''' Create numpy array for added calls for each cell tower '''
    calls = np.array([towers[k][1] for k in towers.keys()])
    
    ''' Initialize population of solutions '''
    pop = get_pop()
    
    ''' Compute fitness for each population member using nested for loops '''
    fitness_long = [] 
    for p in pop:
        fit = 0.0
        for i in range(len(p)):
            fit += towers[p[i]][1]
        fitness_long.append(fit)
    print(fitness_long)
            
    
    ''' Code fitness solution below using numpy, multiprocessing, and compilation '''
    '''    - Use the variable 'fitness' for the result '''
    '''    - Use the function 'pop_fit()' to compute the fitness '''
    
    
    
    ''' Check if two solutions are equivalent '''
    print(fitness_long == fitness)