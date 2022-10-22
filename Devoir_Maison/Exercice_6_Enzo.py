#---------- FUNCTIONS ----------#
def create_squared_matrix():
    matrix = []
    k = 0
    for i in range(N):
        raw = []
        for j in range(N):
            raw.append(k)
            k += 2
        matrix.append(raw)

    return matrix


def create_unit_matrix():
    matrix = []
    for i in range(N):
        raw = []
        for j in range(N):
            if i == j:
                raw.append(1)
            else:
                raw.append(0)
        matrix.append(raw)

    return matrix


def multiply_matrix_by_factor(matrix, factor):
    new_matrix = []
    for i in range(N):
        raw = []
        for j in range(N):
            raw.append(factor * matrix[i][j])
        new_matrix.append(raw)

    return new_matrix


def substract_matrix(matrix_1, matrix_2):
    new_matrix = []
    for i in range(N):
        raw = []
        for j in range(N):
            raw.append(matrix_1[i][j] - matrix_2[i][j])
        new_matrix.append(raw)

    return new_matrix


def print_matrix(M):
    for i in range(0, N):
        for j in range(0, N):
            print(M[i][j], end=" ")
        print()


#---------- MAIN ----------#
N = int(input("Veuillez saisir l'ordre N de la matrice : "))

M1 = create_squared_matrix()
M2 = create_unit_matrix()

print("\nM1 :")
print_matrix(M1)

print("\nM2 :")
print_matrix(M2)

A = multiply_matrix_by_factor(M1, 5)  # A = 5 * M1
B = multiply_matrix_by_factor(M2, 2)  # B = 2 * M2
M3 = substract_matrix(A, B)  # M3 = A - B

print("\nM3 :")
print_matrix(M3)
