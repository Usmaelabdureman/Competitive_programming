t = int(input())
for _ in range(t):

    n = int(input())
    
    grid = []
    for i in range(n):
        grid.append(input())
    

    min_ops = 0

    for row in range(n//2):
        for col in range(row, n - row - 1):
            
            zero_one_count = [0, 0]

            zero_one_count[int(grid[row][col])] += 1
            zero_one_count[int(grid[col][n - row - 1])] += 1
            zero_one_count[int(grid[n - row - 1][n - col - 1])] += 1
            zero_one_count[int(grid[n - col - 1][row])] += 1

            min_ops += min(zero_one_count)

    print(min_ops)