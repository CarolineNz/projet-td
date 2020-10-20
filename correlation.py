def correlation(var1, var2, date1, date2) :
    '''var1 et var2 les INDICES des variables (numéro de colonne)
    Utilise tableau, select_lignes, moyenne et ecart_type
    affiche les courbes des deux variables avec le coeff de corrélation, et renvoie le coeff de corrélation'''
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
    moy1 = moyenne(var1, date1, date2)
    moy2 = moyenne(var2, date1, date2)

    #calcul de la covariance
    cov = moyp - moy1*moy2

    #calcul des écart-types
    sigma1 = ecart_type(var1, date1, date2)
    sigma2 = ecart_type(var2, date1, date2)

    #calcul du coefficient de correlation
    r = cov/(sigma1*sigma2)


    #AFFICHAGE DES DEUX COURBES
    plt.close()
    y1 = np.array(l_var1)
    y2 = np.array(l_var2)
    x = np.array([i for i in range(len(l_var1))]) #car les mesures sont prises à intervalles réguliers

    plt.plot(x, y1, label=titres[var1])
    plt.plot(x, y2, label=titres[var2])
    plt.legend()
    plt.title("Coefficient de corrélation : "+str(r))
    plt.show()

    return r