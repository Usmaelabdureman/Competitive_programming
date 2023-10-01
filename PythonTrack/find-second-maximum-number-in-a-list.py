if __name__ == '__main__':
    n = int(input())
    arr = set(map(int, input().split()))

    result=[]
    for i in arr:
        result.append(i)
    result.sort()
    
    print(result[-2])
