def analyse_positions(date1="2019-08-11 11:30:50+02:00", date2="2019-08-25 17:47:08+02:00") :
    #calcul des moyennes de chaque valeur :
    moy_co2 = moyenne_all("co2")
    moy_lum = moyenne_all("lum")
    ecarts_co2 = []
    ecarts_lum = []
    for id in range(1,7) :
        #calcul des moyennes pour le capteur :
        moy_capt_co2 = moyenne("co2",id,date1,date2)
        moy_capt_lum = moyenne("lum",id,date1,date2)
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