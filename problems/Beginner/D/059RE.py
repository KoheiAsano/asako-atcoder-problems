import sys
AB = [int(n) for n in input().split()]
# N = int(input())
# a = [int(input()) for _ in range(N)]
# S = str(input())
# L = len(S)
# T = str(input())
fin = [[0,0],[1,0],[0,1]]
Alice = True
def Alicewin(state,Alice):
    if(state in fin and Alice):
        return False
    elif(state in fin and not Alice):
        return True
    Ap = 2
    while(Ap<=state[0]):
        if Alicewin([state[0]-Ap,state[1]+Ap/2],not Alice):
            return True
        Ap+=2
    Bp = 2
    while(Bp<=state[1]):
        if Alicewin([state[0]+Bp/2,state[1]-Bp],not Alice):
            return True
        Bp+=2
    return False

print("Alice" if Alicewin(AB, True) else "Brown")
