def analyse_positions() :
    l_capteurs = capteurs()
    #calcul des moyennes de chaque valeur :
    moy_co2 = moyenne("co2")
    moy_lum = moyenne("lum")
    ecarts_co2 = []
    ecarts_lum = []
    for capt in l_capteurs :
        #calcul des moyennes pour le capteur :
        moy_capt_co2=0
        moy_capt_lum=0
        i_co2 = titres.index("co2")
        i_lum = titres.index("lum")
        for ligne in capt :
            moy_capt_co2 = moy_capt_co2+ligne[i_co2]
            moy_capt_lum = moy_capt_lum+ligne[i_lum]
        moy_capt_co2 = moy_capt_co2/len(capt)
        moy_capt_lum = moy_capt_lum/len(capt)
        #calcul des écarts aux moyennes pour ce capteur :
        ecarts_co2.append(moy_co2-moy_capt_co2)
        ecarts_lum.append(moy_lum-moy_capt_lum)

    #affichage :
    plt.clf()
    for i in range(6) :
        #un point de couleur par capteur
        plt.scatter(ecarts_co2[i], ecarts_lum[i], label="capteur"+str(i+1))
    plt.legend()
    axes = plt.gca()

    #affichages d'axes x=0 et y=0
    axes = plt.gca()
    xmin, xmax = axes.get_xlim()
    plt.plot([xmin, xmax],[0, 0], color="k")
    ymin, ymax = axes.get_ylim()
    plt.plot([0, 0], [ymin, ymax], color="k")

    #affichage du texte
    plt.text(xmin,2, "Loin de la rue")
    plt.text(xmax-10,2, "Près de la rue")
    plt.text(0,ymin, "Nord")
    plt.text(0,ymax, "Sud")

    plt.title("Analyse en fonction du co2 et de la luminosité")
    plt.show()


    return
