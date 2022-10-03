def creatMatricepaire(nbrN):
    matrice = [nbrN][nbrN]
    nbr = 0
    for i in range(nbrN):
        for j in range(nbrN):
            matrice[i].append(nbr)
            nbr += 2

    return matrice


def createMatriceDiag(nbrN):
    matrice = [nbrN][nbrN]
    for i in range(nbrN):
        for j in range(nbrN):
            if (i == j):
                matrice[i].append(1)
            else:
                matrice[i].append(0)

    return matrice

# def calculMatrice()
