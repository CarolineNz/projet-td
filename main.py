import numpy as np
import matplotlib.pyplot as plt
import math
import re


##OUVERTURE DU FICHIER
def ouvrir_fichier() :
    '''Ouvre le fichier de données et le convertit en variables exploitables
    renvoie : (titres[liste de chaines], tableau[liste de listes de données]) '''

    file = open("EIVP_KM.csv")
    content = file.read()
    file.close()

    content = content.split("\n")
    tableau = []
    for ligne in content :
        ligne = ligne.split(";")
        tableau.append(ligne)

    titres = tableau[0]
    tableau = tableau[1:len(tableau)-1] #on enlève la première ligne (les titres) et la dernière ligne (qui est vide)

    for i in range(0, len(tableau)) :
        for j in range(0, 7) :
            a = tableau[i][j]
            tableau[i][j] = float(a)

    return (titres, tableau)

(titres, tableau) = ouvrir_fichier()

#tri d'un tableau par valeurs de dates croissantes
def tri(tab) :
    tab_trie = [tab[1]]
    for ligne in tab :
        i = 0
        while i<len(tab_trie) and ligne[7]>=tab_trie[i][7] :
            i = i+1
        if i>=len(tab_trie) :
            tab_trie.append(ligne)
        else :
            tab_trie.insert(i, ligne)
    return tab_trie

tableau = tri(tableau)

##SELECTION DE DONNES
#sélection du tableau associé à un capteur donné
def select_capteur(id) :
    capteur = []
    for ligne in tableau :
        if int(ligne[1]) == int(id) :
            capteur.append(ligne)
    return capteur


#séparation des capteurs
def capteurs() :
    l_capteurs = []
    for id in range(1, 7) :
        l_capteurs.append(select_capteur(id))
    return l_capteurs

#sélection d'une durée entre deux dates pour un capteur donné
def select_lignes(id, date1, date2) :
    '''Crée un nouveau tableau "periode" avec les lignes du tableau de base comprises entre les deux dates incluses '''
    if date1=="2019-08-11 11:30:50+02:00" and date2=="2019-08-25 17:47:08+02:00" :
        return select_capteur(id)
    else :
        periode = []
        for ligne in select_capteur(id) :
            if ligne[-1]>=date1 and ligne[-1]<=date2 :
                periode.append(ligne)
        return periode



#sélection d'une durée entre deux dates pour tous les capteurs
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



##FONCTIONS DE BASE
##stats pour une variable, un capteur, et sur une période de temps donnée
def moyenne(id, nom_var, date1="2019-08-11 11:30:50+02:00", date2="2019-08-25 17:47:08+02:00") :
    var = titres.index(nom_var)
    periode = select_lignes(id, date1, date2)
    l_var = [ligne[var] for ligne in periode]
    moy = 0
    for e in l_var :
        moy = moy+e
    moy = moy/len(l_var)
    return moy

def variance(id, nom_var, date1="2019-08-11 11:30:50+02:00", date2="2019-08-25 17:47:08+02:00") :
    var = titres.index(nom_var)
    periode = select_lignes(id, date1, date2)
    l_var = [ligne[var] for ligne in periode]
    vari = 0
    moy = moyenne(id, nom_var, date1, date2)
    for e in l_var :
        vari = vari + pow(e-moy, 2)
    vari = vari/len(l_var)
    return vari

def ecart_type(id, nom_var, date1="2019-08-11 11:30:50+02:00", date2="2019-08-25 17:47:08+02:00") :
    return math.sqrt(variance(id, nom_var, date1, date2))

def mediane(id, nom_var, date1="2019-08-11 11:30:50+02:00", date2="2019-08-25 17:47:08+02:00") :
    var = titres.index(nom_var)
    periode = select_lignes(id, date1, date2)
    l_var = [ligne[var] for ligne in periode]
    i = len(l_var)//2
    return l_var[i]

def minimum(id, nom_var, date1="2019-08-11 11:30:50+02:00", date2="2019-08-25 17:47:08+02:00") :
    var = titres.index(nom_var)
    periode = select_lignes(id, date1, date2)
    l_var = [ligne[var] for ligne in periode]
    return (min(l_var))

