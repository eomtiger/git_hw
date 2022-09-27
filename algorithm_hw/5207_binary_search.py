T = int(input())

def search(l, r, i):
    global cnt, r_cnt, l_cnt

    if i > arr[r] or i < arr[l]:
        return

    m = (l+r)//2

    if arr[m] == i and r_cnt and l_cnt:
        cnt += 1

        return

    elif arr[m] < i:
        r_cnt += 1
        search(m+1, r, i)



    elif arr[m] > i:
        l_cnt += 1
        search(l, m-1, i)
    return


for tc in range(1, 1+T):
    N, M = map(int, input().split())

    arr = list(map(int, input().split()))

    nums = list(map(int, input().split()))

    # print(arr)
    # print(nums)

    cnt = 0
    r_cnt = 0
    l_cnt = 0



    for i in nums:
        if i == arr[(len(arr)-1) // 2]:
            cnt += 1


        else:
            search(0, len(arr)-1, i)
            r_cnt = 0
            l_cnt = 0

        # print(i, cnt)
    if cnt == 0:
        print(f'#{tc} {cnt}')
    elif cnt and r_cnt and l_cnt:
        print(f'#{tc} {cnt}')
    else:
        print(f'{tc} 0')
