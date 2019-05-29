while(True):
    S0 = str(input())
    if S0 == ".":
        exit()
    S1 = str(input())
    if S0 == S1:
        print("IDENTICAL")
        continue
    S0else = list(S0.split('"')[0::2])
    S1else = list(S1.split('"')[0::2])
    if S0else != S1else:
        print("DIFFERENT")
        continue
    S0str = list(S0.split('"')[1::2])
    S1str = list(S1.split('"')[1::2])
    if len(S0str) != len(S1str):
        print(S0str, S1str)
        print("DIFFERENT")
        continue
    OK = 1
    for i in range(len(S0str)):
        if S0str[i] != S1str[i]:
            OK -= 1
    if OK < 0:
        print("DIFFERENT")
    elif OK >= 0:
        print("CLOSE")
