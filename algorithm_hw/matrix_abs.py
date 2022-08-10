
def matrix_abs_sum(mat):                          #함수 만들기
    total_abs = 0                                 #모든 방향의 차이 절대값 합
    for i in range(5):                            #5x5 행렬  인덱스 뽑기
        for j in range(5):
            udlr = ['a','a','a','a']              #up/down/left/right 값을 담을 리스트
            for k in range(4):
                ni = i+dy[k]                       #델타를 이용하여 구하기
                nj = j + dx[k]
                if 0<=ni<5 and 0<=nj<5:
                    udlr[k]=mat[ni][nj]

            for a in range(4):                      #udlr에서 str이 아닌 것들과
                if type(udlr[a]) != str:            #해당 인덱스 값의 차의 절대값 구하기
                    total_abs += abs(mat[i][j]-udlr[a])

    return total_abs

T = int(input())

result = []
for i in range(T):
    N = int(input())

    matrix = list(list(map(int, input().split())) for _ in range(5))

    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]


    result.append(matrix_abs_sum(matrix))

for i in range(T):
    print('#'+str(i+1), result[i])




