def chaine_bool(chaine):
    for i in range(len(chaine)):
        if (chaine[i] not in ('a', 'c', 't', 'g')):
            return False
    return True


def seqinchain(sequence, chaine):
    if (sequence in chaine):
        return True
    return False


chai = input("Entrez une chaine d'ADN\n")
sschai = input("Entrez une sous-chaîne d'ADN\n")

if (seqinchain(sschai, chai)):
    print("T")
else:
    print("F")
