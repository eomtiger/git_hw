T= 10

for tc in range(1, T+1):
    N = int(input())
    s = list(input())
    stack = []
    top =0

    rst =''
    for i in s:
        if i.isnumeric():                 #피연산자라면
            rst += i                    #rst에 더하고


        elif not i.isnumeric():           #연산자이고
            if i == '(':                  #여는괄호면
                stack.append(i)           #stack에 더해
                top += 1

            elif i == ')':                  #닫는 괄호라면
                while stack[-1] != '(':     #여는 괄호가 나올 때까지
                    rst += stack.pop()      #연산자를 빼서 출력
                    top -= 1
                stack.pop()             #'('도 스택에서 지우기
                top -= 1

            elif i == '+' or i == '-':  #연산자가 +,-이면
                while top != 0 and stack[-1] != '(':
                    rst += stack.pop()
                    top -= 1
                stack.append(i)
                top += 1

            elif i == '*' or i == '/': #연산자가 *,/ 이면
                while top != 0 and (stack[-1] == '*' or stack[-1] == '/'): #바로 앞이 곱하기나 나누기면 pop
                    rst += stack.pop()
                    top -= 1
                stack.append(i)
                top += 1
    if top != 0:
        while top != 0:
            rst += stack.pop()
            top -= 1
    # print(rst)
    '''==================================================
    여기부터 후위 표기법 계산기'''

    c_stack = []
    ops = {'+': (lambda x,y : x + y), '*': (lambda x,y : x*y) }

    for i in rst:
        if i.isnumeric():
            c_stack.append(i)
        else:
            a = c_stack.pop()
            b = c_stack.pop()
            c_stack.append(ops[i](int(a), int(b)))

    print(f'#{tc}', c_stack[0])


