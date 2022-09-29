T = int(input())

def search(l, r, i, select):
    global cnt

    m = (l + r) // 2

    if arr[m] == i:

        return True

    elif arr[m] < i:
        if select == 'right':
            return False

        if search(m+1, r, i, 'right'):
            return True

    elif arr[m] > i:
        if select == 'left':
            return False

        if search(l, m - 1, i, 'left'):
            return True



for tc in range(1, 1+T):
    N, M = map(int, input().split())

    arr = list(map(int, input().split()))

    nums = list(map(int, input().split()))
    arr.sort()



    cnt = 0
    ans =0

    for i in nums:
        if i in arr:
            if search(0, len(arr)-1, i, ''):
                ans += 1


    print(f'#{tc} {ans}')




