from audioop import reverse


T = int(input())

a= []
for i in range(T):

    b = input()
    a.append(b)

for i in range(T):

    if a[i] == a[i][::-1] :
        print('#'+str(i+1), 1)
    
    else :
        print('#' + str(i+1), 0)