t = int(input())

for _ in range(t):
    n = int(input())
    while n > 1:
        n /= 2
    if n == 1:
        print("NO")
    else:
        print("YES")