import numpy as np
import matplotlib.pyplot as plt
import math

##ouverture fichier
def ouvrir_fichier() :
    '''Ouvre le fichier de données et le convertit en variables exploitables
    renvoie : (titres[liste de chaines], tableau[liste de listes de données]) '''

    file = open("D:\Documents\GitHub\projet-td\EIVP_KM.csv") #à changer
    content = file.read()
    file.close()

    content = content.split("\n")
    tableau = []
    for ligne in content :
        ligne = ligne.split(";")
        tableau.append(ligne)

    titres = tableau[0]
    tableau = tableau[1:len(tableau)-1] #on enlève la première ligne (les titres) et la dernière ligne (qui est vide)

    for i in range(0, len(tableau)-1) :
        for j in range(0, 6) :
            a = tableau[i][j]
            tableau[i][j] = float(a)

    return (titres, tableau)

(titres, tableau) = ouvrir_fichier()

##sélection d'une durée entre deux dates
def select_lignes(date1, date2) :
    '''Crée un nouveau tableau "periode" avec les lignes du tableau de base comprises entre les deux dates incluses '''
    periode = []
    for ligne in tableau :
        if ligne[-1]>=date1 and ligne[-1]<=date2 :
            periode.append(ligne)
    return periode


##affichage de la courbe d'une variable
def display(var, date1, date2) :
    '''var INDICE de la variable (numéro de colonne)
    Utilise tableau, select_lignes
    affiche la courbe d'une des variables'''

    #RECUPERATION DE LA VARIABLE UTILE
    periode = select_lignes(date1, date2)
    l_var = [ligne[var] for ligne in period]


    #AFFICHAGE DE LA COURBE
    plt.close()
    y = np.array(l_var)
    x = np.array([i for i in range(len(l_var))])

    plt.plot(x, y, label=titres[var])
    plt.legend()

    plt.show()

##stats

def moyenne(var, date1, date2) :
    periode = select_lignes(date1, date2)
    l_var = [ligne[var] for ligne in periode]
    moy = 0
    for e in l_var :
        moy = moy+e
    moy = moy/len(l_var)
    return moy

def variance(var, date1, date2) :
    periode = select_lignes(date1, date2)
    l_var = [ligne[var] for ligne in periode]
    vari = 0
    moy = moyenne(var, date1, date2)
    for e in l_var :
        vari = vari + pow(e-moy, 2)
    vari = vari/len(l_var)
    return vari

def ecart_type(var, date1, date2) :
    return math.sqrt(variance(var, date1, date2))

def mediane(var, date1, date2) :
    periode = select_lignes(date1, date2)
    print(var)
    l_var = [ligne[var] for ligne in periode]
    i = len(l_var)//2
    return l_var[i]

def minimum(var, date1, date2) :
    periode = select_lignes(date1, date2)
    l_var = [ligne[var] for ligne in periode]
    return (min(l_var))

def maximum(var, date1, date2) :
    periode = select_lignes(date1, date2)
    l_var = [ligne[var] for ligne in periode]
    return (min(l_var))


##affichage des statistiques d'une variable
def displayStat(var, date1, date2) :
    '''var INDICE de la variable (numéro de colonne)
    Utilise tableau, select_lignes
    affiche la courbe d'une des variables avec ses statistiques'''

    #RECUPERATION DE LA VARIABLE UTILE
    periode = select_lignes(date1, date2)
    l_var = [ligne[var] for ligne in periode]

    #CALCUL DES STATISTIQUES + CONVERSION EN CHAINES
    #calcul de la moyenne
    moy = "moyenne : " + str(moyenne(var, date1, date2))
    #calcul de l'écart-type
    sigma = "ecart_type :" + str(ecart_type(var, date1, date2))
    #calcul de la variance
    vari = "variance :" + str(variance(var, date1, date2))
    #calcul de la mediane
    med = "mediane :" + str(mediane(var, date1, date2))
    #calcul du minimum et du maximum
    mini = "minimum :" + str(minimum(var, date1, date2))
    maxi = "maximum :" + str(maximum(var, date1, date2))

    statistiques = mini + "\n" + maxi + "\n" + moy + "\n" + sigma + "\n" + vari + "\n" + med


    #AFFICHAGE DE LA COURBE
    plt.close()
    y = np.array(l_var)
    x = np.array([i for i in range(len(l_var))])

    #plt.text(0.5,0.5,statistiques,horizontalalignment='left', verticalalignment='top',bbox=dict(facecolor='black',alpha=0.5))
    plt.title(statistiques)
    plt.plot(x, y, label=titres[var])
    plt.legend()

    plt.show()

    return



##indice de corrélation
def correlation(var1, var2, date1, date2) :
    '''var1 et var2 les INDICES des variables (numéro de colonne)
    utilise tableau, select_lignes, moyenne et ecart_type
    affiche les courbes des variables et l'indice de corrélation, renvoie l'indice de corrélation'''
    periode = select_lignes(date1, date2)

    #CALCUL DU COEFFICIENT
    #calcul de l'espérence du produit
    l_var1 = [ligne[var1] for ligne in periode]
    l_var2 = [ligne[var2] for ligne in periode]
    l_prod = []
    for i in range(len(periode)) :
        l_prod.append(l_var1[i]*l_var2[i])
    moyp = 0
    for i in range(len(periode)) :
        moyp = moyp+l_prod[i]
    moyp = moyp/len(periode)

    #calcul des deux autres espérences
    moy1 = moyenne(var1, date1, date2)
    moy2 = moyenne(var2, date1, date2)

    #calcul de la covariance
    cov = moyp - moy1*moy2

    #calcul des écart-types
    sigma1 = ecart_type(var1, date1, date2)
    sigma2 = ecart_type(var2, date1, date2)

    #calcul du coefficient de correlation
    r = cov/(sigma1*sigma2)


    #AFFICHAGE DES DEUX COURBES
    plt.close()
    y1 = np.array(l_var1)
    y2 = np.array(l_var2)
    x = np.array([i for i in range(len(l_var1))]) #car les mesures sont prises à intervalles réguliers

    plt.plot(x, y1, label=titres[var1])
    plt.plot(x, y2, label=titres[var2])
    plt.legend()
    plt.title("Coefficient de corrélation : "+str(r))
    plt.show()

    return r

##indice humidex

def humidex(date1, date2) :
    '''utilise tableau, select_lignes
    affiche la courbe de l'humidex sur la période donnée
    renvoie l'humidex moyen'''
    periode = select_lignes(date1,date2)

    #humidex = T + 5/9*(6,112*pow(10, 7,5*T/(237.7+T))*H/100-10)
    l_hum = []
    for i in range(len(periode)) :
        T = periode[i][2]
        H = periode[i][3]
        l_hum.append(T + 5/9*(6.112*pow(10, 7.5*T/(237.7+T))*H/100-10))

    #moyenne sur la période donnée
    hum_moy = 0
    for h in l_hum :
        hum_moy = hum_moy+h
    hum_moy = hum_moy/len(l_hum)

    #affichage sous forme de graphique
    plt.close()
    x = np.array([i for i in range(len(l_hum))]) #car les mesures sont prises à intervalles réguliers
    y1 = np.array(l_hum)
    y2 = np.array([hum_moy for i in range (len(l_hum))])
    plt.plot(x, y1, label="humidex")
    plt.plot(x, y2, label="humidex moyen")
    plt.title("Humidex moyen : "+str(hum_moy))
    plt.legend()
    plt.show()

    return hum_moy
