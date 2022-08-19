T = int(input())

for tc in range(1, T+1):

    N = int(input())
    mat = []
    rot90 = list([0]*N for _ in range(N))           #90도 회전 matrix
    rot180 = list([0]*N for _ in range(N))          #180
    rot270 = list([0]*N for _ in range(N))          #270

    for i in range(N):
        arr = list(map(int, input().split()))
        mat.append(arr)                             #인풋 mat

    for i in range(N):
        for j in range(N):                          #90도 회전
            rot90[j][N-1-i] = mat[i][j]

    for i in range(N):
        for j in range(N):                          #90도 회전 + 90도 회전
            rot180[j][N-1-i] = rot90[i][j]

    for i in range(N):
        for j in range(N):                          #90도 회전 + 90도 회전 + 90도회전
            rot270[j][N-1-i] = rot180[i][j]


###########################여기부터는 프린트 형식 때문에 만든 코드 ##########
    rot90_str_list = []
    for i in range(len(rot90)):
        rot90_str = ''
        for j in range(len(rot90)):
            rot90_str += str(rot90[i][j])
        rot90_str_list.append(rot90_str)

    rot180_str_list = []
    for i in range(len(rot180)):
        rot180_str = ''
        for j in range(len(rot180)):
            rot180_str += str(rot180[i][j])
        rot180_str_list.append(rot180_str)

    rot270_str_list = []
    for i in range(len(rot270)):
        rot270_str = ''
        for j in range(len(rot270)):
            rot270_str += str(rot270[i][j])
        rot270_str_list.append(rot270_str)

    print(f'#{tc}')
    for i in range(N):
        print(rot90_str_list[i], end= ' ')
        print(rot180_str_list[i], end=' ')
        print(rot270_str_list[i])



