# print("YES" if input().replace("eraser", "").replace("erase", "").replace("dreamer", "").replace("dream", "")=="" else "NO")


strings = ['eraser','erase', 'dreamer','dream' ]
# strings = [s[::-1] for s in strings]

S = str(input())
# S = S[::-1]
# print(S,strings)
for s in strings:
    S = S.replace(s, "")

if S == "":
    print('YES')
else:
    print("NO")
