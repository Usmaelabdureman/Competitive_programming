t = int(input())
for _ in range(t):
    n = int(input())
    if n < 7 or n == 9:
        print("NO")
    else:
        print("YES")
        c = n - 3
        if c % 3 == 0:
            print(1, 4, n - 5)
        else:
            print(1, 2, n - 3)