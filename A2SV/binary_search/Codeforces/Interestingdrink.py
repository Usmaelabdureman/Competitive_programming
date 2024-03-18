import bisect
 
n = int(input())
prices = list(map(int, input().split()))
prices.sort()  
 
q = int(input())
for _ in range(q):
    coins = int(input())
    idx = bisect.bisect_right(prices, coins)
    print(idx)