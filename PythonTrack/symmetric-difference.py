# Enter your code here. Read input from STDIN. Print output to STDOUT
msize = int(input())
M = set(input().split())
Nsize = int(input())
N = set(input().split())
answer = list(map(int, M.symmetric_difference(N)))
answer.sort()
for i in answer:
    print(i)


    
