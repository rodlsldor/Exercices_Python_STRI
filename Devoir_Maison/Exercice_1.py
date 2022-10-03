nbre = int(input("Entrez un nombre quelconque supérieur à 1.\n"))


#----------------Somme Diviseurs--------------#
def somDiv(nombre):
    somDiviseur = 0
    return somDiviseur

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
    return True

#----------------Diviseur Propre-------------#


def divPropre(nombre):

    return True
