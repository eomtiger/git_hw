T = int(input())

for tc in range(1, T+1):
    num_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}       #검사할 숫자 세트
    rst = 1
    sudoku = []

    for _ in range(9):                          #스도쿠 판 만들기
        arr = list(map(int, input().split()))
        sudoku.append(arr)

    sudoku_T = list(map(list, zip(*sudoku)))    #전치행렬 만들기
    # print(sudoku_T)


    for i in range(9):                          #행 별로 검사
        if set(sudoku[i]) != num_set:
            rst = 0
            break

    for i in range(9):                          #전치행렬 행별 검사
        if set(sudoku_T[i]) != num_set:
            rst = 0
            break




# ####################### 9구간 나누어 숫자 확인 ################
    s1 = []
    s2 = []
    s3 = []
    s4 = []
    s5 = []                         #구간 별 리스트 만들기
    s6 = []
    s7 = []
    s8 = []
    s9 = []

    s_list = [s1,s2,s3,s4,s5,s6,s7,s8,s9] #구간을 모두 담은 리스트


    for i in range(9):                      # 0~2, 3~5, 6~8로 구간을 나눠 해당 원소를
        for j in range(9):                  #위의 s에 넣음
            if i<3 and j<3:                 #
                s1.append(sudoku[i][j])     #

            elif i<3 and 3<= j <6:          #
                s2.append(sudoku[i][j])     #

            elif i<3 and 6<= j <9:
                s3.append(sudoku[i][j])

            elif 3<=i<6 and j<3:
                s4.append(sudoku[i][j])

            elif 3<=i<6 and 3<= j <6:
                s5.append(sudoku[i][j])

            elif 3<=i<6 and 6<=j<9:
                s6.append(sudoku[i][j])

            elif 6<=i<9 and j<3:
                s7.append(sudoku[i][j])

            elif 6<=i<9 and 3<=j<6:
                s8.append(sudoku[i][j])

            elif 6<=i<9 and 6<=j<9:
                s9.append(sudoku[i][j])


    for i in s_list:
        if set(i) != num_set:
            rst = 0
            break

    print(f'#{tc} {rst}')

