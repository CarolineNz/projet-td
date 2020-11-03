#tri du tableau par dates croissantes
def tri() :
    tab_trie = [tableau[0]]
    for ligne in tableau :
        i = 0
        while i<len(tab_trie) and ligne[6]>=tab_trie[i][6] :
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
    x = []
    blep = 0
    capts = [[] for i in range(6)] #une liste par capteur
    for ligne in tab_trie :
        blep = blep+1
        x.append(blep)
        id = ligne[0]
        for i in range(6) : #ajout de la valeur dans la liste du capteur correspondant, et de None dans les autres
            if i == id :
                capts[i].append(ligne[var])
            else :
                capts[i].append(None)

    #affichage sous forme de graphique
    plt.close()
    for i in range(6) :
        plt.scatter(x, capts[i], s=2, label=str("capteur "+str(i+1)))
    plt.title(nom_var)
    plt.legend()
    plt.show()

    return