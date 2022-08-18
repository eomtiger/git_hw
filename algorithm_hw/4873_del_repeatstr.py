def del_str(s):
    stack = []                      # stack을 만들고
    top = 0                         # top 위치를 0으로 지정

    for i in range(0, len(s)):
        if top == 0:                #top이 0이면 문자를 스택에 추가
            stack.append(s[i])
            top += 1                # top위치 하나 올림
        elif stack[-1] == s[i]:     #스택의 가장 위와 문자열이 같다면
            stack.pop()             #스택의 제일 위에 것을 뺀다
            top -= 1                #top -1
        else:
            stack.append(s[i])      #이외에는 스택에 문자를 추가
            top += 1

    return len(stack)

T = int(input())

for tc in range(1, T+1):

    s= input()

    print(f'#{tc} {del_str(s)}')