T=int(input())
result = []
for tc in range(T):

    arr = list(map(int, input().split()))
    subset_sum_list = []
    for i in range(0b1<<10): # 여기서 i를 2진법으로 이해하기 ex) i = 0 = 00000000000
        subset = []                                             i=1=0000000000001
        for j in range(10): #0부터 9까지의 부분집합에 들어갈래 말래를 결정하는 슬라이드 생성
            if i & (1<<j):  # (1<<1) = 00000000001 (1<<2) = 00000000010
                subset.append(arr[j])
        subset_sum_list.append(sum(subset))
    subset_sum_list.pop(0)

    if 0 in subset_sum_list:
        result.append(1)
    else :
        result.append(0)

for i in range(T):
    print('#'+str(i+1), result[i])