import sys
A,B = [int(n) for n in input().split()]
# N = int(input())
S = str(input())
if(S[A] != "-"):
    print("No")
    sys.exit()
S = S[:A] + S[A+1:]
table = [str(n) for n in range(10)]
for s in S:
    if not( s in table):
        print("No")
        sys.exit()
print("Yes")
