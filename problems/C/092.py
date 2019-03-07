import sys
N = int(input())
A = [0] + [int(n) for n in input().split()] + [0]
sumA = 0
for i in range(1,N+2):
    sumA += abs(A[i]-A[i-1])

for i in range(1,N+1):
    print(sumA - abs(A[i]-A[i-1]) - abs(A[i]-A[i+1]) + abs(A[i-1]-A[i+1]))
