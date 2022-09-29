T = int(input())

def find(x):
    if p[x] != x:               #x 자신이 대장이 아니면
        p[x] = find(p[x])       #대장을 찾아가면서 compression
    return p[x]                 #재귀함수 제일 아래 단의 대장이 리턴되면서 그 값으로 전부 갱신됨

def union(x, y):
    p[find(y)] = find(x)        #y의 대장을 찾아서 x의 대장으로 바꿈


for tc in range(1, T+1):
    V, E = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(E)]
    p = []                      #대장을 저장할 배열
    for i in range(V+1):        #처음엔 전부 자기 자신
        p.append(i)

    rst = 0
    cnt = 0
    edges.sort(key=lambda x: x[2]) #이것 좀 외우자 람다 좀

    for x, y, w in edges:
        if find(x) != find(y):      #대장이 다르면
            rst += w                #가중치 더하고
            cnt += 1                #횟수 더하고(간선의 개수)
            union(x, y)             #합병하자(대장을 통일)

        if cnt == E:                #간선 개수 넘어가면
            break                   #끝

    print(f'#{tc} {rst}')
