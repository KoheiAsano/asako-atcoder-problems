import sys
sx, sy, tx, ty = [int(n) for n in input().split()]
W = tx - sx
H = ty-sy
r1 = "U"*H + "R"*W
r2 = "D"*H + "L"*W
r3 = "D" + "R"*W + "R" + "U"*H + "U" + "L"
r4 = "U" + "L"*W + "L" + "D"*H + "D" + "R"
print(r1 + r2 + r3 + r4)
