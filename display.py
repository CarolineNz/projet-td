def display(nom_var, id, date1="2019-08-11 11:30:50+02:00", date2="2019-08-25 17:47:08+02:00") :
    '''Utilise tableau, select_lignes
    affiche la courbe d'une des variables'''
    var = titres.index(nom_var)
    
    #RECUPERATION DE LA VARIABLE UTILE
    periode = select_lignes(id, date1, date2)
    l_var = [ligne[var] for ligne in periode]

    #Tiré de la fonction DisplayAll
    #Permet de mettre des dates comme abscisse
    #long à executer mais plus élégant
    dates = [] 
    jours = [] 
    for ligne in periode :
        dates.append(ligne[-1])
    jours.append(dates[0][:10]) #"AAAA-MM-JJ"
    mem = jours[0]
    for i in range(1,len(dates)) :
        if not re.match(mem,dates[i]) :
            jours.append(dates[i][:10])
            mem = dates[i][:10]
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