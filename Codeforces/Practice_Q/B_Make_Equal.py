t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    total = sum(a)
    if total % n != 0:
        print("NO")
    else:
        a.sort()
        for i in range(n):
            if a[i] > (i+1):
                print("NO")
                break
            total -= a[i]
            if total < (n-i-1)*(n-i)//2:
                print("NO")
                break
        else:
            print("YES")