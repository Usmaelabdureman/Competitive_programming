from math import ceil
n,m,a = map(int,input().split())
flag1 = ceil(n/a)
flag2 = ceil(m/a)
print(int(flag1*flag2))