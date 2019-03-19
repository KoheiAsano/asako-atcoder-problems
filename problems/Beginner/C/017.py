n,m = map(int,input().split())
c = 0
A = [0]*(m+2)
for i in range(n):
    l,r,s = map(int,input().split())
    A[l] += s#区間の始点に得点を足す
    A[r+1] -= s#あとで累積するとき、その区間を抜けたら失われる(A[i+1] += A[i]で)
    c += s#全得点合計
for i in range(m+1):
    A[i+1] += A[i]
print(c-min(A[1:m+1]))
