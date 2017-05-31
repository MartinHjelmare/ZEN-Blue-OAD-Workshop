# -*- coding: utf-8 -*-
"""
Created on Thu May  4 15:36:45 2017

@author: M1SRH
"""

import numpy as np
import seaborn as sns
import pandas as pd

filename = r'c:\Users\M1SRH\Documents\Testdata_Zeiss\Zen_Output\temp\Experiment-54_Log.txt'
data = np.genfromtxt(filename, dtype=float, skip_header=1, invalid_raise=False, delimiter='\t', usecols=(0, 1, 2, 3))
df = pd.read_csv(filename, sep='\t', header=0)
df['area_t_norm'] = df['area_t']/df['area_t'].max()
df['area_p_norm'] = df['area_p']/df['area_p'].max()*100

g = sns.barplot(x='frame', y='area_p_norm', palette='Blues_d', data=df)
#g = sns.factorplot(x='frame', y='area_p_norm', palette='Blues_d', data=df)

