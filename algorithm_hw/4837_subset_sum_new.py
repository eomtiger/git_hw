A = [1,2,3,4,5,6,7,8,9,10,11,12]

num_list = []          #num을 담을 리스트
T = int(input())
for tc in range(T):
    N, K = map(int,input().split())   #N은 부분집합 원소의 개수, 원소의 합이 K인 부분집합의 개수
    sub_set_list = []                   # 서브셋을 담을 리스트
    for i in range(1<<12):              #00000000부터 100000000까지
        sub_set = []                    #subset 원소를 담자
        for j in range(12):             #가림막 stride
            if i & (1<<j):              #가림막에 걸리는 i가 있다면
                sub_set.append(A[j])    #부분집합에 더하고
        sub_set_list.append(sub_set)    #부분집합을 모아 리스트로 만들고
        #print(N, K)

    num = 0
    for i in range(len(sub_set_list)):      #부분집합 원소 수가 N과 같고 원소합이 K인 부분집합 개수 구하기
        if len(sub_set_list[i]) == N and sum(sub_set_list[i]) ==K:
            num +=1

    num_list.append(num)

for tc in range(T):
    print('#'+str(tc+1), num_list[tc])




