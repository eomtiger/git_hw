def f(i, n):        #i 현재 단계, n 목표단계
    if i  == n:
        print(i)
        return
    else:
        print(i)
        f(i+1, n)

f(0,900)            #재귀 호출 깊이는 작게 사용해라
