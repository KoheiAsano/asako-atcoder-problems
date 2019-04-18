from sys import exit
class UnionFind():
    #負の値は根で集合の個数
    #正の値は次の要素を返す
    def __init__(self,size):
        self.table = [-1 for _  in range(size)]

    #集合の代表を求める
    def find(self,x):
        if self.table[x] < 0:return x
        root = self.find(self.table[x])
        self.table[x] = root
        return root

    #併合
    def union(self,x,y):
        s1 = self.find(x)#代表のIndexを取得する
        s2 = self.find(y)
        if s1 != s2:#代表のIndexが違う場合
            if self.table[s1] < self.table[s2]:#要素数の多い方へMergeする
                self.table[s2] += self.table[s1]#子の和を増やす(-)
                self.table[s1] = s2#Mergeされる側の代表をする側のインデックスに
            else:
                self.table[s1] += self.table[s2]
                self.table[s2] = s1
        return
    def size(self,x):
        return -self.table[self.find(x)]

N,M = [int(n) for n in input().split()]
# N = int(input())
UF = UnionFind(N)
for _ in range(M):
    a, b = [int(n)-1 for n in input().split()]
    UF.union(a,b)
    # print(UF.table)

kind = set()
for i in range(N):
    # print(i)
    kind.add(UF.find(i))
print(len(kind)-1)
