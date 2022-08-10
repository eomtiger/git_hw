import sys

sys.stdin = open('input.txt')

dif_list=[]                                                         #차이를 받을 리스트
for _ in range(10):
    N = int(input())
    arr = list(map(int, input().split()))

    turn=0                                                          #turn이 N보다 작을동안 while문
    dif = [-1]
    while turn<N:
        for i in range(len(arr)-1, -1, -1):                         # ascending bubble sort
            for j in range(i):
                if arr[j]>arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]

        arr[0] = arr[0]+1                                           # arr의 가장 큰 값에서 1을 빼고
        arr[-1] = arr[-1]-1                                         #arr의 가장 작은 값에서 1을 더하는 과정

        for i in range(len(arr)-1, -1, -1):                         #다시 버블 소트
            for j in range(i):
                if arr[j]>arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]

        dif[0] = arr[-1] - arr[0]                                   #차이 구하기

        if dif[0]==1 or dif[0]==0:                                  #차이가 0 또는 1이면 while break
            break
        turn += 1                                                   #한차례 평탄화 했으니 1회 추가

    dif_list.append(dif[0])                                         #while문이 끝나고 남은 dif를 리스트에 추가

#print(dif_list)

for i in range(len(dif_list)):
    print('#'+str(i+1), dif_list[i])