def maximum(id, nom_var, date1="2019-08-11 11:30:50+02:00", date2="2019-08-25 17:47:08+02:00") :
    var = titres.index(nom_var)
    periode = select_lignes(id, date1, date2)
    l_var = [ligne[var] for ligne in periode]
    return (max(l_var))



##stats pour une variable, pour l'ensemble des capteurs, sur une période de temps donnée
def moyenne_all(nom_var, date1="2019-08-11 11:30:50+02:00", date2="2019-08-25 17:47:08+02:00") :
    var = titres.index(nom_var)
    periode = select_lignes_all(date1, date2)
    l_var = [ligne[var] for ligne in periode]
    moy = 0
    for e in l_var :
        moy = moy+e
    moy = moy/len(l_var)
    return moy

def variance_all(nom_var, date1="2019-08-11 11:30:50+02:00", date2="2019-08-25 17:47:08+02:00") :
    var = titres.index(nom_var)
    periode = select_lignes_all(date1, date2)
    l_var = [ligne[var] for ligne in periode]
    vari = 0
    moy = moyenne_all(nom_var, date1, date2)
    for e in l_var :
        vari = vari + pow(e-moy, 2)
    vari = vari/len(l_var)
    return vari

def ecart_type_all(nom_var, date1="2019-08-11 11:30:50+02:00", date2="2019-08-25 17:47:08+02:00") :
    return math.sqrt(variance_all(nom_var, date1, date2))

def mediane_all(nom_var, date1="2019-08-11 11:30:50+02:00", date2="2019-08-25 17:47:08+02:00") :
    var = titres.index(nom_var)
    periode = select_lignes_all( date1, date2)
    l_var = [ligne[var] for ligne in periode]
    i = len(l_var)//2
    return l_var[i]

def minimum_all(nom_var, date1="2019-08-11 11:30:50+02:00", date2="2019-08-25 17:47:08+02:00") :
    var = titres.index(nom_var)
    periode = select_lignes_all(date1, date2)
    l_var = [ligne[var] for ligne in periode]
    return (min(l_var))

def maximum_all(nom_var, date1="2019-08-11 11:30:50+02:00", date2="2019-08-25 17:47:08+02:00") :
    var = titres.index(nom_var)
    periode = select_lignes_all(date1, date2)
    l_var = [ligne[var] for ligne in periode]
    return (max(l_var))



##affichage des courbes
#affichage de la courbe d'une variable pour un capteur
def display(id, nom_var, date1="2019-08-11 11:30:50+02:00", date2="2019-08-25 17:47:08+02:00") :
    '''Utilise tableau, select_lignes
    affiche la courbe d'une des variables'''
    var = titres.index(nom_var)

    #RECUPERATION DE LA VARIABLE UTILE
    periode = select_lignes(id, date1, date2)
    l_var = [ligne[var] for ligne in periode]

    #Permet de mettre des jours comme abscisse
    #long à executer mais plus élégant
    jours = []
    jours.append(periode[0][7][:10]) #"AAAA-MM-JJ"
    mem = jours[0]
    for i in range(len(periode)) :
        if not re.match(mem,periode[i][7]) :
            jours.append(periode[i][7][:10])
            mem = periode[i][7][:10]
        else :
            jours.append("")

    #AFFICHAGE DE LA COURBE
    plt.close()
    y = np.array(l_var)
    x = np.array([i for i in range(len(l_var))])

    plt.plot(x, y, label=titres[var])
    plt.xticks(range(len(jours)), jours, rotation=45)
    plt.ylabel(nom_var)
    plt.legend()

    plt.show()


#affichage pour une variable tous capteurs confondus    (note : pas pertinent)
def display_all(nom_var, date1="2019-08-11 11:30:50+02:00", date2="2019-08-25 17:47:08+02:00") :
    '''Utilise tableau, select_lignes
    affiche la courbe d'une des variables'''
    var = titres.index(nom_var)

    #RECUPERATION DE LA VARIABLE UTILE
    periode = select_lignes_all(date1, date2)
    l_var = [ligne[var] for ligne in periode]


    #Permet de mettre des jours comme abscisse
    #long à executer mais plus élégant
    jours = []
    jours.append(periode[0][7][:10]) #"AAAA-MM-JJ"
    mem = jours[0]
    for i in range(len(periode)) :
        if not re.match(mem,periode[i][7]) :
            jours.append(periode[i][7][:10])
            mem = periode[i][7][:10]
        else :
            jours.append("")

    #AFFICHAGE DE LA COURBE
    plt.close()
    y = np.array(l_var)
    x = np.array([i for i in range(len(l_var))])

    plt.plot(x, y, label=titres[var])
    plt.xticks(range(len(jours)), jours, rotation=45)
    plt.ylabel(nom_var)
    plt.legend()

    plt.show()

