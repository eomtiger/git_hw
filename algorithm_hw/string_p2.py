

T = 6

num_str_list= []
for tc in range(T):


    num = list(input())

    num_str = ''
    for i in range(len(num)):
        if num[i] == '-':
            num_str = num_str + chr(45)

        else:
            num_str = num_str + chr(int(num[i])+48)

    num_str_list.append(num_str)

for i in range(T):
    print('#' + str(i+1), num_str_list[i], type(num_str_list[i]))




