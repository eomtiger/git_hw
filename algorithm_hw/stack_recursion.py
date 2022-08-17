def f(i, n):        #i 현재 단계, n 목표단계
    if i  == n:
        print(i)
        return
    else:
        print(i)
        f(i+1, n)

f(0,3)


def fibonacci(n):
    if n < 2:
        return n
    else :
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(5))