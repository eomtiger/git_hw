def pascaltri(N):
    print(1)                        #첫번째 줄
    print(1, 1)                     #두번째 줄
    s = [1, 1]                     #스택 [1,1]

    turn = 0
    while turn != N-2:              #위에 두줄을 만들었기 때문에 N-2
        for i in range(len(s)-1):   #스택에 길이-1만큼 돌아
            s.append(s[i] + s[i+1]) #i번째 스택 원소와 i+1번째 스택 원소를 더하여 스택에 추가
                                    #[1,1] -> [1,1,2]
        for i in range(turn+2):
            s.pop(0)                #[1,1,2]에서 윗줄의 원소를 뺌 [1,1,2] -> [2]
                                    #다음 시행에서는 [1,2,1,3,3]-> [3,3]
        s.append(1)                 #뒤에 1을 더하고 [3,3]->[3,3,1]
        s.insert(0, 1)              #앞에 1을 더함 [3,3,1]->[1,3,3,1]
        turn += 1

        for i in range(len(s)):
            if i == len(s)-1:
                print(s[i])         #마지막 원소 프린트 후 줄 바꿈
            else:
                print(s[i], end = ' ') #마지막 원소 전까지 공백 후 출력력


T = int(input())

for tc in rage(T):
    N = int(input())
    print('#'+ str(tc+1))
    pascaltri(N)