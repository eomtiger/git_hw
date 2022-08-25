from collections import deque           #deque 써보자

def bfs(V, E):
    visited = []                        #방문한 곳
    q = deque()                         #queue를 deque로
    q.append(1)                         #출발 노드 결정 1
    visited.append(1)                   #방문 지정 1

    while q:                            #q에 원소가 있는 동안 돌자

        for j in range(1, V+1):         #adj_mat의 행의 길이만큼 돌자
            if adj_mat[q[0]][j] and j not in visited:   #q의 첫번째 원소 행과 j가 가르키는 adj_mat이 1
                                                        #그리고 j가 visited에 없다면
                q.append(j)                             #q에 더하자 뒤로
                visited.append(j)                       #visited에도 추가
        q.popleft()                                     #q의 왼쪽 원소를 제거하자

    for i in range(len(visited)):                       #출력
        if i == len(visited)-1:
            print(visited[i])
        else:
            print(visited[i], end='-')


V, E = map(int, input().split())
arr = list(map(int, input().split()))

adj_mat = [[0]*(V+1) for _ in range(V+1)]       #adj_mat 만들기
for i in range(len(arr)-1):
    if i%2 == 0:
        adj_mat[arr[i]][arr[i+1]] = 1

bfs(V, E)
