import sys
N = int(input())
a = [int(n) for n in input().split()]
# A = [0]*N
# for i in range(N):
#     A[i] = int(input())
bucket = [0]*100000
for ak in a:
    bucket[ak]+=1
ans = 0
for i in range(1,99999):
    ans = max(ans,bucket[i-1] + bucket[i] + bucket[i+1])
print(ans)
