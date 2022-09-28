nombre = str(input("Entrez un nombre \n"))
reponse = True
for i in range(len(nombre)//2):
    if (nombre[i] != nombre[(len(nombre))-1]):
        reponse = False

if (reponse):
    print("oui\n")
else:
    print("non\n")
