T = int(input())

for tc in range(1, T+1):
    n1 = 1
    n2 = 3

    N = int(input())

    memo = [1, 3]
    def paper(N):

        if int(N/10 -1) >= len(memo) and int(N/10-1) >=2:
            memo.append(paper(int(N/10-1)-1) + paper(int(N/10-1)-2))
        return memo[int(N/10-1)]

    print(paper(N))