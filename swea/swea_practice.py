N= int(input())

list1=[]
for i in range(N):
    a  = list(input())
    list1.append(a)

b = []
for i in range(len(list1)):
     k = list(map(int, list1[i]))
     b.append(k)
#print(b)

# b=[[0,0,1],
#    [3,0,2],
#    [5,1,0]]

c = [[0,0]]
d = 0
for i in range(len(b)*2 -2):
        
    if c[i][0] == len(b)-1 or c[i][1] == len(b)-1:
        d += i
        break

    elif b[c[i][0]][c[i][1] + 1] < b[c[i][0]+1][c[i][1]] :
        c.append([c[i][0], c[i][1]+1])

    elif b[c[i][0]][c[i][1] + 1] > b[c[i][0]+1][c[i][1]] : 
        c.append([c[i][0]+1, c[i][1]])

    elif b[c[i][0]][c[i][1] + 1] == b[c[i][0]+1][c[i][1]] :
        if b[c[i][0]][c[i][1] + 2] < b[c[i][0]+2][c[i][1]] :
            c.append([c[i][0], c[i][1]+1])
        elif b[c[i][0]][c[i][1] + 2] > b[c[i][0]+2][c[i][1]] :
            c.append([c[i][0]+1, c[i][1]])
                
      


for i in range(d, len(b)*2-2):

    #if c[i][0] == (len(b))-1 and c[i][1] == len(b-1):
     #   break

    if c[i][0] == len(b)-1:

        c.append([c[i][0], c[i][1]+1])

    elif c[i][1] == len(b) -1 :

        c.append([c[i][0]+1, c[i][1]])

    

# print(c)

s = 0

for i in range(len(c)):
    s += b[c[i][0]][c[i][1]]

print(s)

