
T = int(input())

for tc in range(T):
    N = int(input())
    print('#'+ str(tc+1))

    s = []
    for i in range(N-1):
        s.append([])                            #s 빈 이중 리스트를 만듬
    s[0].append(1)                              #[[1,1], [], [], [], [] ...]
    s[0].append(1)

    for i in range(1, N-1):
        for j in range(len(s[i-1])-1):          #이전 인덱스 리스트에서
            s[i].append(s[i-1][j]+s[i-1][j+1])  #원소 합을 현재 리스트에 담음
                                                #ex) [[1,1],[2], [], [], []]
                                                #ex) [[1,1], [1,2,1], [3,3], [], [], []]

        s[i].append(1)                          #리스트의 앞과 뒤에 1씩 더해줌
        s[i].insert(0, 1)
                                                #s = [[1,1], [1,2,1], [1,3,3,1], ...]

    print(1)
    for i in range(len(s)):
        for j in range(len(s[i])):
            if j == len(s[i])-1:
                print(s[i][j])
            else:
                print(s[i][j], end = ' ')

