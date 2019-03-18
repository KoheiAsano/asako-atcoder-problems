import sys
N,A,B = [int(n) for n in input().split()]
#  = int(input())
ans = 0
for i in range(N+1):
    s = [int(s) for s in str(i)]
    if(sum(s)>=A and sum(s)<=B):
        ans+=i
print(ans)
