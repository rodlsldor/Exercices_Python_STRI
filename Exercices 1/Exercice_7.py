def tri_insertion(liste):

    for i in range(0, len(liste)):
        x = liste[i]

        j = i
        while (j > 0 and liste[j-1] > x):
            liste[j] = liste[j-1]
            j -= 1

        liste[j] = x

    return liste


liste_entier = [1, 2, 19, 3, 10, -5, 0, 19, 201, -23]

print(tri_insertion(liste_entier))
