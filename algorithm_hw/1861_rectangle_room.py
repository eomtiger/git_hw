T = int(input())

for tc in range(1, T+1):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]

    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    visited = []
    p = [(N**2+1, 0)]

    for i in range(N):
        for j in range(N):
            q = []
            if (i, j) not in visited:
                visited.append((i, j))
                q.append((i, j, 1))
            else:
                continue
            # print(q)
            while q:
                for k in range(4):
                    ai = q[0][0]+dy[k]
                    aj = q[0][1]+dx[k]
                    # print('k:', k, ai, aj)
                    if 0 <= ai < N and 0 <= aj < N and mat[ai][aj] == mat[q[0][0]][q[0][1]] + 1:
                        visited.append((ai, aj))

                        q.append((ai, aj, q[0][2]+1))
                        print(q)
                        if q[0][2] >= p[0][1] and mat[ai][aj] <= p[0][0]:
                            p[0] = (mat[ai][aj], q[-1][2])
                            print(p)

                q.pop(0)

    print(p)














