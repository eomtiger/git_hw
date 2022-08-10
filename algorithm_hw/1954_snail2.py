T = int(input())

for tc in range(T):
    N = int(input())

    matrix = list([0]*N for i in range(N))
    arr = []
    for i in range(1, N**2+1):
        arr.append(i)

    print(arr)

