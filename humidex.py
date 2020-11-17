def humidex(date1="2019-08-11 11:30:50+02:00", date2="2019-08-25 17:47:08+02:00") :
    '''utilise tableau, select_lignes
    affiche la courbe de l'humidex sur la période donnée
    renvoie l'humidex moyen'''
    periode = select_lignes(date1,date2)

    #humidex = T + 5/9*(6,112*pow(10, 7,5*T/(237.7+T))*H/100-10)
    l_hum = []
    for i in range(len(periode)) :
        T = periode[i][titres.index("temp")]
        H = periode[i][titres.index("humidity")]
        l_hum.append(T + 5/9*(6.112*pow(10, 7.5*T/(237.7+T))*H/100-10))

    #moyenne sur la période donnée
    hum_moy = 0
    for h in l_hum :
        hum_moy = hum_moy+h
    hum_moy = hum_moy/len(l_hum)

    #affichage sous forme de graphique
    plt.close()
    x = np.array([i for i in range(len(l_hum))]) #car les mesures sont prises à intervalles réguliers
    y1 = np.array(l_hum)
    y2 = np.array([hum_moy for i in range (len(l_hum))])
    plt.plot(x, y1, label="humidex")
    plt.plot(x, y2, label="humidex moyen")
    plt.title("Humidex moyen : "+str(hum_moy))
    plt.legend()
    plt.show()

    return hum_moy