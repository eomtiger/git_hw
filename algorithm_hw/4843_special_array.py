T = int(input())
special_array_list = []
for tc in range(T):
    N = int(input())
    arr = list(map(int, input().split()))

    arr.sort()
    # print(arr)
    special_array = []
    for i in range(5):
        maxV = arr.pop(-1)
        MinV = arr.pop(0)
        special_array.append(maxV)
        special_array.append(MinV)

    special_array_list.append(special_array)

for i in range(T):
    print('#'+ str(i+1), end= ' ')
    print(*special_array_list[i])
