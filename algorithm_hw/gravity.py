N = int(input())

for i in range(N):
    arr_len = int(input())
    arr = list(map(int, input().split()))

maxL = [0]                #가장 큰 수를 받는 리스트
maxL_loc = [0]              # 가장 큰 수가 있는 리스트

dropL = []                  #낙차
block = 0                   # 떨어질 때 걸리는 블럭 수

for i in range(len(arr)):
    if arr[i] > maxL[0]:    #가장 큰 수 찾기
        maxL[0] = arr[i]
        
        maxL_loc[0] = i     #가장 큰 수의 위치
   
for i in range(len(arr)):
    if arr[i] >= maxL[0]:
        block += 1          #가장 큰 수와 겹치는 블럭 개수
      
        
dropL.append(len(arr)-maxL_loc[0]-block) # 낙차를 리스트에 넣음
                                        # arr의 길이가 낙차의 높이
                                        #제일 긴 아이의 위치,인덱스
                                        #제일 끝쪽 블럭과 겹치는 블럭들의 수

    


while maxL_loc[0]>0:            #위치가 0일 때까지
    block = 0

    maxL[0] = 0                     
    for i in range(maxL_loc[0]):    #위와 같음
        if arr[i] > maxL[0]:
            maxL[0] = arr[i]
            maxL_loc[0] = i
            #remain = i
            #print(remain)

    
    for i in range(len(arr)):       

        if arr[i] >= maxL[0]:
            block += 1                  #상동
            print(block)
    
    dropL.append(len(arr) - maxL_loc[0] - block)

print(dropL)
dropL_Max = [0]
for i in range(len(dropL)):           #낙차 리스트 중 가장 큰 놈
    if dropL[i]> dropL_Max[0]:
        dropL_Max[0]= dropL[i]

print(dropL_Max[0])




