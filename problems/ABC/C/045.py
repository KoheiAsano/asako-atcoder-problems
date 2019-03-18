# N,M = [int(n) for n in input().split()]
# S = str(input())
# T = str(input())
S = [s for s in str(input())] # ['1', '2', '5']

sum =0
for bit in range(1 << len(S) -1):
    l = []
    tmpS = [s for s in S]
    for i in range(len(S) -1):
        if(bit & (1 << i)):
            l.append(i)
    for i in l:
        tmpS[i] += "+"
    sum+=eval("".join(tmpS))

print(sum)
