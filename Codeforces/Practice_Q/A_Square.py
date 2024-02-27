test_cases = int(input())

for _ in range(test_cases):
     x1,y1 = map(int,input().split())
     x2,y2 = map(int,input().split())
     x3,y3 = map(int,input().split())
     x4,y4 = map(int,input().split())
     area = (max(x1,x2,x3,x4) - min(x1,x2,x3,x4)) *( max(y1,y2,y3,y4) - min(y1,y2,y3,y4))
     print(area)