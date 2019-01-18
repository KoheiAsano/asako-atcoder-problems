N=int(input())
red=sorted([list(map(int,input().split())) for i in range(N)], key=lambda x:-1*x[1])# y座標でSort(Decrease)
blue=sorted([list(map(int,input().split())) for i in range(N)])#x座標Increse
count=0
for i in red:
    for n,j in enumerate(blue):
        if i[0]<j[0] and i[1]<j[1]:
            count+=1
            del blue[n]
            break
print(blue)
print(count)
