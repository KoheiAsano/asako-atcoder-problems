import sys
SA = str(input())
SB = str(input())
SC = str(input())
turn = "A"
while (1):
    if( turn == "A"):
        if SA == "":
            break
        if SA[0] == "a":
            turn = "A"
        elif SA[0] == "b":
            turn = "B"
        else:
            turn = "C"
        SA = SA[1:]
    elif( turn == "B"):
        if SB == "":
            break
        if SB[0] == "a":
            turn = "A"
        elif SB[0] == "b":
            turn = "B"
        else:
            turn = "C"
        SB = SB[1:]
    else:
        if SC == "":
            break
        if SC[0] == "a":
            turn = "A"
        elif SC[0] == "b":
            turn = "B"
        else:
            turn = "C"
        SC = SC[1:]
print(turn)
