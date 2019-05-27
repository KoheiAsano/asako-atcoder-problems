# from sys import exit
N = int(input())
NP = [0 for i in range(N)]
for i in range(N):
    NP[i] = [str(n) for n in input().split()]
    NP[i].append(i+1)
NP = sorted(NP, key=lambda x: -int(x[1]))
NP = sorted(NP, key=lambda x: x[0])
for i in NP:
    print(i[2])
