from re import A


liste_note = []
liste_recu = []
somme_note = 0
note_min = 20
note_max = 0
for i in range(10):
    note = int(input())
    while (note < 0 or note > 20):
        note = int(input())
    liste_note.append(note)
    somme_note += note
    if note_max < note:
        note_max = note
    if note_min > note:
        note_min = note
    if (note > 10):
        liste_recu.append(i+1)

print("Moyenne:", somme_note/len(liste_note),
      "\nNote minimale:", note_min, "\nNote maximale:", note_max, "\nReçus:", liste_recu)
