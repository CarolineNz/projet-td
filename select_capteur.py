def select_capteur(id) :
    capteur = []
    for ligne in tableau :
        if ligne[1] == id :
            capteur.append(ligne)
    return capteur