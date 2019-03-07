from sys import exit
# N = int(input())
# a = [int(input()) for _ in range(N)]
S = str(input())
L = len(S)
cnt = 0
num0 = 0
num1 = 0
ans = L
for i in range(0,L-1):
    if S[i] != S[i+1]:
        ans = min(ans,max(i+1,L-(i+1)))
print(ans)
