T = int(input())
mat_list = []
for tc in range(T):
    N = int(input())

    mat = list([0]*N for i in range(N))
    arr = []
    for i in range(1, N**2+1):
        arr.append(i)

    # print(arr)


    i = 0
    j = 0

    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    mat[i][j] = arr[0]              #(0,0)은 주어지고
    turn = 0                        #우 하 좌 상 바퀴 수
    for k in range(1, N**2):                #우
        if i == turn and j<N-turn-1:
            i += di[3]
            j += dj[3]
            mat[i][j] = arr[k]
            # print('1',mat)


        elif i<N-turn-1 and j ==N-turn-1:   #하
            i += di[1]
            j += dj[1]
            mat[i][j] = arr[k]
            # print('2',mat)

        elif i == N-turn-1 and j>turn and mat[i+di[2]][j+dj[2]]==0: #좌
            i+= di[2]
            j+= dj[2]
            mat[i][j] = arr[k]
            # print('3',mat)

        elif j==turn and i>turn and mat[i+di[0]][j+dj[0]] == 0: #상
            i += di[0]
            j += dj[0]
            mat[i][j] = arr[k]

            if mat[i+di[0]][j+dj[0]] != 0:   # 위에가 0이 아니면 turn을 더해라
                turn += 1
            # print('4',mat)

    mat_list.append(mat)

'''----------------------------------------------------------------'''
#print(mat_list)
# for i in range(T):                        # 출력 헛짓
#     print('#' + str(i+1))
#     for j in range(len(mat_list[i])):
#         for k in range(len(mat_list[i][j])):
#             print(mat_list[i][j][k], end=  ' ')
''' ------------------------------------------------------------------------'''

for i in range(T):
    print('#' + str(i+1))           #asterisk 이용 방법 익히기
    for j in mat_list[i]:
        print(*j)



