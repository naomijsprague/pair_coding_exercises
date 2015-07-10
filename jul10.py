# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 09:19:53 2015

@author: naomi
"""

import pandas as pd
import numpy as np
import statsmodels.api as sm
from patsy import dmatrices

def generator(n):
    df = pd.DataFrame(np.random.randn(200,n))

    elements = 'df[0] ~'
    for i in range(1,n):
        elements = elements + ' + df[' + str(i) + ']'
        
    y, X = dmatrices(elements , data = df, return_type = 'dataframe')
    model = sm.OLS(y, X)
    results = model.fit()

    print results.summary()
    
