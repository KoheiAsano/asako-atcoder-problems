import sys
N,K = [int(n) for n in input().split()]
D = set([str(n) for n in input().split()])
# OK = sorted(list(set([0,1,2,3,4,5,6,7,8,9]) - D))
for i in range(N,100001):
    stri = set(list(str(i)))
    find = True
    for d in D:
        if d in stri:
            find = False
            break
    if find:
        print(i)
        sys.exit()
