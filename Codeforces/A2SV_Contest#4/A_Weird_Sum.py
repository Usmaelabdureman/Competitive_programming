from collections import defaultdict

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

positions = defaultdict(list)
total_distance = 0

for i in range(n):
    for j in range(m):
        color = grid[i][j]
        positions[color].append((i, j))

for cells in positions.values():
    for i in range(len(cells)):
        for j in range(i + 1, len(cells)):
            cell1, cell2 = cells[i], cells[j]
            total_distance += abs(cell1[0] - cell2[0]) + abs(cell1[1] - cell2[1])

print(total_distance)
