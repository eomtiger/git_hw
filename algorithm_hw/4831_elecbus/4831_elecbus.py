# import sys
# sys.stdin("input.txt")
T= int(input())

charge_list = []
for i in range(T):
    K, N, M = map(int, input().split())
    oil = list(map(int, input().split()))
    #print(K ,N, M)
    bus_loc = 0
    charge = 0
    while bus_loc<N:

        pass_station = 0 #한번 충전하고 달릴 때 충전기 없는 역 개수
        oil_station = [] #1이면 충전기잇고 0이면 충전기 없음 길이는 K
        for k in range(1, K+1):
            if bus_loc + k in oil:
                oil_station.append(1)

            elif bus_loc + k not in oil:
                oil_station.append(0)
                pass_station += 1

        bus_pass = 0 #bus가 이전 출발점에서 충전하는 곳까지 지나간 정류장
        for j in range(K):
            if oil_station[j] ==1:
                bus_pass = j+1
        if N-bus_loc>=K:

            bus_loc = bus_loc + bus_pass
        charge += 1

        #print('pass:', pass_station)
        #print('bus:', bus_loc)
        # if N - bus_loc >=K:

        if bus_loc + K >= N:
            charge_list.append(charge)
            break
        elif pass_station == K:
            charge_list.append(0)
            break


    # charge_list.append(charge)

for i in range(T):
    print('#'+str(i+1), charge_list[i])



