import math
x = float(input())
floor_x = math.floor(x)
ceil_x = math.ceil(x)
if x - floor_x >= 0.5:
    round_x = ceil_x
else:
    round_x = floor_x

print(floor_x, ceil_x, round_x)
