t = int(input())
for _ in range(t):
    n = int(input())
    words = [input() for _ in range(n)]
    counts = [[word.count(chr(j + ord('a'))) for j in range(26)] for word in words]
    
    
   
    