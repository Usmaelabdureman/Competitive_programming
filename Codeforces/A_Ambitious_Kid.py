
N=int(input())
A = list(map(abs, map(int, input().split())))
A.sort()
print(min(A))