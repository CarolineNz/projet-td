
def displayStat(var, date1, date2) :
    '''var INDICE de la variable (numéro de colonne)
    Utilise tableau, select_lignes
    affiche la courbe d'une des variables avec ses statistiques'''
    
    #RECUPERATION DE LA VARIABLE UTILE
    periode = select_lignes(date1, date2)
    l_var = [ligne[var] for ligne in period]

    #CALCUL DES STATISTIQUES
    #calcul de la moyenne
    moy = "moyenne : " + moyenne(var, date1, date2)
    #calcul de l'écart-type
    sigma = "ecart_type :" + ecart_type(var, date1, date2)
    #calcul de la variance
    var = "variance :" + variance(var, date1, date2)
    #calcul de la mediane
    med = "mediane :" + mediane(var, date1, date2)
    #calcul du minimum et du maximum
    mini = "minimum :" + minimum(var, date1, date2)
    maxi = "maximum :" + maximum(var, date1, date2)

    statistiques = mini + "\n" + maxi + "\n" + moy + "\n" + sigma + "\n" + var + "\n" + med
    
    
    #AFFICHAGE DE LA COURBE
    plt.close()
    y = np.array(l_var)
    x = np.array([i for i in range(len(l_var))]) 

    plt.text(0.5,0.5,statistiques,horizontalalignment='left',
             verticalalignment='top',bbox=dict(facecolor='black',alpha=0.5))

    plt.plot(x, y, label=titres[var])
    plt.legend()
 
    plt.show()
