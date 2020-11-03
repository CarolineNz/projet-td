
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
