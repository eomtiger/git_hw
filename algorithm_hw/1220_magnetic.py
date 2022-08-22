import sys
sys.stdin = open("input.txt", "r")

for _ in range(10):
    N = int(input())

    mat = []
    for i in range(100):
        arr = list(map(int, input().split()))
        mat.append(arr)

    mat_T = list(map(list, zip(*mat)))         #전치하여 왼쪽이 s극
    # print(mat_T)                             #오른쪽이 N극
    rst = 0                                    #행마다 더해줄 값
    stack = []                                 #스택을 이용
    top = 0
    for i in range(100):

        for j in range(100):
            if mat_T[i][j] ==1 and top == 0:   #[1
                stack.append(1)                 #1은 왼쪽 s극으로 가는데 일단 스택으로 쌓아줌
                top += 1
            elif mat_T[i][j] == 2 and top>0 and stack[-1] ==1: #[12
                stack.append(2)                     #1 다음 2가 오면 쌓는다
                top+=1
            elif mat_T[i][j] == 1 and stack[-1]==2: #[121
                stack.append(1)                 # 2다음에 1이오면 쌓는다
                top += 1
        # print(stack)
        if len(stack) > 0:

            if stack[-1] == 1:              #스택의 마지막이 1이면
                stack.pop()                 #pop 해준다

            # while stack[-1] == 2 and top != 0 :
            #     stack.pop()

        rst += int(len(stack)/2)            #[121212] 이런 식으로 남으면 2로 나눠서
        # print(rst)                        #충돌 횟수를 정하고 rst에 더함
        stack.clear()                       #스택과 top을 날리고
        top = 0                             #for 문 돌기
    print(rst)                              #top은 굳이 없어도 되지만
                                            #while문 정지나 위치 정할 때 한번씩 쓸 수 있음

