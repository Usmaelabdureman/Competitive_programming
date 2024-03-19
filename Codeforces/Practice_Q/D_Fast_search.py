
n = int(input())

a = list(map(int, input().split()))

k = int(input())
a.sort()


for _ in range(k):
    l, r = map(int, input().split())

    left = 0
    right = n - 1
    while left <= right:
        mid = (left + right) // 2
        if a[mid] >= l:
            right = mid - 1
        else:
            left = mid + 1
            
    left_indx = left
    
    left = 0
    right = n - 1
    
    while left <= right:
        mid = (left + right) // 2
        if a[mid] <= r:
            left = mid + 1
        else:
            right = mid - 1
    right_indx = right
    print(right_indx-left_indx+1, end = ' ')
    

                
 
    

            
