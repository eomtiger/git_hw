N= int(input())

a = list(map(int, input().split()))

a = set(a)

a = list(a)

a.sort()

if len(a)%2 == 1:

    print(a[int(int(len(a)-1)/2)])
else :
    print(a[int(int(len(a))/2)+1])