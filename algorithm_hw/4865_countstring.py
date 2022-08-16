T = int(input())

for tc in range(1, T+1):
    str1 = input()
    str2 = input()

    maxV = 0
    for i in str1:          #str1을 순회
        if str2.count(i) > maxV: #str1의 문자가 str2에 몇개 있는지 구하고 최대값 구하기
            maxV = str2.count(i)

    print('#' + str(tc), maxV)
