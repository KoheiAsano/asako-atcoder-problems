class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n+1)]
        self.rank = [0] * (n+1)

    # 検索
    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    # 併合
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
        else:
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    # 同じ集合に属するか判定
    def same_check(self, x, y):
        return self.find(x) == self.find(y)


N, M = [int(n) for n in input().split()]
X = [0]*M
Y = [0]*M
Z = [0]*M
UF = UnionFind(N)
adj = [[0, []] for _ in range(N)]
for i in range(M):
    X[i], Y[i], Z[i] = [int(n) for n in input().split()]
    Z[i] %= 2
    X[i] -= 1
    Y[i] -= 1
    UF.union(X[i], Y[i])
s = set([UF.find(0)])
ans = 1

for i in range(1, N):
    tmp = UF.find(i)
    if not(tmp in s):
        ans += 1
        s.add(tmp)
print(ans)
