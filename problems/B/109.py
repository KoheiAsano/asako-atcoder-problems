import sys
# N,M = [int(n) for n in input().split()]
# S = str(input())
# T = str(input())

N = int(input())
SS = [0]*N
s = set()
SS[0] = str(input())
s.add(SS[0])
for i in range(1,N):
    SS[i] = str(input())
    if(SS[i] in s):
        print('No')
        sys.exit()
    s.add(SS[i])
for i in range(1,N):
    if(SS[i-1][-1] != SS[i][0]):
        print('No')
        sys.exit()
print('Yes')
