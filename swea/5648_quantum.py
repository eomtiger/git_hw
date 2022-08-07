# import copy
# N= int(input())
# sum_energy = 0
# input_list = []
# for i in range(N):
#     x, y, direction, K = map(int, input().split()) #맵으로 띄어쓰기로 받은 인풋을 인트로 할당
#     a= [x,y,direction,K]                #할당받은 변수들을 a라는 리스트에 저장
#     input_list.append(a)   #여기까지 인풋을 리스트로 만들고 이중 리스트로 저장
# turn = 0
# while (len(input_list) != 0) and (turn <= 2000):    #input에 아무것도 없지않고, turn이 2000천번 이하인 동안 while문을 돌림

#     for j in range(len(input_list)):  # 원소마다 싹 돌리기
#         if input_list[j][2] == 0:    #상
#             input_list[j][1] += 0.5    #y축 더하기 1
#         elif input_list[j][2] == 1:   #하
#             input_list[j][1] += -0.5    #y축 빼기 1
#         elif input_list[j][2] == 2:  #좌
#             input_list[j][0] += -0.5   # x축 빼기 1
#         elif input_list[j][2] == 3:   # 우
#             input_list[j][0] += 0.5     #y축 빼기 1
#     loc = []                           #위치 좌표를 담을 리스트
#     for k in range(len(input_list)):    
#         loc_tuple = (input_list[k][0], input_list[k][1]) #위치좌표 생성
#         loc.append(loc_tuple)
#     #print(loc)

#     loc_copy = copy.deepcopy(loc) # 굳이 카피할 필요는 없었음

#     input2 = []                     #빈 리스트를 만들고
#     for l in range(len(loc)):       #a에 팝하고 
#         a = loc_copy.pop(l)
        
#         if a in loc_copy:            #loc에 a랑 같은 좌표가 남아있다면
#             sum_energy += input_list[l][3] #에너지를 합친다

#         elif a not in loc_copy:         #loc에 a와 같은 좌표가 없다면
#             input2.append(input_list[l]) #input2에 해당 인덱스의 input_list 요소를 더한다
        
#         loc_copy.insert(l, a)           #다시 loc의 해당 인덱스에 a를 넣는다
#         #print(loc_copy)   

#     input_list = input2                 #input2를 다시 input_list에 넣음

    
#     turn += 1  

# print(sum_energy)






# T = int(input())
# b=[]
# # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
# for test_case in range(1, T + 1):
#     import copy
#     N= int(input())
#     sum_energy = 0
#     input_list = []
#     for i in range(N):
#         x, y, direction, K = map(int, input().split()) #맵으로 띄어쓰기로 받은 인풋을 인트로 할당
#         a= [x,y,direction,K]                #할당받은 변수들을 a라는 리스트에 저장
#         input_list.append(a)   #여기까지 인풋을 리스트로 만들고 이중 리스트로 저장
#     turn = 0
#     while (len(input_list) != 0) and (turn <= 2000):    #input에 아무것도 없지않고, turn이 2000천번 이하인 동안 while문을 돌림

#         for j in range(len(input_list)):  # 원소마다 싹 돌리기
#             if input_list[j][2] == 0:    #상
#                 input_list[j][1] += 0.5    #y축 더하기 1
#             elif input_list[j][2] == 1:   #하
#                 input_list[j][1] += -0.5    #y축 빼기 1
#             elif input_list[j][2] == 2:  #좌
#                 input_list[j][0] += -0.5   # x축 빼기 1
#             elif input_list[j][2] == 3:   # 우
#                 input_list[j][0] += 0.5     #y축 빼기 1
#         loc = []                           #위치 좌표를 담을 리스트
#         for k in range(len(input_list)):    
#             loc_tuple = (input_list[k][0], input_list[k][1]) #위치좌표 생성
#             loc.append(loc_tuple)
#     #print(loc)

#         loc_copy = copy.deepcopy(loc) # 굳이 카피할 필요는 없었음

#         input2 = []                     #빈 리스트를 만들고
#         for l in range(len(loc)):       #a에 팝하고 
#             a = loc_copy.pop(l)
        
#             if a in loc_copy:            #loc에 a랑 같은 좌표가 남아있다면
#                 sum_energy += input_list[l][3] #에너지를 합친다

#             elif a not in loc_copy:         #loc에 a와 같은 좌표가 없다면
#                 input2.append(input_list[l]) #input2에 해당 인덱스의 input_list 요소를 더한다
        
#             loc_copy.insert(l, a)           #다시 loc의 해당 인덱스에 a를 넣는다
#         #print(loc_copy)   

#         input_list = input2                 #input2를 다시 input_list에 넣음

    
#         turn += 1 
#     b.append(sum_energy)

# for i in range(len(b)):
#     print(b[i])

position_list = [[0 for _ in range(4001)] for _ in range(4001)]
T = int(input())
for t in range(1, T+1):
    #상 하 좌 우
    move_list = [(1, 0), (-1, 0), (0, -1), (0, 1)]
    atom_list = []
    length = int(input())
    remove_list = set()
    energy_sum = 0
    
    #위치보정
    #0.5구간이 생길수있어서 2배로 늘려준다.
    #인덱스 접근을 위해 양수로 보정한다.
    for _ in range(length):
        x, y, move , energy = map(int, input().split())
        y = (y+1000)*2
        x = (x+1000)*2
        atom_list.append([y, x, move, energy])
        position_list[y][x] += 1
        pop_list = []
#모든원소가 사라질때까지 반복한다.
    while atom_list:
        for i in range(len(atom_list)):
            y, x, move, energy = atom_list[i]
            move_y = y + move_list[move][0]
            move_x = x + move_list[move][1]
            #배열밖으로 벗어난다면 없애버리기
            if move_x < 0 or move_x > 4000 or move_y < 0 or move_y > 4000:
                pop_list.append(i)
                continue
            #현재위치에서 삭제하고
            position_list[y][x] -= 1
            #다음위치로이동
            position_list[move_y][move_x] += 1
            #위치 표시해주기
            atom_list[i][0], atom_list[i][1] = move_y, move_x
        #위치를 벗어났다면 리스트에서 제거
        if pop_list:
            for _ in range(len(pop_list)):
                index = pop_list.pop()
                t_y, t_x =  atom_list[index][0], atom_list[index][1]
                position_list[t_y][t_x] -=1
                atom_list.pop(index)
        
        #리스트를 돌면서 원소가 2개이상인곳 찾기
        for i in atom_list:
            y, x = i[0], i[1]
            if position_list[y][x] > 1:
                remove_list.add((y,x))
        #원소가 충돌던위치와 같은 원소를찾아 에너지 더해주기
        if remove_list:
            for y, x in remove_list:
                for i in range(len(atom_list)-1, -1, -1):
                    t_y, t_x, t_e = atom_list[i][0], atom_list[i][1], atom_list[i][3]
                    if t_y == y and t_x == x:
                        position_list[t_y][t_x] -=1
                        energy_sum += t_e
                        atom_list.pop(i)
            remove_list.clear()
 
    print("#{} {}".format(t, energy_sum))





