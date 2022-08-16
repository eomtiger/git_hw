import sys
sys.stdin = open('input.txt', 'r')
T = 1

for _ in range(10):
    tc = int(input())

    maxL = 0                                # 최대 길이를 0으로 두고
    mat = []                                # matrix를 비워둠
    for i in range(100):                    #100개의 라인을
        a = input()                         #a에 선언하고
        mat.append(list(a))                 #list로 만들어서 mat에 넣음 이차원배열
                                            #ex) [['A', 'B', 'A', 'C', .. ],[....], [....]....[...]]

        for j in range(100, 0, -1):         #인풋 받은 a로 길이가 100일 때부터 줄이면서 회문을 확인
            for k in range(0, 100-j+1):     #a를 인덱싱으로 줄여가며
                if a[k:k+j] == a[k: k+j][::-1]: #회문을 확인함
                    if maxL < len(a[k:k+j]):    #가장 긴 회문의 길이를 저장
                        maxL = len(a[k:k+j])     #가로는 여기까지 구한 것

    # print(len(mat[0]))

    matT = list(zip(*mat))                  #전치행렬을 이용

    # print(len(matT[0]))
    for i in range(len(matT)):                                #가로와 같은 방식으로 세로를 구함

        for j in range(100, 0, -1):
            for k in range(0, 100 - j + 1):
                if matT[i][k:k + j] == matT[i][k: k + j][::-1]:
                    if maxL < len(matT[i][k:k + j]):
                        maxL = len(matT[i][k:k + j])        #기존의 maxL을 넘으면 덮어씀

    print(f'{tc}', maxL)






