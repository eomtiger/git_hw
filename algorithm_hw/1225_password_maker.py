from collections import deque
for _ in range(10):

    tc = int(input())
    arr = deque(map(int, input().split()))
    cir = [1, 2, 3, 4, 5]               #1부터 5까지 순환
    cir = deque(cir)
    while arr[-1] != 0:                 #arr의 마지막이 0일 때까지 돌자

        a0 = arr.popleft()              #arr의 첫번째원소 pop
        c0 = cir.popleft()              #cir의 첫번째 원소 pop
        if a0 - c0 <0:                  #빼주고 0보다 작으면
            arr.append(0)               #0으로 대체 후 arr에 추가
        else:                           #0보다 크면
            arr.append(a0 - c0)         #arr에 추가
        cir.append(c0)                  #cir에 다시 c0추가

    print(f'#{tc}', end = ' ')
    for i in range(len(arr)):
        if arr[i] == 0:
            print(arr[i])
        else:
            print(arr[i], end=' ')