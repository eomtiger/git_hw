T = int(input())

ops = {'+': (lambda x, y: x+y),
       '-': (lambda x, y: x-y),
       '*': (lambda x, y: x*y),
       '/': (lambda x, y: int(x/y))}

for tc in range(1, T+1):
    s = list(input().split())
    stack = []


    for i in s:

        if i.isnumeric():
            stack.append(i)

        elif i == '.':
            if len(stack) == 1:
                c = stack.pop()
                print(f'#{tc} {c}')
                break

            else:
                print(f'#{tc}', 'error')
                break


        else:                           #+-*/
            if len(stack) >= 2:
                a = stack.pop()
                b = stack.pop()
                stack.append(ops[i](int(b), int(a)))
            elif len(stack) <= 1 :
                print(f'#{tc}', 'error')
                break






