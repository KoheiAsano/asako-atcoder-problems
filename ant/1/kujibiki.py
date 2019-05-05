from sys import exit
N = int(input())
M = int(input())
k = [int(n) for n in input().split()]
for i in range(N):
    for j in range(N):
        for l in range(N):
            for m in range(N):
                if(k[i] + k[j] + k[l] + k[m] == M):
                    print("Yes")
                    exit()
print("No")
