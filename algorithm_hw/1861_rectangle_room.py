T = int(input())

for tc in range(1, T+1):
    N = int(input())

    mat = [list(map(int, input().split())) for _ in range(N)]

    # print(mat)
    # visited = []
    # q = []
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    maxV = 0
    start = []

    for i in range(N):
        for j in range(N):
            cnt = 0
            visited = [(i, j)]
            q = [(i, j, cnt)]

            while q:
                a = q[0][2] + 1
                for k in range(4):

                    y = q[0][0]
                    x = q[0][1]


                    if 0 <= y+dy[k] < N and 0 <= x+dx[k] < N and mat[y+dy[k]][x+dx[k]] == mat[y][x]+1:

                        if (y+dy[k], x+dx[k]) not in visited:

                            visited.append((y+dy[k], x+dx[k]))


                            q.append((y + dy[k], x + dx[k], a))

                            if a >= maxV:
                                maxV = a
                                start.append([mat[visited[0][0]][visited[0][1]], a])

                q.pop(0)
    # print(start)
    start_num = N**2 + 1
    max_move = 0
    for i in range(len(start)):
        if max_move < start[i][1]+1 and start_num >= start[i][0]:
            max_move = start[i][1]+1
            start_num = start[i][0]

    print(f'#{tc} {start_num} {max_move}')







