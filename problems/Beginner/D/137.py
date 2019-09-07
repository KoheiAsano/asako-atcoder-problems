import heapq
from collections import defaultdict
# setrecursionlimit(10**7)


def main():
    N,M = [int(n) for n in input().split()]
    # {期限:価値}
    jobs = defaultdict(list)
    v = 0
    for i in range(N):
        a,b = [int(n) for n in input().split()]
        if a <= M:
            jobs[a].append(-b)
    cand = []
    ans = 0
    for i in range(1,M+1):
        for e in jobs[i]:heapq.heappush(cand,e)
        if len(cand) != 0:
            ans -= cand[0]
            heapq.heappop(cand)
    print(ans)


if __name__ == "__main__":
    main()
