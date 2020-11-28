def displayStat(nom_var, id, date1="2019-08-11 11:30:50+02:00", date2="2019-08-25 17:47:08+02:00") :
    '''Utilise tableau, select_lignes
    affiche la courbe d'une des variables avec ses statistiques'''
    var = titres.index(nom_var)
    
    #RECUPERATION DE LA VARIABLE UTILE
    periode = select_lignes(id, date1, date2)
    l_var = [ligne[var] for ligne in periode]

    #CALCUL DES STATISTIQUES + CONVERSION EN CHAINES
    #calcul de la moyenne
    moy = "moyenne : " + str(round(moyenne(nom_var, id, date1, date2),2))
    #calcul de l'écart-type
    sigma = "ecart_type :" + str(round(ecart_type(nom_var, id, date1, date2),2))
    #calcul de la variance
    vari = "variance :" + str(round(variance(nom_var, id, date1, date2),2))
    #calcul de la mediane
    med = "mediane :" + str(mediane(nom_var, id, date1, date2))
    #calcul du minimum et du maximum
    mini = "minimum :" + str(minimum(nom_var, id, date1, date2))
    maxi = "maximum :" + str(maximum(nom_var, id, date1, date2))

    statistiques = "\n" + sigma + "\n" + vari

    #Création des courbes à afficher
    plt.close()
    y = np.array(l_var)
    x = np.array([i for i in range(len(l_var))])
    
    y_moy = np.array([moyenne(nom_var, id, date1, date2)]*len(l_var))
    y_med = np.array([mediane(nom_var, id, date1, date2)]*len(l_var))
    y_max = np.array([maximum(nom_var, id, date1, date2)]*len(l_var))
    y_min = np.array([minimum(nom_var, id, date1, date2)]*len(l_var))

    #Permet de mettre des dates en abscisse
    #long à executer mais plus élégant
    dates = [] 
    jours = [] 
    for ligne in select_lignes(id,date1,date2) :
        dates.append(ligne[-1])
    jours.append(dates[0][:10]) #"AAAA-MM-JJ"
    mem = jours[0]
    for i in range(1,len(dates)) :
        if not re.match(mem,dates[i]) :
            jours.append(dates[i][:10])
            mem = dates[i][:10]
        else :
            jours.append("")

    #affichage sous forme de graphiques
    plt.title('Statistiques' + statistiques)
    plt.plot(x, y, label=nom_var)
    plt.plot(x,y_moy,label = moy)
    plt.plot(x,y_med,label = med)
    plt.plot(x,y_max,label = mini)
    plt.plot(x,y_min,label = maxi)
    plt.xticks(range(len(jours)), jours, rotation=45)
    plt.ylabel(nom_var)
    plt.legend(loc='center left',bbox_to_anchor=(1,0.5))

    plt.show()

    return