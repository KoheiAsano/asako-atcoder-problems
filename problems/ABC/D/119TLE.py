import sys
import bisect
A,B,Q = [int(n) for n in input().split()]
# N = int(input())
INF = 10 **18
s = [0]*A
t = [0]*B
x = [0]*Q
s = [-INF] + [int(input()) for n in range(A)] + [INF]
t = [-INF] + [int(input()) for n in range(B)] + [INF]
x = [int(input()) for n in range(Q)]
def binary_search(arry, target):
    result = None
    left = 0
    right = len(arry) - 1

    while left <= right:
        mid = (left + right) // 2
        if arry[mid] == target:
            result = mid
            break
        elif arry[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    if result == None:
        result = mid
        if(mid+1 < len(arry)):
            result = mid+1 if (abs(arry[mid+1] - target) < abs(arry[mid] - target)) else result
        if(mid-1 >= 0):
            result = mid-1 if (abs(arry[result] - target) > abs(arry[mid-1] - target)) else result
        return result
    else:
        return result+1

print(binary_search(s,899))
# for q in x:
#     mostntera = binary_search(s,q)
#     print(mostntera)
#     tera0 = s[mostntera]
#     tera1 = s[mostntera-1] if q-tera0<0 else s[mostntera+1]
#     print(tera0,tera1)
#     mostnzin = binary_search(t,q)
#     zin0 = t[mostnzin]
#     zin1 = t[mostnzin-1] if q-zin0<0 else t[mostnzin+1]
#     print(zin0,zin1)
#     ans = INF
#     for a in [tera0, tera1]:
#         for b in [zin0,zin1]:
#             d1,d2 = abs(q-a) +abs(a-b), abs(q-b) + abs(a-b)
#             ans = min(ans,d1,d2)
#     print(ans)
