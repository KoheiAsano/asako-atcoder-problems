from sys import exit
def gcd(a,b):#greatest common divisor
    if (a<b):
        a,b = b,a
    while(b>0):
        a,b = b ,a%b
    return a
N = int(input())
A = [int(n) for n in input().split()]
straight = [0]*N
straight[0] = gcd(A[0],A[0])
for i in range(1,len(A)):
    straight[i] = gcd(straight[i-1], A[i])

A = A[::-1]
back = [0]*N
back[0] = gcd(A[0],A[0])
for i in range(1,len(A)):
    back[i] = gcd(back[i-1], A[i])

back = back[::-1]
# print(straight)
# print(back)
ans = straight[-2]
for i in range(N-2):
    ans = max(ans, gcd(straight[i], back[i+2]))
    # print(straight[i],back[i+2])
    # print(gcd(straight[i], back[i+2]))
ans = max(ans, back[1])
print(ans)
