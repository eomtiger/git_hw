T = int(input())

for tc in range(1, T+1):

    N, M = map(int, input().split())
    con = list(map(int, input().split()))
    truck = list(map(int, input().split()))

    con.sort(reverse=True)                  #컨테이너 용량 큰 순으로
    truck.sort(reverse=True)                #트럭용량 큰 순으로

    # print(truck)
    w_sum = 0
    for i in range(len(truck)):
        for j in range(len(con)):       #for 문을 돌면서 트럭 용량이 컨테이너 용량보다 크거나 같으면
            if truck[i] >= con[j]:      #w_sum에 무게를 더하고
                # print(con[j])         # 해당 컨테이너 무게를 51로 바꿈
                w_sum += con[j]         #그 후 break
                con[j] = 51             #다시 트럭 for 문 다음이 돌아감
                # print(w_sum)
                break

    print(f'#{tc} {w_sum}')
