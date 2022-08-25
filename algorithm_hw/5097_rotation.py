from collections import deque               #deque 쓰자 아주 편함

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = deque(map(int, input().split()))  #인풋을 deque로 받음

    for i in range(M):
        arr.append(arr.popleft())           #첫번째 인자 빼서 뒤로 더함


    print(f'#{tc} {arr[0]}')