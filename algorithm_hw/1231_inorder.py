def inorder(n):
    if n:
        inorder(ch1[n])
        inorder_arr.append(n)
        inorder(ch2[n])
T = 10

for tc in range(1,T+1):

    N = int(input())
    ch1 = [0]*(N+1)
    ch2 = [0]*(N+1)
    par = [0]*(N+1)

    inorder_arr = []  # 1부터 N까지 완전 이진 트리로 만들 리스트

    arr = []  # arr는 1부터 N까지 리스트
    for i in range(1, N + 1):
        arr.append(i)

    ch1 = [0] * (N + 1)  # 왼쪽 자식
    ch2 = [0] * (N + 1)  # 오른쪽 자식

    par = [0] * (N + 1)  # 부모

    for i in range(1, N // 2 + 1):  # 1부터 자식이 있는 노드까지
        if 2 * i + 1 <= N:  # 오른쪽 자식이 N보다 작거나 같으면

            p = i
            c = [2 * i, 2 * i + 1]

            par[2 * i] = i  # 부모 자식 두개 다 저장
            par[2 * i + 1] = i

            ch1[i] = c[0]
            ch2[i] = c[1]

        else:  # 오른쪽 자식이 없다면
            p = i
            c = [2 * i, 2 * i + 1]

            par[2 * i] = i  # 왼쪽 자식만 저장

            ch1[i] = c[0]

    inorder(1)  # 중위 순회 함수로 1부터 N까지 자리를 뽑자
    # print(inorder_arr)
    # N이 8이면 [8, 4, 2, 5, 1, 6, 3, 7] 인덱스 중위순회

    arr_alpha = []
    for _ in range(N):                  #인풋의 두번째 인자를 뽑아서 저장
        arr = list(input().split())
        arr_alpha.append(arr[1])
    # print(arr_alpha)
    node_dic = {}                       #딕셔너리 형태로 만들기
    for i in range(N):
        node_dic[i+1] = arr_alpha[i]    #인덱스 키로 가지고 알파벳을 value로

    # print(node_dic)

    answer = ''
    for i in inorder_arr:
        answer += node_dic[i]

    print(f'#{tc}', answer)
