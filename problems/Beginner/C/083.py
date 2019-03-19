from sys import exit
X,Y = [int(n) for n in input().split()]

ans = 0
while(X<=Y):
    ans+=1
    X*=2
print(ans)
