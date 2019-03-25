from sys import exit
# A,B,C = [int(n) for n in input().split()]
Sa = list(input())
Sb = list(input())
Sc = list(input())
turn = "A"
while(True):
    if turn == "A":
        if(Sa != []):
            turn = Sa[0].upper()
            del Sa[0]
        else:
            print("A")
            exit()
    elif turn == "B":
        if(Sb != []):
            turn = Sb[0].upper()
            del Sb[0]
        else:
            print("B")
            exit()
    else:
        if(Sc != []):
            turn = Sc[0].upper()
            del Sc[0]
        else:
            print("C")
            exit()

# N = int(input())
# a = [int(input()) for _ in range(N)]
# S = str(input())
# L = len(S)
# T = str(input())
exit()
