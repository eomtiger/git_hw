
T = int(input())

for tc in range(T):
    N = int(input())
    print('#'+ str(tc+1))
    print(1)                                    #첫번째 줄 1 출력
    if N>=2:                                    #N이 2이상이면 1 1 출력
        print(1,1)
    s = [1, 1]                                  #stack 에 1,1을 두고
    temp = []
    for _ in range(N-2):                        #위의 두줄 이후 N-2 행을 뽑아내자

        while len(s)!= 1:                       #stack에 1만 남을 때까지
            for i in range(len(s)-1, 0, -1):    #거꾸로 뽑는다
                temp.append(s[i] + s[i-1])      #거꾸로 뽑아서 뒤에 두 원소를 temp에 더함
                s.pop()
                # print(s)
                break                           #브레이크로 for문을 깨고 다시 while 시작
        s.extend(temp)                          # while문이 다 돌면 s에는 1만 남고
                                                #temp를 s에 더함
        temp.clear()                            #temp를 날리고
        s.append(1)                             # s에 1을 추가하여 행을 완성

        for i in range(len(s)):                 #행 출력
            if i == len(s)-1:
                print(s[i])
            else:
                print(s[i], end = ' ')



