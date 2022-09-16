T = int(input())

def move(R, C, cnt, check):
    if cnt > L:
        return

    # if tunnel[R][C] == 0:
    #     return
    if (R, C) in check:
        return
    else:
        check.append((R,C))

    if (R, C) not in visited:
        visited.append((R, C))
    # up and (R-1, C) not in visited
    # down and (R+1, C) not in visited
    # left and (R, C-1) not in visited
    # right and (R, C+1) not in visited

    #상하좌우 다 될 때
    if tunnel[R][C] == 1:
        if R-1 >= 0 and (tunnel[R-1][C] not in up_x):
            move(R-1, C, cnt+1, check)
        if R+1 < N  and (tunnel[R+1][C] not in down_x):
            move(R+1, C, cnt+1, check)
        if C-1 >= 0  and (tunnel[R][C-1] not in left_x):
            move(R, C-1, cnt+1, check)
        if C+1 < M  and (tunnel[R][C+1] not in right_x):
            move(R, C+1, cnt+1, check)
        # print(visited, cnt)

    #상하
    elif tunnel[R][C] == 2:
        if R-1 >= 0  and (tunnel[R-1][C] not in up_x)  :
            move(R-1, C, cnt+1, check)
        if R+1 < N  and (tunnel[R+1][C] not in down_x)  :
            move(R+1, C, cnt+1, check)

    #좌우
    elif tunnel[R][C] == 3:
        if C-1 >= 0  and (tunnel[R][C-1] not in left_x)  :
            move(R, C-1, cnt+1, check)
        if C+1 < M  and (tunnel[R][C+1] not in right_x)  :
            move(R, C+1, cnt+1, check)

    #상우
    elif tunnel[R][C] == 4:
        if R-1 >= 0  and (tunnel[R-1][C] not in up_x)  :
            move(R-1, C, cnt+1, check)
        if C+1 < M  and (tunnel[R][C+1] not in right_x)  :
            move(R, C+1, cnt+1, check)

    #하우
    elif tunnel[R][C] == 5 :
        if R+1 < N  and (tunnel[R+1][C] not in down_x)  :
            move(R+1, C, cnt+1, check)
        if C+1 < M  and (tunnel[R][C+1] not in right_x)  :
            move(R, C+1, cnt+1, check)

    #하좌
    elif tunnel[R][C] == 6 :
        if R+1 < N  and (tunnel[R+1][C] not in down_x)  :
            move(R+1, C, cnt+1, check)
        if C-1 >= 0  and (tunnel[R][C-1] not in left_x)  :
            move(R, C-1, cnt+1, check)

    #상좌
    elif tunnel[R][C] == 7:
        if R-1 >= 0  and (tunnel[R-1][C] not in up_x)  :
            move(R-1, C, cnt+1, check)
        if C-1 >= 0  and (tunnel[R][C-1] not in left_x)  :
            move(R, C-1, cnt+1, check)





for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    tunnel = [list(map(int, input().split())) for _ in range(N)]
    cnt = 1
    visited = []
    up_x = {0, 3, 4, 7}
    down_x = {0, 3, 5, 6}
    left_x = {0, 2, 6, 7}
    right_x = {0, 2, 4, 5}
    check = []
    move(R, C, cnt, check)


    # print(tunnel)
    #
    # visited = set(visited)
    print(visited)
    print(f'#{tc} {len(visited)}')

