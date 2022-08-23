def powerset(s):
    for i in range(1<<len(s)):
        selected = []
        for j in range(len(s)):
            if i & (1<<j):
                selected.append(s[j])
        if sum(selected) == 10:
            print(set(selected))

s= {1,2,3,4,5,6,7,8,9,10}

s= list(s)

powerset(s)