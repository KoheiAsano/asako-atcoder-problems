import sys
# A,B,C = [int(n) for n in input().split()]
# N = int(input())
# A = [0]*N
# for i in range(N):
#     A[i] = int(input())
S = str(input())
ll = list("abcdefghijklmnopqrstuvwxyz")
for al in ll:
    if not (al in S):
        print(al)
        sys.exit()
print("None")
