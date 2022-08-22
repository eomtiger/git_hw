T = int(input())

for tc in range(1, T+1):
    N, Q = map(int, input().split())

    arr = [0]*N

    for q in range(1,Q+1):              #Q만큼 돌면서 계속 arr을 갱신
        L, R = map(int, input().split())
        for i in range(L-1, R):
            arr[i] = q

    print(f'#{tc}', end = ' ')

    for i in range(len(arr)):
        if i == len(arr)-1:
            print(arr[i])
        else:

            print(arr[i], end=' ')

