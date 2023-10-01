t = int(input())
for _ in range(t):
    n = int(input())
    b = list(map(int, input().split()))
    a = [0] * n
    # fill the sequence alternately from left and right
    left, right = 0, n - 1
    while left <= right:
        if left == right:
            a[left] = b[0]
        else:
            a[left] = max(b)
            b.remove(a[left])
            a[right] = max(b)
            b.remove(a[right])
        left += 1
        right -= 1
    print(*a)
