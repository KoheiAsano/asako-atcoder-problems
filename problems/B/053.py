import sys
# A,B,C = [int(n) for n in input().split()]
# N = int(input())
S = str(input())
# T = str(input())
L = len(S)
ans = ""
begin = L
end = 0
for i in range(L):
    if(S[i] == "A" and begin == L):
        begin = i
    elif(S[i] == "Z" and begin != L):
        end = i+1

print(end - begin)
