T = int(input())


def inorder(n):                 #중위순회를 이용하자
    if n:                       #완전이진트리이기 때문에
        inorder(ch1[n])
        inorder_arr.append(n)
        inorder(ch2[n])

for tc in range(1, T+1):
    N = int(input())

    inorder_arr = []            #1부터 N까지 완전 이진 트리로 만들 리스트

    arr = []                    #arr는 1부터 N까지 리스트
    for i in range(1, N+1):
        arr.append(i)

    ch1 = [0]*(N+1)             #왼쪽 자식
    ch2 = [0]*(N+1)             #오른쪽 자식

    par = [0]*(N+1)             #부모


    for i in range(1, N//2+1):  # 1부터 자식이 있는 노드까지
        if 2*i+1 <= N:          # 오른쪽 자식이 N보다 작거나 같으면

            p = i
            c = [2*i, 2*i+1]

            par[2*i] = i        #부모 자식 두개 다 저장
            par[2*i+1] = i

            ch1[i] = c[0]
            ch2[i] = c[1]

        else:                   #오른쪽 자식이 없다면
            p = i
            c = [2 * i, 2 * i + 1]

            par[2 * i] = i       #왼쪽 자식만 저장


            ch1[i] = c[0]




    inorder(1)              #중위 순회 함수로 1부터 N까지 자리를 뽑자

    node_dic = {}           #자리를 뽑고 arr에 있는 1부터 N까지 숫자들을
    for i in range(N):      #대응하여 딕셔너리를 만들자
        node_dic[inorder_arr[i]] = arr[i]
    # print(node_dic)
    # {4: 1, 2: 2, 5: 3, 1: 4, 6: 5, 3: 6}

    print(f'#{tc}', node_dic[1], node_dic[N//2])
