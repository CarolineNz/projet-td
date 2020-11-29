def display_all(nom_var, date1="2019-08-11 11:30:50+02:00", date2="2019-08-25 17:47:08+02:00") :
    '''Utilise tableau, select_lignes
    affiche la courbe d'une des variables'''
    var = titres.index(nom_var)
    
    #RECUPERATION DE LA VARIABLE UTILE
    periode = select_lignes_all(date1, date2)
    l_var = [ligne[var] for ligne in periode]

    #AFFICHAGE DE LA COURBE
    plt.close()
    y = np.array(l_var)
    x = np.array([i for i in range(len(l_var))])

    plt.plot(x, y, label=titres[var])
    plt.ylabel(nom_var)
    plt.legend()

    plt.show()