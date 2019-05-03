from sys import exit
N,K = [int(n) for n in input().split()]
# N = int(input())
# a = [int(input()) for _ in range(N)]
S = str(input())
L = len(S)
lis = []
if(S[0] == "0"):#偶数Indexがブリッジ
    lis.append(0)
tmp = S[0]

for i in range(1,L):
    if(S[i]!=S[i-1]):
        lis.append(len(tmp))
        tmp =S[i]
    else:
        tmp+=S[i]
lis.append(len(tmp))
#0で終わっていたら最後に１が0個であるとする
if("0" in tmp):
    lis.append(0)
# print(lis)

#累積和をとる
L = len(lis)
# print(L)
asum = [0]*(L+1)
asum[0] = 0
for i in range(1,L+1):
    asum[i] = asum[i-1] + lis[i-1]
# print(asum)

#尺をとる
l = 0
ans = max(lis) if l+2*K+1 < L+1 else sum(lis)
for r in range(l+2*K+1 , L+1,2):
    # print(l,r)
    # print(asum[r] - asum[l])
    ans = max(asum[r] - asum[l],ans)
    l+=2
print(ans)

# 14 2
# 11101010110011
# 10 1
# 0000000001
