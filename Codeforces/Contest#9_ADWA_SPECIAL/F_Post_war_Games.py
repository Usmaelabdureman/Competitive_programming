from sys import stdin

def input(): 
    return stdin.readline().strip()

T = int(input())
for _ in range(T):
    n, k = map(int, input().split())

    if n == k:
        print(0)
        continue

    ans = (n - (k + 1)) * 3 + ((k - 1) // 2) * 3 + (k - 1) % 2 + 1
    print(ans)
