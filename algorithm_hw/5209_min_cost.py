def cost(depth, acc):
    global min_cost

    if acc > min_cost:          #백트래킹: 이미 누적합이 최소 비용보다 함수 끝
        return

    if depth == N:              #최대 깊이까지 갔으면
        if acc < min_cost:      #누적합과 최소비용 비교
            min_cost = acc

    for i in range(N):
        if check[i] == 0:       #check 원소가 0이면
            check[i] = 1        #1로 만들고 (다음 층 함수에서 해당 위치에 잡히지 않기 위해)
            cost(depth + 1, acc + mat[depth][i])    #한층 더 들어가고 acc값을 함께
            check[i] -= 1           #함수에서 빠져나온 후 check값을 원래대로 돌리고
                                    #남은 for문을 다시 돈다

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]
    min_cost = 99999999
    check =[0]*N

    cost(0,0)

    print(f'#{tc} {min_cost}')







