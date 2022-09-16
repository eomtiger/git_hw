T = 10


for tc in range(1, T+1):
    N, S = map(int, input().split())
    arr = list(map(int, input().split()))
    maxV = max(arr)                 #제일 큰 값을 찾아서
    cnt = 0
    adj_mat = [[0]*(maxV+1) for _ in range(maxV+1)]  #인접 매트릭스 크기 구하고

    for i in range(0, len(arr), 2):                  #인접 메트릭스 만들기
        adj_mat[arr[i]][arr[i+1]] = 1

    visited = []                                     #bfs로 구하기
    visited_tuple = []
    q = [(S, cnt)]                                   #큐에 연락 횟수 추가

    while q:
        current = q.pop(0)
        if current[0] not in visited:
            visited.append(current[0])
            visited_tuple.append((current[0], current[1]))

        for destination in range(maxV+1):
            if adj_mat[current[0]][destination] and destination not in visited:
                q.append((destination, current[1]+1))

    last_cnt = visited_tuple[-1][1]                 #마지막 연락 횟수를 구하고
    # ex) [(2,0), (4,1), (3,1), (7,2), (9,2), (10,3)]
    last_contact_list = []                          #마지막 연락한 번호 리스트를 만들어서
    for i in range(len(visited_tuple)):
        if visited_tuple[i][1] == last_cnt:         #마지막 연락 횟수와 같으면 추가하기
            last_contact_list.append(visited_tuple[i][0])

    print(f'#{tc} {max(last_contact_list)}')







