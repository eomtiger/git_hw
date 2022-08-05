N= int(input())
sum_energy = 0
input_list = []
for i in range(N):
    x, y, direction, K = map(int, input().split())
    a= [x,y,direction,K]
    input_list.append(a)   #여기까지 인풋을 리스트로 만들고 이중 리스트로 저장
turn = 0
while (len(input_list) != 0) and (turn <= 3):

    for j in range(len(input_list)):  # 원소마다 싹 돌리기
        if input_list[j][2] == 0:    #상
            input_list[j][1] += 0.5    #y축 더하기 1
        elif input_list[j][2] == 1:   #하
            input_list[j][1] += -0.5    #y축 빼기 1
        elif input_list[j][2] == 2:  #좌
            input_list[j][0] += -0.5   # x축 빼기 1
        elif input_list[j][2] == 3:   # 우
            input_list[j][0] += 0.5     #y축 빼기 1
    loc = []                           #위치 좌표를 담을 리스트
    for k in range(len(input_list)):    
        loc_tuple = (input_list[k][0], input_list[k][1]) #위치좌표 생성
        loc.append(loc_tuple)
    print(loc)
    loc_set = set(loc)
    for l in range(len(loc)):
        if loc[l] in loc_set:
            sum_energy += input_list[l][3]
    # input_copy = input_list.copy        
    # for m in range(len(loc)):
    #     if loc[m] in loc_set:
    #         input_list.pop(m)
    turn += 1  

print(sum_energy)
-1,0,3,10
1,0,2,10





        # if loc_tuple in loc:
        #     input_list.pop(k)       #위치 좌표가 loc 안에 있으면 input_list에서 원자를 날림

        # elif loc_tuple not in loc:
        #     loc.append(loc_tuple)








