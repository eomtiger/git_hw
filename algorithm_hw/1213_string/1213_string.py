import sys
sys.stdin = open("input.txt", "r", encoding='UTF8')

for _ in range(10):
    N = int(input())
    word = input()
    sent = input()

    cnt = 0
    for i in range(len(sent)+1-len(word)):
        if sent[i:i+len(word)] == word:
            cnt += 1

    print(cnt)
