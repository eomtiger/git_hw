# T=int(input())
#
# for tc in range(T):
#
#     arr = list(map(int, input().split()))
#     subset_sum_list = []
#     for i in range(0b1<<10):
#         subset_sum = 0
#         for j in range(10):
#             if i & (1<<j):
#                 subset_sum += arr[j]
#                 subset_sum_list.append(subset_sum)

print(0b1<<10)