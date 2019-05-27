# from sys import exit
# N = int(input())
# a = [int(input()) for _ in range(N)]
S = str(input())
L = len(S)
YYMM = 0 < int(S[2:]) <= 12

MMYY = 0 < int(S[:2]) <= 12
if MMYY & YYMM:
    print("AMBIGUOUS")
elif not (MMYY or YYMM):
    print("NA")
else:
    print("YYMM" if YYMM else "MMYY")
