
n = int(input())
exerc = list(map(int, input().split()))
ch = 0
bi = 0
back = 0

for i in range(n):
    if i % 3 == 0:
        ch += exerc[i]
    elif i % 3 == 1:
        bi += exerc[i]
    else:
        back += exerc[i]
        
# print(ch, bi, back)

if ch > bi and ch > back:
    print("chest")
elif bi > ch and bi > back:
    print("biceps")
else:
    print("back")


