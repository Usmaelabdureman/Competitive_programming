
t = int(input())
test_cases = []

for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    
    pos = [i for i in a if i>=0]
    neg = [-1*(i) for i in a if i < 0]
    ans = sum(pos) + sum(neg)
    print(ans)

