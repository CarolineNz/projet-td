def ouvrir_fichier() :
    '''Ouvre le fichier de données et le convertit en variables exploitables
    renvoie : (titres[liste de chaines], tableau[liste de listes de données]) '''

    file = open("D:\Documents\GitHub\projet-td\EIVP_KM.csv") #à changer
    content = file.read()
    file.close()

    content = content.split("\n")
    tableau = []
    for ligne in content :
        ligne = ligne.split(";")
        tableau.append(ligne)

    titres = tableau[0]
    tableau = tableau[1:len(tableau)-1] #on enlève la première ligne (les titres) et la dernière ligne (qui est vide)

    for i in range(0, len(tableau)-1) :
        for j in range(0, 7) :
            a = tableau[i][j]
            tableau[i][j] = float(a)

    return (titres, tableau)