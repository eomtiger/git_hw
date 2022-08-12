face = input()

left_face = ''
right_face = ''
for i in range(len(face)):
    if face[i] == '(':
        left_face += face[0:i]
        right_face += face[i:]



cnt_l=0
cnt_r=0

for i in range(len(left_face)):
    if left_face[i] == '@':
        cnt_l += 1
for i in range(len(right_face)):
    if right_face[i] == '@':
        cnt_r +=1

print(cnt_l, cnt_r)



