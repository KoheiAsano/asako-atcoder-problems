import sys
# A,B,C = [int(n) for n in input().split()]
n,X = [int(n) for n in input().split()]
a = [int(n) for n in input().split()]
# S = str(input())
# T = str(input())
ans = 0
for i in range(n):
    if(X & (1 << i)):
        ans += a[i]
print(ans)
		# for( int i = 0; i < n; ++i){
		# 	if (bit & (1 << i)) {
		# 		S.push_back(i);
		# 	}
		# }
