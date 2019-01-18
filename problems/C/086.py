import sys
N = int(input())
t = [0]*N
x = [0]*N
y = [0]*N
for i in range(N):
    t[i],x[i],y[i] = [int(n) for n in input().split()]
dt = t[0]
d = x[0] + y[0]
if(dt < d or dt%2 != d%2):
    print("No")
    sys.exit()
for i in range(1,N):
    dt = t[i] - t[i-1]
    d = abs(x[i] - x[i-1]) + abs(y[i] - y[i-1])
    if(dt < d or dt%2 != d%2):
        print("No")
        sys.exit()
print("Yes")
