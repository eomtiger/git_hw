N = int(input())

babyjin_list = []
for i in range(N):

    arr = list(map(int, input()))
    countV = [0]*10              # 0부터 9까지 나타난 숫자의 개수를 담을 빈 리스트

    for i in range(len(arr)):
        countV[arr[i]] += 1    # 바로 담았다

    triplet = 0
    run = 0
    for i in range(len(countV)): #triplet이 2개이고 같은 수인 경우
        if countV[i] == 6:
            triplet +=2
            countV[i] -= 6
    
    for i in range(len(countV)): #triplet이 2개이고 다른 위치에 있는 경우
        if countV[i] == 3:
            triplet += 1
            countV[i] -= 3

    if triplet == 1: #triplet이 1개일 때
        for i in range(1, len(countV)-1): #i는 중간부터 양옆
            if countV[i-1] == 1 and countV[i] ==1 and countV[i+1]==1: #중간 i부터 양옆 =1이면
                run += 1            #run에 더함 1을
                countV[i-1] -=1     # 그리고 뺀다 해당조건을
                countV[i] -=1
                countV[i+1] -=1
    
    if triplet == 0:   # triplet이 0 일때

        for i in range(1,len(countV)-1): # 일단 3연속을 뽑고
            if countV[i-1] >= 1 and countV[i] >=1 and countV[i+1]>=1:
                run += 1
                countV[i-1] -=1
                countV[i] -=1
                countV[i+1] -=1
        if run ==1:         # 처음 for문을 돌았을 때 run이 1이면
            for i in range(1, len(countV)-1): # 한번 더 돌아라
                if countV[i-1] >= 1 and countV[i] >=1 and countV[i+1]>=1:
                    run += 1        #이하 상동
                    countV[i-1] -=1                    
                    countV[i] -=1
                    countV[i+1] -=1
    
         
            
    
    if triplet + run == 2: # trilet이나 run의 횟수의 합이 2가 넘으면 babyjin
        babyjin_list.append(1)
    else :
        babyjin_list.append(0)

for i in range(len(babyjin_list)):
    print(babyjin_list[i])

    

