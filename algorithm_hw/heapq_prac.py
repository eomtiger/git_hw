import heapq

min_heap = []
heapq.heappush(min_heap, (3, 6))
heapq.heappush(min_heap, (1, 6))
heapq.heappush(min_heap, (4, 'hi'))
print(min_heap)

max_heap = []

heapq.heappush(max_heap, -3)
heapq.heappush(max_heap, -4)
heapq.heappush(max_heap, -5)

print(max_heap)