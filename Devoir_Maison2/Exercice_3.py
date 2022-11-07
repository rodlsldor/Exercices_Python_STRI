import os


def saisir(fo):
    try:
        file_object = open(os.path.realpath(__file__).replace(
            os.path.basename(__file__), '')+fo, "w+")
    except IOError:
        print("Erreur lors de l'ouverture du fichier.")
        return -1
    else:
        nombre_etud = int(
            input("Entrez le nombre d'étudiants que vous souhaitez entrer."))
        for i in range(nombre_etud):
            file_object.write(input("Entrez les informations relatives à l'étudiant n°"+str(i) +
                                    "\nNOTE:Entrez les informations dans l'ordre suivant(avec les point-virgules):\nNuméro;Nom;Prénom;Âge;Moyenne générale;Mention obtenue")+"\n")
        return 0
    finally:
        file_object.close()


print(saisir(""))
