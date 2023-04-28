import math

a = float(input())
b = float(input())

c = math.sqrt(a**2 + b**2)
theta = math.atan(a/b) * 180/math.pi

print(str(round(theta)) + chr(176))