#affichage de toutes les courbes de chaque capteur en parallèle
def display_capts(nom_var, date1="2019-08-11 11:30:50+02:00", date2="2019-08-25 17:47:08+02:00") :
    var = titres.index(nom_var)
    periode = select_lignes_all(date1, date2)
    capts = [[] for i in range(6)] #une liste par capteur
    xcapts = [[] for i in range(6)] #une liste d'abcisses par capteur
    kdate = 0 #servira pour les abcisses parce que sinon ça sera pas classé par ordre croissant
    dates = [] #servira pour la légende des x
    jours = [] #légende finale avec juste les jours

    for ligne in periode :
        dates.append(ligne[-1])
        kdate = kdate+1
        id = ligne[1]
        for i in range(6) : #ajout de la valeur dans la liste du capteur correspondant
            if i == id :
                capts[i].append(ligne[var])
                xcapts[i].append(kdate)

    #Permet de mettre des jours comme abscisse
    #long à executer mais plus élégant
    jours = []
    jours.append(periode[0][7][:10]) #"AAAA-MM-JJ"
    mem = jours[0]
    for i in range(len(periode)) :
        if not re.match(mem,periode[i][7]) :
            jours.append(periode[i][7][:10])
            mem = periode[i][7][:10]
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


##affichage des statistiques d'une variable
def display_stat(id,nom_var, date1="2019-08-11 11:30:50+02:00", date2="2019-08-25 17:47:08+02:00") :
    '''Utilise tableau, select_lignes
    affiche la courbe d'une des variables avec ses statistiques'''
    var = titres.index(nom_var)

    #RECUPERATION DE LA VARIABLE UTILE
    periode = select_lignes(id, date1, date2)
    l_var = [ligne[var] for ligne in periode]

    #CALCUL DES STATISTIQUES + CONVERSION EN CHAINES
    #calcul de la moyenne
    moy = "moyenne : " + str(round(moyenne(id, nom_var, date1, date2),2))
    #calcul de l'écart-type
    sigma = "ecart_type :" + str(round(ecart_type(id, nom_var, date1, date2),2))
    #calcul de la variance
    vari = "variance :" + str(round(variance(id, nom_var, date1, date2),2))
    #calcul de la mediane
    med = "mediane :" + str(mediane(id, nom_var, date1, date2))
    #calcul du minimum et du maximum
    mini = "minimum :" + str(minimum(id, nom_var, date1, date2))
    maxi = "maximum :" + str(maximum(id, nom_var, date1, date2))

    statistiques = "\n" + sigma + "\n" + vari

    #Création des courbes à afficher
    plt.close()
    y = np.array(l_var)
    x = np.array([i for i in range(len(l_var))])

    y_moy = np.array([moyenne(id, nom_var, date1, date2)]*len(l_var))
    y_med = np.array([mediane(id, nom_var, date1, date2)]*len(l_var))
    y_max = np.array([maximum(id, nom_var, date1, date2)]*len(l_var))
    y_min = np.array([minimum(id, nom_var, date1, date2)]*len(l_var))

    #Permet de mettre des jours comme abscisse
    #long à executer mais plus élégant
    jours = []
    jours.append(periode[0][7][:10]) #"AAAA-MM-JJ"
    mem = jours[0]
    for i in range(len(periode)) :
        if not re.match(mem,periode[i][7]) :
            jours.append(periode[i][7][:10])
            mem = periode[i][7][:10]
        else :
            jours.append("")

    #affichage sous forme de graphiques
    plt.title('Statistiques' + statistiques)
    plt.plot(x, y, label=nom_var)
    plt.plot(x,y_moy,label = moy)
    plt.plot(x,y_med,label = med)
    plt.plot(x,y_max,label = maxi)
    plt.plot(x,y_min,label = mini)
    plt.xticks(range(len(jours)), jours, rotation=45)
    plt.ylabel(nom_var)
    plt.legend(loc='center left',bbox_to_anchor=(1,0.5))

    plt.show()

    return


