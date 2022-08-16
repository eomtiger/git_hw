T = int(input())

for tc in range(1, T+1):
    mat = list(input() for i in range(5))

    print(mat)

    sero = ''
    maxL = 0
    for i in range(5):
        if len(mat[i]) > maxL:
            maxL = len(mat[i])
    print(maxL)

    for i in range(5):
        if len(mat[i]) < maxL:
            while len(mat[i]) != maxL:
                mat[i] + '.'

    print(mat)




