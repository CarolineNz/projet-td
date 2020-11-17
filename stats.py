def moyenne(nom_var, date1="2019-08-11 11:30:50+02:00", date2="2019-08-25 17:47:08+02:00") :
    var = titres.index(nom_var)
    periode = select_lignes(date1, date2)
    l_var = [ligne[var] for ligne in periode]
    moy = 0
    for e in l_var :
        moy = moy+e
    moy = moy/len(l_var)
    return moy

def variance(nom_var, date1="2019-08-11 11:30:50+02:00", date2="2019-08-25 17:47:08+02:00") :
    var = titres.index(nom_var)
    periode = select_lignes(date1, date2)
    l_var = [ligne[var] for ligne in periode]
    vari = 0
    moy = moyenne(nom_var, date1, date2)
    for e in l_var :
        vari = vari + pow(e-moy, 2)
    vari = vari/len(l_var)
    return vari

def ecart_type(nom_var, date1="2019-08-11 11:30:50+02:00", date2="2019-08-25 17:47:08+02:00") :
    return math.sqrt(variance(nom_var, date1, date2))

def mediane(nom_var, date1="2019-08-11 11:30:50+02:00", date2="2019-08-25 17:47:08+02:00") :
    var = titres.index(nom_var)
    periode = select_lignes(date1, date2)
    print(var)
    l_var = [ligne[var] for ligne in periode]
    i = len(l_var)//2
    return l_var[i]

def minimum(nom_var, date1="2019-08-11 11:30:50+02:00", date2="2019-08-25 17:47:08+02:00") :
    var = titres.index(nom_var)
    periode = select_lignes(date1, date2)
    l_var = [ligne[var] for ligne in periode]
    return (min(l_var))

def maximum(nom_var, date1="2019-08-11 11:30:50+02:00", date2="2019-08-25 17:47:08+02:00") :
    var = titres.index(nom_var)
    periode = select_lignes(date1, date2)
    l_var = [ligne[var] for ligne in periode]
    return (min(l_var))