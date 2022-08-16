T = int(input())

for tc in range(T):
    A, B = input().split()
    #print(A, B)
    new_A = A.replace(B, 'a')  # B에 해당하는 문자열을 임의의 문자 a로 바꿈
    # print(C)

    print('#' + str(tc+1), len(new_A))   #B문자열이 a로 바뀌었기 때문에 newA의 문자열 길이를 구함
