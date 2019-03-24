from sys import exit
H,W,N = [int(n) for n in input().split()]
dxy = [[1,0],[0,1],[-1,0],[0,-1],[1,-1],[-1,1],[1,1],[-1,-1],[0,0]]
# ansdic = {0:(H-2)*(W-2),1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
efdic = {}


for i in range(N):
    ab = [int(n) for n in input().split()]
    ab[0]-=1
    ab[1]-=1
    for d in dxy:
        per = [ab[0] + d[0],ab[1] + d[1]]
        if(1 <= per[0] <= H-2 and 1 <= per[1] <= W-2):
            rep = "".join([str(per[0]),str(per[1])])
            if not rep in efdic:
                efdic[rep] = 1
            else:
                efdic[rep] +=1

ans = {0:(H-2)*(W-2),1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
for k in efdic.keys():
    ans[efdic[k]]+=1
    ans[0]-=1

for k in ans.keys():
    print(ans[k])
# S = str(input())
# L = len(S)
# T = str(input())
exit()
