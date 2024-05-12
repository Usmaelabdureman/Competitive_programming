
n = int(input())
arr = []
operations = []

for _ in range(n):
    method , *args = input().split()
    args = list(map(int, args))
    if method == 'insert':
        arr.append(args[0])
        operations.append('insert {0}'.format(args[0]))
    elif method == 'getMin':
        if args[0] in arr:
            operations.append('getMin {0}'.format(args[0]))
        else:
            arr.append(args[0])
            operations.append('insert {0}'.format(args[0]))
            operations.append('getMin {0}'.format(args[0]))
    elif method == 'removeMin':
        if arr:
            arr.remove(min(arr))
            operations.append('removeMin')
        else:
            operations.append('removeMin')
    else:
        operations.append('insert')
        operations.append('removeMin')
        operations.append('getMin')
print(len(operations))
for operation in operations:
    print(operation)
    