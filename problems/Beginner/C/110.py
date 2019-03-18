# A,B,C = [int(n) for n in input().split()]
# N = int(input())
S = list(input())
T = list(input())
s = {}
for i in range(len(S)):
    if not(S[i] in s):
        s[S[i]] = i
        S[i] = i
    else:
        S[i] = s[S[i]]
s = {}
for i in range(len(T)):
    if not(T[i] in s):
        s[T[i]] = i
        T[i] = i
    else:
        T[i] = s[T[i]]
print("Yes" if T == S  else "No")
