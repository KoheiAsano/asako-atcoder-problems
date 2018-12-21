import sys
# N,M = [int(n) for n in input().split()]
S = str(input())
# T = str(input())
if (not "B" in S) or (not "W" in S):
    print(0)
    sys.exit()

changecount = 0
for i in range(1,len(S)):
    if(S[i] != S[i-1]):
        changecount+=1
print(changecount)
