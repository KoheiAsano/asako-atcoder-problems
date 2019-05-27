N, K = [int(n) for n in input().split()]
S = list(str(input()))
L = len(S)
S[K-1] = S[K-1].lower()
print("".join(S))
