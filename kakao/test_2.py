def solution(cap, n, deliveries, pickups):
    answer = -1
    stack = []
    for i in range(n):
        stack.append([deliveries[i], pickups[i]])
    print(stack)

    while stack != 0:
        d = 0       # 배달갈 물건 개수
        p = 0
        for a in range(len(stack), -1, -1):
            for b in range(1, stack[a][0] + 1):
                d += 1
                stack[a][0] -= 1
                if d == cap or stack[a][0] == 0:
                    break
            if d == cap or stack[a][0] == 0:
                break

        if stack[-1][0] >= cap:
            d = cap
            stack[-1][0] -= d
            for i in range(len(stack), -1, -1):
                for j in range(1, stack[i][1] + 1):
                    p += 1
                    stack[i][1] -= 1
                    if p == cap:
                        break





    return answer

cap = 4
n = 5
deliveries = [1,0,3,1,2]
pickups = [0,3,0,4,0]

solution(cap, n, deliveries, pickups)
