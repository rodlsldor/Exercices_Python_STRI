# MARCHE PAS POUR L'INSTANT
MAX = 8
# fonctions


def calcul(d, n):
    """Calcul recursif du nombre de facons de faire <n> avec <d> des."""

    resultat, debut = 0, 1
    if d == 1 or n == d or n == 6*d:  # conditions terminales
        return 1
    else:  # sinon appels recursifs
        if n > 6*(d-1):  # optimisation importante
            debut = n - 6*(d-1)
            for i in range(debut, 7):
                if n == i:
                    break
        resultat += calcul(d-1, n-i)
    return resultat


# programme principal -----------------------------------------------
nbd = int(input("Nombre de des entre 2 et {} : ".format(MAX)))
while not (2 <= nbd <= MAX):
    nbd = int(input("Nombre de des entre 2 et {}, s.v.p. : ".format(MAX)))
s = int(input("Entrez un entier entre {} et {} : ".format(nbd, 6*nbd)))
while not (nbd <= s <= 6*nbd):
    s = int(input("Entrez un entier entre {} et {}, s.v.p. : ".format(nbd, 6*nbd)))
print("Il y a {} facon(s) de faire {} avec {} des.".format(calcul(nbd, s), s, nbd))
