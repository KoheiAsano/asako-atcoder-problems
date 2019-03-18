import sys
A,B,C = [int(n) for n in input().split()]
# N = int(input())
# A = [0]*N
# for i in range(N):
#     A[i] = int(input())
ans0 = A + B
ans1 = A - B
if(ans0 == C and ans1 == C):
    print("?")
elif(ans0 != C and ans1 == C):
    print("-")
elif(ans0 == C and ans1 != C):
    print("+")
else:
    print("!")
