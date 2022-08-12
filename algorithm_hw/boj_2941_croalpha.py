croalpha_list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

inputt = list(input())
num = 0

for i in range(len(inputt)-2):
    if inputt[i]+inputt[i+1] +inputt[i+2] == 'dz=':
        inputt.pop(i)
        inputt.insert(i, '0')
        inputt.pop(i+1)
        inputt.insert(i+1, '0')
        inputt.pop(i+2)
        inputt.insert(i+2, '0')
        num +=1

for i in range(len(inputt)-1):
    if inputt[i]+inputt[i+1] in croalpha_list:
        inputt.pop(i)
        inputt.insert(i, '0')
        inputt.pop(i+1)
        inputt.insert(i+1, '0')
        num += 1


new_input = []
for i in range(len(inputt)):
    if inputt[i] != '0':
        new_input.append(inputt[i])


num  += len(new_input)


print(num)