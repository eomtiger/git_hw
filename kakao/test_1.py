def solution(today, terms, privacies):
    ops = {}
    for i in range(len(terms)):
        if len(terms[i]) == 3:
            ops[terms[i][0]] = int(terms[i][-1])
        else:
            ops[terms[i][0]] = int(terms[i][-2] + terms[i][-1])
    answer = []
    for p in range(len(privacies)):
        p_list = list(privacies[p])
        # print(p_list)
        if True:  # p_list[5] == '0':      # 10월보다 작을 때
            m = int(p_list[5] + p_list[6]) + ops[p_list[-1]]  # 더한 달
            print(m)
            # 연도와 달 구하기
            if m > 24:
                if m % 12 >= 10:
                    s = str(m % 12)
                    p_list[5] = s[0]
                    p_list[6] = s[1]
                    y = int(p_list[3]) + 2

                    if y > 9:
                        p_list[3] = str(y)[1]
                        p_list[2] = str(int(p_list[2]) + 1)
                    else:
                        p_list[3] = str(y)
                elif m % 12 == 0:
                    p_list[5] = '1'
                    p_list[6] = '2'
                    y = int(p_list[3]) + 2
                    if y > 9:
                        p_list[3] = str(y)[1]
                        p_list[2] = str(int(p_list[2]) + 1)
                    else:
                        p_list[3] = str(y)
                else:
                    s = str(m % 12)
                    p_list[5] = '0'
                    p_list[6] = s[0]
                    y = int(p_list[3]) + 2
                    if y > 9:
                        p_list[3] = str(y)[1]
                        p_list[2] = str(int(p_list[2]) + 1)
                    else:
                        p_list[3] = str(y)
            elif m > 12:
                if m % 12 >= 10:
                    s = str(m % 12)
                    p_list[5] = s[0]
                    p_list[6] = s[1]
                    y = int(p_list[3]) + 1
                    if y > 9:
                        p_list[3] = str(y)[1]
                        p_list[2] = str(int(p_list[2]) + 1)
                    else:
                        p_list[3] = str(y)

                elif m % 12 == 0:
                    p_list[5] = '1'
                    p_list[6] = '2'
                    y = int(p_list[3]) + 1
                    if y > 9:
                        p_list[3] = str(y)[1]
                        p_list[2] = str(int(p_list[2]) + 1)
                    else:
                        p_list[3] = str(y)


                else:
                    s = str(m % 12)
                    # print(s)
                    p_list[5] = '0'
                    p_list[6] = s[0]
                    y = int(p_list[3]) + 1
                    if y > 9:
                        p_list[3] = str(y)[1]
                        p_list[2] = str(int(p_list[2]) + 1)
                    else:
                        p_list[3] = str(y)
            else:
                if m % 12 >= 10:
                    s = str(m % 12)
                    p_list[5] = s[0]
                    p_list[6] = s[1]
                    # y = int(p_list[3]) + 1
                    # p_list[3] = str(y)
                elif m % 12 == 0:
                    p_list[5] = '1'
                    p_list[6] = '2'

                else:
                    s = str(m % 12)
                    p_list[5] = '0'
                    p_list[6] = s[0]
                    # y = int(p_list[3]) + 1
                    # p_list[3] = str(y)

            # 일 구하기
            # print(p_list)
            d = p_list[-4] + p_list[-3]
            change_d = int(d) - 1
            if change_d >= 10:
                p_list[-4] = str(change_d)[0]
                p_list[-3] = str(change_d)[1]
            elif 0 < change_d < 10:
                p_list[-4] = '0'
                p_list[-3] = str(change_d)
            else:
                p_list[-4] = '2'
                p_list[-3] = '8'

                month = p_list[5] + p_list[6]
                change_m = int(month) - 1
                if change_m >= 10:
                    p_list[5] = str(change_m)[0]
                    p_list[6] = str(change_m)[1]
                elif 0 < change_m < 10:
                    p_list[5] = '0'
                    p_list[6] = str(change_m)
                else:
                    p_list[5] = '1'
                    p_list[6] = '2'

                    year = p_list[2] + p_list[3]
                    change_y = int(year) - 1
                    if change_y >= 10:
                        p_list[2] = str(change_y)[0]
                        p_list[3] = str(change_y)[1]
                    elif 0 < change_y < 10:
                        p_list[2] = '0'
                        p_list[3] = str(change_y)

            p_str = ''
            for i in range(0, 10):
                p_str += p_list[i]
            print(p_str)

        if int(today[2] + today[3]) > int(p_str[2] + p_str[3]):
            answer.append(p + 1)

        elif int(today[2] + today[3]) == int(p_str[2] + p_str[3]):
            if int(today[5] + today[6]) > int(p_str[5] + p_str[6]):
                answer.append(p + 1)

            elif int(today[5] + today[6]) == int(p_str[5] + p_str[6]):
                if int(today[8] + today[9]) > int(p_str[8] + p_str[9]):
                    answer.append(p + 1)

    # print(ops)

    return answer

today = "2022.05.19"

terms = ["A 6", "B 12", "C 3"]
privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]

print(solution(today, terms, privacies))

#"2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]