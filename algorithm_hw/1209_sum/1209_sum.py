import sys
sys.stdin = open("input.txt", "r")

maxV = []
for tc in range(10):
    N = int(input())
    mat = []
    for j in range(100):
        arr = list(map(int, input().split()))
        mat.append(arr)


    garo = 0
    sero = 0
    cross_r = 0
    cross_l = 0
    for a in range(100):    #가로
        if sum(mat[a])>garo:
            garo = sum(mat[a])

    for b in range(100):     #세로
        sero_sum = 0
        for c in range(100):
            sero_sum += mat[c][b]
            if sero_sum > sero:
                sero =sero_sum


    for i in range(100):   #오른쪽 아래 대각

        for j in range(100):
            if i == j :
                cross_r += mat[i][j]

    for i in range(100):   #왼쪽 아래 대각
        for j in range(100):
            if i+j == 99:
                cross_l += mat[i][j]

    maxV.append(max(garo, sero, cross_r, cross_l))

for i in range(10):
    print('#' + str(i+1), maxV[i])


