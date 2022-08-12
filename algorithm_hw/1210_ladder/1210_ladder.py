import sys
sys.stdin = open("input.txt", "r")
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]
result = []
for tc in range(10):
    N = int(input())
    mat =[]
    for _ in range(100):
        arr = list(map(int, input().split()))
        mat.append(arr)

    end = 0
    for a in range(100):
        mat[a].insert(0, 0)
        mat[a].insert(101, 0)

    for k in range(101):
        if mat[-1][k] == 2:
            end += k




    i = 99
    j = end




    while i!=0:

        if mat[i+di[2]][j+dj[2]] == 0 and mat[i+di[3]][j+dj[3]] == 0:
            i += di[0]
            j += dj[0]

        elif mat[i + di[2]][j + dj[2]] == 1:
            while mat[i+di[2]][j+dj[2]] == 1:
                i = i + di[2]
                j = j + dj[2]

            i += di[0]
            j += dj[0]

        elif mat[i + di[3]][j + dj[3]] == 1:
            while mat[i+di[3]][j+dj[3]] == 1:
                i = i + di[3]
                j = j + dj[3]

            i += di[0]
            j += dj[0]

    result.append(j-1)
for i in range(10):
    print('#' + str(i+1), result[i])





