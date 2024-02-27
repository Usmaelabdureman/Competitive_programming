def dfs(v, p):
    cnt = [0] * n  # Add the missing variable declaration for "cnt"
    if len(g[v]) == 1 and g[v][0] == p:
        cnt[v] = 1
    else:
        for u in g[v]:
            if u != p:
                dfs(u, v)
                cnt[v] += cnt[u]

def solve():
    n = int(input())
    q = int(input())

    g = [[] for _ in range(n)]

    for _ in range(n - 1):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        g[u].append(v)
        g[v].append(u)

    cnt = [0] * n
    dfs(0, -1)

    for _ in range(q):
        c, k = map(int, input().split())
        c -= 1
        k -= 1

        res = cnt[c] * cnt[k]
        print(res)

tests = int(input())
for _ in range(tests):
    solve()
