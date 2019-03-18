import sys
# N = int(input())
# a = [int(input()) for _ in range(N)]
S = sorted(list(input()))
L = len(S)
# T = str(input())
num0 = 0
for i in range(L):
    if(S[i] == "1"):
        num0 = i
        break
print(min((L-num0)*2,num0*2))
