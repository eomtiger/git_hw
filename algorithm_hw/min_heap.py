heap = ['최소힙:']

def heap_push(item):
    heap.append(item)

    child = len(heap)-1
    parent = child//2

    while parent and heap[parent] > heap[child]:
        heap[parent], heap[child] = heap[child], heap[parent]
        child = parent
        parent = child//2


def heap_pop():
    if len(heap) == 1:
        return

    result = heap[1]
    item = heap.pop()
    heap[1] = item

    parent = 1
    child = parent*2 #왼쪽 자식이 작다고 가정

    if child+1 <= len(heap)-1:
        if heap[child] > heap[child+1]:
            child += 1

    while child <= len(heap)-1 and heap[parent]>heap[child]:

        heap[parent], heap[child] = heap[child], heap[parent]

        parent = child
        child = parent*2

        if child + 1 <= len(heap) - 1:
            if heap[child] > heap[child + 1]:
                child += 1


    return result


arr = [6,13,2,11,9,7,4]
for i in range(len(arr)):
    heap_push(arr[i])
print(heap)
heap_pop()
print(heap)
