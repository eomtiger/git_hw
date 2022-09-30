T = int(input())

move = {
    0: 0,
    1: -1,
    2: 1,
    3: -1,
    4: -1
}

for tc in range(1, T+1):
    M, A = map(int, input().split())

    move_a = list(map(int, input().split()))
    mave_b = list(map(int, input().split()))

    info = []
    for _ in range(A):
        info.append(tuple(map(int, input().split())))

    mat = [[-1] + [0]*10 for _ in range(10)]
    print(mat)
