# import sys
# sys.stdin = open('input.txt')
T =  int(input())
dif_sum = []
for t in range(T):

    N, M = map(int, input().split())

    v = list(map(int, input().split()))


    sum_list = []         #합들의 리스트
    for i in range(len(v)-M+1):   #인덱스 M까지 돌리기
        sum_1 = 0                   #sum_1은 0으로 두고 더하기
        for j in range(M):
            sum_1 += v[i+j]            #sum_1 더하기
        sum_list.append(sum_1)          #sum_1을 sum_list에 추가하기



    for i in range(len(sum_list)-1, -1, -1):     #버블소트
        for j in range(i):
            if sum_list[j]> sum_list[j+1]:
                sum_list[j], sum_list[j+1] = sum_list[j+1], sum_list[j]

    dif_sum.append(sum_list[-1] - sum_list[0])
    # print(sum_list[-1] - sum_list[0]) #최대최소 양끝의 요소

for i in range(T):
    print('#'+str(i+1), dif_sum[i])





