N = int(input())
a = [int(n) for n in input().split(" ")]
a = [a[n] - n - 1  for n in range(N)]
a = sorted(a)
if(N%2==1):
    median = a[int(N/2)]
else:
    median = (a[int(N/2)-1] + a[int(N/2)] )/ 2
sum = 0
for i in range(N):
    sum += abs(a[i] - median)
print(int(sum))
