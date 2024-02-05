n = int(input())
m = int(input())
size_usb = []
for _ in range(n):
    size_usb.append(int(input()))
size_usb.sort(reverse=True)

needed = 0
for i in range(n):
    if m > 0:
        m -= size_usb[i]
        needed += 1
    else:
        break
print(needed)