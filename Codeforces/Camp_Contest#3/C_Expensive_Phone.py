
testc = int(input())
for _ in range(testc):
    days = int(input())
    prices = list(map(int, input().split()))
    
    stack = []
    bad = 0
    
    for price in prices:
        while stack and stack[-1] > price:
            stack.pop()
            bad += 1
        stack.append(price)
        
    print(bad)