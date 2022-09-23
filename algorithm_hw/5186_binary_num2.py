T = int(input())

for tc in range(1, T+1):
    N = float(input())

    rst = ''
    v = 0.5
    cnt = 1
    while cnt != 4:
        if v <= N:
            v += 2**(-cnt)
            rst += '1'
            cnt +=1

        else:
            rst += '0'
            cnt += 1
    print(rst)

