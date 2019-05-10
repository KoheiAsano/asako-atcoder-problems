from sys import exit
n = int(input())
a = [int(n) for n in input().split()]
k = int(input())

def dfs(sum,i):
    if sum == k:
        print("Yes")
        exit()
    elif(i==n):
        return False
    dfs(sum,i+1)
    dfs(sum+a[i],i+1)

dfs(0,0)
print("No")
