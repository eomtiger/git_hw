dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def move(i, j, cost, visited):
    global min_cost
    # if cost > min_cost:
    #     return

    if i == N-1 and j == N-1 and cost < min_cost:
        min_cost = cost
        return


    for k in range(4):
        ay = i+dy[k]
        ax = j+dx[k]
        if 0 <= ay < N and 0 <= ax < N and (ay, ax) not in visited and cost+mat[ay][ax] < min_cost:
            visited.append((i+dy[k], j+dx[k]))
            move(i+dy[k], j+dx[k], cost+mat[i+dy[k]][j+dx[k]], visited)
            visited.pop()

cnt = 0
while True:
    cnt+=1
    N = int(input())
    if N == 0:
        break
    mat = [list(map(int, input().split())) for _ in range(N)]
    min_cost = 987654321
    cost = mat[0][0]
    visited = [(0, 0)]
    move(0, 0, cost, visited)
    print(f'Probelm {cnt}: {min_cost}')