T = int(input())

for tc in range(1, T+1):
    d, m, q, y = map(int, input().split())
    arr = list(map(int, input().split()))
    check = [0]*12
    cost = [0]*12    #매달 들어가는 비용
    for i in range(12):
        if arr[i]:
            check[i] = 1
    print(check)
    # 연속된 3달인 경우를 리스트로 저장해보자
    row_q = []
    for i in range(12):
        if arr[i] and arr[i+1] and arr[i+2]:
            row_q.append((i+1, i+2, i+3))
    print(row_q)

    for i in range(12):             #12달 동안
        if arr[i]:                  #수영장을 가는 달이라면
            if arr[i]*d >= m:       #매일 내는 요금이 한달 요금보다 비싸면
                cost[i] = m         #그달 비용은 m
            else:                   #반대면
                cost[i] = arr[i] * d#비용은 arr[i]*d

    print(cost)
    total_cost = 1000000
    for qrt in row_q:




