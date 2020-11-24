# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 16:14:24 2020

@author: Sophie
"""

def moyenne_bis(nom_var, id, date1="2019-08-11 11:30:50+02:00", date2="2019-08-25 17:47:08+02:00") :
    var = titres.index(nom_var)
    periode = select_capteur(id)
    l_var = [ligne[var] for ligne in periode]
    moy = 0
    for e in l_var :
        moy = moy+e
    moy = moy/len(l_var)
    return moy