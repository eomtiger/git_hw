T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    str_mat = []                        #문자열을 매트릭스로 받을 예정
    for _ in range(N):

        string = input()                #string을 받고
        str_mat.append(list(string))    # str_mat에 string을 더하여 만들어줌

    # print(str_mat)

    for i in range(len(str_mat)):

        for j in range(N, 0, -1):                       #길이 N부터 내려가면서 순회
            for k in range(0, N - j + 1):               #str_mat[i]를 인덱싱 슬라이싱으로 줄여가며
                if str_mat[i][k:k + j] == str_mat[i][k: k + j][::-1] and len(str_mat[i][k: k + j]) == M: #회문을 확인함
                    result =''                          #결과를 받을 빈 문자열
                    for a in range(len(str_mat[i][k:k+j])): #palindrome을 확인하여 첫글자부터
                        result += str_mat[i][k:k+j][a]      # 하나씩 더해감
                    print(f'#{tc}', result)


    matT = list(zip(*str_mat))                          #전치하고

    for i in range(len(matT)):                               #가로와 같은 방식으로 세로를 구함

        for j in range(N, 0, -1):
            for k in range(0, N - j + 1):
                if matT[i][k:k + j] == matT[i][k: k + j][::-1] and len(matT[i][k: k + j]) == M:
                    result = ''
                    for a in range(len(matT[i][k:k + j])):
                        result += matT[i][k:k + j][a]
                    print(f'#{tc}', result)
