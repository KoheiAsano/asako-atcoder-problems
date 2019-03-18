import sys

# N = int(input())
# S = str(input())
# T = str(input())

ABCDE = [int(n) for n in input().split()]
sum = set()
for a in range(5):
    for b in range(a+1,5):
        for c in range(b+1,5):
            sum.add(ABCDE[a] + ABCDE[b] + ABCDE[c])
sum = list(sum)
sum = sorted(sum)
print(sum[-3])
