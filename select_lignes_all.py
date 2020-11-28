# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 20:59:55 2020

@author: Sophie
"""

##sélection d'une durée entre deux dates pour tous les capteurs
def select_lignes_all(date1, date2) :
    '''Crée un nouveau tableau "periode" avec les lignes du tableau de base comprises entre les deux dates incluses '''
    if date1=="2019-08-11 11:30:50+02:00" and date2=="2019-08-25 17:47:08+02:00" :
        return tableau
    else :
        periode = []
        for ligne in tableau :
            if ligne[-1]>=date1 and ligne[-1]<=date2 :
                periode.append(ligne)
        return periode