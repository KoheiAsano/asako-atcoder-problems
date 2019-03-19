import sys
N = int(input())
S = [0]*N
# T = str(input())
s = set([n for n in input().split()])

if(len(s) == 3):
    print("Three")
else:
    print("Four")
