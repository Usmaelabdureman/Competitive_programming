t = int(input())
for _ in range(t):
    wd=input()
    if len(wd)>10:
        print(f"{wd[0]}{len(wd)-2}{wd[-1]}")
    else:
        print(wd)