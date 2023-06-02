t = int(input())
days=[]
for i in range(t):
    r, g, b = sorted(map(int, input().split()), reverse=True)
    days.append(min(r+g,r+b,g+b, (r+g+b)//2))
for i in days:
    print(i)