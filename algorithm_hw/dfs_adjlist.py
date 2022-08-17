

def dfs(v, N):

    visited = [0]*N     #visited생성
    stack = [0]*N       # stack 생성
    top = -1


    visited[v] = 1
    print(v)
    while True:
        for w in adjlist[v]:
            if visited[w] == 0:
                top+=1
                stack[top] = v
                v = w
                visited[w]=1
                print(v)
                break
        else:
            if top != -1:
                v = stack[top]
                top -= 1
            else:
                break

v, N = map(int, input().split())
arr = list(map(int, input().split()))
adjlist = list([]*(v))

print(adjlist)

