T = int(input())

def minsum(i, j, sum_v, cnt):                   #좌표, 누적합, 움직인 횟수
    global min_sum
    sum_v += mat[i][j]
    cnt += 1
    # print(i, j)
    # print(sum_v)
    # print(cnt)
    if cnt == 2*N or sum_v >= min_sum:          #최대 움직인 회수 초과 또는 누적합이 최소 합보다 크거나 같다면
        return
    if cnt == 2*N - 1 and sum_v < min_sum:      #최대 움직인 회수일 때, 누적합이 최소 합보다 작다면
        min_sum = sum_v
    if i+dy < N:                                #아래로 이동
        minsum(i + dy, j, sum_v, cnt)
    if j+dx < N:                                #오른쪽으로 이동
        minsum(i, j + dx, sum_v, cnt)
        return



for tc in range(1, T+1):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]
    # print(mat)

    dy = 1
    dx = 1
    min_sum = 1000000

    minsum(0, 0, 0, 0)

    print(f'#{tc} {min_sum}')