##INDICE HUMIDEX
#pour un capteur donné
def humidex(id, date1="2019-08-11 11:30:50+02:00", date2="2019-08-25 17:47:08+02:00") :
    '''utilise tableau, select_lignes
    affiche la courbe de l'humidex sur la période donnée
    renvoie l'humidex moyen'''
    periode = select_lignes(id, date1,date2)

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

    #Permet de mettre des jours comme abscisse
    #long à executer mais plus élégant
    jours = []
    jours.append(periode[0][7][:10]) #"AAAA-MM-JJ"
    mem = jours[0]
    for i in range(len(periode)) :
        if not re.match(mem,periode[i][7]) :
            jours.append(periode[i][7][:10])
            mem = periode[i][7][:10]
        else :
            jours.append("")

    #affichage sous forme de graphique
    plt.close()
    x = np.array([i for i in range(len(l_hum))]) #car les mesures sont prises à intervalles réguliers
    y1 = np.array(l_hum)
    y2 = np.array([hum_moy for i in range (len(l_hum))])
    plt.plot(x, y1, label="humidex")
    plt.plot(x, y2, label="humidex moyen")
    plt.title("Humidex moyen : "+str(hum_moy))
    plt.xticks(range(len(jours)), jours, rotation=45)
    plt.legend()
    plt.show()

    return hum_moy

#Pour tous les capteurs :
def humidex_all():
    resultat=0
    for i in range(1,7):
        resultat+=humidex(i)
    return resultat/6



##INDICE DE CORRELATION

def correlation(id, nom_var1, nom_var2, date1="2019-08-11 11:30:50+02:00", date2="2019-08-25 17:47:08+02:00") :
    '''var1 et var2 les INDICES des variables (numéro de colonne)
    utilise tableau, select_lignes, moyenne et ecart_type
    affiche les courbes des variables et l'indice de corrélation, renvoie l'indice de corrélation'''
    var1 = titres.index(nom_var1)
    var2 = titres.index(nom_var2)
    periode = select_lignes(id, date1, date2)

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
    moy1 = moyenne(id, nom_var1, date1, date2)
    moy2 = moyenne(id, nom_var2, date1, date2)

    #calcul de la covariance
    cov = moyp - moy1*moy2

    #calcul des écart-types
    sigma1 = ecart_type(id, nom_var1, date1, date2)
    sigma2 = ecart_type(id, nom_var2, date1, date2)

    #calcul du coefficient de correlation
    r = round(cov/(sigma1*sigma2),2)

    #Permet de mettre des jours comme abscisse
    #long à executer mais plus élégant
    jours = []
    jours.append(periode[0][7][:10]) #"AAAA-MM-JJ"
    mem = jours[0]
    for i in range(len(periode)) :
        if not re.match(mem,periode[i][7]) :
            jours.append(periode[i][7][:10])
            mem = periode[i][7][:10]
        else :
            jours.append("")

    #AFFICHAGE DES DEUX COURBES
    plt.close()
    y1 = np.array(l_var1)
    y2 = np.array(l_var2)
    x = np.array([i for i in range(len(l_var1))]) #car les mesures sont prises à intervalles réguliers

    #affichages avec deux ordonnées à échelles différentes :
    c1 = plt.plot(x, y1, color="blue")
    plt.legend(c1,[nom_var1], loc = 'upper left')
    plt.xticks(range(len(jours)), jours, rotation=45)
    ax2 = plt.gca().twinx()



    c2=ax2.plot(x, y2, color="orange")
    plt.legend(c2,[nom_var2],loc='upper right')
    #ax2.xticks(range(len(jours)), jours, rotation=45)
    plt.title("Coefficient de corrélation : "+str(r))

    plt.show()

    return r


