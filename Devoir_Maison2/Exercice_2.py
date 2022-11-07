import os
import string


def insertion_mot(fichier, mot, pos):
    if (pos > 0):
        chemin_princ = os.path.realpath(__file__)
        chemin_princ = chemin_princ.replace(os.path.basename(__file__), '')
        if (os.path.isfile(chemin_princ+fichier)):
            try:
                file = open(chemin_princ+fichier, "r")
            except IOError:
                print(
                    "Erreur lors de l'ouverture du fichier, veuillez vérifier son accessibilité.")
            else:
                list_fic = file.readlines()
                list_fic.insert(pos-1, mot+"\n")
            finally:
                file.close()
            try:
                file = open(chemin_princ+fichier, "w")
            except IOError:
                print(
                    "Erreur lors de l'ouverture du fichier, veuillez vérfier son accessibilité.")
            else:
                fichier_fin = "".join(list_fic)
                file.write(fichier_fin)
            finally:
                file.close()
        else:
            print("Veuillez entrer le chemin relatif du fichier.")
    else:
        print("Veuillez insérer une positio positive.")


insertion_mot(input("Chemin relatif du fichier ?\n"),
              input("le mot fdp"), int(input("le chiffre fdp")))
