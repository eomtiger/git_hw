T = int(input())

for tc in range(1, T+1):
    arr = list(input())

    rst_list = []
    for i in range(0, len(arr), 7):         #배열에서 7칸씩 나눔
        rst = 0
        for j in range(0, 7):               #나눠진 7칸을 돌면서
            if arr[i+j] == '1':             #값이 '1' 이면
                rst += 2**(6-j)             #2진법으로 바꿔주고
                # print(rst)                #rst에 더함
        rst_list.append(rst)                #7칸을 돌고 나온 결과를 리스트에 저장장


    for i in range(len(rst_list)):
        if i == len(rst_list):
            print(rst_list[i])
        else:
            print(rst_list[i], end=' ')