def correlation_all(nom_var1, nom_var2, date1="2019-08-11 11:30:50+02:00", date2="2019-08-25 17:47:08+02:00") :
    '''var1 et var2 les INDICES des variables (numéro de colonne)
    utilise tableau, select_lignes, moyenne et ecart_type
    renvoie l'indice de corrélation'''
    var1 = titres.index(nom_var1)
    var2 = titres.index(nom_var2)
    periode = select_lignes_all(date1, date2)

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
    moy1 = moyenne_all(nom_var1, date1, date2)
    moy2 = moyenne_all(nom_var2, date1, date2)

    #calcul de la covariance
    cov = moyp - moy1*moy2

    #calcul des écart-types
    sigma1 = ecart_type_all(nom_var1, date1, date2)
    sigma2 = ecart_type_all(nom_var2, date1, date2)

    #calcul du coefficient de correlation
    r = cov/(sigma1*sigma2)

    #AFFICHAGE DES DEUX COURBES
    plt.close()
    y1 = np.array(l_var1)
    y2 = np.array(l_var2)
    x = np.array([i for i in range(len(l_var1))]) #car les mesures sont prises à intervalles réguliers

    #Permet de mettre des jours comme abscisse
    #long à executer mais plus élégant
    jours = []
    jours.append(periode[0][7][:10]) #"AAAA-MM-JJ"
    mem = jours[0]
    for i in range(len(periode)) :
        if not re.match(mem,periode[i][7]) :
            jours.append(periode[i][7][:10])
            mem = periode[i][7][:10]
        else :
            jours.append("")

    #affichages avec deux ordonnées à échelles différentes :
    c1 = plt.plot(x, y1, color="blue")
    plt.legend(c1,[nom_var1], loc = 'upper left')
    plt.xticks(range(len(jours)), jours, rotation=45)
    ax2 = plt.gca().twinx()



    c2=ax2.plot(x, y2, color="orange")
    plt.legend(c2,[nom_var2],loc='upper right')
    #ax2.xticks(range(len(jours)), jours, rotation=45)
    plt.title("Coefficient de corrélation : "+str(r))

    plt.show()

    return r




##PROBLEME OUVERT : POSITION DES CAPTEURS
#comparaison : au dessus/en dessous de la moyenne pour chaque capteur
def analyse_moy(nom_var, date1="2019-08-11 11:30:50+02:00", date2="2019-08-25 17:47:08+02:00"):
    sup=[]
    inf=[]
    for i in range(1,6):
        if moyenne(i,nom_var,date1,date2)>=moyenne_all(nom_var,date1,date2):
            sup.append(i)
        else :
            inf.append(i)
    print("Supérieur à la moyenne :",sup)
    print("Inférieur à la moyenne :",inf)
    return

def analyse_moy_all():
    for i in titres[2:-1]:
        print(i)
        analyse_moy(i)
        print("\n")

    return

def analyse_position(date1="2019-08-11 11:30:50+02:00", date2="2019-08-25 17:47:08+02:00") :
    #calcul des moyennes de chaque valeur :
    moy_co2 = moyenne_all("co2")
    moy_lum = moyenne_all("lum")
    ecarts_co2 = []
    ecarts_lum = []
    for id in range(1,7) :
        #calcul des moyennes pour le capteur :
        moy_capt_co2 = moyenne(id,"co2",date1,date2)
        moy_capt_lum = moyenne(id,"lum",date1,date2)
        #calcul des écarts aux moyennes pour ce capteur :
        ecarts_co2.append(moy_capt_co2-moy_co2)
        ecarts_lum.append(moy_capt_lum-moy_lum)

    #affichage :
    plt.clf()
    for i in range(6) :
        #un point de couleur par capteur
        plt.scatter(ecarts_co2[i], ecarts_lum[i], label="capteur"+str(i+1))
    plt.legend()
    axes = plt.gca()

    #affichages d'axes x=0 et y=0
    axes = plt.gca()
    xmin, xmax = axes.get_xlim()
    plt.plot([xmin, xmax],[0, 0], color="k")
    ymin, ymax = axes.get_ylim()
    plt.plot([0, 0], [ymin, ymax], color="k")

    #affichage du texte
    plt.text(xmin,2, "Loin de la rue")
    plt.text(xmax-10,2, "Près de la rue")
    plt.text(0,ymin, "Nord")
    plt.text(0,ymax, "Sud")
    plt.title("Analyse en fonction du co2 et de la luminosité")

    plt.show()


    return