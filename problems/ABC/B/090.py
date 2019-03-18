import sys
A,B = [int(n) for n in input().split()]
# N = int(input())
# S = str(input())
# T = str(input())
ans = 0
for s in range(A,B+1):
    s = str(s)
    rs = s[::-1]
    if(s == rs):
        ans +=1
print(ans)
