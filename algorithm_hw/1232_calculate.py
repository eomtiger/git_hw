T = 10

def inorder(n, level):                              #중위순회로 계산을 해보자
    if value[n]:
        inorder(left[n], level+1)
        if value[n].isnumeric():                    #숫자형식이면
            cal_list.append((int(value[n]), level)) #레벨과 함께 튜플로 cal_list에 저장
        else:
            cal_list.append(value[n])               #연산자 기호면 그냥 저장
        inorder(right[n], level+1)

for tc in range(1, T+1):
    N = int(input())
    left = [0]*(N+1)                                #왼쪽자식 인덱스
    right = [0]*(N+1)                               #오른쪽 자식 인덱스
    parent = [0]*(N+1)                              #부모 인덱스
    value = [0]*(N+1)                               #각 인덱스의 값 저장
    cal_list = []                                   #계산에 필요한 값들 저장
    level = 0                                       #level 저장


    for _ in range(N):
        arr = list(input().split())

        if len(arr) == 4:                                       #인풋으로 왼쪽 오른쪽 자식까지 받았을 때
            p, c1, c2 = int(arr[0]), int(arr[2]), int(arr[3])
            if left[p] == 0:                                    #왼쪽 자식 인덱스 저장
                left[p] = c1
            if right[p] == 0:                                   #오른쪽 자식 인덱스 저장
                right[p] = c2


            parent[c1] = p                                      #부모 인덱스 저장
            parent[c2] = p                                      #부모 인덱스 저장

            value[p] = arr[1]                                   #실제 값 저장

        elif len(arr) == 3:                                     #왼쪽 자식만 인풋으로 받았을 때
            p, c1 = int(arr[0]), int(arr[2])
            if left[p] == 0:
                left[p] = c1
            if p != 1:
                parent[c1] = p

            value[p] = arr[1]

        elif len(arr) == 2:                                     #자식이 없을 때
            p = int(arr[0])
            value[p] = arr[1]


    # print(left)
    # print(right)
    # print(parent)
    # print(value)

    inorder(1, level)                               #inorder 재귀 함수 타기
    # print(cal_list) ex) [(261, 2), '-', (61, 2), '/', (81, 2), '-', (71, 2)]

    ops = {                                         #연산자 람다함수로 만들기
        '+': (lambda x, y: x + y),
        '*': (lambda x, y: x * y),
        '-': (lambda x, y: x - y),
        '/': (lambda x, y: x / y)
    }

    stack = []                                      #스택에 쌓으면서 문제 해결
    for i in range(len(cal_list)):
        if (cal_list[i] == '+') or (cal_list[i] == '-') or (cal_list[i] == '*') or (cal_list[i] == '/'):
            stack.append(cal_list[i])   #연산자이면 스택에 쌓기

        else:                           #연산자가 아니면
            stack.append(cal_list[i])   #일단 스택에 쌓고
            # print(stack)
            while len(stack) != 1:      #스택 길이가 1보다 크면 계속
                if len(stack) >= 3 and stack[-1][1] == stack[-3][1]:
                    #스택의 길이가 3보다 크고 스택의 마지막 값의 레벨과 스택의 마지막에서 -2번째 값의 레벨이 같다면
                    new_tuple = (ops[stack[-2]](stack[-3][0], stack[-1][0]), stack[-1][1]-1)
                    #새로운 튜플을 만들어서 저장
                    stack.pop()
                    stack.pop()
                    stack.pop()
                    stack.append(new_tuple)
                    #ex) [(261, 2), '-', (61, 2)] -> [(200, 1)]
                elif len(stack) >= 3 and stack[-1][1] != stack[-3][1]:
                    break
                # 스택의 길이는 3이상인데 두 튜플의 레벨이 다르다면 while문을 깨고 for문 돌림
    print(f'#{tc} {int(stack[0][0])}')


