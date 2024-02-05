from collections import defaultdict
T = int(input())

for _ in range(T):
   
    n,m = map(int,input().split())
    mat = [list(map(int,input().split())) for i in range(n)]
   
    front_diagonal = defaultdict(int)
    back_diagonal = defaultdict(int)

    for r, row in enumerate(mat):
        for c, val in enumerate(row):
            front_diagonal[r + c] += val
            back_diagonal[r - c] += val
   
    ans = 0

    for r in range(n):
        for c in range(m):
            cur_total =  front_diagonal[r + c] + back_diagonal[r - c] - mat[r][c]
            ans = max(ans,cur_total)
   
    print(ans)