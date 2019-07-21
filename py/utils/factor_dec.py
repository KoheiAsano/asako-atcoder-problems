N = int(input())
# 1は全ての約数
a = [1]

for i in range(2, int(N**0.5)+1):
    if N % i == 0:
        a.append(i)
        if i != N//i:
            a.append(N//i)
# ソートはしない
print(a)
