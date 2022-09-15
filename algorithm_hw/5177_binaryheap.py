T = int(input())

def heap_push(item):                    #교수님이 알려주신 최소힙 push
    heap.append(item)
    child_index = len(heap)-1
    parent_index = child_index//2

    while parent_index and heap[child_index] < heap[parent_index]:
        heap[parent_index], heap[child_index] = heap[child_index], heap[parent_index]

        child_index = parent_index
        parent_index = child_index//2



for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    heap = ['최소힙:']
    rst = 0                     #조상들의 합
    for i in arr:
        heap_push(i)            #힙 자료구조 만들기

    flag = N
    while flag != 1:            #1번 조상까지

        rst += heap[flag//2]    # 노드 값 더하기
        flag //= 2              #부모로 가기

    # print(heap)
    print(f'#{tc} {rst}')


