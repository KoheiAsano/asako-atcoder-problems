from sys import exit
from collections import defaultdict
H,W,N = [int(n) for n in input().split()]
Sr,Sc = [int(n) for n in input().split()]
#上に
Dout = H-Sr + 1
#下に
Uout = Sr
#右に落とすのに必要な歩数
Rout = W - Sc + 1
#左に
Lout = Sc
# print(Uout, Dout,Rout, Lout)
S = str(input())
T = str(input())
ptrC = defaultdict(int)
ptrA = defaultdict(int)
for s,t in zip(S,T):
    ptrC[s]+=1
    ptrA[t]+=1
# print(ptrC,ptrA)
# if ptrC["R"] - ptrA["L"] >= Rout or ptrC["L"] - ptrA["R"] >= Lout or ptrC["D"] - ptrA["U"] >= Dout or ptrC["U"] - ptrA["D"] >= Uout:
#     print("NO")
#     exit()
def check(outcnt, C, A, lim, B):
    backed = 0
    for s,t in zip(S,T):
        if s == B and outcnt == lim -1 and backed > 0:
            outcnt -= 1
            backed -= 1
        if( s == C ):
            outcnt -= 1
        if( outcnt == 0 ):
            print("NO")
            exit()
        if( t == A and outcnt < lim ):
            outcnt += 1
            backed += 1

check(Rout, "R", "L", W, "L")
check(Lout, "L", "R", W, "R")
check(Uout, "U", "D", H, "D")
check(Dout, "D", "U", H, "U")
print("YES")
