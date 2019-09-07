from sys import exit, stderr, stdin
input = stdin.readline
# setrecursionlimit(10**7)
from collections import defaultdict


def main():
    N = int(input())
    A = [0]*N
    dic = defaultdict(int)
    for i in range(N):
        A[i] = "".join(sorted((input()[:-1])))
        dic[A[i]] +=1
    ans = 0
    for k in dic:
        if dic[k] >= 2:
            ans += dic[k]*(dic[k]-1)//2
    print(ans)






if __name__ == "__main__":
    main()
