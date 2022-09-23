T = int(input())



def noname(end, cnt):
    global maxV                 #최대 화물 개수
    end_list.clear()            #끝나는 시간 리스트 비우기
    # print(end)
    for i in range(N):
        if schedule[i][0] >= end:   #시작 시간이 이전 끝나는 시간보다 뒤면
            end_list.append(schedule[i][1])#end리스트에 추가
    if end_list:
        end = min(end_list) #끝나는 시간이 제일 작은 값을 end값으로
        noname(end, cnt+1) #재귀함수 블랙홀

    if cnt > maxV:          #end list가 비었으면
        maxV = cnt          # 그때 카운트가 maxV보다 크면 값 교체
    return





for tc in range(1, T+1):
    N = int(input())
    schedule = [tuple(map(int, input().split())) for _ in range(N)]
    end_list = []                       #끝 시간을 담은 리스트
    for i in range(N):
        end_list.append(schedule[i][1])

    end_list.sort()
    # print(end_list)
    end = min(end_list)
    cnt = 1
    maxV = 0
    noname(end, cnt)


    print(f'#{tc} {maxV}')







