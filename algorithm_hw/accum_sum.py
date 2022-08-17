# 1 전역변수 sum 활용하기
arr = [2, 6, 4, 1, 8]

sum = arr[0]


def abc(x):
    global sum
    print(sum)
    if x == 4:
        return
    sum += arr[x + 1]
    abc(x + 1)


abc(0)

# 2 매개변수 sum 이용
# arr = [2, 6, 4, 1, 8]
#
#
# def abc(x, sum):
#     print(sum)
#     if x == 4:
#         return
#     abc(x + 1, sum + arr[x + 1])
#
#
# abc(0, arr[0])
