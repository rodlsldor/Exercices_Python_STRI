nbre = int(input("Entrez un nombre quelconque supérieur à 1.\n"))


#----------------Nombre Parfait----------------#


def estParfait(nombre):
    if (nombre != somDiv(nombre)):
        return False
    return True

#----------------Nombre Premiers----------------#


def estPremier(nombre):
    if (nombre > 1):
        nbDiviseur = 0
        for i in nombre:
            if (i % nombre == 0):
                nbDiviseur += 1
        if (nbDiviseur > 1):
            return False
    return True

#------------------Nombre Chanceux--------------#


def estChanceux(nombre):
        for i
    return True

#----------------Diviseur Propre-------------#


def divPropre(nombre):
    liste = []
    for i in nombre:
        if (nombre % i == 0):
            liste.append(i)
    return liste

#----------------Somme Diviseurs--------------#
def somDiv(nombre):
    somDiviseur = 0
    for i in range(divPropre(nombre)-1):
        somDiviseur += divPropre(nombre)[i]
    return somDiviseur