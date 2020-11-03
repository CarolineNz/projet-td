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