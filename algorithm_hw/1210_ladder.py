import sys
sys.stdin = open("input.txt", "r")
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]
for tc in range(10):
    N = int(input())
    mat =[]
    for _ in range(100):
        arr = list(map(int, input().split()))
        mat.append(arr)

    end = 0
    for k in range(100):
        if mat[-1][k] == 2:
            end += k
        mat[k].insert(0, 0)
        mat[k].insert(-1, 0)
    print('end', end)


    i = 99
    j = end
    # print(len(mat[0]))
    # print(j)

    while i!= 0:

        # if j == 0:
        #     if mat[i+di[3]][j+dj[3]] == 0:
        #         i = i + di[0]
        #         j = j + dj[0]
        #     elif mat[i + di[3]][j + dj[3]] == 1:
        #         while mat[i + di[3]][j + dj[3]] == 1:
        #             i = i + di[3]
        #             j = j + dj[3]
        #
        # elif j ==99:
        #     if mat[i+di[2]][j+dj[2]] == 0:
        #         i = i + di[0]
        #         j = j + dj[0]
        #     elif mat[i + di[2]][j + dj[2]] == 1:
        #         while mat[i + di[2]][j + dj[2]] == 1:
        #             i = i + di[2]
        #             j = j + dj[2]


        if (mat[i+di[2]][j+dj[2]] == 0) and (mat[i+di[3]][j+dj[3]] == 0):
            i = i + di[0]
            j = j + dj[0]
            print(i, j)

        else:
            break

        # elif mat[i+di[2]][j+dj[2]] == 1:
        #     while mat[i+di[2]][j+dj[2]] == 1:
        #         i = i + di[2]
        #         j = j + dj[2]
        #
        #         print(i,j)
        #
        # elif mat[i+di[3]][j+dj[3]] == 1:
        #     while mat[i+di[3]][j+dj[3]] == 1:
        #         i = i + di[3]
        #         j = j + dj[3]
        #         print(i,j)






