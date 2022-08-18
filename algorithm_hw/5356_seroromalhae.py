T = int(input())

for tc in range(1, T+1):
    mat = list(input() for i in range(5))

    maxL = 0                                #가로 문자열 최대 길이
    for i in range(len(mat)):
        if len(mat[i]) > maxL:
            maxL = len(mat[i])              #받은 문자열 중 가장 긴 길이 지정
    #print(maxL)
    for i in range(len(mat)):
        if len(mat[i]) < maxL:
            while len(mat[i]) != maxL:      #문자열의 길이가 maxL보다 작다면 뒤에 '.'을 붙임
                mat[i] += '.'               #문자열 길이가 maxL이 될 때까지
    #print(mat[1])
    result = ''
    for i in range(maxL):                   #행렬로 생각하고 result에 문자를 하나씩
        for j in range(len(mat)):           #세로로 더함
            result += mat[j][i]

    if '.' in result:                       #result에 '.'이 있다면
        result = result.replace('.', '')    #아무것도 없는것으로 바꿔줌
    print(f'#{tc} {result}')





