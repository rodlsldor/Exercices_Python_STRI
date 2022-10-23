from msilib import CreateRecord


def isempty(l):
    if (len(l) == 0):
        print("La pile/file est vide")
        return True
    return False


def create_pile(l):
    pile = []
    for i in range(len(l)):
        pile.append(l[i])
    return pile


def empiler(p, x):
    p.append(x)


def depiler(p):  # enlève un élement de la pile
    if (not isempty(p)):
        p.pop()


def creer_file(l):
    file = []
    for i in range(len(l)):
        file.append(l[i])
    return file


def enfiler(f, x):
    f.append(x)


def defiler(f):  # enlève un élement de la file
    if (not isempty(f)):
        f.pop(0)


pile = create_pile([1, 2, 3, 4, 5])
print(pile)
empiler(pile, 7)
print(pile)
depiler(pile)
print(pile)

file = creer_file([])
print(file)
enfiler(file, 8)
print(file)
defiler(file)
print(file)
defiler(file)
