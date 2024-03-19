w , h , n = map(int, input().split())  

def check(w, h, n, x):
    return (x // w) * (x // h) >= n

left = 0
right = 10 ** 18
    
while right - left > 1 :
    mid = (left + right) // 2
    if check(w, h, n, mid):
        right = mid
    else:
        left = mid
print(right)