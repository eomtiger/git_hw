T = int(input())

for tc in range(T):
    N = int(input())

    matrix = list([0]*N for i in range(N))
    arr = []
    for i in range(1, N**2+1):
        arr.append(i)

    print(arr)







    for i in range(N):          #맨위
        matrix[0][i] = arr[i]

#-----------------------------------------------#
    ''' 여기부터 while 돌려'''
    k = 1
    #while
    for i in range(k, N-k+1):          #  오른쪽
        matrix[i][N-k] = arr[N-1+i] #N -1 -k-1

    for i in range(N-k-1, -1 ,-1): #  아래쪽
        matrix[N-1][i] = arr[N+(N-1)+(N-1)-1-i] #3N-3

    for i in range(N-k-1 , 0 ,-1): #  왼쪽
        matrix[i][0] =arr[N+N-1+N-1+N-2-i]  #4N-4

    for i in range(k, N-k):        # 위쪽
        matrix[1][i] = arr[N+N-1+N-1+N-2-1+i] #4N-4 -1

    for i in range(2, N-2+1):
        matrix[i][N-2] = arr[N+N-1+N-1+N-2+N-2-2+i] #5N-5 -3



    print(matrix)