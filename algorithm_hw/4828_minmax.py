T = int(input())

dif_list=[]
for i in range(T):
    N = int(input())
    arr = list(map(int, input().split()))

    for j in range(N-1 , -1, -1):
        for k in range(j):
            if arr[k]>arr[k+1]:
                arr[k], arr[k+1] = arr[k+1], arr[k]

    #print(arr)
    dif_list.append((arr[-1] - arr[0]))

for i in range(len(dif_list)):
    print('#' + str(i+1), dif_list[i])
