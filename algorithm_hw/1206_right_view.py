N=int(input())
arr = list(map(int, input().split()))

total_floor = 0 # 조망권이 있는 전체 층수의 합

for i in range(2, N-2):
    diff_list=[]        #기준과 양옆 네 칸의 차이를 담을 리스트
    if arr[i]>arr[i-2] and arr[i]>arr[i-1] and arr[i]>arr[i+1] and arr[i] > arr[i+2]:
        diff_list.append(arr[i]-arr[i-2])
        diff_list.append(arr[i]-arr[i-1])
        diff_list.append(arr[i]-arr[i+1])
        diff_list.append(arr[i]-arr[i+2])
    
        least_diff=[255]    #최소 차가 255부터 시작
        for i in range(4):          
            if diff_list[i]<least_diff[0]:    #최소 차의 값을 구함
                least_diff[0] = diff_list[i]

        total_floor += least_diff[0] # 최소 차의 값을 구하고 전체에 더함

print(total_floor)

        
