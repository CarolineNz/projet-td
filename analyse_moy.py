# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 17:25:36 2020

@author: Sophie
"""

def analyse_moy(nom_var):
    sup=[]
    inf=[]
    for i in range(1,6):
        if moyenne_bis(nom_var,i)>=moyenne(nom_var):
            sup.append(i)
        else : 
            inf.append(i)
    return sup,inf 