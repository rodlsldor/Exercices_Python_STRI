nb_v = int(input("Entrez un nombre inférieur à 100 000\n"))
cpt = 0
for i in range(nb_v):
    somme = 0
    produit = 1
    str_i = str(i)
    for j in str_i:
        somme += int(j)
        produit *= int(j)
    if (somme == produit):
        cpt += 1

print(cpt)
