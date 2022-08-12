word = list(input())
camb = list('CAMBRIDGE')
# print(camb)

new_word = ''
for i in range(len(word)):
    if word[i] not in camb:
        a = word.pop(i)
        word.insert(i, 0)
        new_word += a

print(new_word)
