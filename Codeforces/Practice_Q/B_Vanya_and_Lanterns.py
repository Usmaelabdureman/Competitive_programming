n, l = map(int, input().split())
lanterns = list(map(int, input().split()))

lanterns.sort()

max_radius = max(lanterns[0], l - lanterns[-1]) * 2

for i in range(n - 1):
    max_radius = max(max_radius, lanterns[i + 1] - lanterns[i])
# print(max_radius)
print(f"{max_radius/2:.10f}")
