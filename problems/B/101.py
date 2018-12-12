import sys
# N,M = [int(n) for n in input().split()]
# S = str(input())
# T = str(input())

S = str(input())
N = int(S)
sum = 0
for i in range(len(S)):
    sum+=int(S[i])
if(N%sum == 0):
    print("Yes")
else:
    print("No")
