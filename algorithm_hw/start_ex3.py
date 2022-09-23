T = int(input())
ops = {
    'A': 10,
    'B': 11,
    'C': 12,
    'D': 13,
    'E': 14,
    'F': 15,
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
}
pat = {
    '001101': 0,
    '010011': 1,
    '111011': 2,
    '110001': 3,
    '100011': 4,
    '110111': 5,
    '001011': 6,
    '111101': 7,
    '011001': 8,
    '101111': 9,
}
for tc in range(1, 1+T):
    arr = list(input())
    new_arr = []
    temp = []
    for i in range(len(arr)):
        s1 = ops[arr[i]] // 2
        r1 = ops[arr[i]] % 2
        temp.append(r1)
        s2 = s1 // 2
        r2 = s1 % 2
        temp.append(r2)
        s3 = s2 // 2
        r3 = s2 % 2
        temp.append(r3)
        r4 = s3 % 2
        temp.append(r4)

        temp.reverse()
        new_arr.extend(temp)
        temp.clear()
    # print(new_arr)


    rst_list = []
    flag = True
    while flag:
        if len(new_arr) <6:
            break

        for i in range(len(new_arr)-6):
            # print(len(new_arr))
            pwd = ''
            # print(pwd)
            if len(new_arr) >= 6:
                for j in range(6):
                    pwd += str(new_arr[i+j])
                    # print(pwd)

                if pwd in pat:
                    rst_list.append(pat[pwd])
                    # print(rst_list)
                    for _ in range(i+6):
                        new_arr.pop(0)
                    break

                else:
                    continue

    for i in range(len(rst_list)):
        if i == len(rst_list)-1:
            print(rst_list[i])
        else:

            print(rst_list[i], end = ' ')



