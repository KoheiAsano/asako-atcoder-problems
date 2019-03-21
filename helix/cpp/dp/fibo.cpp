#include <bits/stdc++.h>
using namespace std;


int n;

int memo[50];

int fibo(int n) {
	if(n==1 || n == 0) return 1;
	if(memo[n] != -1) return memo[n];
	return memo[n] = fibo(n-1) + fibo(n-2);
}

int main(){
	scanf("%d", &n);
	for(int i=0;i<50;i++)memo[i] = -1;
	printf("%d\n",fibo(n));
	return 0;
}
