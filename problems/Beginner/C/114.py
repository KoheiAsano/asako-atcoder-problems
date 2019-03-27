from sys import exit
# A,B,C = [int(n) for n in input().split()]
N = int(input())
# a = [int(input()) for _ in range(N)]
# S = str(input())
# L = len(S)
# T = str(input())
# exit()

three = ['357', '375', '537', '573', '735', '753']
cand = ['3' , '5' , '7']
ans = 0
s = set()
def rladd(cur):
    global ans,N,s
    if(int(cur) > N) or cur in s: return False
    s.add(cur)
    ans+=1
    for i in range(len(cur)):
        for c in cand:
            temp = list(cur)
            temp.insert(i,c)
            rladd("".join(temp))
for th in three:
    rladd(th)

print(ans)
