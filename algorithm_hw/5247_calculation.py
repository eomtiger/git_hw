from collections import deque       #deque로 bfs

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    visited = set()
    q = deque([])
    rst = 0                         #연산 횟수 결과

    visited.add(N)
    q.append((N, 0))                #연산 결과와 횟수를 튜플로 저장
    while not rst:                  #연산결과가 생기면 끝냄

        if q[0][0] - 1 > 0 and q[0][0]-1 not in visited:    #-1일 때
            if q[0][0] - 1 == M:                            #결과가 나오면
                rst = q[0][1] + 1                           #끝냄
                break
            q.append((q[0][0]-1, q[0][1]+1))                #아니면 q에 연산결과와 횟수를 추가
            visited.add(q[0][0]-1)                          #visited에 연산결과 추가

        #위와 같이 나머지 연산도 진행
        if q[0][0] +1 > 0 and q[0][0] + 1 not in visited:
            if q[0][0] + 1 == M:
                rst = q[0][1] + 1
                break
            q.append((q[0][0]+1, q[0][1]+1))
            visited.add(q[0][0] + 1)

        if q[0][0] - 10 > 0 and q[0][0] - 10 not in visited:
            if q[0][0] - 10 == M:
                rst = q[0][1] + 1
                break
            q.append((q[0][0]-10, q[0][1]+1))
            visited.add(q[0][0]-10)

        #마지막 곱하기 2 연산에서는 연산 결과가 (원하는 값 +10) 보다 크면 if문 실행 x( 백트래킹)
        if q[0][0] *2 > 0 and q[0][0]*2 not in visited and q[0][0] *2 <= M+10:
            if q[0][0] * 2 == M:
                rst = q[0][1] + 1
                break
            q.append((q[0][0] *2, q[0][1]+1))
            visited.add(q[0][0]*2)

        q.popleft()             #while문 한바퀴 돌고 q 맨 앞은 빼줌


    print(f'#{tc} {rst}')









