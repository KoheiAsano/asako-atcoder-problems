from sys import exit

S = str(input())#["F","F","T","F"]
Gx, Gy = [int(n) for n in input().split()]#[4,4]
Xds = []
Yds = []
X = True
L = len(S)
for s in S.split("T"):
    if X:
        Xds.append(len(s))
    else:
        Yds.append(len(s))
    X = not X
# print(Xds)
# print(Yds)
if(len(Xds) != 0):
    memox = [set([Xds[0]])] + [0]*(len(Xds)-1)
else:
    memox = [0]
for i in range(1,len(Xds)):
    can = set()
    for x in memox[i-1]:
        can.add(x+Xds[i])
        can.add(x-Xds[i])
    memox[i]=can

if(len(Yds) != 0):
    memoy = [set([Yds[0],-Yds[0]])] + [0]*(len(Yds)-1)
else:
    memoy = [0]
for i in range(1,len(Yds)):
    can = set()
    for y in memoy[i-1]:
        can.add(y+Yds[i])
        can.add(y-Yds[i])
    memoy[i]=can
if Gx in memox[-1] and Gy in memoy[-1]:
    print("Yes")
else:
    print("No")
