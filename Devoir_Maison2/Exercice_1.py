import os


def mot_commun(fichier1, fichier2):
    # Inscription du chemin absolu dans une variable
    chemin_princ = os.path.realpath(__file__)
    chemin_princ = chemin_princ.replace(os.path.basename(__file__), '')
    if (fichier1 != fichier2):  # On vérifie que les fichiers ne sont pas identiques
        # On vérifie la véracité des fichiers
        if (os.path.isfile(chemin_princ+fichier1) or os.path.isfile(chemin_princ+fichier2)):
            try:  # Ouverture des fichiers avec exception
                file1 = open(chemin_princ+fichier1)
                file2 = open(chemin_princ+fichier2)
            except IOError:
                print("Veuillez vérifier le chemin du fichier ou son existence")
            else:
                texte1 = file1.read()  # On met l'entiereté des fichiers dans des variables
                texte2 = file2.read()
                # On enlève les séparateurs de texte1 et texte2 puis mise en liste des mots obtenus
                liste_mot1 = texte1.split()
                liste_mot2 = texte2.split()
                # Création d'une liste vide qui affichera les mots communs des deux fichiers
                liste_commun = []
                # Pour chaque mot dans une liste on teste la correspondance
                for i in range(len(liste_mot1)):
                    for j in range(len(liste_mot2)):
                        if (liste_mot1[i] == liste_mot2[j]):
                            # S'il y a correspondance entre deux mots on les mets dans la liste
                            liste_commun.append(liste_mot2[j])
            finally:
                # Fermeture des deux fichiers même si échec d'ouverture.
                file1.close()
                file2.close()
                print(liste_commun)  # Affichage de la liste des mots communs
        else:
            print("Fichiers introuvables !")  # Gestion d'erreur
    else:
        print("Impossible de lancer le programme les fichiers sont identiques !")


mot_commun(input("Entrez le chemin du premier fichier :\n"),
           input("Entrez le chemin du second fichier :\n"))
