liste_note = []
liste_recu = []
somme_note = 0

for i in range(10):
    note = int(input())
    while (note < 0 or note > 20):
        note = int(input())
    liste_note.append(note)
    somme_note += note

moyenne = somme_note/len(liste_note)

for i in range(10):
    if (liste_note[i] >= moyenne):
        liste_recu.append(i+1)

print("Moyenne:", moyenne, "\nReçus:", liste_recu)
