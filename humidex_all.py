def humidex_all():
    resultat=0
    for i in range(1,7):
        resultat+=humidex(i)
    return resultat/6
