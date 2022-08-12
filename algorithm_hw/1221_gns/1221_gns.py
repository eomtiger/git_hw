import sys
sys.stdin = open('GNS_test_input.txt', 'r')

a=['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']


# print(str(ZRO), type(str(ZRO)))
T = int(input())
arr_convert_list = []
for tc in range(T):
    tc, length = input().split()
    arr = list(input().split())

    for i in range(len(arr)):
        arr[i] = a.index(arr[i])

    arr.sort()

    for i in range(len(arr)):
        arr[i] = a[arr[i]]

    arr_convert_list.append(arr)

for i in range(10):
    print('#'+str(i+1))
    print(*arr_convert_list[i])



