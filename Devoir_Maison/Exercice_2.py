from itertools import count


def adnValide():
    chaine = input()
    for i in range(len(chaine)-1):
        if (chaine[i] not in ('a', 'c', 't', 'g')):
            adnValide()
    return chaine


def occAdn():
    print("Entrez une chaine ADN:\n")
    chaine = str(adnValide())
    print("Entrez la sous chaine ADN:\n")
    sschaine = str(adnValide())
    return chaine.count(sschaine)


print("Nombre d'occurence : ", occAdn())
