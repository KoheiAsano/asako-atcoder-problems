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
        # while self.table[x] >= 0:
        #     #根に来た時,self.table[根のindex]は負の値なのでx = 根のindexで値が返される。
        #     x = self.table[x]
        # return x

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
        # while self.table[x] >= 0:
        #     #根に来た時,self.table[根のindex]は負の値なのでx = 根のindexで値が返される。
        #     x = self.table[x]
        return -self.table[self.find(x)]
UF = UnionFind(9)
UF.union(0,1)
print(UF.table)
print(UF.size(1))
print(UF.size(0))
print(UF.size(4))
UF.union(4,5)
print(UF.table)
UF.union(7,8)
print(UF.table)
UF.union(1,7)
print(UF.size(8))
print(UF.table)
UF.find(8)
print(UF.table)
