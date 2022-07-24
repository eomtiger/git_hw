T = input()
N= input()

a = []
for i in range(int(N)):
    b = list(input().split(' '))

    a.append(b)
print(T)
print(N)

for i in range(int(N)):
    print(a[i][0] * int(a[i][1])) 