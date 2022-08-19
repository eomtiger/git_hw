import sys
sys.stdin = open("input.txt", "r")

for _ in range(10):
    N = int(input())

    mat = []
    for i in range(100):
        arr = list(map(int, input().split()))
        mat.append(arr)

    mat_T = list(map(list, zip(*mat)))
    rst = 0
    stack = []
    top = 0
    for i in range(100):
        for j in range(100):
            if mat_T[i][j] ==2 and top == 0:   #[2
                stack.append(2)
                top += 1
            elif mat_T[i][j] == 1 and top>0 and mat_T[i][j-1] ==2: #[21
                stack.append(1)
                top+=1
            elif mat_T[i][j] == 2 and mat_T[i][j-1]==1: #[212
                stack.append(2)
                top += 1

        if len(stack) > 0:

            while stack[-1] ==1 and top != 0:
                stack.pop()

        rst += int(len(stack)/2)

    print(rst)


