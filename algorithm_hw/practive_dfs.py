V, C = map(int, input().split())

mat = list([0]*(V+1) for _ in range((V+1)))

arr = list(map(int, input().split()))

for i in range(len(arr)):
    if i%2 == 0:
        mat[arr[i]][arr[i+1]] = 1
        mat[arr[i+1]][arr[i]] = 1

stack = [1]
visited = []

while stack:
    current = stack.pop()
    if current not in visited:
        visited.append(current)

    for destination in range(V+1):
        if mat[current][destination] and destination not in visited:
            stack.append(destination)


print(visited)


