# from sys import exit
N = int(input())
S = [str(input()) for _ in range(N)]
Aend = 0
Bstart = 0
BstartAend = 0
ABcon = 0
for s in S:
    if s[0] == "B" and s[-1] == "A":
        BstartAend += 1
    elif(s[0] == "B"):
        Bstart += 1
    elif(s[-1] == "A"):
        Aend += 1
    ABcon += s.count("AB")
# 小さい方を答えへ、そうじゃないのはあまり
tmp = min(Aend, Bstart)
if BstartAend == 0:
    print(ABcon + tmp)
else:
    if max(Aend, Bstart) == 0:
        print(ABcon + BstartAend - 1)
    else:
        print(ABcon + BstartAend + tmp)
