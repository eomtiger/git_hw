from collections import deque
T = int(input())

for tc in range(1, T+1):
    K = int(input())
    m1 = deque(map(int, input().split()))
    m2 = deque(map(int, input().split()))
    m3 = deque(map(int, input().split()))
    m4 = deque(map(int, input().split()))

    m_list = [m1, m2, m3, m4]
    touch = [m1[2], [m2[6], m2[2]], [m3[6], m3[2]], m4[6]]  #자석끼리 맞닿은 부분


    rot = [tuple(map(int, input().split())) for _ in range(K)]

    for i in range(len(rot)):
        if rot[i][0] == 1 and rot[i][1] == 1:      #첫번째 자석인데 시계 방향이면
            if touch[0] != touch[1][0]:            #첫번째와 두번째와 맞닿은 부분이 다르면
                if touch[1][1] != touch[2][0]:     #두번째와 세번째와 맞닿은 부분이 다르면
                    if touch[2][1] != touch[3]:    #세번째와 네번째 맞닿은 부분이 다르면
                        m4.append(m4.popleft())    #네번째부터 돌려
                    m3.appendleft(m3.pop())        #세번째 돌려
                m2.append(m2.popleft())            #두번째 돌려
            m1.appendleft(m1.pop())                #첫번째 돌려
            touch = [m1[2], [m2[6], m2[2]], [m3[6], m3[2]], m4[6]] #맞닿은 부분 리스트 업데이트

            #여기 아래로 전부 위와 같은 로직

        elif rot[i][0] == 1 and rot[i][1] == -1:    #반시계방향
            if touch[0] != touch[1][0]:
                if touch[1][1] != touch[2][0]:
                    if touch[2][1] != touch[3]:
                        m4.appendleft(m4.pop())
                    m3.append(m3.popleft())
                m2.appendleft(m2.pop())
            m1.append(m1.popleft())
            touch = [m1[2], [m2[6], m2[2]], [m3[6], m3[2]], m4[6]]


    # 두번째 자석인데 시계방향
        elif rot[i][0] == 2 and rot[i][1] == 1:
            if touch[1][1] != touch[2][0]:
                if touch[2][1] != touch[3]:
                    m4.appendleft(m4.pop())
                m3.append(m3.popleft())
            if touch[1][0] != touch[0]:
                m1.append(m1.popleft())
            m2.appendleft(m2.pop())
            touch = [m1[2], [m2[6], m2[2]], [m3[6], m3[2]], m4[6]]
    #두번째 반시계
        elif rot[i][0] == 2 and rot[i][1] == -1:
            if touch[1][1] != touch[2][0]:
                if touch[2][1] != touch[3]:
                    m4.append(m4.popleft())
                m3.appendleft(m3.pop())
            if touch[1][0] != touch[0]:
                m1.appendleft(m1.pop())
            m2.append(m2.popleft())
            touch = [m1[2], [m2[6], m2[2]], [m3[6], m3[2]], m4[6]]

    #세번째 시계
        elif rot[i][0] == 3 and rot[i][1] == 1:
            if touch[2][0] != touch[1][1]:
                if touch[1][0] != touch[0]:
                    m1.appendleft(m1.pop())
                m2.append(m2.popleft())
            if touch[2][1] != touch[3]:
                m4.append(m4.popleft())
            m3.appendleft(m3.pop())
            touch = [m1[2], [m2[6], m2[2]], [m3[6], m3[2]], m4[6]]
    #세번째 반시계
        elif rot[i][0] == 3 and rot[i][1] == -1:
            if touch[2][0] != touch[1][1]:
                if touch[1][0] != touch[0]:
                    m1.append(m1.popleft())
                m2.appendleft(m2.pop())
            if touch[2][1] != touch[3]:
                m4.appendleft(m4.pop())
            m3.append(m3.popleft())
            touch = [m1[2], [m2[6], m2[2]], [m3[6], m3[2]], m4[6]]

    #네번째 시계
        if rot[i][0] == 4 and rot[i][1] == 1:
            if touch[3] != touch[2][1]:
                if touch[2][0] != touch[1][1]:
                    if touch[1][0] != touch[0]:
                        m1.append(m1.popleft())
                    m2.appendleft(m2.pop())
                m3.append(m3.popleft())
            m4.appendleft(m4.pop())
            touch = [m1[2], [m2[6], m2[2]], [m3[6], m3[2]], m4[6]]

        elif rot[i][0] == 4 and rot[i][1] == -1:    #반시계방향
            if touch[3] != touch[2][1]:
                if touch[2][0] != touch[1][1]:
                    if touch[1][0] != touch[0]:
                        m1.appendleft(m1.pop())
                    m2.append(m2.popleft())
                m3.appendleft(m3.pop())
            m4.append(m4.popleft())
            touch = [m1[2], [m2[6], m2[2]], [m3[6], m3[2]], m4[6]]


    rst = 0
    if m1[0] == 1:
        rst += 1
    if m2[0] == 1:
        rst += 2
    if m3[0] == 1:
        rst += 4
    if m4[0] ==1:
        rst += 8

    print(f'#{tc} {rst}')








