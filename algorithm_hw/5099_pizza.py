from collections import deque
T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    pizzas = deque(map(int, input().split()))    #피자들을 deque로

    for i in range(len(pizzas)):                #피자에 인덱스를 담아주자
        pizzas.append([i+1, pizzas[i]])
    for i in range(M):                          #피자 리스트에서 인덱스 없는 원소는 제거하자
        pizzas.popleft()


    fire_pit = deque()                          #화덕을  deque로 구현

    for i in range(N):                          #화덕에 피자를 올리자
        fire_pit.append(pizzas.popleft())              #화덕 용량만큼



    while len(fire_pit) != 1:                            #화덕에 피자가 하나 남을 때까지 돌아라
        if fire_pit[0][1] == 0 and len(pizzas) != 0:   #한바퀴 돌았을 때 치즈가 0이고 넣어야 할 피자가 있으면
            fire_pit.popleft()                      #화덕에서 피자를 빼고
            fire_pit.appendleft(pizzas.popleft())   #다음 피자를 넣는다


        while len(fire_pit) != 1 and fire_pit[0][1] == 0:  #화덕에 남은 피자 수가 1 이상이고 꺼낼 피자의 치즈가 0인 동안
            fire_pit.popleft()                              #꺼내라

        fire_pit.append(fire_pit.popleft())         # 화덕을 돌린다 꺼낼 장소를 지나치면
        fire_pit[-1][1] //= 2                          #치즈를 녹인다

    print(f'#{tc} {fire_pit[0][0]}')
