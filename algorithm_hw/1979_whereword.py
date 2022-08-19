T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    mat = []
    pad = [0] * (N + 2)                         #제로패딩 상하좌우
    di = [-1,1,0,0]
    dj = [0,0,-1,1]
    for _ in range(N):
        arr = list(map(int, input().split()))
        mat.append([0]+arr+[0])                 #패딩 양옆


    mat =  [pad] + mat + [pad]                  #패딩 위 아래
    # print(mat)
    rst = 0                                     #결과 하나씩 더해갈 것

    for i in range(1,N+1):      #가로 먼저 (i,j 순서 중요)
        for j in range(1,N+1):

            if mat[i][j] == 1 and j <= N-K+1 and mat[i][j-1] == 0:
                length = 1          #1이고 슬라이딩하면서 개수를 맞추고 왼쪽이 0

                while mat[i][j+1] == 1 and length <K:
                    length += 1     #오른쪽이 1이고 길이가  K 보다 짧으면
                    j += dj[3]      # 길이에 1을 더하고 오른쪽으로 한칸 이동

                if length ==K and mat[i][j+1] == 0: #while문이 터지고 오른쪽이 0이면
                    rst += 1                        #결과에 1을 더 함

    for j in range(1, N + 1):           #세로 위와 같은 방식
        for i in range(1, N + 1):       #i,j 순서 중요
            if mat[i][j] == 1 and i <= N-K+1 and mat[i-1][j] == 0 :
                length = 1
                # print(i, j)
                while mat[i+1][j] == 1 and length < K:
                    length += 1
                    i += di[1]

                if length == K and mat[i+1][j] == 0:

                    rst += 1

    print(f'#{tc} {rst}')
