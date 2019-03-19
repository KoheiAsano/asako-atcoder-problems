import sys
A = int(input())
B = int(input())
if(A > B):
    print("GREATER")
    sys.exit()
if(A < B):
    print("LESS")
    sys.exit()
else:
    print("EQUAL")
