from collections import Counter
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
count=0
# for i in range(n):
#     for j in range(m):
#         if a[i] ==b[j]:
#             count+=1
# print(count)

count_a = Counter(a)
count_b = Counter(b)
count = 0
for num in count_a.keys():
    count += count_a[num] * count_b[num]
print(count)

