T = int(input())

from collections import deque

def perm(depth):                        #순열로 뽑기
    if depth == N-1 :

        rst.append(tuple(sel))          #결과들을 튜플로 rst에 저장
        return

    for i in range(N-1):
        if not check[i]:
            check[i] = 1
            sel[depth] = nums[i]
            perm(depth+1)
            check[i] = 0



for tc in range(1, T+1):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]

    nums = []
    for i in range(1, N):
        nums.append(i)
    rst = []
    sel = deque([0] * (N-1))
    check = [0] * (N-1)

    perm(0)
    print(rst)
    #[(1, 2), (2, 1)] N= 3일 때

    #각 튜플의 양 옆에 0이 있다고 생각하고 아래 for 문으로 합을 구하자

    min_sum = 1000000
    acc_sum = 0
    for i in range(len(rst)):
        for j in range(N-1):
            if j == 0:                              #j가 0일 때는 rst[i] 왼쪽에 0이 있다고 생각하고
                acc_sum += mat[0][rst[i][j]]
                acc_sum += mat[rst[i][j]][rst[i][j+1]]

            elif j == N-2:                          #j가 N-2일 때는 rst[i] 오른쪽에 0이 있다고 생각
                acc_sum += mat[rst[i][j]][0]

            else:                                   #나머지일때는 (j, j+1)
                acc_sum += mat[rst[i][j]][rst[i][j+1]]
        # print(acc_sum)
        if acc_sum < min_sum:
            min_sum = acc_sum
        acc_sum = 0

    print(f'#{tc} {min_sum}')





