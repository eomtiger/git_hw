T = int(input())

for tc in range(1, T+1):
    s = list(input())
    stack = []
    top =0

    rst =''
    for i in s:
        if i.numeric():
            rst += i

        elif not i.numeric():
            if i == ')':
                rst += stack.pop()
