testC = int(input())
for i in range(testC):
    if i>= 1: input()
    
    n , x  = map(int,input().split())
    array_a = list(map(int,input().split()))
    array_b = list(map(int,input().split()))
    array_a.sort()
    array_b.sort(reverse=True)
    count = []
    for i in range(n):
        ab = array_a[i] + array_b[i]
        if ab <= x:
            count.append(ab)
    if count and len(count) == n:
        print("Yes")
    else:
        print("No")