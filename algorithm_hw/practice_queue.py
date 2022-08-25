input_list = list(map(int, input().split()))
q = []
front = -1
rear = -1
for i in range(len(input_list)):
    q.append(input_list[i])
    rear += 1

for i in range(len(q)):
    out = q.pop(0)
    front +=1
    print(out)


