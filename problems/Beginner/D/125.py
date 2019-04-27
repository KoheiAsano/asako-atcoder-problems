from sys import exit

N = int(input())
A = sorted([int(n) for n in input().split()], key=lambda x:abs(x))
# a = [int(input()) for _ in range(N)]
# S = str(input())
# L = len(S)
# T = str(input())
# exit()
minus = False
for i in range(N):
    if(A[i] < 0):
        minus = not minus
        A[i]*=-1
# print(A)
if(minus):
    print(sum(A) - A[0]*2)
else:
    print(sum(A))
