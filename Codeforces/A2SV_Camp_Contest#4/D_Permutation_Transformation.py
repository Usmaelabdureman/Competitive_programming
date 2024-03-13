
def buildTree(left, right, a, d, curr_depth=0):
    if right < left:
        return
    if left == right:
        d[left] = curr_depth
        return
    
    max_index = left
    
    for i in range(left + 1, right + 1):
        if a[max_index] < a[i]:
            max_index = i
    d[max_index] = curr_depth
    
    buildTree(left, max_index - 1, a, d, curr_depth + 1)
    
    buildTree(max_index + 1, right, a, d, curr_depth + 1)


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    depth = [0] * n
    
    buildTree(0, n - 1, a, depth)
    
    print(*depth)