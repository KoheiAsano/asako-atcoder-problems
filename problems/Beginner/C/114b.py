from sys import exit
# A,B,C = [int(n) for n in input().split()]
N = int(input())
# a = [int(input()) for _ in range(N)]
# S = str(input())
# L = len(S)
# T = str(input())
# exit()

cand = ['3' , '5' , '7']
ans = 0
def rladd(cur):
    global ans,N,s
    if(int(cur) > N): return False
    if all(c in cur for c in cand):
        ans+=1
        # print(cur)
    for c in cand:
        rladd(cur+c)

rladd("0")

print(ans)
