import sys
# N,M = [int(n) for n in input().split()]
# S = str(input())
# T = str(input())
S = str(input())
K = int(input())

for i in range(len(S)):
    if(S[i] == "1" and i+1 == K):
        print("1")
        sys.exit()
    elif(S[i]!="1"):
        print(S[i])
        sys.exit()
