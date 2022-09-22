T = int(input())

# def sub_set(depth):
#     if depth == N:
#         result = []
#         for j in range(N):
#             if check[j] == 1:
#                 result.append(schedule[j])
#         subset_list.append(result)
#         return
#
#     check[depth] = 0
#     sub_set(depth+1)
#
#     check[depth] = 1
#     sub_set(depth+1)

def noname(end, cnt):
    global maxV
    end_list.clear()
    print(end)
    for i in range(N):
        if schedule[i][0] >= end:
            end_list.append(schedule[i][1])
            end = min(end_list)
            noname(end, cnt+1)

    if cnt > maxV:
        maxV = cnt
    return





for tc in range(1, T+1):
    N = int(input())
    schedule = [tuple(map(int, input().split())) for _ in range(N)]
    end_list = []
    for i in range(N):
        end_list.append(schedule[i][1])

    end_list.sort()
    # print(end_list)
    end = min(end_list)
    cnt = 1
    maxV = 0
    noname(end, cnt)


    # print(maxV)
    print()






