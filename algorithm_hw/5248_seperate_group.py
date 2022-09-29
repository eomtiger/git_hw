T = int(input())

def find(x):                    #대장을 찾는 함수
    if p[x] != x:
        p[x] = find(p[x])       #compression
    return p[x]

def union(x, y):                #합병
    p[find(y)] = find(x)


for tc in range(1, T+1):
    N, M = map(int, input().split())

    arr = list(map(int, input().split()))
    p = []                  #각 인덱스 별 대장 기록 리스트
    for i in range(N+1):    # 처음은 자기 자신이 보스
        p.append(i)

    rst = 0
    visited = set()         #set을 하나 파준다

    for i in range(0, len(arr), 2):         #짝수마다 돌면서
        if arr[i] not in visited and arr[i+1] not in visited:   #i, i+1이 visited에 없으면
            rst += 1                                            #결과에 1 추가 하나의 조가 생성
            visited.add(arr[i])                                 #visited에 추가
            visited.add(arr[i+1])
            union(arr[i], arr[i+1])                             #둘의 조장을 정함


        elif arr[i] in visited and arr[i+1] in visited:         #i, i+1이 둘 다 있다면
            if find(arr[i]) != find(arr[i+1]):                  #둘의 조장을 비교하여 다르면
                rst -= 1                                        #조를 병합하는 것이기 때문에 결과에 1을 빼줌
                union(arr[i], arr[i+1])
            else:                                               #둘의 조장이 같다면
                pass                                            #그냥 같은 조이므로 패스

        else:                                                   #둘 중 하나만 visited에 있다면
            visited.add(arr[i])                                 #visited에 더해주고
            visited.add(arr[i+1])
            union(arr[i], arr[i + 1])                           #조장을 정해줌


    for i in range(1, N+1):                                     #위의 for문이 다 돌면
        if i not in visited:                                    #visited에 없는 애들을 찾아서
            rst += 1                                            #결과에 하나씩 추가


    print(f'#{tc} {rst}')

