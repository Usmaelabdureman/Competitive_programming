def solve(n, k):
    s = ['a'] * n
    for i in range(n - 2, -1, -1):
        if k <= (n - i - 1):
            s[i] = s[n - k] = 'b'
            return ''.join(s)
        k -= (n - i - 1)

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    result = solve(n, k)
    print(result)
