T = int(input())

num_purple_list = []        #겹친 보라색 격자 개수를 담은 리스트
for tc in range(T):
    N = int(input())
    arr_list = []
    for n in range(N):
        arr = list(map(int, input().split()))  #input을 arr에 담음
        arr_list.append(arr)

    red_list = []                   #red 격자 모음
    blue_list = []                  #blue 격자 모음

    for a in range(len(arr_list)):
        if arr_list[a][-1] == 1:        #arr 마지막 숫자가 1이면 red
            for i in range(arr_list[a][0], arr_list[a][2]+1):  #가로 길이와 세로 길이의 범위로 격자 모두 구함
                for j in range(arr_list[a][1], arr_list[a][3]+1):
                    red_list.append((i, j))

        elif arr_list[a][-1] == 2:              #상동 (blue)
            for i in range(arr_list[a][0], arr_list[a][2]+1):
                for j in range(arr_list[a][1], arr_list[a][3]+1):
                    blue_list.append((i, j))

    set_red_list = set(red_list)    #겹치는 부분을 set으로 없애줌
    set_blue_list = set(blue_list)

    num_purple = len(set_red_list & set_blue_list) #레드와 블루의 교집합
    num_purple_list.append(num_purple)              #퍼플 격자 개수를 리스트에 담음

for i in range(T):
    print('#'+str(i+1), num_purple_list[i])


