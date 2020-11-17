def correlation(nom_var1, nom_var2, date1="2019-08-11 11:30:50+02:00", date2="2019-08-25 17:47:08+02:00") :
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