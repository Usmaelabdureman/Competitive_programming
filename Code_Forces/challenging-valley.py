t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    if n == 1:
        print("YES")
        continue
    
    # Find the index of the maximum value in the array
    max_idx = a.index(max(a))
    
    # Check if the array is a "valley"
    if max_idx == 0 or max_idx == n - 1:
        print("NO")
        continue
    elif a[:max_idx] != sorted(a[:max_idx], reverse=True) or a[max_idx:] != sorted(a[max_idx:]):
        print("NO")
        continue
    elif a[:max_idx][-1] == a[max_idx] or a[max_idx:][0] == a[max_idx]:
        print("NO")
        continue
    else:
        print("YES")
