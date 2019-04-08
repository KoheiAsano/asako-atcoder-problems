from sys import exit
# A,B,C = [int(n) for n in input().split()]
# N = int(input())
A = [0]*5
last = 129

for _ in range(5):
    A[_] = int(input())
    if(A[_]%10 != 0 and last%10 >= A[_]%10):
        last = A[_]
ans = 0
once = False
for a in A:
    if(a == last and not once):
        once = True
        continue
    if(a%10 != 0 ):
        a+=10 - a%10
    ans+=a
if(last == 129):
    print(ans)
else:
    print(ans+last)
# S = str(input())
# L = len(S)
# T = str(input())
# exit()
