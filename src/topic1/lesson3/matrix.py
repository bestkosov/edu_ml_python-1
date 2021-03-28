def main_matrix():
    M1 = [[1, 2, 3, 4, 11],
          [5, -6, 7, 8, 11],
          [5, 2, -42, 8, 11],
          [1, 6, 7, 11, 100]]

    print('\n whole rectangular matrix')
    for i in range(len(M1[0]) - 1):
        print('\n')
        for j in range(len(M1[1])):
            print("|", M1[i][j], "|", end=" ")


def main_diagonal():
    M2 = [[1, 2, 3, 4],
          [5, -6, 7, 8],
          [5, 6, 5, 8],
          [1, 6, 7, 11]]
    print('\n Main diagonal of the matrix')
    for i in range(len(M2[0])):
        print(M2[i][i], end=" ")


def reverse_diagonal():
    print('\nReverse diagonal')
    M3 = [[1, 2, 3, 4],
          [5, 2, 7, 8],
          [5, 6, 3, 8],
          [1, 6, 7, 4]]
    matrix_size = len(M3[0])
    for i in range(matrix_size):
        print(M3[matrix_size - 1 - i][matrix_size - 1 - i], end=" ")


if __name__ == '__main__':
    main_matrix()
    main_diagonal()
    reverse_diagonal()
