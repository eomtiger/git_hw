T = int(input())
ops = {                             #암호코드 딕셔너리에 저장
    '0001101': 0,
    '0011001': 1,
    '0010011': 2,
    '0111101': 3,
    '0100011': 4,
    '0110001': 5,
    '0101111': 6,
    '0111011': 7,
    '0110111': 8,
    '0001011': 9,
}

for tc in range(1, T+1):
    N, M = map(int, input().split())
    mat = [list(map(int, input())) for _ in range(N)]


    pwd_arr = []                        #비밀번호 배열을 구하자
    for i in range(N):
        for j in range(M-1, -1, -1):    #한줄씩 뒤지다가 (행의 맨 뒤부터 찾음)
            if mat[i][j] == 1:          #1이 나오면
                for k in range(56):     #앞으로 56개까지 저장
                    pwd_arr.append(mat[i][j-k])
                break
        if pwd_arr:
            break
    pwd_arr.reverse()                   #행을 거꾸로 찾았기 때문에 reverse

    pwd_list = []                       #이제 7비트씩 나눠서 리스트에 담아보자
    for i in range(0, len(pwd_arr), 7):
        pwd = ''
        for j in range(7):
            pwd += str(pwd_arr[i+j])
        pwd_list.append(pwd)

    # print(pwd_list)

    for i in range(8):                  #비트로 담긴 애들을 암호를 풀어 숫자로 바꾸자
        pwd_list[i] = ops[pwd_list[i]]

    # print(pwd_list)
    odd = 0                             #짝수
    even = 0                            #홀수
    for i in range(8):
        if i % 2 == 0:
            even += pwd_list[i]
        else:
            odd += pwd_list[i]

    if (even*3 + odd)%10 == 0:          #조건에 맞으면
        print(f'#{tc}', sum(pwd_list))  #숫자 다 더해서 출력

    else:
        print(f'#{tc}', 0)              #아니면 0


