s = str(input())
K = int(input())
S = set()
anslength = K
while 0 < anslength:
    for i in range(0,len(s)-anslength+1):
        S.add(s[i:i+anslength])
    anslength-=1
LS = list(S)
LS.sort()
print(LS[K-1])
