N = int(input())
S = list(str(input()))
Sinv = S[::-1]
T = ""

while(S != []):
    if S > Sinv:
        T += Sinv[0]
        del S[-1]
        del Sinv[0]
    else:
        T += S[0]
        del S[0]
        del Sinv[-1]
print(T)
