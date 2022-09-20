T = int(input())
from collections import deque
for tc in range(1, 1+T):
    N, M = map(int, input().split())

    # mat = [list(map(int, input().split())) for _ in range(N)]
    mat = []
    home = 0
    for _ in range(N):
        arr = list(map(int, input().split()))
        mat.append(arr)
        a = arr.count(1)
        home += a



    # home = 0
    # for i in range(N):
    #     a = mat[i].count(1)
    #     home += a

    #최대 지불 가능 금액
    max_pay = home * M

    #모든 집이 최대로 지불할 수 있을 때, 운영 비용

    K = 0
    max_cost = K*K + (K-1)*(K-1)
    for k in range(1, 100):
        if k*k + (k-1)*(k-1) <= max_pay:
            max_cost = k*k + (k-1)*(k-1)
            K = k
        else:
            break
    home_set = set()

    for i in range(N):
        for j in range(N):
            if mat[i][j] == 1:
                home_set.add((i, j))



    # print(home)
    # print(max_cost)
    # print(K)
    max_home = 0
    #마름모 가상좌표를 만들자
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    for b in range(K, 0, -1):
        # if max_home == home:
        #     break
        for i in range(N):
            # if max_home == home:
            #     break
            for j in range(N):
                # if max_home == home:
                #     break
                visited = []
                q = deque([])
                visited.append((i, j))
                q.append((i, j))
                cnt = 0
                profit = 0
                if (i, j) in home_set:
                    cnt += 1
                    profit += 1

                while q:
                    y = q[0][0]
                    x = q[0][1]

                    for k in range(4):
                        ay = y + dy[k]
                        ax = x + dx[k]
                        if 0 <= ay < N and 0 <= ax < N and (ay, ax) not in visited and abs(ay-i)+abs(ax-j) <= b-1:
                            visited.append((ay, ax))
                            # print(visited)
                            if mat[ax][ay] == 1:
                                cnt += 1
                                profit += M
                            q.append((ay, ax))

                    q.popleft()
                # print(visited)
                # print(len(visited))

                #수익을 구해보자
                profit = 0
                cnt = 0             #마름모 영역 안 집의 개수
                for v in visited:
                    if mat[v[0]][v[1]] == 1:
                        cnt += 1
                        profit += M

                #마진을 구해보자
                cost = b*b + (b-1)*(b-1)
                margin = profit - cost
                # print('p:', profit)
                # print('c:', max_cost)
                # print('m:', margin)
                if margin >= 0 and cnt > max_home:
                    max_home = cnt

                if max_home == home:
                    break
            if max_home == home:
                break
        if max_home == home:
            break
    print(f'#{tc} {max_home}')











