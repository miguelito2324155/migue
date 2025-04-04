a, b = map(int, input().split())

d = a // b
r = a % b

if r < 0:
    r += abs(b)
    d -= 1

print(d, r)
