import sys
# A,B,C = [int(n) for n in input().split()]
N = int(input())
# S = str(input())
# T = str(input())
# a,b,c = [int(n) for n in input().split()]
MARCH = ["M","A","R","C","H"]
MARCHn = {"M":0,"A":0,"R":0,"C":0,"H":0}
S = [0]*N
s = set()
n = 0
P=[0 ,0 ,0 ,0 ,0 ,0 ,1 ,1 ,1 ,2]
Q=[1 ,1 ,1 ,2 ,2 ,3 ,2 ,2 ,3 ,3]
R=[2 ,3 ,4 ,3 ,4 ,4 ,3 ,4 ,4 ,4]
for i in range(N):
    S[i] = str(input())
    initi = S[i][0]
    if(initi in MARCH):
        MARCHn[initi] = MARCHn[initi]+1
ans = 0
for i in range(10):
    ans += MARCHn[MARCH[P[i]]]*MARCHn[MARCH[Q[i]]]*MARCHn[MARCH[R[i]]]
print(ans)
