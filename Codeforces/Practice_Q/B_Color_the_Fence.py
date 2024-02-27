
paint = int(input())

a = list(map(int,input().split()))

index_min = a.index(min(a))

if paint > 0:
    print(int(str(index_min+1)*paint))
else:
    print(-1)