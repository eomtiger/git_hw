from collections import deque                                   #deque를 쓰자

T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())

    adj_mat = [[0]*(V+1) for _ in range(V+1)]                   #인접행렬을 만들자

    for _ in range(E):
        i, j = map(int, input().split())
        adj_mat[i][j] = 1
        adj_mat[j][i] = 1

    S, G = map(int, input().split())

    visited = [S]                                               #visited에 출발점 지정
    visited_tup =[(S,0)]                                        #bfs의 층을 표현하기 위해 튜플형태로 하나 만듬
    q = deque([S])                                              #q를 deque로
    c = 0                                                       #층의 위치를 표현

    while len(q) != 0:                                          #q에 원소가 남아있다면 돌아라

        for j in range(V+1):
            if adj_mat[q[0]][j] == 1 and j not in visited:      #행기준으로 탐색하면서 원소가 1이고 방문기록이 없다면

                for i in range(len(visited_tup)):               #층을 구하기 위해 visited_tup을 뒤지고
                    if q[0] == visited_tup[i][0]:               #현재 노드와 visited_tup의 값이 같으면
                        c = visited_tup[i][1]                   #현재 층은 visited_tup[i]과 같다


                q.append(j)                                     #q에 j를 추가하고
                visited_tup.append((j, c+1))                    #visited_tup에 j와 현재층을 같이 저장
                visited.append(j)                               #visited에도 j를 추가



        if G in visited:                                        #G가 visited에 있으면
            q.clear()                                           #q를 날리고
            continue                                            #while문 터뜨림

        q.popleft()                                             #q에서 방금 돌린 원소 빼버리고 while 처음으로 돌아감


    if G not in visited:
        print(f'#{tc} 0')                                       #만약 시작과 끝이 연결되어있지 않다면
    else:
        print(f'#{tc} {visited_tup[-1][1]}')








