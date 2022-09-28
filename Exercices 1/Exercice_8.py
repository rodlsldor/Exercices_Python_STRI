class Employe:

    def __init__(self, nom, prenom, salaire, anciennete):
        self.nom = nom
        self.prenom = prenom
        self.salaire = salaire
        self.anciennete = anciennete

    def print_employe(self):
        print("{} {} touche {} et est dans l'entreprise depuis {} ans".format(
            self.nom, self.prenom, self.salaire, self.anciennete))


def saisir_employe():

    nom = input("Rentrez le nom de votre employé : ")
    prenom = input("Rentrez le prenom de l'employé : ")
    salaire = int(input("Rentrez le salaire de l'employé : "))
    anciennete = int(input("Rentrez l'anciennete de l'employé : "))
    print("")

    return Employe(nom, prenom, salaire, anciennete)


def melanchon(liste_employe):

    for i in range(0, len(liste_employe)):

        liste_employe[i].salaire *= 1.02
        if (liste_employe[i].anciennete > 4):
            liste_employe[i].salaire += 200

    return liste_employe


liste_employe = []
nombre_employe = int(input("Rentrez le nombre d'employe : "))
print("")

if (nombre_employe > 0):

    for i in range(0, nombre_employe):

        liste_employe.append(saisir_employe())

    melanchon(liste_employe)

    for i in range(0, nombre_employe):
        liste_employe[i].print_employe()
