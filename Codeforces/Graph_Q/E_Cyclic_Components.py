
n, m = map(int, input().split())
deg = [0] * (n + 1)
visited = [False] * (n + 1)

conn_comp = [[] for _ in range(n + 1)]

def dfs(v):
    visited[v] = True
    conn_comp.append(v)
    
    for to in g[v]:
        if not visited[to]:
            dfs(to)

g = [[] for _ in range(n + 1)] 

for _ in range(m):
    verts, edges = map(int, input().split())
    g[verts].append(edges)
    g[edges].append(verts)
    deg[verts] += 1
    deg[edges] += 1

ans = 0
for i in range(1, n + 1):
    if not visited[i]:
        conn_comp = []
        dfs(i)
        ok = all(deg[v] == 2 for v in conn_comp)
        if ok:
            ans += 1

print(ans)
