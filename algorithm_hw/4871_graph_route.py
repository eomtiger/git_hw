T = int(input())

for tc in range(1, 1+T):
    V, E = map(int, input().split())

    mat = list([0]*(V+1) for _ in range(V+1))       #dfs 인접행렬 만들기

    for _ in range(E):
        start, end = map(int, input().split())      #단방향 인접행렬
        mat[start][end] = 1
        # mat[end][start] = 1
    S, G = map(int, input().split())

    visited = []
    stack = [S]

    while stack:
        current = stack.pop()                       #스택[-1]을 뽑아서 current에
        if current not in visited:                  #이전에 방문하지 않았다면
            visited.append(current)                 # visited에 추가


        for destination in range(V+1):
            if mat[current][destination] and destination not in visited :   #현재랑 도착점이 이어져있고
                stack.append(destination)                                   #도착점 방문 기록이 없다묜 stack에 추가
    print(visited)
    if G in visited:                            #원하는 도착점이 방문기록에 있다면
        print(f'#{tc}', 1)

    else:
        print(f'#{tc}', 0)

