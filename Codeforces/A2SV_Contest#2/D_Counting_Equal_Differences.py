t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    pairs_diff = {}
    
    for i in range(len(a)):
        diff = a[i] - i
        if diff in pairs_diff:
            ans+=pairs_diff[diff]
        if diff in pairs_diff:
            pairs_diff[diff] += 1
        else:
            pairs_diff[diff] = 1   
    print(ans)