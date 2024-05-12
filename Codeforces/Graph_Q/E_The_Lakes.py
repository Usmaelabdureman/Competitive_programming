
def dfs(i, j):
    visited[i][j] = True
    ans = grid[i][j]
    if i != 0 and grid[i-1][j] != 0 and not visited[i-1][j]:
        ans += dfs(i-1, j)
    if i != rows-1 and grid[i+1][j] != 0 and not visited[i+1][j]:
        ans += dfs(i+1, j)
    if j != 0 and grid[i][j-1] != 0 and not visited[i][j-1]:
        ans += dfs(i, j-1)
    if j != cols-1 and grid[i][j+1] != 0 and not visited[i][j+1]:
        ans += dfs(i, j+1)
    return ans

def solve():
    global rows, cols, grid, visited
    rows, cols = map(int, input().split())
    grid = []
    visited = [[False] * cols for _ in range(rows)]
    for _ in range(rows):
        row = list(map(int, input().split()))
        grid.append(row)

    ans = 0
    for i in range(rows):
        for j in range(cols):
            if not visited[i][j] and grid[i][j] != 0:
                ans = max(ans, dfs(i, j))
    print(ans)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()
