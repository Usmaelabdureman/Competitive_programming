from collections import defaultdict
def solve():
    global g  # Add this line
    n = int(input())
    g = defaultdict(list)
    subtree_size = [0] * (n + 1)
    leaf_counts = [0] * (2 * n)
    ans = [0] * (n + 1)

    for _ in range(n - 1):
        u, v = map(int, input().split())
        g[u].append(v)
        g[v].append(u)

    dfs(1, 0, 1, subtree_size, leaf_counts)

    q = int(input())
    for _ in range(q):
        x, y = map(int, input().split())
        result = ans[x] + ans[y]
        print(result)


def dfs(v, p, depth, subtree_size, leaf_counts):
    global ans
    subtree_size[v] = 1

    for u in g[v]:
        if u != p:
            dfs(u, v, depth + 1, subtree_size, leaf_counts)
            subtree_size[v] += subtree_size[u]

    leaf_counts[depth - subtree_size[v] + 1] += 1
    leaf_counts[depth] -= 1

    ans[v] = leaf_counts[depth - subtree_size[v] + 1]

    q = int(input())
    for _ in range(q):
        x, y = map(int, input().split())
        result = ans[x] + ans[y]
        print(result)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()
