T = int(input())

def preorder(N):                #전위순회로 개수를 세어보자
    global cnt
    if N:
        cnt += 1
        preorder(ch1[N])
        preorder(ch2[N])
    return cnt

for tc in range(1, T+1):
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))
    V = E+1

    ch1 = [0]*(V+1)             #자식 왼
    ch2 = [0]*(V+1)             #자식 오

    par = [0]*(V+1)             #부모
    cnt = 0
    for i in range(E):
        p, c = arr[i*2], arr[i*2+1]
        if ch1[p] == 0:
            ch1[p] = c

        else:
            ch2[p] = c

        par[c] = p

    # print(ch1)
    # print(ch2)
    # print(par)
    print(f'#{tc}', preorder(N))


