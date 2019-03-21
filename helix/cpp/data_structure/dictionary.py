import sys
# A,B,C = [int(n) for n in input().split()]
N = int(input())
# S = str(input())
# T = str(input())
# a,b,c = [int(n) for n in input().split()]
S = [0]*N
s = set()
for i in range(N):
    S[i] = str(input())
for i in range(N):
    if(S[i][0] == "i"):
        s.add(S[i][7:])
    elif(S[i][0] == "f"):
        if(S[i][5:] in s):
            print("yes")
        else:
            print("no")
