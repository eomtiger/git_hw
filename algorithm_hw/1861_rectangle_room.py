T = int(input())

def room(i, j, cnt, s):
    global max_v, min_v
    for k in range(4):
        if 0 <= i+dy[k] < N and 0 <= j+dx[k] < N and mat[i+dy[k]][j+dx[k]] == mat[i][j] + 1:
            room(i+dy[k], j+dx[k], cnt+1, s)


    if cnt >= max_v:
        max_v = cnt

        visited.append((s, cnt))
        return




for tc in range(1, T+1):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]

    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    max_v = 0
    cnt = 1
    visited = []
    min_v = 100000
    for i in range(N):
        for j in range(N):
            s = mat[i][j]
            room(i, j, cnt, s)
    # print(visited)
    for i in range(len(visited)):
        if visited[i][1] == max_v and visited[i][0] < min_v:
            min_v = visited[i][0]
    print(f'#{tc} {min_v} {max_v}')

















