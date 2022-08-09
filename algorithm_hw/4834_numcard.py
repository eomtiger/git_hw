T = int(input())

num_list = []
cnt_num_list = []
for i in range(T):
    N = int(input())

    arr = list(map(int, input()))

    #print(arr)

    cnt_list = [0]*10   #[0,0,0,0,0,0,0,0,0,0,0]

    for j in range(len(arr)):  #arr가 들어가면 1씩 더함
        cnt_list[arr[j]] += 1

    #print(cnt_list)

    maxV = [0]                  #카드의 개수 최대
    num = [0]                    # 카드의 숫자
    for k in range(len(cnt_list)):  #최대값 찾기
        if cnt_list[k] >= maxV[0]:
            maxV[0] = cnt_list[k]
            num[0] = k
    #print(num[0])
    num_list.append(num[0])
    cnt_num_list.append(cnt_list[num[0]])
    # print(num[0], cnt_list[num[0]])

for i in range(len(num_list)):
    print(num_list[i], cnt_num_list[i])




