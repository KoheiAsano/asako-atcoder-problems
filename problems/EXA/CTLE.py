from sys import exit
N,Q = [int(n) for n in input().split()]
# a = [int(input()) for _ in range(N)]
S = str(input())
L = len(S)
dic ={'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6,
 'H': 7, 'I': 8, 'J': 9, 'K': 10,'L': 11, 'M': 12, 'N': 13, 'O': 14,
  'P': 15, 'Q': 16, 'R': 17, 'S': 18,'T': 19, 'U': 20, 'V': 21,
   'W': 22, 'X': 23, 'Y': 24, 'Z': 25}
adj = [set() for _ in range(26)]
gorem = [1 for _ in range(N)]
goremap = dict(enumerate(gorem))
# print(goremap)
ap = set()
for i in range(L):
    adj[dic[S[i]]].add(i)
# print(adj)
INF = 10**9
ans = N

for i in range(Q):
    #t == 文字、D = {L,R}
    t,d = [str(n) for n in input().split()]
    if d == "L":
        # print(adj[dic[t]])
        for mass in adj[dic[t]]:#その指示のマス
            gon = gorem[mass]
            gorem[mass]-=gon
            if mass == 0 :
                ans-=gon
                # print("die")
            else:
                gorem[mass-1]+=gon
    else:
        # print(adj[dic[t]])
        for mass in adj[dic[t]]:#その支持のマス
            gon = gorem[mass]
            gorem[mass]-=gon
            if mass == L-1:
                ans-=gon
                # print("die")
            else:
                gorem[mass+1]+=gon
    # print(gorem)

# print(adj)
print(ans)
# T = str(input())
# exit()
