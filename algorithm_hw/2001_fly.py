# import sys
# sys.stdin = open("input.txt", "r")

T = int(input())


for tc in range(1, T+1):
    N, M = map(int, input().split())
    mat = []                                    #매트릭스 만들기
    for _ in range(N):

        arr = list(map(int, input().split()))   #arr 인풋받고
        mat.append(arr)                         #매트릭스에 넣기

    max_mat = 0                                 #파리채에 잡힌 최대 파리수를 0으로 두고 시작
    for i in range(N-M+1):                      #파리채와 전체 매트릭스 넓이를 계산하여
        for j in range(N-M+1):                  #좌표를 옮겨가며 파리를 잡음
            mat_sum = 0                         #파리채로 한번에 잡은 파리 수

            for c in range(M):                  #파리채의 넓이 만큼
                for r in range(M):
                    mat_sum += mat[i+c][j+r]    #잡은 파리 수 갱신
            if max_mat < mat_sum:
                max_mat = mat_sum

    print(f'#{tc}', max_mat)

