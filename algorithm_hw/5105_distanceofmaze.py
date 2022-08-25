def maze_dis(si, sj, cnt):                                                      #미로 거리를 구하는 함수

    if maze[si][sj] == 3:                                                       #미로를 돌다가 3이 나오면
        cnt_list.append(cnt-1)                                                  #그동안 이동했던 횟수 -1만큼 cnt_list에 추가
        return

    if (si+1, sj) not in visited and 0 <= si+1 < N and maze[si+1][sj] != 1:     # 아래로 이동, 좌표가 방문기록에 없고 좌표가 범위에 맞고 벽이 아니라면
        visited.append((si+1, sj))
        maze_dis(si+1, sj, cnt+1)                                               # 아래로 한칸 이동하고 이동횟수 1을 더해서 재귀함수를 탄다


    if (si-1, sj) not in visited and 0 <= si-1 < N and maze[si-1][sj] != 1:     # 위로 이동, 좌표가 방문기록에 없고 좌표가 범위에 맞고 벽이 아니라면

        visited.append((si-1, sj))
        maze_dis(si-1, sj, cnt + 1)                                             # 위로 한칸 이동하고 이동횟수 1을 더해서 재귀함수를 탄다

    if (si, sj+1) not in visited and 0 <= sj+1 < N and maze[si][sj+1] != 1:     # 방법은 상동

        visited.append((si, sj+1))
        maze_dis(si, sj+1, cnt + 1)

    if (si, sj-1) not in visited and 0 <= sj-1 < N and maze[si][sj-1] != 1:     #상동

        visited.append((si, sj-1))
        maze_dis(si, sj-1, cnt + 1)


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]              #미로를 2차원배열로
    si = 0                                                          #출발 좌표
    sj = 0                                                          #출발 좌표
    for i in range(N):                                              #출발좌표 찾기
        for j in range(N):
            if maze[i][j] == 2:
                si = i
                sj = j
    visited = [(si, sj)]                                            #방문 기록 남기기
    cnt = 0                                                         #이동 횟수 기록
    cnt_list = []                                                   #도착점까지 경로가 여러가지일 경우를 대비해
                                                                    #이동 횟수 리스트를 만듬
    maze_dis(si, sj, cnt)

    if len(cnt_list) == 0:
        print(f'#{tc} 0')
    else:
        print(f'#{tc} {min(cnt_list)}')
