def queen(stage, board):      #stage는 층수 (보드의 제일 위 행을 stage=0이라고 생각하자)
    global cnt                  #두번째 행은 stage =1 이다
    if stage == N:
        cnt += 1                #전층에 걸쳐 놓을 수 있다면 횟수 1을 더함
        return

    for k in range(N):              #옆으로 하나씩 시도하며
        i = stage                   #행의 위치는 stage부터
        j = k
        if board[i][j] >= 1:        #보드의 각 좌표가 1 보다 크다면
            continue                #다음 옆칸으로

        while i < N-1:              #아래로 쭉 1씩 더하기
            board[i+1][j] += 1
            i += 1
        i = stage

        while i < N-1 and j<N-1:    #오른쪽 아래 대각 1씩 더하기
            board[i+1][j+1] += 1
            i += 1
            j += 1
        i = stage
        j = k

        while i<N-1 and j>0:        #왼쪽 아래 대각 1씩 더하기
            board[i+1][j-1] += 1
            i += 1
            j -= 1
        i = stage
        j = k

        queen(stage+1, board)       #다음 층으로 내려가 바뀐 보드와 함께
        #나와서 보드를 돌려놔#################################

        while i < N-1:              #아래로 쭉 -1을 해줘
            board[i+1][j] -= 1
            i += 1
        i = stage

        while i < N-1 and j<N-1:    #오른쪽 아래 대각 -1을 해줘
            board[i+1][j+1] -= 1
            i += 1
            j += 1
        i = stage
        j = k

        while i<N-1 and j>0:        #왼쪽 아래 대각 -1을 해줘
            board[i+1][j-1] -= 1
            i += 1
            j -= 1
        i = stage
        j = k



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    board = [[0]*N for _ in range(N)]

    cnt = 0
    queen(0, board)

    print(f'#{tc} {cnt}')

