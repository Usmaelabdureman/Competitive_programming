
t= int(input())

for _ in range(t):
    n,m = map(int,input().split())
    grid=[]
    for i in range(n):
        grid.append(list(map(int,input().split())))
    print(grid)
    
    # Sorting the grid
    sorted_v=sorted(grid[0])
    # checking if by one swap its possible
    ans=[]
    for i in range(1,m+1):
        if grid[0][i] !=sorted_v[0][i]:
            ans.append([])
            
