from sys import exit
N = int(input())
A = [int(n) for n in input().split()]
# print(A)
# a = [int(input()) for _ in range(N)]
# S = str(input())
# L = len(S)
# T = str(input())
# exit()
for j in range(1,len(A)):#短い周期からチェック
    temp = A[:j]
    # print(temp)
    OK = True
    for i in range(len(A)):
        # print(i,j,temp[i%j], A[i])
        if(A[i] != 0) and temp[i%j] != A[i]:
            if(temp[i%j] == 0):
                temp[i%j] = A[i]
            else:
                OK = False
                break
    if(OK):
        print(j)
        exit()
print(len(A))
