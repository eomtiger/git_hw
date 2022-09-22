T = int(input())

for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    p1 = []
    p2 = []
    rst = 0
    flag = False
    for i in range(len(arr)):
        if flag:
            break
        if i % 2 == 0:
            p1.append(arr[i])
            if p1.count(p1[-1]) >= 3:
                rst = 1
                break
            elif len(p1) >= 3:
                p1.sort()

                for j in range(8):
                    if p1.count(j) and p1.count(j + 1) and p1.count(j+2):
                        rst = 1
                        flag = True
                        break

        # elif i % 2 == 1:
        else:
            p2.append(arr[i])
            if p2.count(p2[-1]) >= 3:
                rst = 2
                break
            elif len(p2) >= 3:
                p2.sort()

                for j in range(8):
                    if p2.count(j) and p2.count(j + 1) and p2.count(j+2) :
                        rst = 2
                        flag = True
                        break


    print(f'#{tc} {rst}')





