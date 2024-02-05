t = int(input())
for _ in range(t):
    n = int(input())
    row1 = input()
    row2 = list(input()) 
    pointer1 = 0
    pointer2 = 0
    # print(row1)
    
    while pointer1 < n and pointer2 < n:
        if row1[pointer1] == 'G' and row2[pointer2] == 'B':
            row2[pointer2] = 'G' 
        elif row1[pointer1] == 'B' and row2[pointer2] == 'G':
            row2[pointer2] = 'B'
        pointer1 += 1
        pointer2 += 1
    row2 = ''.join(row2)  
    if row1 == row2:
        print('YES')
    else:
        print('NO')
