T = int(input())

for tc in range(1, T+1):
    s = list(input())
    stack1 = []
    top1 = 0
    stack2 = []
    top2 = 0

    for i in s:
        if i.isnumeric():
            stack1.append(i)
            top1 += 1
        else:
            stack2.append(i)
            top2 += 1

    rst = ''
    for i in range(len(stack1)):
        rst += stack1[i]

    for i in range(len(stack2)):
        rst += stack2.pop()

    print(f'#{tc} {rst}')


