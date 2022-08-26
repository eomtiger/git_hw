from collections import deque

def card_game(arr):
    stack = deque([])

    if len(arr) == 1:                   #한명만 남았을 때
        print(f'#{tc} {arr[0][0]}')
        return

    elif len(arr) % 2 == 0:               # 짝수 일때
        for i in range(0, len(arr)-1, 2):


            if arr[i][1] == 1 and arr[i+1][1] == 1:
                stack.append(arr[i])
            elif arr[i][1] == 1 and arr[i+1][1] == 2:
                stack.append(arr[i+1])
            elif arr[i][1] == 1 and arr[i+1][1] == 3:
                stack.append(arr[i])
            elif arr[i][1] == 2 and arr[i+1][1] == 1:
                stack.append(arr[i])
            elif arr[i][1] == 2 and arr[i+1][1] == 2:
                stack.append(arr[i])
            elif arr[i][1] == 2 and arr[i+1][1] == 3:
                stack.append(arr[i+1])
            elif arr[i][1] == 3 and arr[i+1][1] == 1:
                stack.append(arr[i+1])
            elif arr[i][1] == 3 and arr[i+1][1] == 2:
                stack.append(arr[i])
            elif arr[i][1] == 3 and arr[i+1][1] == 3:
                stack.append(arr[i])



    elif len(arr) % 2 == 1:               #홀수일 때

        if (len(arr) // 2)%2 == 1:      #길이를 2로 나눈 몫이 홀수이면

            for i in range(0, len(arr), 2):

                if i == len(arr)-1:
                    stack.append(arr[i])

                else:
                    if arr[i][1] == 1 and arr[i + 1][1] == 1:
                        stack.append(arr[i])
                    elif arr[i][1] == 1 and arr[i + 1][1] == 2:
                        stack.append(arr[i + 1])
                    elif arr[i][1] == 1 and arr[i + 1][1] == 3:
                        stack.append(arr[i])
                    elif arr[i][1] == 2 and arr[i + 1][1] == 1:
                        stack.append(arr[i])
                    elif arr[i][1] == 2 and arr[i + 1][1] == 2:
                        stack.append(arr[i])
                    elif arr[i][1] == 2 and arr[i + 1][1] == 3:
                        stack.append(arr[i + 1])
                    elif arr[i][1] == 3 and arr[i + 1][1] == 1:
                        stack.append(arr[i + 1])
                    elif arr[i][1] == 3 and arr[i + 1][1] == 2:
                        stack.append(arr[i])
                    elif arr[i][1] == 3 and arr[i + 1][1] == 3:
                        stack.append(arr[i])

        elif (len(arr) // 2) % 2 == 0:  # 길이를 2로 나눈 몫이 짝수이면

            for i in range(0, len(arr), 2):
                # print(i)

                if i == int((len(arr) - 1)/2):
                    stack.append(arr[i])

                elif i > int((len(arr) - 1)/2):
                    i -= 1
                    if arr[i][1] == 1 and arr[i + 1][1] == 1:
                        stack.append(arr[i])
                    elif arr[i][1] == 1 and arr[i + 1][1] == 2:
                        stack.append(arr[i + 1])
                    elif arr[i][1] == 1 and arr[i + 1][1] == 3:
                        stack.append(arr[i])
                    elif arr[i][1] == 2 and arr[i + 1][1] == 1:
                        stack.append(arr[i])
                    elif arr[i][1] == 2 and arr[i + 1][1] == 2:
                        stack.append(arr[i])
                    elif arr[i][1] == 2 and arr[i + 1][1] == 3:
                        stack.append(arr[i + 1])
                    elif arr[i][1] == 3 and arr[i + 1][1] == 1:
                        stack.append(arr[i + 1])
                    elif arr[i][1] == 3 and arr[i + 1][1] == 2:
                        stack.append(arr[i])
                    elif arr[i][1] == 3 and arr[i + 1][1] == 3:
                        stack.append(arr[i])

                else:
                    if arr[i][1] == 1 and arr[i + 1][1] == 1:
                        stack.append(arr[i])
                    elif arr[i][1] == 1 and arr[i + 1][1] == 2:
                        stack.append(arr[i + 1])
                    elif arr[i][1] == 1 and arr[i + 1][1] == 3:
                        stack.append(arr[i])
                    elif arr[i][1] == 2 and arr[i + 1][1] == 1:
                        stack.append(arr[i])
                    elif arr[i][1] == 2 and arr[i + 1][1] == 2:
                        stack.append(arr[i])
                    elif arr[i][1] == 2 and arr[i + 1][1] == 3:
                        stack.append(arr[i + 1])
                    elif arr[i][1] == 3 and arr[i + 1][1] == 1:
                        stack.append(arr[i + 1])
                    elif arr[i][1] == 3 and arr[i + 1][1] == 2:
                        stack.append(arr[i])
                    elif arr[i][1] == 3 and arr[i + 1][1] == 3:
                        stack.append(arr[i])



    card_game(stack)






T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = deque(map(int, input().split()))
    arr_tup = deque([])
    for i in range(len(arr)):
        arr_tup.append((i+1, arr[i]))
    arr = arr_tup
    # print(arr)
    card_game(arr)

