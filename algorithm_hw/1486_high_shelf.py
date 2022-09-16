T = int(input())

for tc in range(1, T+1):
    N, B = map(int, input().split())

    heights = list(map(int, input().split()))

    sum_list = []
    for i in range(1<< len(heights)):
        selected = []
        for j in range(len(heights)):
            if i & (1 << j):
                selected.append(heights[j])

        sum_list.append(sum(selected))

    stack_list = []
    for i in range(len(sum_list)):
        if sum_list[i] >= B:
            stack_list.append(sum_list[i])

    print(f'#{tc} {min(stack_list)-B}')




