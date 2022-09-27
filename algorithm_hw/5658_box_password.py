from collections import deque

T = int(input())

for tc in range(1, 1+T):
    N, K = map(int, input().split())
    arr = deque(input())
    set_10 = set()                  #10진수로 바꾼 수를 담을 set

    for i in range(int(N/4)):        #한칸씩 밀면서
        arr.append(arr.popleft())
        for j in range(0, len(arr), int(N/4)): # 한 변에 있는 문자들을
            password = ''
            for k in range(int(N/4)):           # password에 담고
                password += arr[j+k]

            set_10.add(int(password, 16))       #10진수로 바꿔서 set에 담는다
    set_10 = list(set_10)                   #set을 리스트로 바꿔서  sorting
    set_10.sort(reverse= True)

    print(f'#{tc} {set_10[K-1]}')






