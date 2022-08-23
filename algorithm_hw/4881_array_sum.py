def min_sum(depth, acc, a):                #a는 없어도 됨
    global minS


    if acc > minS:                      # 층마다 더한 값이 최소값보다 작으면
        return

    if depth == N:                      #마지막 층까지 갔을 때
        if acc < minS:                  #누적합이 최소값보다 작으면
            minS = acc
        return

    arr = mat[depth]                    #층마다의 배열
    for i in range(N):
        if not check[i]:                #check를 보고 0이면

            acc += arr[i]               #arr값을 더해줌
            check[i] = 1                #check에 1을 더하고

            min_sum(depth + 1, acc, a)  #다음 층으로 내려감
            check[i] = 0                #돌아온 후 check를 다시 0으로 바꾸고
            acc-=arr[i]                 #acc에서 arr값을 빼고 for문을 다시 돈다 ##중요##

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]


    check = [0]*N
    sel =[0]*N
    minS = 999999999
    a = {0}                 #없어도 됨
    min_sum(0, 0, a)


    print(f'#{tc} {minS}')










