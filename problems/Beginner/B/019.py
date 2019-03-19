import sys
# N = int(input())
# a = [int(input()) for _ in range(N)]
S = str(input())
# T = str(input())
L = len(S)
ans=""
cnt = 1
for i in range(1,L):
    if(S[i-1] != S[i]):
        ans += S[i-1]+ str(cnt)
        cnt = 0
    cnt+=1
ans += S[L-1] + str(cnt)
print(ans)
