ops = {                                         #연산자 람다함수로 만들기
        '+1': (lambda x: x + 1),
        '-1': (lambda x: x - 1),
        '*2': (lambda x: x * 2),
        '-10': (lambda x: x - 10)
    }

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    cnt = 0
    while N <= M:
        N = N*2
        cnt += 1
    print(cnt)
    print(N)
    temp = 0
    if M - int(N/2) > N - M:
        temp = N

    elif M - int(N/2) <= N -M and M - int(N/2) < 10:
        temp = int(N/2)
        cnt -= 1
        while temp != M:
            temp = ops['+1'](temp)
            cnt += 1

    else:
        temp = N
    print(cnt)
    print(temp)
    if temp - M > 10 :
        if temp % 10 <=5:
            while temp > M+10:
                temp = temp -10
                cnt += 1
            while temp != M:
                temp -= 1
                cnt += 1
        else:
            while temp < M:
                temp -=10
                cnt += 1
            while temp != M:
                temp += 1
                cnt += 1
    else:
        while temp != M:
            temp -= 1
            cnt += 1
    print(cnt)







