T = 10

def inorder(n, level):
    if value[n]:
        inorder(left[n], level+1)
        if value[n].isnumeric():
            cal_list.append((value[n], level))
        else:
            cal_list.append(value[n])
        inorder(right[n], level+1)

for tc in range(1, T+1):
    N = int(input())
    left = [0]*(N+1)
    right = [0]*(N+1)
    parent = [0]*(N+1)
    value = [0]*(N+1)
    cal_list = []
    level = 0


    for _ in range(N):
        arr = list(input().split())

        if len(arr) == 4:
            p, c1, c2 = int(arr[0]), int(arr[2]), int(arr[3])
            if left[p] == 0:
                left[p] = c1
            if right[p] == 0:
                right[p] = c2


            parent[c1] = p
            parent[c2] = p

            value[p] = arr[1]

        elif len(arr) == 3:
            p, c1 = int(arr[0]), int(arr[2])
            if left[p] == 0:
                left[p] = c1
            if p != 1:
                parent[c1] = p

            value[p] = arr[1]

        elif len(arr) == 2:
            p = int(arr[0])
            value[p] = arr[1]


    # print(left)
    # print(right)
    # print(parent)
    # print(value)

    inorder(1, level)
    print(cal_list)

    ops = {
        '+': (lambda x, y: x + y),
        '*': (lambda x, y: x * y),
        '-': (lambda x, y: x - y),
        '/': (lambda x, y: x / y)
    }

    stack =  []
    for i in range(len(cal_list)):
