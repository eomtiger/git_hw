T = int(input())

def bisearch(page, result):
    l = 1
    r = page
    cnt = 0

    while l<=r:
        cnt+=1
        c = int((l+r)/2)

        if result >c:
            l = c
            # print(l)

        elif result <c:
            r = c
            #print(r)
        elif result == c:
            break


    return(cnt)

result = []
for tc in range(T):

    P, A, B = map(int, input().split())
    if bisearch(P,A)== bisearch(P,B):
        result.append(0)
    elif bisearch(P,A) > bisearch(P,B):
        result.append('B')
    elif bisearch(P,A) < bisearch(P,B):
        result.append('A')

for tc in range(T):
    print('#' + str(tc+1), result[tc])
