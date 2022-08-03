import random  # 랜덤 모듈 활용

print("================================")
print("        Battle Ship Game        ")
print("            START !!            ")
print("================================")

a = 0
while a < 1 or a >= 14:

    a = int(input('배를 위치시킬 시작점을 고르세요. :'  ))

    if a > 13 :
        print('----해당 위치에는 배를 둘 수 없습니다.')
    
loc = a
com_loc = random.randint(1,13)

player_sea = [0] * 15  # 플레이어의 해역
player_attacked = [False] * 15  # 플레이어의 공격 위치 기록

computer_sea = [0] * 15  # 컴퓨터의 해역
computer_attacked = [False] * 15  # 컴퓨터의 공격 위치 기록

for i in range(loc-1,loc+2):
    player_sea[i]= 1

for i in range(com_loc-1, com_loc +2):
    computer_sea[i] =1

print('------------------------------------------------------------------')
print('<information>')
print('플레이어 해역 : ', player_sea)
print('플레이어의 공격 기록: ', player_attacked)
print('------------------------------------------------------------------')
#print(player_sea)
#print(computer_sea)

switch = True
i = 0
while switch :
    i += 1
    att_loc = 0

    while 1 > att_loc or att_loc >= 14:

        att_loc = int(input('공격할 위치를 선택하세요 : '))

        if att_loc > 15  or att_loc<1:
            print('해역의 범위를 벗어난 위치를 선택하셨습니다. 다시 선택해주세요')

    player_attacked[att_loc-1] = True


    if computer_sea[att_loc-1] == 1:

        print(player_attacked)
        print('<'+str(i)+'라운드 결과!>')
        print('컴퓨터의 해역 : ', computer_sea)
        print('플레이어는 컴퓨터의 해역'+str(att_loc)+'번째 칸을 공격하였고, 컴퓨터 배는 파괴되었습니다.')
        print('게임이 종료'+' '+ str(i)+'라운드 만에 플레이어의 승리입니다.')
        switch = False

    elif computer_sea[att_loc-1] == 0:
        
        com_att_loc = random.randint(1,15)
        while computer_attacked[com_att_loc-1] == True:          
            com_att_loc = random.randint(1,15)

        computer_attacked[com_att_loc-1] = True
        print('플레이어의 공격기록', player_attacked)
        #print(computer_attacked)

        if player_sea[com_att_loc-1] == 1:
        
            print('<'+str(i)+'라운드 결과!>')
            print('플레이어는 컴퓨터 해역'+ str(att_loc)+'칸을 공격하였으나 실패')
            print('컴퓨터는 플레이어의 해역'+str(com_att_loc)+'번째 칸을 공격하였고, 플레이어 배는 파괴되었습니다.')
            print('게임이 종료'+' '+ str(i)+'라운드 만에 컴퓨터의 승리입니다.')
            switch = False
        elif player_sea[com_att_loc-1] == 0:
        
            print('<'+str(i)+'라운드 결과!>')
            print('플레이어는 컴퓨터 해역'+ str(att_loc)+'칸을 공격하였으나 실패')
            print('컴퓨터는 플레이어의 해역'+str(com_att_loc)+'번째 칸을 공격하였으나 실패')


    
       







#------------------------------------------------------------------------------------------------------------------------------




# 필요에 따라 추가적으로 함수를 만들어 자유롭게 활용할 수 있습니다.
# 각자의 해역에 배를 위치시키는 함수
#def set_ship(index, sea):
#    pass
    

#player_sea = [0] * 15  # 플레이어의 해역
#player_attacked = [False] * 15  # 플레이어의 공격 위치 기록

#computer_sea = [0] * 15  # 컴퓨터의 해역
#computer_attacked = [False] * 15  # 컴퓨터의 공격 위치 기록

#round = 1  # 게임 라운드

# 1. 게임 준비
#while True:
    #pass
    # 1-1) 플레이어의 배 시작 위치 고르기

    # 1-2) 범위를 벗어난 시작점을 고른 경우


# 1-3) 컴퓨터의 배 시작 위치를 랜덤으로 지정합니다.

# 1-4) 플레이어와 컴퓨터의 해역에 각각 배 위치시키기

# 2. 라운드 진행
#while True:
    #pass
    # 2-1) 플레이어 공격

    # 2-2) 플레이어의 공격 위치 선택

    # 2-3) 플레이어의 공격이 성공한 경우

    # 2-4) 플레이어의 공격이 실패한 경우

    # 2-5) 컴퓨터의 공격 위치 지정
    # 컴퓨터가 공격하지 않은 위치를 나타내는 리스트

    # 2-6) 컴퓨터의 공격이 성공한 경우

    # 2-7) 컴퓨터의 공격이 실패한 경우
