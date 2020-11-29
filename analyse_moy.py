def analyse_moy(nom_var, date1="2019-08-11 11:30:50+02:00", date2="2019-08-25 17:47:08+02:00"):
    sup=[]
    inf=[]
    for i in range(1,6):
        if moyenne(nom_var,i,date1,date2)>=moyenne_all(nom_var,date1,date2):
            sup.append(i)
        else :
            inf.append(i)
    print("Supérieur à la moyenne :",sup)
    print("Inférieur à la moyenne :",inf)
    return

def analyse_moy_all():
    for i in titres[2:-1]:
        print(i)
        analyse_moy(i)
        print("\n")

    return