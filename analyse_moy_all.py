# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 17:35:00 2020

@author: Sophie
"""

def analyse_moy_all():
    L=[]
    for i in titres[2:-1]:
        L.append(i)
        L.append(analyse_moy(i))
    return (L)