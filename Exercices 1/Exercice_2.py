note = int(input())

while (note < 0 or note > 20):
    print("SAISISSEZ UNE NOTE COMPRISE ENTRE 0 ET 20 !")
    note = int(input())
if (note < 10):
    print("Insuffisant")
elif (note >= 10 and note < 12):
    print("Passable")
elif (note >= 12 and note < 14):
    print("AB")
elif (note >= 14 and note < 16):
    print("B")
elif (note >= 16):
    print("TB")
