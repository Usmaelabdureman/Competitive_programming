def solve(n):
    ans = n
    
    if n == 1:
        return 1
    return ans + solve(n//2)
for _ in range(int(input())):
    n = int(input())
    ans = 0
    
    while n >= 1:
        ans += n
        
        n //= 2
    print(ans)