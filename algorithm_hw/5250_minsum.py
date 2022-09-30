T = int(input())

def move(i, j, cost, visited):
    global min_cost


    if i == N-1 and j == N-1 and cost < min_cost:
        min_cost = cost
        return


    for k in range(4):
        ay = i+dy[k]
        ax = j+dx[k]
        if 0 <= ay < N and 0 <= ax < N and mat[i][j] < mat[ay][ax]:
            cost += mat[ay][ax] - mat[i][j]

        if 0 <= ay < N and 0 <= ax < N and (ay, ax) not in visited and cost+1 < min_cost:
            visited.append((i+dy[k], j+dx[k]))
            move(i+dy[k], j+dx[k], cost+1, visited)

            cost -= (mat[ay][ax] - mat[i][j])
            visited.pop()

for tc in range(1, T+1):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]

    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    cost = 0
    min_cost = 987654321
    visited = [(0, 0)]
    move(0, 0, cost, visited)
    print(f'#{tc} {min_cost}')











    # stack = [(0, 0)]
    # flag = True
    #
    # while stack or flag:
    #     for i in range(4):
    #         ay = stack[0][0] + dy[i]
    #         ax = stack[0][1] + dx[i]
    #         if 0 <= ay < N and 0 <= ax < N and (ay, ax) not in visited:
    #             stack.append((ay, ax))
    #             cost += 1
    #             if cost > min_cost:
    #                 continue
    #             if mat[ay][ax] > mat[stack[0][0]][stack[0][1]]:
    #                 cost += mat[ay][ax]-mat[stack[0][0]][stack[0][1]]
    #                 if cost > min_cost:
    #                     continue
    #             stack.append((ax, ay))
    #         if ax == N-1 and ay == N-1:
    #             if cost < min_cost:
    #                 min_cost = cost
    #                 flag = False
    #                 break
    #     visited.append(stack.pop(0))
    #
    # print(min_cost)

