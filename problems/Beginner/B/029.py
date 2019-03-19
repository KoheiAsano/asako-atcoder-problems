import sys
# A,B,C = [int(n) for n in input().split()]

# S = str(input())
# T = str(input())
S = [0]*12
ans = 0
for i in range(12):
    S[i] = str(input())
    if ("r" in S[i]):
        ans +=1
print(ans)
