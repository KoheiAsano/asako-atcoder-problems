# import time
#
# start = time.time()

import sys
input = sys.stdin.readline
N,Q = [int(n) for n in input().split()]
S = "f" + input() + "f"
t = [""]*Q
d = [""]*Q
for i in range(Q):
    t[i],d[i] = [s for s in input().split()]

#左に落ちるやつで一番右のゴーレムのインデックスを探す
def leftbinarysearch():
    l = 0
    r = N + 1
    # cnt = 0#デバグ用カウンタ
    while(l<r):
        m = (l+r)//2 + 1#探索範囲の中央値のIndexのゴーレムでシミュレーション
        cur = m#探す一つのゴーレムの現在地
        fall = False
        # print(l,r,m)
        for i in range(Q):
            if t[i] == S[cur]:
                if d[i] == "L":
                    cur-=1
                else:
                    cur+=1
                if(cur == 0):#左端に落ちるなら次はもっと右のやつを確かめる
                    l = m
                    fall = True
                    break
                elif(cur == N+1):#右端に落ちるなら下の処理に飛ぶ
                    break
        if not fall:#落ちなかったならそれより左端を探す
            r = m - 1
        # cnt+=1
        # if(cnt == 10):print("loop", file=sys.stderr);break;
    return l

#→に落ちるやつを返す
def rightbinarysearch():
        l = 0
        r = N + 1
        # cnt = 0
        while(l<r):
            m = (l+r)//2#探索範囲の中央値のIndexのゴーレムでシミュレーション
            cur = m#探す一つのゴーレムの現在地
            fall = False
            # print(l,r,m)
            for i in range(Q):
                if t[i] == S[cur]:
                    if d[i] == "L":
                        cur-=1
                    else:
                        cur+=1
                    if(cur == N+1):#右端に落ちるなら次はもっと左のやつを確かめる
                        r = m
                        fall = True
                        break
                    elif(cur == -1):#左端に落ちるなら下の処理まで飛ぶ
                        break
            if not fall:#落ちなかったならそれより右端を探す
                l = m + 1
            # cnt+=1
            # if(cnt == 10):print("loop", file=sys.stderr);break;
        return l
print(rightbinarysearch()-leftbinarysearch()-1)

# end = time.time()
# print(end - start)
