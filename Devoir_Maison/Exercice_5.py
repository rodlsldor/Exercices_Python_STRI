def create_pile(liste):
    return liste


def empiler(liste, num):
    return liste.append(num)


def depiler(liste):
    if (liste.length == 0):
        return -1
    else:
        return liste.pop()


def defiler(liste):  # enlève un élement de la file
    if (liste.length == 0):
        return -1
    else:
        return liste.pop(0)
