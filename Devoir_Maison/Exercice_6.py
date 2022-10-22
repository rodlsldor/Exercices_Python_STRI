from pylab import *


def creatMatricepaire(nbrN):
    matrice = [nbrN][nbrN]
    nbr = 0
    for i in range(nbrN-1):
        for j in range(nbrN-1):
            matrice[i].append(nbr)
            nbr += 2

    return matrice


def createMatriceDiag(nbrN):
    matrice = [nbrN][nbrN]
    for i in range(nbrN-1):
        for j in range(nbrN-1):
            if (i == j):
                matrice[i].append(1)
            else:
                matrice[i].append(0)

    return matrice


def calculMatrice(matrice1, matrice2, multipl1, multipl2):
    matrice1 = multipl1*matrice1
    matrice2 = multipl2*matrice2

    matrice = matrice1+matrice2

    return matrice


print(calculMatrice(creatMatricepaire(int(input("Entrez le nombre de lignes/colonnes"))),
      createMatriceDiag(int(input("Entrez le nombre de lignes/colonnes"))), 2, 2))
