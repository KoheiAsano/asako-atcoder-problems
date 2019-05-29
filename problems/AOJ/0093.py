# from sys import exit
init = False
while(True):
    A, B = [int(n) for n in input().split()]
    if A == 0 and B == 0:
        exit()
    if init:
        print()
    aaa = False
    for a in range(A, B+1):
        if a % 4 == 0:
            if a % 100 == 0 and a % 400 != 0:
                continue
            print(a)
            aaa = True
    if (not aaa):
        print("NA")
    init = True
