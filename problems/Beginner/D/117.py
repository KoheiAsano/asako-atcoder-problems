from sys import exit
N,K = [int(n) for n in input().split()]
A = [int(n) for n in input().split()]

sums = []
maximum_size = len(bin(max(A))) - 2
countdic = [{"0":0,"1":0} for _ in range(maximum_size)]
#全候補のバイナリ表示で各桁それぞれ0,1をカウントする
for i in range(N):
    # print(bin(A[i]))
    ta = bin(A[i])[2:].zfill(maximum_size)
    ta = ta[::-1]
    # print(ta)
    # print(ta)
    for i in range(len(ta)):
        if ta[i] == "0":
            countdic[i]["0"] +=1
        else:
            countdic[i]["1"] +=1
#さっきのカウントの少ない方になるようにフラグをたてる
ans = ""
for num in countdic:
    if num["0"] < num["1"]:
        ans = "0" + ans
    else:
        ans = "1" + ans
lim = bin(K)[2:]
# print("lim:" + str(lim))
#埋められるだけ1を埋めて、超えちゃったら上から1をつぶしていく
if K != 0:
    maxcand_size = len(bin(K)) - 2
    # print(maxcand_size)
    ans = abs(maxcand_size - len(ans))*"1" + ans
    ans = ans[-maxcand_size:]
    # if(int(ans,2) > K):
    # print(int(ans,2))
    if(int(ans,2) > K):
        for i in range(1,len(lim)):
            if(lim[i] == "0" and ans[i] == "1"):
                ans = ans[:i] + "0" + ans[i+1:]
                if(int(ans,2) <= K):break
    # print(int(ans,2))
else:
    ans = "0"
# print(bin(K))
# print("asako" + str(maxcand_size))

# print(ans)
# print(int(ans,2))

#解答計算
ans = int(ans,2)
answer = 0
# print(ans)
for i in range(N):
    answer+=ans^A[i]
print(answer)
