T = int(input())

for tc in range(1, T+1):
<<<<<<< HEAD
    n1 = 1
    n2 = 3

    N = int(input())

    memo = [1, 3]
    def paper(N):

        if int(N/10 -1) >= len(memo) and int(N/10-1) >=2:
            memo.append(paper(int(N/10-1)-1) + paper(int(N/10-1)-2))
        return memo[int(N/10-1)]

    print(paper(N))
=======
                                         #memoization 활용하자
    N = int(input())

    n = int(N/10)-1                     #n을 조정

    memo = [1, 3]                       #피보나치처럼 인덱스 0과 1을 먼저 설정
    def paper(n):                       #재귀 함수 이용하여 구현

        if n >= len(memo) and n >=2:
            memo.append(paper(n-1) + paper(n-2)*2)
        return memo[n]

    print(f'#{tc}', paper(n))
>>>>>>> 18f43fbdf59f00c736f5062c3d50773c6f23b2fa
