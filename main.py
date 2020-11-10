import numpy as np
import matplotlib.pyplot as plt
import math
import re


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
        for j in range(0, 7) :
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
def display(nom_var, date1, date2) :
    '''Utilise tableau, select_lignes
    affiche la courbe d'une des variables'''
    var = titres.index(nom_var)
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

def moyenne(nom_var, date1, date2) :
    var = titres.index(nom_var)
    periode = select_lignes(date1, date2)
    l_var = [ligne[var] for ligne in periode]
    moy = 0
    for e in l_var :
        moy = moy+e
    moy = moy/len(l_var)
    return moy

def variance(nom_var, date1, date2) :
    var = titres.index(nom_var)
    periode = select_lignes(date1, date2)
    l_var = [ligne[var] for ligne in periode]
    vari = 0
    moy = moyenne(nom_var, date1, date2)
    for e in l_var :
        vari = vari + pow(e-moy, 2)
    vari = vari/len(l_var)
    return vari

def ecart_type(nom_var, date1, date2) :
    return math.sqrt(variance(nom_var, date1, date2))

def mediane(nom_var, date1, date2) :
    var = titres.index(nom_var)
    periode = select_lignes(date1, date2)
    print(var)
    l_var = [ligne[var] for ligne in periode]
    i = len(l_var)//2
    return l_var[i]

def minimum(nom_var, date1, date2) :
    var = titres.index(nom_var)
    periode = select_lignes(date1, date2)
    l_var = [ligne[var] for ligne in periode]
    return (min(l_var))

def maximum(nom_var, date1, date2) :
    var = titres.index(nom_var)
    periode = select_lignes(date1, date2)
    l_var = [ligne[var] for ligne in periode]
    return (min(l_var))


##affichage des statistiques d'une variable
def displayStat(nom_var, date1, date2) :
    '''Utilise tableau, select_lignes
    affiche la courbe d'une des variables avec ses statistiques'''
    var = titres.index(nom_var)

    #RECUPERATION DE LA VARIABLE UTILE
    periode = select_lignes(date1, date2)
    l_var = [ligne[var] for ligne in periode]

    #CALCUL DES STATISTIQUES + CONVERSION EN CHAINES
    #calcul de la moyenne
    moy = "moyenne : " + str(moyenne(nom_var, date1, date2))
    #calcul de l'écart-type
    sigma = "ecart_type :" + str(ecart_type(nom_var, date1, date2))
    #calcul de la variance
    vari = "variance :" + str(variance(nom_var, date1, date2))
    #calcul de la mediane
    med = "mediane :" + str(mediane(nom_var, date1, date2))
    #calcul du minimum et du maximum
    mini = "minimum :" + str(minimum(nom_var, date1, date2))
    maxi = "maximum :" + str(maximum(nom_var, date1, date2))

    statistiques = mini + "\n" + maxi + "\n" + moy + "\n" + sigma + "\n" + vari + "\n" + med


    #AFFICHAGE DE LA COURBE
    plt.close()
    y = np.array(l_var)
    x = np.array([i for i in range(len(l_var))])

    #plt.text(0.5,0.5,statistiques,horizontalalignment='left', verticalalignment='top',bbox=dict(facecolor='black',alpha=0.5))
    plt.title(statistiques)
    plt.plot(x, y, label=nom_var)
    plt.legend()

    plt.show()

    return



##indice de corrélation
def correlation(nom_var1, nom_var2, date1, date2) :
    '''var1 et var2 les INDICES des variables (numéro de colonne)
    utilise tableau, select_lignes, moyenne et ecart_type
    affiche les courbes des variables et l'indice de corrélation, renvoie l'indice de corrélation'''
    var1 = titres.index(nom_var1)
    var2 = titres.index(nom_var2)
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
    moy1 = moyenne(nom_var1, date1, date2)
    moy2 = moyenne(nom_var2, date1, date2)

    #calcul de la covariance
    cov = moyp - moy1*moy2

    #calcul des écart-types
    sigma1 = ecart_type(nom_var1, date1, date2)
    sigma2 = ecart_type(nom_var2, date1, date2)

    #calcul du coefficient de correlation
    r = cov/(sigma1*sigma2)


    #AFFICHAGE DES DEUX COURBES
    plt.close()
    y1 = np.array(l_var1)
    y2 = np.array(l_var2)
    x = np.array([i for i in range(len(l_var1))]) #car les mesures sont prises à intervalles réguliers

    plt.plot(x, y1, label=nom_var1)
    plt.plot(x, y2, label=nom_var2)
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
        T = periode[i][titres.index("temp")]
        H = periode[i][titres.index("humidity")]
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


##COMPARAISON DES CAPTEURS

##séparation des capteurs
def capteurs() :

    def select_capteur(id) :
        capteur = []
        for ligne in tableau :
            if ligne[1] == id :
                capteur.append(ligne)
        return capteur

    l_capteurs = []
    for id in range(1, 7) :
        l_capteurs.append(select_capteur(id))
    return l_capteurs

#AFFICHAGE DES COURBES

#tri du tableau par dates croissantes
def tri() :
    tab_trie = [tableau[1]]
    for ligne in tableau :
        i = 0
        while i<len(tab_trie) and ligne[7]>=tab_trie[i][7] :
            i = i+1
        if i>=len(tab_trie) :
            tab_trie.append(ligne)
        else :
            tab_trie.insert(i, ligne)
    return tab_trie

#affichage des courbes
def display_all(nom_var) :
    var = titres.index(nom_var)
    tab_trie = tri()
    capts = [[] for i in range(6)] #une liste par capteur
    xcapts = [[] for i in range(6)] #une liste d'abcisses par capteur
    kdate = 0 #servira pour les abcisses parce que sinon ça sera pas classé par ordre croissant
    dates = [] #servira pour la légende des x
    jours = [] #légende finale avec juste les jours

    for ligne in tab_trie :
        dates.append(ligne[-1])
        kdate = kdate+1
        id = ligne[1]
        for i in range(6) : #ajout de la valeur dans la liste du capteur correspondant
            if i == id :
                capts[i].append(ligne[var])
                xcapts[i].append(kdate)


    #remplissage de la liste "jours" pour la légende
    jours.append(dates[0][:10]) #"AAAA-MM-JJ"
    mem = jours[0]
    for i in range(1,len(dates)) :
        if not re.match(mem,dates[i]) :
            jours.append(dates[i][:10])
            mem = dates[i][:10]
        else :
            jours.append("")

    #affichage sous forme de graphique
    plt.close()
    for i in range(6) :
        plt.plot(np.array(xcapts[i]), np.array(capts[i]),label="capteur "+str(i+1))
    plt.xticks(range(len(jours)), jours, rotation=45)
    plt.title(nom_var)
    plt.legend()
    plt.show()

    return




