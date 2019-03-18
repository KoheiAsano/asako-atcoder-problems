class UnionFind():
    #負の値はルートで集合の個数
    #正の値は次の要素を返す
    def __init__(self,size):
        self.table = [-1 for _  in range(size)]

    #集合の代表を求める
    def find(self,x):
        while self.table[x] >= 0:
            #根に来た時,self.table[根のindex]は負の値なのでx = 根のindexで値が返される。
            x = self.table[x]
        return x

    #併合
    def union(self,x,y):
        s1 = self.find(x)#代表のIndexを取得する
        s2 = self.find(y)
        if s1 != s2:#代表のIndexが違う場合
            if self.table[s1] < self.table[s2]:#要素数の少ない方へMergeする
                self.table[s1] += self.table[s2]#子の和を増やす(-)
                self.table[s2] = s1#Mergeされる側の代表をする側のインデックスに
            else:
                self.table[s2] += self.table[s1]
                self.table[s1] = s2
        return
    def size(self,x):
        while self.table[x] >= 0:
            #根に来た時,self.table[根のindex]は負の値なのでx = 根のindexで値が返される。
            x = self.table[x]
        return abs(self.table[x])
N,M = [int(n) for n in input().split()]
UF = UnionFind(N)
a = [0]*M
b = [0]*M
for i in range(M):
    a[i], b[i] = [int(n)-1 for n in input().split()]
ans = [0]*M
ans[M-1] = int(N*(N-1)/2)
for i in range(M-1,0,-1):
    if(UF.find(a[i]) != UF.find(b[i])):
        ans[i-1] = ans[i] - UF.size(a[i])*UF.size(b[i])
    else:
        ans[i-1] = ans[i]
    UF.union(a[i],b[i])
for i in range(M):
    print(ans[i])
