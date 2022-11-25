import os


class etudiant:
    def __init__(self, numero, nom, prenom, age, moyenne, mention):
        self.numero = numero
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.moyenne = moyenne
        self.mention = mention

    def all_etudiant(self):
        return self.nom+" "+self.prenom+" "+self.age+" "+self.moyenne+" "+self.mention+"\n"


def create_liste_etudiant(nb_etu):
    liste_etu = []
    for i in range(nb_etu):
        liste_etu.append(etudiant(i+1, input("Nom ?"), input("Prénom ?"), int(
            input("Âge ?")), int(input("Moyenne ?"))))
    return liste_etu


def mention_etudiant(moyenne):
    if (moyenne < 10):
        return "Insuffisant"
    elif (moyenne >= 10 and moyenne < 12):
        return "Passable"
    elif (moyenne >= 12 and moyenne < 14):
        return "AB"
    elif (moyenne >= 14 and moyenne < 16):
        return "B"
    elif (mention >= 16 and moyenne <= 20):
        return "TB"


def admis():
    try:
        fopen("Admis_STRI.txt", "w")
    except IOError:
        print("Erreur lors de la création du fichier")
    else:
        liste_etudiant = create_liste_etudiant()
# def attente()


# def calc_pourcent()


# def tri_admis()


# def gest_affich()
