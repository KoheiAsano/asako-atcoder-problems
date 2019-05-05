import itertools

#累積和
li = [1,1,2,2,3,2,1]
for a in itertools.accumulate(li):
    print(a)

#直積()
for x,y in itertools.product(li,li):
    print(x,y)

# 連続するのをまとめる gはイテレータ
for k,g in itertools.groupby(li):
    print(k,list(g))

#Combination li C r
r = 2
for c in itertools.combinations(li,r):
    print(c)
