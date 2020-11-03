def moyenne(var, date1, date2) :
    periode = select_lignes(date1, date2)
    l_var = [ligne[var] for ligne in periode]
    moy = 0
    for e in l_var :
        moy = moy+e
    moy = moy/len(l_var)
    return moy

def variance(var, date1, date2) :
    periode = select_lignes(date1, date2)
    l_var = [ligne[var] for ligne in periode]
    vari = 0
    moy = moyenne(var, date1, date2)
    for e in l_var :
        vari = vari + pow(e-moy, 2)
    vari = vari/len(l_var)
    return vari

def ecart_type(var, date1, date2) :
    return sqrt(variance(var, date1, date2))

def mediane(var, date1, date2) :
    periode = select_lignes(date1, date2)
    l_var = [ligne[var] for ligne in periode]
    i = len(l_var)//2
    return l_var[i]

def minimum(var, date1, date2) :
    periode = select_lignes(date1, date2)
    l_var = [ligne[var] for ligne in periode]
    return (min(l_var))

def maximum(var, date1, date2) :
    periode = select_lignes(date1, date2)
    l_var = [ligne[var] for ligne in periode]
    return (min(l_var))