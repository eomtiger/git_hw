T = int(input())
ops = {
    'A': 10,                        #16진수 딕셔너리
    'B': 11,
    'C': 12,
    'D': 13,
    'E': 14,
    'F': 15,
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
}

for tc in range(1, T+1):
    N, S = input().split()

    S = list(S)                     #리스트로 인풋을 나눔
                                    #ex) ['4', 'F', '7', 'E']
    # print(S)
    new_arr = []                    #이진수로 변환 값을 담을 리스트
    temp = []
    for i in range(len(S)):
        s1 = ops[S[i]] // 2         #2로 나눠가며 나머지를 temp에 저장
        r1 = ops[S[i]] % 2
        temp.append(r1)
        s2 = s1 // 2
        r2 = s1 % 2
        temp.append(r2)
        s3 = s2 // 2
        r3 = s2 % 2
        temp.append(r3)
        r4 = s3 % 2
        temp.append(r4)

        temp.reverse()              #temp를 reverse하여 이진법으로 나타냄
        new_arr.extend(temp)        #temp를 이어붙임
        temp.clear()

    # print(new_arr)
    rst = ''
    for i in new_arr:
        rst += str(i)

    print(f'#{tc} {rst}')


    # print(temp)