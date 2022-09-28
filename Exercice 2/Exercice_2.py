liste = []

nb_elem = int(input("Nombre d'éléments dans la liste ?"))

for i in range(nb_elem):
    liste.append(input("Entrez un mot \n"))

for i in range(len(liste)-1):
    print(liste[i])
