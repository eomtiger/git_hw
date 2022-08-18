for _ in range(10):
    T, E = map(int, input().split())

    adj_mat = list([0]*100 for _ in range(100))     #인접행렬 생성

    arr = list(map(int, input().split()))


    for i in range(len(arr)-1):                     #arr로 받은 input에서 짝수 번호만 선택
        if i % 2 == 0:
            adj_mat[arr[i]][arr[i+1]] = 1           #단방향 경로를 adj_mat에서 1로 지정

    stack = [0]
    visited = []

    while stack:
        current = stack.pop()
        if current not in visited:
            visited.append(current)                                 #dfs

        for destination in range(100):
            if adj_mat[current][destination] and destination not in visited:
                stack.append(destination)
    if 99 in visited:
        print(f'#{T}', 1)
    elif 99 not in visited:
        print(f'#{T}', 0)

