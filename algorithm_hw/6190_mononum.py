T= int(input())

for tc in range(1, T+1):
    N = int(input())

    arr = list(map(int,input().split()))
    # print(arr)


    multiple_list = []
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            multiple_list.append(arr[i] * arr[j])
    # print(multiple_list)


    mono_none = []
    #########################나누기 자릿수 실패 #################################
    # for i in range(len(multiple_list)):
    #     m = multiple_list[i]  # m =8
    #
    #     share = None      # 0
    #     remainder = 10
    #
    #     # print(remainder)
    #     while share:
    #         next_share = m // 10
    #         next_remainder = m % 10
    #         if next_remainder > remainder:
    #             mono_none.append(multiple_list[i])
    #             break
    #         else:
    #             minR = next_remainder
    #             remainder = next_remainder
    #             print(remainder)
    #             share = next_share
    #         print(remainder)
    #
    #     flag = False
    #
    #     # print(share, remainder)
    #
    # print(mono_none)
########################################################################################


#################스트링으로 구함 ##########################

    for i in range(len(multiple_list)):
        num = str(multiple_list[i])
        for j in range(len(num)-1):
            if int(num[j]) > int(num[j+1]):
                mono_none.append(multiple_list[i])
                break
###########################################################


    mono_set = set(multiple_list) - set(mono_none)
    if not mono_set:
        print(f'#{tc}', -1)
    else:
        print(f'#{tc}', max(mono_set))