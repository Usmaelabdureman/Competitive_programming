# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
E= set(map(int,input().split()))

b = int(input())
F = set(map(int,input().split()))

print(len(E.union(F)))
