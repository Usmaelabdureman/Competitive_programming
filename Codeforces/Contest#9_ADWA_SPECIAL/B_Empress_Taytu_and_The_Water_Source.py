from math import ceil

def canBeHappy(d, a, k, size):
    total_hour = 0
    for i in range(len(d)):
        trip = ceil(max(0, d[i]) / size)
        total_hour += trip * a[i]
    return total_hour <= k

def minimumWagon(k, d, a):
    low, high = 1, max(d)
    ans = -1

    while high - low >= 0:
        mid = (low + high) // 2
        if canBeHappy(d, a, k, mid):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    d = list(map(int, input().split()))
    a = list(map(int, input().split()))

    ans = minimumWagon(k, d, a)
    print(ans)
