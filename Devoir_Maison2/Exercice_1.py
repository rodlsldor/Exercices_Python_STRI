import os


def mot_commun(fichier1, fichier2):
    if (os.path.isfile(fichier1) or os.path.isfile(fichier2)):
        try:
            file1 = open(fichier1)
            file2 = open(fichier2)
        except IOError:
            print("Veuillez vérifier le chemin du fichier ou son existence")
            return -1
    else:
        print("Fichiers introuvables !")


mot_commun(input("Entrez le chemin du premier fichier\n"),
           input("Entrez le chemin du second fichier\n"))
