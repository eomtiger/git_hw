def bracket(s):

    stack = []
    top = 0
    rst = 1

    for i in range(len(s)):
        if s[i] == '{' or s[i] == '(':                      #여는 괄호면 스택에 쌓음
            stack.append(s[i])
            top += 1


        elif top == 0 and (s[i] == '}' or s[i] == ')'):     #스택이 비었는데 닫는 괄호가 들어오면 결과값 0으로 바꾸고 브레이크
            rst = 0
            break

        elif s[i] == '}' and stack[-1] == '{':              #앞뒤 괄호가 맞으면
            stack.pop()                                     #여는 괄호 pop
            top -= 1                                        #한칸 내림
        elif s[i] == '}' and stack[-1] == '(':              #앞뒤 괄호가 다르면
            rst = 0                                         #브레이크
            break
        elif s[i] == ')' and stack[-1] == '(':              #위와 같은 방식
            stack.pop()
            top -= 1
        elif s[i] == ')' and stack[-1] == '{':
            rst = 0
            break

    if top != 0:                                            #마지막에 높이가 0이 아니면
        rst = 0                                             #결과는 0


    return rst




T = int(input())

for tc in range(1, T+1):
    s = input()
    print(f'#{tc} {bracket(s)}')