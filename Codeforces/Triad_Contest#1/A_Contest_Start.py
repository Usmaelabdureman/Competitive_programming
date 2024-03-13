def solve(n, x, t):
    max_part = max(0, n - t // x)
    min_part = min(n - 1, t // x - 1)
    total_diss = max_part * (t // x) + (min_part * (min_part + 1)) // 2
    return total_diss

k = int(input())

for _ in range(k):
    n, x, t = map(int, input().split())
    print(solve(n, x, t))
