def fonction(x):
    return 2*(x ^ 3)+x-5


born_inf = int(input("Entrez la borne inférieure : "))
born_sup = int(input("Entrez la borne supérieure : "))
pas = int(input("Entrez le pas : "))

for i in range(born_inf, born_sup, pas):
    print("\n", fonction(i))
