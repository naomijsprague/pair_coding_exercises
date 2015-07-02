# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 09:20:25 2015

@author: naomi
"""
import numpy as np

data = [2,7,1,5,10]
candidates = np.arange(0.1,10.1,0.1)
output = []

result = [(i - a)**2 for a in candidates for i in data]

for v in range(0,len(result),5):   
    output.append(sum(result[v:v+4]))
    
print min(output)