dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

while True:

    N = int(input())
    if N == 0:
        break
    mat = [list(map(int, input().split())) for _ in range(N)]

    adj = [[987654321]*N for _ in range(N)]
    cnt = 0
    v_list = []
    for i in range(N):
        for j in range(N):
            v_list.append((i, j, cnt))
            cnt += 1
    for i in range(N):
        for j in range(N):
            for k in range(4):
                if 0 <= i + dy[k] < N and 0 <= j +dx[k] < N:



