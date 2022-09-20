T = int(input())

for tc in range(1, T+1):
    N = int(input())
    temp = int(N**(1/3)+0.1)
    if temp**3 != N:
        temp = -1

    print(f'{tc} {temp}')

