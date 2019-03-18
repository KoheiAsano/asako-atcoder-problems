from sys import exit
N,M = [int(n) for n in input().split()]
P = [0]*M
Y = [0]*M
l = [0]*M
dic = dict(zip(range(1,N+1),[0]*N))
for i in range(M):
    P[i], Y[i] = [int(n) for n in input().split()]
    l[i] = [i,P[i], Y[i], str(P[i]).zfill(6)]

l = sorted(l,key=lambda x:x[2])
for i in range(M):
    dic[l[i][1]]+=1
    l[i][3]+=str(dic[l[i][1]]).zfill(6)
l = sorted(l,key=lambda x:x[0])
for i in range(M):
    print(l[i][3])
# a = [int(input()) for _ in range(N)]
# S = str(input())
# L = len(S)
# T = str(input())
