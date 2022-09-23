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

for tc in range(1, T+1):
    arr = list(input())
    # print(arr)
    # print(ops[arr[1]])
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
    print(new_arr)
    rst_list = []
    for i in range(0, len(new_arr), 7):
        rst = 0
        if len(new_arr) - i >= 7:

            for j in range(0, 7):
                if new_arr[i + j]:
                    rst += 2 ** (6 - j)

        else:
            for j in range(0, len(new_arr) - i):
                if new_arr[i+j]:
                    rst += 2**(6-j)
                # print(rst)
        rst_list.append(rst)

    for i in range(len(rst_list)):
        if i == len(rst_list) - 1:

            print(f'{rst_list[i]}')

        else:
            print(f'{rst_list[i]}', end = ' ')









