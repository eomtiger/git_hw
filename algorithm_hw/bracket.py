T = int(input())

for tc in range(1, T+1):
    brac = input()                  #괄호 인풋받기

    s = []                          #스택
    top = 0                         #스택 높이

    for i in range(len(brac)):
        if brac[i] == '(':          #여는 괄호면 s
            s.append(brac[i])       #s에 더하고
            top += 1                #top 한칸 위로

        elif brac[i] == ')':        #닫는 괄호면
            if len(s) == 0:         #stack 높이가 0 일 때
                s.append(')')       #')'를 더함

            elif s[top-1] == '(' :  #스택 높이-1(인덱스 컨트롤)이 여는 괄호이면
                s.pop(top-1)        #'('을 빼주고
                top -= 1            #스택높이를 한칸 내림


                                    #for문을 다 돌고 난 후
    if len(s) != 0:                 #스택 높이가 0이 아니면
        print(-1)
    elif len(s) == 0:               #스택 높이가 0이면
        print(1)


