import sys
A,B,C = [int(n) for n in input().split()]

for i in range(1,101):
    if(A*i%B == C):
        print("YES")
        sys.exit()
print("NO")
