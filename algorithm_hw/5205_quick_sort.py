T = int(input())

def lomuto(low, high):
    def partition(low, high):
        pivot = arr[high]
        left = low

        for right in range(low, high):
            if arr[right] < pivot:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1

        arr[left], arr[high] = arr[high], arr[left]

        return left

    if low < high:
        pivot = partition(low, high)
        lomuto(low, pivot-1)
        lomuto(pivot + 1, high)


for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    lomuto(0, len(arr)-1)
    rst = arr[N//2]
    print(f'#{tc} {rst}')

