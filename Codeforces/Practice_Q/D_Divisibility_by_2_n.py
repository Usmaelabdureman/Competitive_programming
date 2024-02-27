from math import prod, lcm

testc = int(input())

for _ in range(testc):
    n = int(input())
    a = list(map(int, input().split()))

    product = prod(a)
    LCM = lcm(product, 2 ** n)
    temp = LCM / product
    indPro = prod([i+1 for i in range(n)])
    
    temp2= indPro / temp
    
    counter = 0
    
    for i in range(n, 0, -1):
        if(temp == 1):
            break
        if(temp%(i) == 0):
            temp /= (i)
            counter += 1
            
    temp = temp2
    counter2 = 0
    
    for i in range(1, n+1):
        if(temp == 1):
            break
        if(temp%(i) == 0):
            temp /= (i)
            counter2 += 1
            
    if(temp == 1): print(min(counter, counter2))
    else: print(-1)
    
