def find_root(V):               #루트찾기
    for i in range(1,V+1):
        if par[i] == 0:         #parent가 없는 경우
            return i

def preorder(n):                #전위순회
    if n:
        print(n, end = ' ')     #root
        preorder(ch1[n])        #left
        preorder(ch2[n])        #right

V = int(input())
arr = list(map(int, input().split()))
E = V - 1

ch1 = [0]*(V+1)
ch2 = [0]*(V+1)
par = [0]*(V+1)

for i in range(E):
    p, c = arr[i*2], arr[i*2+1]     #부모와 자식 값
    if ch1[i] == 0:
        ch1[p] = c
    else:
        ch2[p] = c

    par[c] = p

root = find_root(V)
preorder(root)
