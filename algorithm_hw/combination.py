arr = ['a', 'b', 'c']

# for i in range(len(arr)):
#     for j in range(i+1, len(arr)):
#         # print(arr[i], arr[j])

''' =================================='''

for i in range(len(arr)):
    for j in range(i, len(arr)):
        print(arr[i], arr[j])

''' =================================='''
n = 5
m = 3
arr = ['a', 'b', 'c', 'd', 'e']
sel = [0]*m
def combination(idx, sidx):
    if sidx == m:
        print(sel)
        return

    if idx == n:
        return

    sel[sidx] = arr[idx]
    combination(idx+1, sidx+1)
    combination(idx+1, sidx)

combination(0,0)


