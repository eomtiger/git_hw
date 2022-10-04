import sys
sys.stdin = open('input2.txt', 'r')
T= int(input())

for tc in range(1, T+1):
    N = int(input())

    mat = [list(map(int, input().split())) for _ in range(N)]   #N*N 배열
    pat = [list(map(int, input().split())) for _ in range(3)]   #3*3 패턴
    cnt = 0                                                     #mat에서 pat와 같은 패턴의 개수

    for i in range(N - 3 + 1):                                  #mat에서 시작점
        for j in range(N-3+1):                                  #정하기
            new_mat = [[0]*3 for _ in range(3)]                 #pat와 같은 크기의 새로운 mat 만들기
            for y in range(3):
                for x in range(3):
                    new_mat[y][x] = mat[i+y][j+x]               #시작점부터 오르쪽, 아래쪽으로 3만큼 이동하는 동안의 값들을
                                                                #new_mat에 저장

            if new_mat == pat:                                  #새로 만든 mat와 pat의 배열이 같다면
                cnt += 1                                        #count에 1을 더해줌

    print(f'#{tc} {cnt}')
