def isPowerOfThree(n):
    if n<1:return False
    while(n%3==0):
        n=n/3
    return True if n==1 else False
print(isPowerOfThree(27))
    
    