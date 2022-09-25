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
        y = int(p_list[0] + p_list[1] + p_list[2] + p_list[3])
        m = int(p_list[5] + p_list[6])
        d = int(p_list[8] + p_list[9])

        m = m + ops[p_list[-1]]
        if m > 12:
            m = m % 13 +1
            y += 1
        elif m > 24:
            m = m % 13 +1
            y += 2

        d -= 1

        if d == 0:
            d += 28
            m -= 1

        if m == 0:
            m += 12
            y -= 1
        s_m = ''
        print(len(str(m)))
        if len(str(m)) == 1:
            s_m += '0'
            s_m += str(m)
        elif len(str(m)) == 2:
            s_m += str(m)
        s_d = ''
        if len(str(d)) == 1:
            s_d += '0'
            s_d += str(d)
        else:
            s_d += str(d)


        p_str = str(y)+'.'+s_m+'.'+s_d
        # print(p_str)
        # print(today)

        if int(today[0:4]) > int(p_str[0:4]):
            answer.append(p+1)
        elif int(today[0:4]) == int(p_str[0:4]):
            if int(today[5:7]) > int(p_str[5:7]):
                answer.append(p+1)
            elif int(today[5:7]) == int(p_str[5:7]):
                if int(today[8:]) > int(p_str[8:]):
                    answer.append(p+1)





    return answer

# today = "2009.05.01"
#
# terms = ["A 8"]
# privacies = ["2009.05.01 A"]

today = "2022.05.19"

terms = ["A 6", "B 12", "C 3"]
privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]

print(solution(today, terms, privacies))