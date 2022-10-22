def saisir_n_2_des():
    n = int(input("Saisir entier n dans [2; 12] : "))
    while not (2 <= n <= 12):
        n = int(input("Saisir entier n dans [2; 12] : "))
    return n


def saisir_n_3_des():
    n = int(input("Saisir entier n dans [3; 18] : "))
    while not (3 <= n <= 18):
        n = int(input("Saisir entier n dans [3; 18] : "))
    return n


def obtenir_n_2_des(n):
    cpt = 0
    for i in range(1, 7):
        for j in range(1, 7):
            if i + j == n:
                cpt += 1
    return cpt


def obtenir_n_3_des(n):
    cpt = 0
    for i in range(1, 7):
        for j in range(1, 7):
            for k in range(1, 7):
                if i + j + k == n:
                    cpt += 1
    return cpt


print("Il existe {} façon(s) d'obtenir n avec 2 dés.".format(
    obtenir_n_2_des(saisir_n_2_des())))
print("Il existe {} façon(s) d'obtenir n avec 3 dés.".format(
    obtenir_n_3_des(saisir_n_3_des())))
