import sys
# N = int(input())
# A = [0]*N
# for i in range(N):
#     A[i] = int(input())
S = str(input())
# T = str(input())
chock = ["ch","o","k","u"]
al = "".join(S.split("ch"))
for alp in al:
    if not (alp in chock):
        print("NO")
        sys.exit()

print("YES")
