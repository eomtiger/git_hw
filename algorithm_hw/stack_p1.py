stackSize = 10
stack = [0] * stackSize
top = -1

top +=1             #탑 증가
stack[top] = 1      #스택에 push

top += 1            #push(2)
stack[top] = 2

top -= 1            #탑 감소 pop
temp = stack[top+1] #temp에 위에 있던 값을 담음
print(temp)

temp = stack[top]   #pop(2)
top = -1
print(top)
'''===================================================='''

stack2 = []             #리스트로 스택만들기
stack2.append(10)       #push
stack2.append(20)
print(stack2.pop())     #pop
print(stack2.pop())
