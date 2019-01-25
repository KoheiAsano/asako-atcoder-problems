import sys
import math
S = str(input())
N = int(input())
l = [0]*N
r = [0]*N
for i in range(N):
    l[i],r[i] = [int(n) for n in input().split()]
    # print(S[:l[i]-1] +"+"+ S[l[i]-1:r[i]:][::-1] +"+"+ S[r[i]:])
    S = S[:l[i]-1] + S[l[i]-1:r[i]:][::-1] + S[r[i]:]
print(S)
