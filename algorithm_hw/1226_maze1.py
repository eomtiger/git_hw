for _ in range(10):
    tc = int(input()) + 1

    maze = [list(map(int, input())) for _ in range(16)]
    # print(maze)
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    si =0
    sj =0
    for i in range(16):
        for j in range(16):
            if maze[i][j] == 2:
                si += i
                sj += j
                break
        if si:
            break

    print(si, sj)

    visited = []
    stack = []
    while stack:
        for i in range(4):
            if stack[-1][0]+di == 0 and stack[-1] not in visited:
                stack.pop()
                visited.append(stack[-1][0]+di, stack[-1][1]+di)



