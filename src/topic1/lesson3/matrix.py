if __name__ == '__main__':

    M1 = [[1, 2, 3, 4, 11],
          [5, -6, 7, 8, 11],
          [5, 2, -42, 8, 11],
          [1, 6, 7, 11, 100]]

    # TODO print ALL elements of matrix
    for i in range(len(M1)):
        for j in range(len(M1) + 1):
            print(M1[i][j])

    # TODO print ALL elements of matrix
    for i in M1:
        for j in i:
            print(j)

    M2 = [[1, 2, 3, 4],
          [5, -6, 7, 8],
          [5, 6, 5, 8],
          [1, 6, 7, 11]]
    # TODO print diagonal - 1,-6,5,11
    s = 0
    while s < len(M2):
        for i in range(len(M2)):
            print(M2[i][s])
            s += 1

    M3 = [[1, 2, 3, 4],
          [5, 2, 7, 8],
          [5, 6, 3, 8],
          [1, 6, 7, 4]]
    # TODO print diagonal in oposite order  4, 3, 2, 1
    s = len(M3) - 1
    while s >= 0:
        for i in reversed(range(len(M3))):
            print(M3[i][s])
            s -= 1
