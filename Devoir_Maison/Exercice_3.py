import random


def tousDiff(listNbr):
    for i in range(len(listNbr)-1):
        if (listNbr.count(listNbr[i]) > 1):
            return False
    return True


def nbAlea():
    nbr = int(input("Entrez le nombre de nombre que vous souhaitez générer :\n"))
    liste_nbr = []
    for i in range(nbr):
        liste_nbr.append(random.randint(0, 1000))
    return liste_nbr


rep = tousDiff(nbAlea())

if (rep):
    print("Liste OK!")
else:
    print("Liste PAS OK!")
