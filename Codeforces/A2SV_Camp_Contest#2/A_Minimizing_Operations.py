
t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    
    min_oper = 0
    diff_arr = [0]*n
    a.sort()
    for i in range(1,n):
        diff_arr[i] = a[i]-a[i-1]
    print(sum(diff_arr))
        