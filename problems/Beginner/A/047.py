import sys
ABC = [int(n) for n in input().split()]
# N = int(input())
# a = [int(input()) for _ in range(N)]
# S = str(input())
# L = len(S)
# T = str(input()
sumABC = sum(ABC)
for i in range(0,3):
    if(sumABC - ABC[i] == ABC[i]):
        print("Yes")
        sys.exit()
print("No")
