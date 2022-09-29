T = int(input())

def merge_sort(arr):

    if len(arr) == 1:
        return arr

    m = len(arr)//2

    l_half = arr[:m]
    r_half = arr[m:]


    left = merge_sort(l_half)
    right = merge_sort(r_half)

    return merge(left, right)

def merge(left, right):
    global cnt
    if left[-1] > right[-1]:
        cnt += 1
    result = [0]*(len(left)+len(right))
    l = r = idx = 0
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            result[idx] = left[l]
            l += 1
            idx += 1
        else:
            result[idx] = right[r]
            r += 1
            idx += 1

    while l < len(left):
        result[idx] = left[l]
        l += 1
        idx += 1

    while r < len(right):
        result[idx] = right[r]
        r+=1
        idx += 1

    return result


for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    ans1 = merge_sort(arr)[N//2]
    ans2 = cnt

    print(f'#{tc} {ans1} {ans2}')
    # print(ans1)
    # print(ans2)

