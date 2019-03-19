import sys
# N,M = [int(n) for n in input().split()]
N = int(input())
S = list(input())
st = set(S)
# for s in S:
#     st.add(s)
kind = len(st)
maxi = 0
# print(kind)
for i in range(1,len(S)-1):
    # print(i)
    l = set(S[:i])
    r = set(S[i:])
    tmp = len(l&r)
    # print(tmp)
    maxi = max(tmp,maxi)

print(maxi)
