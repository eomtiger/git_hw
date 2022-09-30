T = int(input())

def subset(honey):                    #각 사람이 가진 꿀통의 부분집합의 합 중 최대 값을 구하는 함수
    max_sum = 0
    for i in range(1 << len(honey)):  # 총 2³, 8개의 경우의 수 체크
        selected = []
        sum_sub = 0
        for j in range(len(honey)):  # 셀로판지가 가야하는 길이는 3
            if i & (1 << j):  # 1칸씩 왼쪽으로 옮겨가며 총 3칸을 대조해본다.
                selected.append(honey[j])

        if len(selected) == 0:
            pass

        elif sum(selected) <= C:            #부분집합의 합이 c보다 작거나 같으면
            for k in range(len(selected)):
                sum_sub += selected[k]**2

        if sum_sub > max_sum:               #부분 집합의 합이 다른 부분집합의 합 중 제일 크면
            max_sum = sum_sub

    return max_sum




for tc in range(1, T+1):

    N, M, C = map(int, input().split())

    mat = [list(map(int, input().split())) for _ in range(N)]

    honey1 = []
    honey2 = []
    max_profit = 0
    for i in range(N):
        for j in range(N-M+1):
            #첫번째 사람의 시작 꿀통을 정하고
            for honey in range(j, j+M):
                honey1.append(mat[i][honey])
            # print(honey1)

            #두번째 꿀통을 위의 행에서 아직 구할 수 있을 때
            if (N-1) - (j+M-1) >= M:
                for b in range(j+M, N-M+1):
                    for honey in range(b, b+M):
                        honey2.append(mat[i][honey])

                    #수익을 구해보자
                    h1_profit = subset(honey1)
                    h2_profit = subset(honey2)
                    profit = h1_profit + h2_profit
                    if profit > max_profit:
                        max_profit = profit
                    # print(honey1, 'honey2', honey2, profit)
                    honey2.clear()

            #두번째 꿀통을 다음 행부터 다시 구할 때
            for a in range(i+1, N):
                for b in range(N-M+1):
                    for honey in range(b, b+M):
                        honey2.append(mat[a][honey])
                    # print(honey1, 'honey2', honey2)

                    #수익을 구해보자
                    h1_profit = subset(honey1)
                    h2_profit = subset(honey2)
                    profit = h1_profit + h2_profit
                    if profit > max_profit:
                        max_profit = profit
                    # print(honey1, 'honey2', honey2, profit)
                    honey2.clear()

            honey1.clear()

    print(f'#{tc} {max_profit}')
