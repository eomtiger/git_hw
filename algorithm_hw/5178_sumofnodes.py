T = int(input())

for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    rst = 0                             #자식들로부터 더해진 최종 값

    for _ in range(M):
        arr = list(map(int, input().split()))

        k = arr[0]                      #인덱스가 2로 나눈 몫을 취하면서
        node_list = []                  #리스트에 더하고
        while k:
            node_list.append(k//2)
            k //= 2

        if L in node_list:              #리스트에 L이 들어있으면
            rst += arr[1]               #인덱스에 대응했던 노드의 값을 더함

    print(f'#{tc} {rst}')


