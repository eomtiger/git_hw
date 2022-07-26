a, b = input().split(' ')

a = int(a)
b = int(b)

if (a == 1 and b == 3) or (a == 2 and b== 1) or (a == 3 and b ==2):
    print('A')

elif (a == 1 and b ==2) or (a==2 and b ==3) or (a == 3 and b ==1):
    print('B')