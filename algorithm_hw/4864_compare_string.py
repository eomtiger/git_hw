T = int(input())

for tc in range(1, T+1):
    str1 = input()
    str2 = input()

    if str1 in str2:
        print('#'+str(tc), 1)

    else:
        print('#' + str(tc), 0)