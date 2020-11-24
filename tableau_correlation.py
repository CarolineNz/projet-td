# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 15:43:13 2020

@author: Sophie
"""


def tableau_correlation():
    L=['noise','temp','humidity','lum','co2']
    tableau=[]
    for i in L:
        tableau.append(i)
        [tableau.append(coef_correlation(i,j)) for j in L]
            
    return [L]+tableau
    
    