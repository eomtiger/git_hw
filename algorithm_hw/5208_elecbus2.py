T = int(input())

def move(loc, cnt):
    global rst
    if arr[loc] + loc >= d:     #내 위치의 배터리 크기와 지금까지 온 거리의 합이 도착지보다 크거나 같으면
        rst = cnt               #rst에 저장
        return

    cnt += 1                    #충전 한 번 했다

    if cnt >= rst:              #충전 횟수가 결과보다 크다면(백트래킹)
        return                  #리턴

    for i in range(1, arr[loc]+1): #현재 위치에서 교환한 베터리로 갈 수 있는 거리만큼
        move(loc+i, cnt)           #블랙홀로 들어간다



for tc in range(1, 1+T):
    arr = list(map(int, input().split()))
    d = arr[0]      # 정류장 개수
    cnt = 0             #교체 횟수
    loc = 1             #현재 위치
    rst = 100000

    move(loc, cnt)

    print(f'#{tc} {rst}')

