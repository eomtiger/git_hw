N=int(input())
word_rev_list = []
for i in range(N):
    word = input()
    word_rev = word[::-1]
    word_rev_list.append(word_rev)

for i in range(N):
    print('#' + str(i+1), word_rev_list[i])