T = int(input())

def minsum(i, j, sum_v, cnt):
    global min_sum
    sum_v += mat[i][j]
    cnt += 1
    if cnt == 2*N -1 or sum_v > min_sum:
        return
    print(mat[i][j])
    min_sum += mat[i][j]
    if i+dy < N:
        i += dy
        minsum(i, j, sum_v, cnt)
    if j+dx < N:
        j += dx
        minsum(i, j, sum_v, cnt)
    return

for tc in range(1, T+1):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]
    print(mat)

    dy = 1
    dx = 1
    start = (0, 0)
    min_sum = 1000000

    minsum(0, 0, 0, 0)

    print(min_sum)
