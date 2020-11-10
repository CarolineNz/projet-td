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