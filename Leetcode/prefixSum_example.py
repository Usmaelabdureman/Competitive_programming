def presum(num):
    prev=[i for i in range (len(num))]
    print(num)
    prev[0]=num[0]
    for i in range(1,len(num)):
        prev[i]=prev[i-1]+num[i]
    return prev


test=[10,5,20,5,30,40]
print(presum(test))