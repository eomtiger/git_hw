def maze_road(si, sj):

    if (si + 1, sj) in road:        #재귀 함수 이용하여
        road.remove((si + 1, sj))   #방문한 길은 없애고
        maze_road(si + 1, sj)       #다음 함수로 들어감

    if (si - 1, sj) in road:        #사방향으로 반복하고
        road.remove((si - 1, sj))
        maze_road(si - 1, sj)

    if (si, sj + 1) in road:
        road.remove((si, sj + 1))
        maze_road(si, sj + 1)

    if (si, sj - 1) in road:
        road.remove((si, sj - 1))
        maze_road(si, sj - 1)

    if maze[si][sj] == 3:           # 위의 재귀 함수들이 모두 돌면서
        global rst                  # 길이 사라지고 도착점까지 가능한 유일한 길만
        rst = 1                     # 남아있다면 rst값을 1로 바꿈



T = int(input())

for tc in range(1, T+1):
    N = int(input())

    maze = [list(map(int, input())) for _ in range(N)]
    road = []                   #밟을 수 있는 좌표 리스트
    si = 0                      #시작 좌표
    sj = 0                      #시작 좌표
    rst = 0                     #결과
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                si = i
                sj = j

            if maze[i][j] != 1:     #좌표에 해당 값이 1이 아니면 길이 있는것
                road.append((i, j)) #길에 추가해줌
    maze_road(si, sj)
    print(f'#{tc} {rst}')




















