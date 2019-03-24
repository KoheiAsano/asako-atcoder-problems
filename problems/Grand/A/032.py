from sys import exit
# A,B,C = [int(n) for n in input().split()]
N = int(input())
b = [int(n) for n in input().split()]
test = [i for i in range(1,N+1)]
ans = []
i = N
while(i != 0):#for i in range(N,0,-1)
    # print(i)
    if b[i-1] == i:
        ans.append(b[i-1])
        del b[i-1]
        i = len(b)
    else:
        i-=1
    if len(b) == 0:
        for l in range(len(ans)-1,-1,-1):
            print(ans[l])
        exit()

print(-1)

# S = str(input())
# L = len(S)
# T = str(input())
exit()
