import sys
sys.stdin = open('input.txt', 'r')

for _ in range(10):
    T = int(input())
    ladder = [([0] + list(map(int, input().split())) + [0]) for _ in range(100)]

    # print(len(ladder[1]))
    di = [-1,1,0,0]
    dj = [0,0,-1,1]

    Min_move = 1000
    start = 0
    rst = 0
    for i in range(1, 101):
        j=i
        if ladder[0][j] == 1:
            loc = 0
            move = 0

            while loc != 99:
                if ladder[loc][j+dj[2]] == 0 and ladder[loc][j+dj[3]] == 0:
                    loc += 1
                    move += 1

                elif ladder[loc][j+dj[2]] == 1:
                    while ladder[loc][j+dj[2]] == 1:
                        j += dj[2]
                        move += 1
                    loc += 1
                    move += 1

                elif ladder[loc][j+dj[3]] == 1:
                    while ladder[loc][j+dj[3]] == 1:
                        j += dj[3]
                        move += 1
                    loc += 1
                    move += 1

            if move <= Min_move:
                Min_move = move
                rst = i-1
    print(rst)





