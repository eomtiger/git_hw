T= int(input())

def room(k):
    if i-1 >=0 and mat[i-1][j] == mat[i][j] + 1:
        room(k)
    elif i+1 < N and mat[i+1][j] == mat[i][j] + 1:
        room(k)

    elif j-1 >=0 and mat[i][j-1] == mat[i][j] +1:
        room(k)

    elif j + 1 < N and mat[i][j+1] == mat[i][j] +1:
        room(k)

for tc in range(1, T+1):
    N = int(input())

    mat = [list(map(int, input().split())) for _ in range(N)]
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    for i in range(N):
        for j in range(N):
            visited = []
            stack = [mat[i][j]]

            if stack[-1] not in visited:
                visited.append(stack.pop())

            while 0 <= i+dy[0] <N and 0 <= i+dy[1] < N and
