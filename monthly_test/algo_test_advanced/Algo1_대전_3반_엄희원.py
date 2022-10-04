import sys
sys.stdin = open('input1.txt', 'r')
T = int(input())

for tc in range(1, T+1):

    N = int(input())
    si, sj, ei, ej = map(int, input().split())                  #왼쪽 상단 좌표와 오른쪽 하단 좌표의 값 저장
    mat = [list(map(int, input().split())) for _ in range(N)]   #mat 만들기
    height_sum = 0                                              #높이들의 합
    breadth = (ei - si + 1) * (ej - sj + 1)                     #넓이
    cnt = 0                                                     #평탄화 횟수

    for i in range(si, ei+1):
        for j in range(sj, ej+1):
            height_sum += mat[i][j]                             #각 원소에서 높이를 더해줌

    avg = height_sum//breadth                                   #높이의 합과 넓이로 평균값을 구함

    for i in range(si, ei+1):
        for j in range(sj, ej+1):
            if mat[i][j] >= avg:                                #평균값보다 해당 위치의 높이가 크다면
                cnt += mat[i][j] - avg                          #높이 - 평균값을 횟수에 더함
            elif mat[i][j] < avg:                               #평균값보다 해당 위치의 높이가 낮다면
                cnt += avg - mat[i][j]                          #평균값 - 높이를 횟수에 더함

    print(f'#{tc} {cnt}')





