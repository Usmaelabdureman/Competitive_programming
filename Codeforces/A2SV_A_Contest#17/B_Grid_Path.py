
t = int(input())

for _ in range(t):
    n ,m, k = list(map(int, input().split()))
    
    dp = [[i for i in range(m)] for j in range(n)]
    
    for i in range(n):
        dp[i][0] = i
    
    for i in range(m):
        dp[0][i] = i
    

    for i in range(1, n):
        for j in range(1, m):
            
            left = top = float('inf')
            if j - 1 >= 0:
                left = dp[i][j - 1] + i+1
                
            if i  - 1 >= 0:
                top = dp[i - 1][j] + j + 1
            
            dp[i][j] = min(top, left)
    # print(dp)
    if dp[n - 1][m - 1] == k:
        print('YES')
    else:
        print('NO')
