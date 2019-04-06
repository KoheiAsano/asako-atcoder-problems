from sys import exit
N,Y = [int(n) for n in input().split()]
# N = int(input())
# s = set()
for i in range(N+1):
    for j in range(N+1):
        if (Y-10000*i-5000*j)//1000 == N - i - j and Y-10000*i-5000*j >= 0:
            print(i,j,N - i - j)
            exit()
print(-1,-1,-1)
# print(len(s))
# S = str(input())
# L = len(S)
# T = str(input())
# exit()
